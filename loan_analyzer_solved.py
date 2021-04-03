# coding: utf-8
import csv
from pathlib import Path

# this is a loan analyzer program
# loan information:

loan_costs = [500, 600, 200, 1000, 450]


#to calculate the total number of loans

def number_of_loans(loan_costs):
    total_number_of_loans = len(loan_costs)
    print(f"The are {total_number_of_loans} loans in the list.")

number_of_loans([500, 600, 200, 1000, 450])

#to calculate the total value of the loans

def value_of_loans(loan_costs):
    total_value_of_loans = sum(loan_costs)
    print ("The total value of loans is:", total_value_of_loans)

value_of_loans([500, 600, 200, 1000, 450])        

# to calculate the average value of the loans

def average(loan_costs):
    average_loan_price = sum(loan_costs) / len(loan_costs)
    print("The average loan amount is:", average_loan_price)

average([500, 600, 200, 1000, 450])    



"""Part 2: Analyze Loan Data.

Analyze the following to determine the investment evaluation.

    **Present Value
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.
    **If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# this is the loan data
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# extracting the Future Value and Remaining Months on the loan.
# Printing each variable

future_value = loan.get("future_value")
print("The future value is:", future_value)

remaining_months = loan.get("remaining_months")
print("The remaining months are:", remaining_months)

# Using the monthly formula for Present Value to calculate a "fair value" of the loan.
# Formula: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
# We will use a minimum required return of 20% as the discount rate.
discount_rate = .20

fair_value = future_value / (1 + discount_rate/12) ** remaining_months
print("The Present Value of the loan is: $", fair_value)

# print("The Present Value of the loan is: $", present_value)

# Using conditional statements to determine if it makes sense to buy the loan at its cost

if fair_value >= future_value:
    print("The loan is worth at least the cost to buy it.")
else:
    print("The loan is too expensive and not worth the price.")




#Part 3:  Financial Calculations.


# calculating the present value for the loan given the following loan data:
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
    
}

def npv(future_value, remaining_months, annual_discount_rate):
    present_value_home = future_value / (1 + annual_discount_rate) ** remaining_months
    return present_value_home

present_value_home= npv(future_value =1000, remaining_months = 12, annual_discount_rate = .20)

# Used the function to calculate the present value of the new loan given below.
# Used an `annual_discount_rate` of 0.2 for this new loan calculation

print(f"The present value of the loan is: $ {present_value_home: .2f}")
                                           

#Part 4: Conditionally filter lists of loans. For this exercise, I will filter loans equal or lesser than $500

#loan data:

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]


# This is an empty list called `inexpensive_loans`
inexpensive_loans = []

# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    if loan["loan_price"] < 500:
        inexpensive_loans.append(loan)


# To print the `inexpensive_loans` list
print("Inexpensive Loans List:", inexpensive_loans)


"""Part 5: Saving the results.

Output this list of inexpensive loans to a csv file
    
"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Used the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
csvpath = Path("list_of_inexpensive_loans_.csv")
with open (csvpath, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(header)
    for loan in inexpensive_loans :
        csvwriter.writerow(loan.values())

# end of code