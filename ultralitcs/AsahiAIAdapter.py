import cv2
import numpy as np
import torch

from IA.ultralitcs.UltralitcsAIAdapter import UtralitcsAIAdapter
from IA.ultralitcs.core.asahi.PatchDivider import PatchDivider
from IA.ultralitcs.core.asahi.PatchInferenceRunner import PatchInferenceRunner
from IA.ultralitcs.core.asahi.DetectionMerger import DetectionMerger
from IA.ultralitcs.core.asahi.NMSProcessor import NMSProcessor
from ultralytics.engine.model import Model
from ultralytics.engine.results import Results
from .UltralitcsAIRunConfiguration import UtralitcsAIRunConfiguration
from .scripts.io.ResultsSaver import ResultsSaverInText   
from IA.ultralitcs.core.asahi.InvertedImage import InvertedImage
from IA.ultralitcs.core.asahi.ConvertYolo import ConvertYolo

# TODO: descobrir o motivo do erro abaixo acontecer de vez em quadno; merge na development; backup das imagens no drive com 400gb; melhorar arquitetura da sahi 
# celery_worker-1  | [2025-05-20 15:36:02,309: ERROR/ForkPoolWorker-8] Task apps.plantations.tasks.predict_and_save_task[508e803c-c44c-490d-ae73-1831521c60eb] raised unexpected: IndexError('too many indices for array: array is 1-dimensional, but 2 were indexed')
# celery_worker-1  | Traceback (most recent call last):
# celery_worker-1  |   File "/usr/local/lib/python3.10/dist-packages/celery/app/trace.py", line 453, in trace_task
# celery_worker-1  |     R = retval = fun(*args, **kwargs)
# celery_worker-1  |   File "/usr/local/lib/python3.10/dist-packages/celery/app/trace.py", line 736, in __protected_call__
# celery_worker-1  |     return self.run(*args, **kwargs)
# celery_worker-1  |   File "/origin/apps/plantations/tasks.py", line 22, in predict_and_save_task
# celery_worker-1  |     countsReponse = AIService.predictImagesInDirectory(_dir)
# celery_worker-1  |   File "/origin/apps/plantations/views/prediction_service/AIService.py", line 16, in predictImagesInDirectory
# celery_worker-1  |     response = ImagePrediction.call(ImagePredictionCallOptions.BEST, directory)
# celery_worker-1  |   File "/origin/IA/controller/ImagePrediction.py", line 40, in call
# celery_worker-1  |     return model.run()
# celery_worker-1  |   File "/origin/IA/adapter/AIRunner.py", line 25, in run
# celery_worker-1  |     self.__model.predict()
# celery_worker-1  |   File "/origin/IA/ultralitcs/AsahiAIAdapter.py", line 58, in predict

class AsahiAIAdapter(UtralitcsAIAdapter):
    """
    Classe responsável por subescrever o método `predict` de `UltralitcsAIAdapter` para utilização de Asahi.
    """
    def __init__(self, model: Model, runconfig: UtralitcsAIRunConfiguration, resultsSaver: ResultsSaverInText | None) -> None:
        super().__init__(model, runconfig, resultsSaver)
        self.patch_divider = PatchDivider()
        self.detection_runner = None  # Inicializa em predict() com o modelo correto
        self.detection_merger = DetectionMerger()
        self.nms_processor = NMSProcessor()
        self.inverted_image = InvertedImage()
        self.convert_yolo = ConvertYolo()

    def predict(self) -> None:
        """
        Método para imitar o comportamento de `YOLO.predict()` para o modelo Asahi. 
        """
        results_list = []

        runconfig = self._getRunConfig()
        model = self._getModel()
        LS = runconfig.ls 

        self.detection_runner = PatchInferenceRunner(model)

        self.inverted_image.inverted(runconfig.imagesDir)
        images = [str(f) for f in runconfig.imagesDir.glob("*.*") if f.suffix.lower() in [".jpg", ".jpeg", ".png"]]
        # LS = self.__calculate_LS(runconfig.restrict_size, runconfig.l)

        for img_path in images:
            image = cv2.imread(img_path)
            patches = self.patch_divider.divide(image, LS)

            all_detections, offsets = [], []
            for patch, offset in patches:
                detections = self.detection_runner.run(patch)
                all_detections.append(detections)
                offsets.append(offset)

            combined = self.detection_merger.merge(all_detections, offsets)
            final_dets = np.array(self.nms_processor.apply(combined))

            h , w = image.shape[:2]
            converted_boxes = []
            for det in final_dets:
                xc, yc, bw, bh, conf, cls = self.convert_yolo.convert_to_yolo_format(det, w, h)
                converted_boxes.append([xc, yc, bw, bh, conf, cls])

            tensor_boxes = torch.tensor(converted_boxes) if len(converted_boxes) > 0 else None

            results = Results(orig_img=image.copy(), path=img_path, boxes=tensor_boxes, names=model.names)
            results_list.append(results)

        self._setResults(list(results_list))



    # virou um método estático de UltralicsRunConfiguration
    # def __calculate_LS(self, restrict_size, l):
    #     return restrict_size * (4 - 3 * l) + 1
