def calculateBill(b,tp):
    
    total = b * (1 + (0.01*tp))
    return total

bill = int(input("enter the Bill amount: "))
tipPerc = float(input("enter the Tip amount: "))

total = calculateBill(bill,tipPerc)

print(f"\n\n Total bill with tip:{total} ")
print(f"Total tip: {total-bill} ")