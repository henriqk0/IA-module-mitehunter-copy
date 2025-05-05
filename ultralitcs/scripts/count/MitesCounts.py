from dataclasses import dataclass
from enum import Enum

from ..errors.MiteClassNotExits import ErrorMiteClassNotExits


class ClassesMatch(Enum):
    """
    Classe com os tpos de ácaros e os IDs deles na IA da ultralitcs.
    """
    NEOSEIULUS_CALIFORNICUS = 0
    PHYTOSEILUS_MACROPILIS = 1
    THETRANICUS_URTICAE = 2

    
@dataclass
class MitesCounts:
    """
    Classe responsável por arazenar a contagem de ácaros em um folíolo.
    """
    thetranicusUrticae: int = 0
    phytoseilusMacropilis: int = 0
    neoseiulusCalifornicus: int = 0
    
    def incremantCount(self, clazz: int):
        """
        Aumenta a contagem interna dos ácaros baseado na classe passada.

        Args:
            clazz (int): id da classe do ácaro.

        Raises:
            ErrorMiteClassNotExits: caso seja passado um id desconhecido. Caso ocorra indaca a potencial necessidade de adpatação no código.
        """
        match clazz:
            case ClassesMatch.NEOSEIULUS_CALIFORNICUS.value: self.neoseiulusCalifornicus+=1
            case ClassesMatch.PHYTOSEILUS_MACROPILIS.value: self.phytoseilusMacropilis+=1
            case ClassesMatch.THETRANICUS_URTICAE.value: self.thetranicusUrticae+=1
            case default: raise ErrorMiteClassNotExits(clazz)
