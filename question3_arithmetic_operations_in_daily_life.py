#Task 1 -  Calculate the total cost of three items you'd commonly find in a grocery store, given their individual prices. For example, what would be the cost of bread, peanut butter, and jelly be? Prices don't need to be realistic!
print("**********************************Grocery Total************************************")
# set local to format pricing correctly
import locale
locale.setlocale(locale.LC_ALL, 'en_US')

# set prices for items- using a dictionary so the code will work regardless of # of items added to it
items_prices = {
    'Wonder Bread': 3.45,
    'Skippy Peanut Butter': 4.50,
    'Smuckers Jelly': 3.75
}
#calculate total cost of dictionary items
total = sum(items_prices.values())
#print total cost
print (f"The total cost of all the items is: {locale.currency(total,grouping=True)}")

print("**********************************Savings Account************************************")

#Task 2-  If you have a savings account with a particular initial amount and a fixed yearly interest rate, calculate the total amount in your account after a year. So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. For the example the expected outcome would be $10,700.

starting_amount = (input("What is the starting amount in your savings account? "))
interest_rate = (input("What is the interest rate on your savings account? Whole number only, no percentage sign. "))
#convert input to float
starting_amount = float(starting_amount)
input_interest_rate = float(interest_rate)
#convert whole float to proper percentage
final_interest_rate = input_interest_rate / 100
#calculate total amount after a year
total_amount = starting_amount + (starting_amount * final_interest_rate)
#print total amount
print(f"With a starting value of {starting_amount} and an interest rate of {interest_rate}%, the total amount in your account after a year is: {locale.currency(total_amount,grouping=True)}")
print("*********************************************************************************")

