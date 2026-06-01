stock_price={
        "APPLE":200,
        "MICROSOFT":345,
        "AMAZON":567,
        "SAMSUNG":136,
        "LENOVO":456
     }

print("-----stock tracker-----")
stock_name =input("enter the stock name :".upper())
if stock_name in stock_price:
    quantity=int(input(f"how many shares of {stock_name} are owned :-"))
    price= stock_price[stock_name]
    total_value_of_stocks = price*quantity

    print("-------details found-------")
    print(f"Stock_name: {stock_name}")
    print(f"Price per share: ${quantity}")
    print(f"Current Value: ${total_value_of_stocks}")
    
else:
    print(f"Sorry, {stock_name} is not in our records.")

printrint("----save a file-----")
Saving_file = input("Save as (1) TXT or (2) CSV? : ")

if Saving_file == "1":
    with open("report.txt", "a") as f:
        f.write(f"{stock_name}: {quantity} shares - Total ${total_value_of_stocks}\n")
    print("Saved to report.txt")

elif Saving_file == "2":
    with open("report.csv", "a") as f:
        f.write(f"{stock_name},{quantity},{total_value_of_stocks}\n")
    print("Saved to report.csv")
    

