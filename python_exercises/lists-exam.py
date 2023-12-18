employeee_names = ["Anna", "Peter", "Moses", "George", "Irene", "Edna", "Bob", "John", "Mary", "Purity"]

print(employeee_names)

# split the list

subList1 = employeee_names[:5]
print(subList1)

# Output
# ['Anna', 'Peter', 'Moses', 'George', 'Irene']

subList2 = employeee_names[5:]
print(subList2)

# Output
# ['Edna', 'Bob', 'John', 'Mary', 'Purity']

# Add new employee to subList2
subList2.append("Kriti Brown")
print(subList2)

# output
# ['Edna', 'Bob', 'John', 'Mary', 'Purity', 'Kriti Brown'

# Remove the second employee's name from subList1
subList1.pop(1)
print(subList1)

# Output
# ['Anna', 'Moses', 'George', 'Irene']

# Merge both the lists.
employee_names_merged = subList1 + subList2

print(employee_names_merged)
# output
# ['Anna', 'Moses', 'George', 'Irene', 'Edna', 'Bob', 'John', 'Mary', 'Purity', 'Kriti Brown']

salaryList = [200, 310, 330, 500, 250, 600, 400, 450, 550]

# Apply a 4% salary increase to each employee and update the salaryList
for i in range(len(salaryList)):
    salaryList[i] += salaryList[i] * 0.04
print(salaryList)

# output
# [208.0, 322.4, 343.2, 520.0, 260.0, 624.0, 416.0, 468.0, 572.0]

# sort the list and return a new array use sorted instead of sort

sorted_salary_list = sorted(salaryList, reverse=True)
print(sorted_salary_list)

#output
[624.0, 572.0, 520.0, 468.0, 416.0, 343.2, 322.4, 260.0, 208.0]

# top 3 salaries
top_three_salaries = sorted_salary_list[:3]
print(top_three_salaries)

#output
#[624.0, 572.0, 520.0]
