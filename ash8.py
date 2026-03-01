import json

employee_data = {
    "name": "John Doe",
    "age": 30,
    "department": "HR",
    "skills": ["communication", "management"]
}

with open("employee.json", "w") as f:
    json.dump(employee_data, f, indent=4)

print("Employee data written to employee.json")
with open("employee.json", "r") as f:
    data = json.load(f)

print("Employee Data:", data)
print("Name:", data["name"])
print("Skills:", ", ".join(data["skills"]))
data["skills"].append("teamwork")

with open("employee.json", "w") as f:
    json.dump(data, f, indent=4)

print("Updated employee data with new skill saved.")
  
a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))
try:
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
