minutes = 0
texts = 0
totalCost = 0

COST_PER_MINUTE = 0.10
COST_PER_TEXT = 0.05
MONTHLY_CHARGE = 10.00

minutes = int(input("Minutes: "))
texts = int(input("Texts: "))

minutesTotalCost = minutes * COST_PER_MINUTE
textsTotalCost = texts * COST_PER_TEXT

totalCost = minutesTotalCost + textsTotalCost + MONTHLY_CHARGE

print(f'Total cost: £{totalCost:.2f}')
