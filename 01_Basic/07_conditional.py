name = input("Enter student name: ")
marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks entered!")

elif marks >= 90:
    print(name, "got Grade A+")
    print("Excellent Performance")
    print("Eligible for Scholarship")

elif marks >= 80:
    print(name, "got Grade A")
    print("Very Good Performance")
    print("Eligible for Merit Certificate")

elif marks >= 70:
    print(name, "got Grade B")
    print("Good Performance")
    print("Keep Improving")

elif marks >= 60:
    print(name, "got Grade C")
    print("Average Performance")
    print("Need More Practice")

elif marks >= 40:
    print(name, "got Grade D")
    print("Passed")
    print("Work Hard Next Time")

else:
    print(name, "got Grade F")
    print("Failed")
    print("Needs Improvement")

