class CoinAcceptor:
    def __init__(self):
        self.__amount = 0
        self.__value = 1.0
    
    def insertCoin(self) -> None:
        self.__amount += 1
    
    def getAmount(self) -> int:
        return self.__amount
    
    def returnCoins(self) -> int:
        returned_coins = self.__amount
        self.__amount = 0
        return returned_coins