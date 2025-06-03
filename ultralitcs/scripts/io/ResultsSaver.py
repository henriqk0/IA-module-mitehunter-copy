from ultralytics.engine.results import Results
from pathlib import Path
from os import path, mkdir
import numpy as np
import re



from ....adapter.IResultSaver import IResultsSaver


class ResultsSaverInText(IResultsSaver):
    """
    Classe responsável por lidar com operações de IO pertinentes ao salvamento dos dados de perdição.
    """
    __logDirName: str = "log"
    
    def __init__(self, savePath: Path, saveFilePrefix: str, debug: bool, log: bool, force: bool) -> None:
        """
        Args:
            savePaht (Path): caminho onde o arquivo deve ser salvo
            saveFilePrefix (str): prefixo utilizado para salvar o arquivo
            debug (bool): imprimir código de erro caso ele ocorra?
            log (bool): salvar o código de erro como um log?
            force (bool): tentar forçar o salvamento caso o caminho passado não exista?
        """
        self.__savePath = savePath
        self.__saveFilePrefix = saveFilePrefix
        self.__debug = debug
        self.__log = log
        self.__force = force
        
    def setSavePath(self, savePath: Path) -> None:
        """
        atualiza o caminho de salvamento.

        Args:
            savePath (Path): novo caminho de salvamento.
        """
        self.__savePath = savePath
    
    def save(self, results: list[Results]) -> None:
        if(not path.exists(self.__savePath)):
            if(not self.__force): # Se o caminho não existir e não for forçado o salvamento
                raise FileNotFoundError(f"Attention, the folder {self.__savePath} not exists.")
            mkdir(self.__savePath)
        
        for result in results:
            # regex, e nao enumerate, para obter o índice, pois as imagens podem ser inseridas fora de ordem usando celery
            match = re.search(r'image_(\d+)\.(jpeg|jpg|pgn)', result.path, re.IGNORECASE)
            if match:
                resultIndex = int(match.group(1))

            try:
                detections = result.boxes.data  

                detections[:, 5] = detections[:, 5].int()  # Converte classe para int
                detections_gt = detections[:, [5, 0, 1, 2, 3]]

                output_path = self.__savePath / f"{self.__saveFilePrefix}{resultIndex}.txt"
                np.savetxt(output_path, detections_gt.cpu().numpy(), fmt=['%d', '%.6f', '%.6f', '%.6f', '%.6f'])

            except Exception as e:
                if(self.__debug): # se quiser debugar, imprime o codigo de erro passado
                    print(f"Error while try save results.\nResult index: {resultIndex}\nResult: {result}\nError: {e}")
                if(self.__log): # se quiser salvar o erro como um log
                    try:
                        logDir = self.__savePath / ResultsSaverInText.__logDirName
                        mkdir(logDir) # cria o diretório do log
                        with open(logDir / f"{self.__saveFilePrefix}{resultIndex}_log.txt", "a+") as f: # cria um novo arquivo .txt caso não exista e adiciona novos logs caso já exista
                            f.write(e.__str__())
                    except Exception as oe: # Se der um outro erro ao logo do salvamento do log (aí também fudeu tudo né).
                        print(f"Error while try generate log.\nResult index: {resultIndex}\nResult: {result}\nError: {oe}")
                        
                        