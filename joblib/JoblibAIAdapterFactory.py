from .AiRunnerData import AiRunnerData
from .JobLibAiAdapter import JoblibAiAdapter
from pathlib import Path
from .scripts.io.ModelLoader import ModelLoader

class JoblibAIAdapterFactory:
    """
    Responsável por construir as instâncias do adaptador das iasi de prdição da joblib.
    """
    @staticmethod
    def buildBest(modelPath: Path, predictionData: AiRunnerData) -> JoblibAiAdapter:
        """
        Construi o melhor modelo possível.

        Args:
            predictionData (AiRunnerData): os dados em que deseja-se fazer a predição.

        Returns:
            JoblibAiAdapter: instância do adaptador buscado.
        """
        return JoblibAiAdapter(
            ModelLoader.loadBestModel(modelPath),
            predictionData
        )