from typing import Any
import threading

from .IPredictableModelAdapter import IPredictableModelAdapter


class AIRunner:
    """
    Realiza a predição com um modelo de predição fornecido pelo usuário.
    """
    def __init__(self, model: IPredictableModelAdapter) -> None:
        """
        Args:
            model (IPredictableModelAdapter): instância do modelo que deseja-se utilizar para fazer a predição
        """
        self.__model = model
    
    def run(self) -> Any:
        """
        Executa a predição potencialmente salvando os resultados (depende da implementação de cada modelo).

        Returns:
            Any: objeto Python com os resultados da predição. Não possui uma interface padrão, o usuário quem deve conhecer os resultados de retorno.
        """
        self.__model.predict()
        self.__model.savePrediction()
        return self.__model.returnData()
    
    def parallelRun(self) -> Any:
        """
        Executa a predição potencialmente salvando os resultados (depende da implementação de cada modelo) de modo paralelo. Não foi devidamente implementado.

        Returns:
            Any: objeto Python com os resultados da predição. Não possui uma interface padrão, o usuário quem deve conhecer os resultados de retorno.
        """
        # Supõe que a predição já não é feita paralelamente!
        self.__model.parallelPredict()
        self.__model.savePrediction()
        return self.__model.returnData()
