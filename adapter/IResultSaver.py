from abc import ABC, abstractmethod

from typing import Any


class IResultsSaver(ABC):
    """
        Simulação de Interface no Python.
        Determina os métodos que uma classe que salva resultados deve conter.    
    """
    def __init__(self) -> None:
        ABC.__init__(self)
    
    @abstractmethod
    def save(self, results: list[Any]) -> None: 
        """
        Salva uma lista de resultados.

        Args:
            results (list[any]): lista de qualquer objeto Python que seja entendido pela implementação do método.
        """
        pass 
    
    