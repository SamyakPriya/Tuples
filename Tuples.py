
month = ("January", "February", "March", "April", "May", "June", "July", "August", "September",
         "October", "November", "December")

profits = (20000,45000,78000,98000,13000,564000,56000,54000,10000,30000,70000,90000)


max_profit = max(profits)
max_profit_index = profits.index(max_profit)
print(max_profit_index)

max_profit_month = month[max_profit_index]
print("The maximun profit of " + str(max_profit)+ " was recorded in the month of "
      + str(max_profit_month))

min_profit = min(profits)
min_profit_index = profits.index(min_profit)
print(min_profit_index)

min_profit_month = month[min_profit_index]
print("The minimum profit of " + str(min_profit)+ " was recorded in the month of "
      + str(min_profit_month))
