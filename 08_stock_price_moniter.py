# Hint: Market conditions are unpredictable - you monitor until something happens
stock_symbol = input("Enter stock symbol: ")
current_price = float(input("Enter starting price: "))
target_price = float(input("Enter target price: "))
stop_loss = float(input("Enter stop-loss price: "))
price_updates = 0
alert_triggered = False
# Think: What approach handles unpredictable market timing?
# Your monitoring logic here

while current_price < target_price: # create a while loop for the variable
     current_price = float(input("Enter starting price: ")) #create multiple if statements to see if the current price is zero(Error), if the currentprice is less than stop_loss(Stop loss hit) or greater than target price(Target hist)
     if current_price == 0:
      print("ERROR")
      break
     if current_price <= stop_loss:
      print("Stop-loss hit")
      break
     if current_price >= target_price:
      print("Target hit")
      break
         




