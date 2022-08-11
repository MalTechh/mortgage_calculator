max_or_pay = input("Are you searching for the maximum amount you can borrow or \n the monthly payment for a certain mortgage?: (Enter 1 for monthly payment or 2 for max amount)")
loan_length = int(input("Are you looking for a 15 or 30 year mortgage?:"))
num_payments = loan_length *12
credit_score = int(input("What is your current credit score?:"))
income = int(input("What is your annual gross income?:"))
def monthly_interest_rate(credit_score):
    if credit_score<400:
        interest = .08
        return interest/12
    elif credit_score<650:
        interest = .06
        return interest/12
    elif credit_score<750:
        interest = .045
        return interest/12
    elif credit_score<850:
        interest = .04
        return interest/12
    elif credit_score>850 or credit_score<400:
        interest = "Your credit score is not in an applicable range! Try again once it is between 400 and 850."
        return interest
def max_amount(interest,num_payments,income):
    max_payment = income/36
    amount = ((max_payment*((1+interest)**num_payments-1))/(interest*(1+interest)**num_payments))
    print("Your interest will be "+ str(interest*100) + "%, and you can take out a maximum of $"+ str(int(round(amount,0))))
def monthly_payment(interest,num_payments):
    house_price = int(input("How expensive is the house you are buying?:"))
    payment = ((interest *house_price)*((1+interest)**num_payments))/((1+interest)**num_payments-1)
    print("Your interest will be "+ str(interest*100) + "%, and this will give you a monthly payment of $" + str(round(payment,2)))
if int(max_or_pay) == 2:
    max_amount(monthly_interest_rate(credit_score), num_payments, income)
elif int(max_or_pay) == 1:
    monthly_payment(monthly_interest_rate(credit_score), num_payments)
else:
    print("Something went wrong")
