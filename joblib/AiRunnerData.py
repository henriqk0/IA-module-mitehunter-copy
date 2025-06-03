from dataclasses import dataclass

@dataclass
class AiRunnerData:
    """
    Classe que armazena os dados necessários para fazer a predição.
    
    Args:
        Predator_0__SpiderM_1a5: Integer representando a porcentagem de folíolos com zero ácaros predadores e um a cinco ácaros de duas manchas;
        Predator_0__SpiderM_6a9: Integer representando a porcentagem de folíolos com zero ácaros predadores e seis a nove ácaros de duas manchas;
        Predator_0__SpiderM_10more: Integer representando a porcentagem de folíolos com zero ácaros predadores e dez ou mais ácaros de duas manchas;
        Predator_0__SpiderM_0: Integer representando a porcentagem de folíolos com zero ácaros predadores e zero ácaros de duas manchas;
        Predator_1more__SpiderM_0: Integer representando a porcentagem de folíolos com um ou mais ácaros predadores e zero ácaros de duas manchas;
        Predator_1more__SpiderM_1more: Integer representando a porcentagem de folíolos com um ou mais ácaros predadores e um ou mais ácaros de duas manchas.
    Return: Uma string contendo a ação sugerida a ser tomada.
    """
    
    __Predator_0__SpiderM_1a5: int = 0
    __Predator_0__SpiderM_6a9: int = 0
    __Predator_0__SpiderM_10more: int = 0
    __Predator_0__SpiderM_0: int = 0
    __Predator_1more__SpiderM_0: int = 0
    __Predator_1more__SpiderM_1more: int = 0
    
    def incrementValue(self, thetranicus: int, californicus: int, macropilis: int) -> None:
        """
        Aumenta o valor das condições baseado nas regras de negócio de quantidades de ácaros por folíolo.

        Args:
            thetranicus (int): quantidade de ácaro rajado no folíolo.
            californicus (int): quantidade de ácaro californicus no folíolo.
            macropilis (int): quantidade de ácaro macropilis no folíolo.
        """
        
        if(thetranicus + californicus + macropilis == 0):  # Nenhum ácaro no folíolo
            self.__Predator_0__SpiderM_0 += 1
        elif(californicus + macropilis == 0):  # Caso não tenha ácaros predadores...
            if(thetranicus <= 5): 
                self.__Predator_0__SpiderM_1a5 += 1
            elif(thetranicus <= 9): 
                self.__Predator_0__SpiderM_6a9 += 1
            else: 
                self.__Predator_0__SpiderM_10more += 1
        elif(thetranicus <= 0): 
            self.__Predator_1more__SpiderM_0 += 1  # O elif anterior garante que existe pelo menos um ácaro predador nas amostras
        else: 
            self.__Predator_1more__SpiderM_1more += 1 
    
    # may not return pure integers, but since the network was trained with 2-decimal floats, then there seems to be no problem
    @property
    def Predator_0__SpiderM_1a5(self) -> int:
        return round(( self.__Predator_0__SpiderM_1a5 / self.totalFolieleAnilisys ) * 100, 2)
    
    @property
    def Predator_0__SpiderM_6a9(self) -> int:
        return round((self.__Predator_0__SpiderM_6a9 / self.totalFolieleAnilisys) * 100, 2)
    
    @property
    def Predator_0__SpiderM_10more(self) -> int:
        return round((self.__Predator_0__SpiderM_10more / self.totalFolieleAnilisys) * 100, 2)
    
    @property
    def Predator_0__SpiderM_0(self) -> int:
        return round((self.__Predator_0__SpiderM_0 / self.totalFolieleAnilisys) * 100, 2)
    
    @property
    def Predator_1more__SpiderM_0(self) -> int:
        return round((self.__Predator_1more__SpiderM_0 / self.totalFolieleAnilisys) * 100, 2)
    
    @property
    def Predator_1more__SpiderM_1more(self) -> int:
        return round((self.__Predator_1more__SpiderM_1more / self.totalFolieleAnilisys) * 100, 2)
    
    @property
    def totalFolieleAnilisys(self) -> int:
        return (self.__Predator_0__SpiderM_1a5 + self.__Predator_0__SpiderM_6a9 + self.__Predator_0__SpiderM_10more + self.__Predator_0__SpiderM_0 + self.__Predator_1more__SpiderM_0 + self.__Predator_1more__SpiderM_1more)
    
    def toList(self) -> list[list[int]]:
        """
        Pega as informações dos resultados e converte em uma lista.

        Returns:
            list[list[int]]: lista com os resultados da distribuição dos ácaros pela regra de negócio.
        """
        return [[self.Predator_0__SpiderM_1a5, self.Predator_0__SpiderM_6a9, self.Predator_0__SpiderM_10more, self.Predator_0__SpiderM_0, self.Predator_1more__SpiderM_0, self.Predator_1more__SpiderM_1more]]
    
        