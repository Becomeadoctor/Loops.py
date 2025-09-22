def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

name=input ("Enter student name: ")
g1=int(input("Enter grade 1: "))
g2=int(input("Enter grade 2: "))
g3=int(input("Enter grade 3: "))
g4=int(input("Enter grade 4: "))
g5=int(input("Enter grade 5: "))

grades=[g1,g2,g3,g4,g5]
average=sum(grades)/len(grades)

letter = get_letter_grade(average)
print("\n" + name)
print("Average:", average)
print("Letter Grade:",letter)

