import sys

def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg < 90:
        return "A"
    elif 65 <= avg < 80:
        return "B"
    elif 50 <= avg < 65:
        return "C"
    elif 40 <= avg < 50:
        return "D"
    else:
        return "F"

def main():
    if len(sys.argv) < 7:
        print("Usage: python student.py <name> <department> <semester> <m1> <m2> <m3>")
        sys.exit(1)

    name = sys.argv[1]

    # Department may contain spaces
    department = " ".join(sys.argv[2:-4])

    semester = sys.argv[-4]
    marks1 = int(sys.argv[-3])
    marks2 = int(sys.argv[-2])
    marks3 = int(sys.argv[-1])

    average = (marks1 + marks2 + marks3) / 3
    grade = calculate_grade(average)

    print("===== STUDENT DETAILS =====")
    print(f"Name       : {name}")
    print(f"Department : {department}")
    print(f"Semester   : {semester}")
    print(f"Average    : {average:.2f}")
    print(f"Grade      : {grade}")

if __name__ == "__main__":
    main()
