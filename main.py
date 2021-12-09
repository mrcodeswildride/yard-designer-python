print()

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
material = input("Choose a material [dirt/grass/pavers]: ")

area = length * width

if material == "dirt":
  cost_per_sqft = 1
elif material == "grass":
  cost_per_sqft = 2
elif material == "pavers":
  cost_per_sqft = 3

total_cost = area * cost_per_sqft

print(f"\nArea:\t\t{area} sqft")
print(f"Cost per sqft:\t${cost_per_sqft}")
print(f"Total cost:\t${total_cost}")
