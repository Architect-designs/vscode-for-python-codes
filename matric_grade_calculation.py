def Grade_cal():
    urdu=int(input("enter the marks of urdu 0-150= "))
    english=int(input("enter the marks of english 0-150= "))
    islamiyat=int(input("enter the marks of islamiyat 0-100= "))
    quran_translation=int(input("enter the marks of quran translationm0-100= "))
    Pak_study=int(input("enter the marks of Pak study 0-100= "))
    physics=int(input("enter the marks of physics 0-120= "))
    mathematics=int(input("enter the marks of mathematics 0-150= "))
    chemistry=int(input("enter the marks of chemsitry 0-120= "))
    computer_science=int(input("enter the marks of computer science(if you are comuter science student else enter 0) 0-100= "))
    biology=int(input("enter marks of biology(if you are biology student else enter 0) 0-120= "))
    practical_physics=int(input("enter marks of physics practical 0-30= "))
    practical_chemistry=int(input("enter marks of chemistry practical 0-30= "))
    practical_computer_science=int(input("enter marks of computer science practical(if you are comuter science student else enter 0) 0-50= "))
    practical_biology=int(input("enter marks of practical biology(if you are biology student else enter 0) 0-30= "))
    total_marks_gained=urdu+english+islamiyat+quran_translation+Pak_study+physics+mathematics+chemistry+computer_science+biology+practical_physics+practical_chemistry+practical_computer_science+practical_biology
    total_marks=1200
    percentage=(total_marks_gained/total_marks)*100
    if percentage>=80:
        print("A+")
    elif percentage>=70:
        print("A")
    elif percentage>=60:
        print("B")
    elif percentage>=50:
        print("C")
    elif percentage>=40:
        print("D")
    elif percentage>=33:
        print("E")
    else:
        print("Sorry, You are Fail")
    return "This is all you have done in your matriculation examination"
grade_calculation=Grade_cal()
print(grade_calculation)