from pathlib import Path

from .UltralitcsAIAdapter import UtralitcsAIAdapter
from .scripts.io.LoadModel import LoadModel
from .scripts.io.ResultsSaver import ResultsSaverInText
from .UltralitcsAIRunConfiguration import UtralitcsAIRunConfiguration
from mitehunter.settings.default import IA_DIR


class UltralitcsAIAdapterFactory:
    """
    Classe responsável por construir as instâncias dos adaptadores da ultralitics.
    """
    @staticmethod
    def buildBestAdapter(imagesDir: Path) -> UtralitcsAIAdapter:
        """
        Construi o adapter com as melhores configurações encontradas.

        Args:
            imagesDir (Path): diretório com as imagens onde deseja-se fazer a predição.

        Returns:
            UtralitcsAIAdapter: instância do melhor adaptador da ultralitycs.
        """
        return UtralitcsAIAdapter(
            LoadModel.loadBestYOLOModel(Path(IA_DIR)),
            UtralitcsAIRunConfiguration(
                imagesDir = imagesDir,
                stream = True,
                confiance = 0.1,
                iou = 0.45
                ),
            
            ResultsSaverInText(
                savePath = "",
                saveFilePrefix = "image_",
                debug = False,
                log = False,
                force = False
                )
        )
        
        