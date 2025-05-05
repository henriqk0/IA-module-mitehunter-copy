from ultralytics.engine.model import Model
from ultralytics.engine.results import Results

from .UltralitcsAIRunConfiguration import UtralitcsAIRunConfiguration
from .scripts.io.ResultsSaver import ResultsSaverInText   
from .scripts.count.MitesCounts import MitesCounts

from ..adapter.IPredictableModelAdapter import IPredictableModelAdapter
        
        
class UtralitcsAIAdapter(IPredictableModelAdapter):
    """
    Classe responsável por adptar as IAs da ultralitycs para a interface de comunicação padrão.
    """
    def __init__(self, model: Model, runconfig: UtralitcsAIRunConfiguration, resultsSaver: ResultsSaverInText | None) -> None:
        """
        Args:
            model (Model): modelo da ultralitycs utilizado.
            runconfig (UtralitcsAIRunConfiguration): configurações de execução da predição.
            resultsSaver (ResultsSaverInText | None): classe que determina o modo de salvamento; se for vazio entende-se que não deseja-se salvar os resultads da predição.
        """
        IPredictableModelAdapter.__init__(self)
        
        self.__model = model
        self.__runconfig: UtralitcsAIRunConfiguration = runconfig
        self.__results: list[Results] = None
        self.__resultsSaver = resultsSaver
        
    def predict(self) -> None:
        self.__results = list(self.__model.predict(self.__runconfig.imagesDir, stream=self.__runconfig.stream, conf=self.__runconfig.confiance, iou=self.__runconfig.iou))

    def parallelPredict(self):
        return super().parallelPredict();

    def savePrediction(self):
        if(self.__resultsSaver != None):
            self.__resultsSaver.setSavePath(self.__runconfig.imagesDir)
            self.__resultsSaver.save(self.__results)

    def getResults(self) -> list[Results]:
        return self.__results
    
    def returnData(self) -> list[MitesCounts]:
        mitesCounts: list[MitesCounts] = []

        for i, result in enumerate(self.__results):
            count = MitesCounts()
            for clazz in result.boxes.cls.int():
                count.incremantCount(clazz.int())

            mitesCounts.append(count)
                
        return mitesCounts
    
    
