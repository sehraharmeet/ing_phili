# 2. Write a Python program to evaluate student marks of 5 subjects.
# Conditions:
# Calculate total marks and percentage.
# Use a loop to accept marks.
# Use if/elif/else to give grade:
# >= 90: Grade A
# >= 75 and < 90: Grade B
# >= 50 and < 75: Grade C
# < 50: Fail

total = 0

for i in range(1, 6):
    marks = float(input(f"Enter marks for subject {i}: "))
    total += marks

percentage = total / 5

if percentage >= 90: 
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

print("\n----- Result -----")
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
