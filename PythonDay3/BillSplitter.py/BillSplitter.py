BillAmt = float(input("Enter the bill amount:"))
HeadCount = int(input("Enter the head count:"))
PerPerson = BillAmt / HeadCount
Service = int(input("How was the service in a scale of 0-5:"))
if Service == 5:
    Tip = PerPerson * 0.20
elif Service == 4:
    Tip = PerPerson * 0.15
elif Service == 3:
    Tip = PerPerson * 0.10
else:
    Tip = PerPerson * 0.00

TotalPerPerson = PerPerson + Tip
print (f"The total amount per person is: ${TotalPerPerson:.2f}")

