from abc import ABC, abstractmethod
from typing import Any


class IPredictableModelAdapter(ABC):
    """
    Simulação de uma interface em python.
    Descreve os métodos que um Adaptador de Modelos de Predição deve conter para que possa ser utilizado pela classe AIRunner.
    """
    def __init__(self) -> None:
        ABC.__init__(self)
        
    @abstractmethod
    def predict(self) -> None:
        """
        Realiza a predição.
        """
        pass
    
    @abstractmethod
    def parallelPredict(self) -> None:
        """
        Realiza a predição de forma paralelizada.
        """
        pass
        
    @abstractmethod
    def savePrediction(self) -> None:
        """
        Salva o resultado das predições
        """
        pass
    
    @abstractmethod
    def getResults(self) -> Any:
        """
        Pega o resultado das perdições como um objeto interno da biblioteca utilizada.
        Exemplo: a predição de um objeto do tipo ultralitycs.YOLO é ultrailitycs.results.Rulst. Dessa forma, esse método deve retornar esse objeto, ou algum outro objeto da camada da biblioteca utilizada que seja relevante para o contexto de uso interno.

        Returns:
            Any: qualquer objeto Python.
        """
        pass
    
    @abstractmethod
    def returnData(self) -> Any:
        """
        Retorna os resultados da predição em algum tipo de objeto Python conhecido pelo usuário.

        Returns:
            Any: qualquer objeto Python estabelecido como obrigatório de conhcimento pelo usuário.
        """
        pass
    
    