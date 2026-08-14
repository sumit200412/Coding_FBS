area = int(input("Enter the area for one wall : "))
interior_cost = int(input("Enter the cost of interior wall : "))
exterior_cost = int(input("Enter the cost of exterior wall : "))

interior_area = interior_cost*2
exterior_area = exterior_cost*7

total_exterior_cost = exterior_area * exterior_cost
total_interior_cost = interior_area * interior_cost

total_cost = total_interior_cost + total_exterior_cost

print(f'Exterior wall cost : {total_exterior_cost}')
print(f'Interior wall cost : {total_interior_cost}')
print(f'Total cost : {total_cost}')
