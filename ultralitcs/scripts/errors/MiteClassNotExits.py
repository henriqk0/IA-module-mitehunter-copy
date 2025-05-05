class ErrorMiteClassNotExits(Exception):
    """
    Erro Personalizado para quando a classe de ácaro passada nfor desconhecida.
    """
    def __init__(self, miteCode: int) -> None:
        Exception.__init__(self)
        self.__miteCode = miteCode
        
    def __str__(self) -> str:
        return super.__str__() + f"\nMiteCode: {self.__miteCode}"    
    