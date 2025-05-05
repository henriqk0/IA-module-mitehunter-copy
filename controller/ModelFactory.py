from enum import Enum
from pathlib import Path
from dataclasses import dataclass

from ..adapter.AIRunner import AIRunner
from ..joblib.AiRunnerData import AiRunnerData
from ..joblib.JoblibAIAdapterFactory import JoblibAIAdapterFactory
from ..ultralitcs.scripts.io.LoadModel import LoadModel
from ..ultralitcs.UltralitcsAIAdapter import UtralitcsAIAdapter
from ..ultralitcs.UltralitcsAIAdpaterFactory import UltralitcsAIAdapterFactory
from ..ultralitcs.UltralitcsAIRunConfiguration import UtralitcsAIRunConfiguration


class ImagePredctionModels(Enum):
    YOLO = 0


@dataclass
class ImageModelOptions:
    model: ImagePredctionModels
    

class ModelFactory:
    @staticmethod
    def buildDefaultImageModel(imagesDir: Path) -> AIRunner:
        return AIRunner(UltralitcsAIAdapterFactory.buildBestAdapter(imagesDir))
        
    @staticmethod
    def buildImageModel(model: ImagePredctionModels, imagesDir: Path, confiance: float, iou: float) -> AIRunner:
        imagemModel = None
        
        match model:
            case ImagePredctionModels.YOLO:
                imagemModel = UtralitcsAIAdapter(
                    LoadModel.loadBestYOLOModel(ModelFactory.aiDir),
                    UtralitcsAIRunConfiguration(imagesDir, True, confiance, iou)
                )
                
        return AIRunner(imagemModel)
    
    @staticmethod
    def buildDefaultActionModel(modelPath: Path, predictionData: AiRunnerData) -> AIRunner:
        return AIRunner(
            JoblibAIAdapterFactory.buildBest(
                modelPath, 
                predictionData
            )  
        ) 
        
        