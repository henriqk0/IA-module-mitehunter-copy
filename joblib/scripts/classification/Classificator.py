from typing import Any
from .PossibleClassifications import PossibleClassifications


class Classificator:
    """
    Classe responsável por realizar a classificação dos ácaros
    """
    @staticmethod
    def classifing(predictingValue: Any) -> str:
        """
        Retorna a descrição textual da classificação

        Args:
            predictingValue (Any): valor retornado pela joblib.predict (a interface dessa lib é estranha e mal documentada, então a definição da tipagem fica irregular)

        Returns:
            str: texto com a descrição da classificação
        """
        # predictingValue indica a classe retornada pela classificação. Sim, fica estranho assim mesmo, tenha fé no processo.
        return PossibleClassifications.buildByNumber(predictingValue).value
    
    