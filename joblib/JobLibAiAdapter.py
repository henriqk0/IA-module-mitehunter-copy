from typing import Any

from .AiRunnerData import AiRunnerData

from .scripts.classification.Classificator import Classificator

from ..adapter.IPredictableModelAdapter import IPredictableModelAdapter


class JoblibAiAdapter(IPredictableModelAdapter):
    """
    Classe responsável por adaptar a IA da joblib para a interface de comunicação padrão.
    """
    def __init__(self, model, predictionData: AiRunnerData) -> None:
        self.__model = model
        self.__data = predictionData
        self.__result: Any = None
        
    def predict(self):
        self.__result = (self.__model.predict(self.__data.toList())[0])
        
    def savePrediction(self):
        # Not implemented :p
        pass

    def parallelPredict(self):
        # Also not implemented :p
        pass
        
    def getResults(self) -> str:
        return self.__results
    
    def returnData(self) -> str:
        return Classificator.classifing(self.__result)

