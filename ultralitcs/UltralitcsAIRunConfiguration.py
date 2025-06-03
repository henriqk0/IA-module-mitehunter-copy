from pathlib import Path, PosixPath

class UtralitcsAIRunConfiguration:
    """
    Classe responsável por armazenar as configuração de execução da predição.
    """
    
    def __init__(self, imagesDir: Path, stream: bool, confiance: float, iou: float, restrict_size: int=0, l:float=0) -> None:
        """
        Args:
            imagesDir (Path): diretório com as imagens que deseja-se predizer.
            stream (bool): Se verdadeiro, trata a fonte de entrada como um fluxo contínuo para previsões.
            confiance (float): margem de confiança aceitável para cada objeto identificado.
            iou (float): Intersecção sobre União desejada.
        """
        assert(isinstance(imagesDir, (Path, PosixPath)))
        assert(type(confiance) == float)
        assert(type(iou) == float)
        assert(0 < confiance < 1)
        assert(0 < iou < 1)
        
        self.__imagesDir = imagesDir
        self.__stream: bool = stream
        self.__confiance: float = confiance
        self.__iou: float = iou
        self.__restrict_size: int = restrict_size
        self.__l: float = l
    
    @property
    def imagesDir(self) -> Path:
        return self.__imagesDir
    
    @property
    def stream(self) -> bool:
        return self.__stream
    
    @property
    def confiance(self) -> float:
        return self.__confiance
    
    @property
    def iou(self) -> float:
        return self.__iou
    
    @property
    def restrict_size(self) -> int:
        return self.__restrict_size
    
    @property
    def l(self) -> float:
        return self.__l

    @property
    def ls(self) -> float:
        return self.__restrict_size * (4 - 3 * self.__l) + 1
        
        