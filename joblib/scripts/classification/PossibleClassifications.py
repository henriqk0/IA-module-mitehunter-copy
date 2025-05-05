from typing import Any
from enum import Enum


class PossibleClassifications(Enum):
    """
    Classe responsável por armazenar a descrição textual das possíveis classificações de infestação.
    """
    
    SITUACAO_CONTROLADA = "Continuar realizando amostras a cada 7 dias"
    SITUACAO_PARCIAL = "Liberar ácaros predadores nas reboleiras"
    SITUACAO_CALIMITICA = "Intervenção química"
    
    @staticmethod
    def buildByNumber(number: int):
        """
        Determina a classificação baseada em um número

        Args:
            number (int): número da classe de classificação

        Returns:
            _type_: um objeto do tipo PossibleClassification com a classificação determinada. Para acessar sua descrição textual utilize ".value"
        """
        match(number):
            case 0: return PossibleClassifications.SITUACAO_CONTROLADA
            case 1: return PossibleClassifications.SITUACAO_PARCIAL
            case 2: return PossibleClassifications.SITUACAO_CALIMITICA
            
            