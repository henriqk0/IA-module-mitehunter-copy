from ultralytics import YOLO

from pathlib import Path

from os import path


class LoadModel:
    """
    Classe responsável por lidar com operações IO pertinetnes à leitura do arquivo de pesos dos modelos.
    """

    __ultraliticsDir: str = "ultralitcs"
    __modelsDir: str = "modelo"
    __bestModelName: str = "best.pt"
    
    @staticmethod
    def loadBestYOLOModel(aiDir: Path) -> YOLO:
        """
        Carrega o melhor arquivo de pesos e instancia um modelo do tipo YOLO

        Args:
            aiDir (Path): caminho referente ao local onde a pasta IA está.

        Raises:
            FileNotFoundError: caso o arquivo do modelo não tenha sido encontrado.

        Returns:
            YOLO: Objeto do tipo ultralitycs.YOLO
        """
        bestModelPath = aiDir / LoadModel.__ultraliticsDir / LoadModel.__modelsDir / LoadModel.__bestModelName
        
        if(path.exists(bestModelPath)):
            return YOLO(aiDir / bestModelPath)
        
        raise FileNotFoundError(f"Atention, the file {bestModelPath} not exists!")      
        
        