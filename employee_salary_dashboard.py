import matplotlib.pyplot as plt

# Employee Data
names = ['Amit', 'Priya', 'Rahul', 'Sneha', 'Riya', 'Karan']
salary = [40000, 55000, 35000, 60000, 45000, 55000]
departments = ['HR', 'IT', 'Sales', 'IT', 'HR', 'Sales']

# Salary Analysis
total = sum(salary)
average = total / len(salary)

print("EMPLOYEE SALARY ANALYTICS")
print("Total Salary:", total)
print("Average Salary:", round(average, 2))
print("Highest Salary:", max(salary))
print("Lowest Salary:", min(salary))

# Dashboard
plt.figure(figsize=(12, 8))
plt.suptitle("Employee Salary Analytics Dashboard", fontsize=16)

# Bar Chart
plt.subplot(2, 2, 1)
plt.bar(names, salary, color='skyblue')
plt.title("Employee-wise Salary")
plt.ylabel("Salary (Rs.)")

# Pie Chart
dept_salary = {}
for d, s in zip(departments, salary):
    dept_salary[d] = dept_salary.get(d, 0) + s

plt.subplot(2, 2, 2)
plt.pie(dept_salary.values(),
        labels=dept_salary.keys(),
        autopct='%1.1f%%')
plt.title("Department-wise Salary")

# Line Chart
plt.subplot(2, 2, 3)
plt.plot(names, salary, marker='o', color='green')
plt.title("Salary Comparison")
plt.ylabel("Salary (Rs.)")

# Summary Chart
plt.subplot(2, 2, 4)
plt.bar(['Total', 'Average', 'Highest'],
        [total, average, max(salary)],
        color=['orange', 'purple', 'red'])
plt.title("Salary Summary")

plt.tight_layout()
plt.savefig("salary_dashboard.png")
plt.show()
