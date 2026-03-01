marks = {"Alice": 85, "Bob": 92, "Charlie": 78}

print(marks)

marks["Diana"] = 88
marks["Alice"] = 90

print("Updated marks:", marks)

for name, score in marks.items():
    if score > 80:
        print(f"{name} scored {score}")

with open("student_marks.txt", "w") as f:
    for name, score in marks.items():
        f.write(f"{name}: {score}\n")
        
with open("student_marks.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)
    new_marks = {}
with open("student_marks.txt", "r") as f:
    for line in f:
        name, score = line.strip().split(": ")
        new_marks[name] = int(score)

print("Reconstructed dictionary:", new_marks)
