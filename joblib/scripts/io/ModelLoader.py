from pathlib import Path
from os import path
import joblib


class ModelLoader:
    """
    Classe responsável por lidar com operações de IO para ler o modelo.

    Raises:
        FileNotFoundError: caso o arquivo do modelo de IA não seja encontrado.
    """

    __joblibDir: str = "joblib"
    __modelsDir: str = "modelo"
    __bestModelName: str = "smote_original_RF_entropy.joblib"
    
    @staticmethod
    def loadBestModel(aiDir: Path):
        """
        Método que carrega o arquivo com o melhor peso possível

        Args:
            aiDir (Path): caminho referente à pasta da IA.

        Raises:
            FileNotFoundError: caso o arquivo de pesos não tenha sido encontrado.

        Returns:
            Any: a joblib não possui um forma de retorno padrão, então retorna qualquer objeto Python.
        """
        bestModelPath = aiDir / ModelLoader.__joblibDir / ModelLoader.__modelsDir / ModelLoader.__bestModelName
        
        if(path.exists(bestModelPath)):
            return joblib.load(bestModelPath)
        
        raise FileNotFoundError(f"Atention, the file {bestModelPath} not exists!")      