cost=int(input("Enter the cost of the item: "))
if cost>100000:
  print("You have 15% of TAX")
elif cost>50000 and cost<=100000:
  print("You have 10% of TAX")
elif cost<=50000:
  print("You have 5% of TAX")
else:
  print("You have no TAX")
