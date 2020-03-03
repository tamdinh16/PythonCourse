import random                                           #This is needed for the price to work.
                                                        #Because the way to do mutual fund is the same as stock, I will only comment for stock.
class Stock(object):
    def __init__(self, price, name):
        self.price = price
        self.name = name
 
    def Stock_SellingPrice(self):
        return self.price * random.uniform(0.5, 1.5)


class MutualFund(object):
    def __init__(self, name):
        self.name = name
        self.price = 1
 
    def MF_SellingPrice(self):
        return self.price * random.uniform(0.9, 1.2)

        
class Portfolio(object):
    def __init__(self):
        self.CashBalance = 0
        self.transaction = ""
        self.StockBalance = {}
        self.MFBbalance = {}
         
    def history(self):
        print(self.transaction)

    def addCash(self, amount):
        self.CashBalance = self.CashBalance + amount
        self.transaction = self.transaction + (f"Cash balance is increased by an amount of {amount}")
        
    def withdrawCash(self, amount):
        self.CashBalance = self.CashBalance - amount
        self.transaction = self.transaction + (f"Cash balance is decreased by an amount of {amount}")
          
    def buyStock(self, share_amount, stock):                            
        totalstockbuy = share_amount * stock.price
        
        if totalstockbuy > self.CashBalance:                      
            print("What you buy exceeds the money you currently have. Please buy less.")
     
        elif (totalstockbuy <= self.CashBalance) & (share_amount % 1 == 0):
            self.CashBalance -= totalstockbuy
            self.StockBalance = {"symbol": stock.name, "shares": share_amount, "type of stock": stock}          #when I buy a stock, I want to define my StockBalance in a way that I know what type of stock it is, how many shares it have and its symbol.
            self.transaction = self.transaction + (f"Buy {share_amount} shares of stock {stock}. Cash balance is decreased by an amount of {totalstockbuy}.")
            self.StockBalance = {**self.StockBalance}                       #I want to update my StockBalance (in a dictionary way). Unfortunately, this does not work.
                       
        elif (totalstockbuy <= self.CashBalance) & (share_amount % 1 != 0):
            print("Stocks can only be purchased as whole units. Please enter a whole number of shares.")
  
        else:
            print("Invalid input.")
   
    def sellStock(self, name, share_amount):
        if name != self.StockBalance["symbol"]:             #I have to search if the stock is available in my Stock Balance to sell.
            print("This stock is not available.")

        elif (name == self.StockBalance["symbol"]) & (share_amount > self.StockBalance["shares"]):      #The stock is available but I cannot sell an amount that is higher than what I currently have.
            print ("You cannot sell something you don't have enough.")
             
        elif (name == self.StockBalance["symbol"]) & (share_amount <= self.StockBalance["shares"]):     #The stock is available and I have enough shares to sell.
            self.StockBalance["shares"] -= share_amount
            stock_to_sell = self.StockBalance["type of stock"]
            totalstocksell = share_amount * stock_to_sell.Stock_SellingPrice()
            self.CashBalance += totalstocksell
            self.transaction = self.transaction + (f"Sell {share_amount} shares of stock {stock_to_sell}. Cash balance is increased by an amount of {totalstocksell}.")
            
        else:
            print("Undefined.")

    def buyMutualFund(self, share_amount, mutualfund):
        totalmfbuy = share_amount * 1
        
        if totalmfbuy > self.CashBalance:
            print("What you buy exceeds the money you currently have. Please buy less.")

        elif (totalmfbuy <= self.CashBalance) & (share_amount % 1 != 0):
            self.CashBalance -= totalmfbuy
            self.MFBalance = {"symbol": mutualfund.name, "shares": share_amount, "type of mutual fund": mutualfund}
            self.transaction = self.transaction + (f"Buy {share_amount} shares of mutual fund {mutualfund}. Cash balance is decreased by an amount of {totalmfbuy}")
            
        elif (totalmfbuy <= self.CashBalance) & (share_amount % 1 == 0):
            print("Mutual funds can only be purchased as fractional shares. Please enter a fractional number of shares.")

        else:
            print("Invalid input.")

    def sellMutualFund(self, name, share_amount):
        if name != self.MFBalance["symbol"]:
            print("This mutual fund is not available.")

        elif (name == self.MFBalance["symbol"]) & (share_amount > self.MFBalance["shares"]):
            print ("You cannot sell something you don't have enough.")
              
        elif (name == self.MFBalance["symbol"]) & (share_amount <= self.MFBalance["shares"]):
            self.MFBalance["shares"] -= share_amount
            mf_to_sell = self.MFBalance["type of mutual fund"]
            totalmfsell = share_amount * mf_to_sell.MF_SellingPrice()
            self.CashBalance += totalmfsell
            self.transaction = self.transaction + (f"Sell {share_amount} shares of mutual fund {mf_to_sell}. Cash balance is increased by an amount of {totalmfsell}.")
                            
        else:
            print("Undefined.")
    
# The problem of my solution is that because my Stock Balance is not updated, it cannot remember the previous stocks that I buy.
# For example, s = Stock(5, "AAA"). I bought it. Then, t = Stock(6, "BBB"). I also bought it. My Stock Balance at that time only shows t, not s.
# Hence, after I bought t and I want to sell s, it will say "The stock is not available".
# I don't know why the code does not work. I know that there are other solutions such as turning dict into strings and vice versa. However, I don't want that because I want to update my dict, which is cleaner and easier to follow. Also, I don't have enough time to really look into other solutions. Each code is everything new to me. 
# I hope my solutions are not bad, or "reckless".
# Thank you.
