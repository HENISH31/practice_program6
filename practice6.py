balance=int(input("Enter your account balance: "))
withdraw=int(input("Enter amount to withdraw: "))
if withdraw<=balance:
    if withdraw%100==0:
        balance-=withdraw
        print("Please collect your cash")
        print("Thank you for banking with us.")
        print("Remaining balance:",balance)
    else:
        print("Please enter the amount in multiples of 100")
else:
    print("Insufficient balance")