from pathlib import Path

from .ModelFactory import ModelFactory
from ..ultralitcs.scripts.count.MitesCounts import MitesCounts
from ..joblib.AiRunnerData import AiRunnerData

class ActionPrediction:
    """
    Classe que determina a interface de comunicação da camada apps com a camada joblib da camada IA.
    """
    
    @staticmethod
    def call(imageDir: Path, predictionData: list[MitesCounts]) -> str:
        """
        Método que chama o modelo de classificação e retorna o resultado da predição.

        Args:
            predictionData (list[MitesCounts]): conjunto de contagem dos ácaros.

        Returns:
            str: resultado da predição.
        """
            
        trueData = AiRunnerData()
        for data in predictionData: trueData.incrementValue(data.thetranicusUrticae, data.neoseiulusCalifornicus, data.phytoseilusMacropilis)
        
        model = ModelFactory.buildDefaultActionModel(imageDir, trueData)
        return model.run()
    
    