managers = ["M1", "M2", "M3"]
employees = ["E" + str(i) for i in range(1, 13)]

n = len(employees) // len(managers)  # Employees per manager
employee_chunks = list(map(lambda i: employees[i*n:(i+1)*n], range(len(managers))))  # Split

reporting = dict(map(lambda m_i: (managers[m_i[0]], m_i[1]), enumerate(employee_chunks)))  # Map

for manager, emps in reporting.items():
    print(f"{manager} → {emps}")
