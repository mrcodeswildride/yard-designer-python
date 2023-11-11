print()

length = float(input("Enter the length in feet: "))
width = float(input("Enter the width in feet: "))
grass_unit = float(input("Enter the cost of grass per square foot: $"))
fence_unit = float(input("Enter the cost of fence per linear foot: $"))

area = length * width
grass_total = grass_unit * area

border = (length * 2) + width
fence_total = fence_unit * border

total_cost = grass_total + fence_total

print(f"\nArea:\t{area:,} square feet")
print(f"Border: {border:,} feet")
print(f"Grass:\t${grass_total:,.2f}")
print(f"Fence:\t${fence_total:,.2f}")
print(f"Total:\t${total_cost:,.2f}")
