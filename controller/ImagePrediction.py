from enum import Enum
from pathlib import Path

from .ModelFactory import ModelFactory

from ..ultralitcs.scripts.count.MitesCounts import MitesCounts


class ImagePredictionCallOptions(Enum):
    """
    Classe que contém os possíveis modos de configuração de execução dos modelos.
    """
    BEST = 0


class ImagePrediction:
    """
    Classe que determina a interface de comunicação da camada apps com a camada ultralitycs da camada IA.
    """
    
    @staticmethod
    def call(option: ImagePredictionCallOptions, imageDir: Path) -> list[MitesCounts]:
        """
        Executa a predição na configuração passada em cima do diretório estabelecido.

        Args:
            option (ImagePredictionCallOptions): modo de configuração da execução
            imageDir (Path): macinho para a pasta que deseja-se fazer a predição

        Returns:
            list[MitesCounts]: lista com a contagem de cada tipo de ácaro.
        """
        model = None
        match option:
            case ImagePredictionCallOptions.BEST: model = ModelFactory.buildDefaultImageModel(imageDir)
            
        if(model == None):
            return None
        
        return model.run()
    
    
