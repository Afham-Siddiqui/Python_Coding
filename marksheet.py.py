print("MARK SHEET OF STUDENT")
maths = int(input("enter your marks...."));
computer = int(input("enter your marks....."));
pakistan_studies = int(input("enter your marks...."));
chemistry = int(input("enter your marks....."));
urdu = int(input("enter your marks......"));
marks_obt=(maths+computer+pakistan_studies+chemistry+urdu)
total_marks= 500
percentage=(marks_obt/total_marks)*100
print(percentage)

if percentage>=80:
    print("A-ONE")
if percentage < 80 and percentage >= 60:
    print("A-Grade")
if percentage<60 and percentage >50:
    print("B-Grade")
