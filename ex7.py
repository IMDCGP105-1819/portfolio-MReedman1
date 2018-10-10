annual_salary = float(input('Enter your annual salary:'))
portion_saved = float(input('Enter the amount saved as decimal:'))
total_cost = float(input('Dream House price:'))
portion_deposit = 0.20
current_savings = 0
monthly_salary = annual_salary/12
r = 0.04
months = 0
while(current_savings < portion_deposit):
    current_savings += annual_salary * r / 12
    current_savings += monthly_salary * portion_saved
    months = months + 1
print("Number of months:",(months))
