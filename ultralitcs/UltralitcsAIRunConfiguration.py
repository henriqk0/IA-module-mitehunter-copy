from pathlib import Path, PosixPath

class UtralitcsAIRunConfiguration:
    """
    Classe responsável por armazenar as configuração de execução da predição.
    """
    
    def __init__(self, imagesDir: Path, stream: bool, confiance: float, iou: float) -> None:
        """
        Args:
            imagesDir (Path): diretório com as imagens que deseja-se predizer.
            stream (bool): Se verdadeiro, trata a fonte de entrada como um fluxo contínuo para previsões.
            confiance (float): margem de confiança aceitável para cada objeto identificado.
            iou (float): Intersecção sobre Unidão desejada.
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
        
        