from coin_acceptor import CoinAcceptor

def Main():
    print("Program starting.")

    coin_acceptor = CoinAcceptor()

    while True:
        print("1 - Insert coin")
        print("2 - Show coin")
        print("3 - Return coin")
        print("0 - Exit program")
        choice = input("Your choice: ")

        if choice == "1":
            coin_acceptor.insertCoin()
            print("Coin inserted.")
        elif choice == "2":
            print(f"Currently '{coin_acceptor.getAmount()}' coins in coin acceptor")
        elif choice == "3":
            returned = coin_acceptor.returnCoins()
            print(f"Coin acceptor returned '{returned}' coins.")
        elif choice =="0":
            print("Program ending.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Main()