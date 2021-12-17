gradeA = set()
gradeB = set()
gradeB2 = set()
gradeC = set()
gradeC2 = set()
gradeD = set()
gradeD2 = set()
gradeF = set()
a = 0 
b1 = 0
b2 = 0
c1 = 0
c2 = 0 
d1 = 0
d2 = 0 
f = 0
x = ''

while x != 'x' :
    x = input("x = ")
    txt = "Your grade is "
    if x.isnumeric() :
        if float(x) >= 80: 
            print(txt+"A")
            a=a+1
            gradeA.add(x)
            #print(gradeA)
            print("Number of students has grade A = "+str(a))
        elif float(x) >= 75: 
            print(txt+"B+")
            b1=b1+1
            gradeB.add(x)
            #print(gradeA)
            print("Number of students has grade B+ = "+str(b1))
        elif float(x) >= 70: 
            print(txt+"B")
            b2=b2+1
            gradeB2.add(x)
            #print(gradeA)
            print("Number of students has grade B = "+str(b2))
        elif float(x) >= 65: 
            print(txt+"C+")
            c1=c1+1
            gradeC.add(x)
            #print(gradeA)
            print("Number of students has grade C+ = "+str(c1))
        elif float(x) >= 60: 
            print(txt+"C")
            c2=c2+1
            gradeC2.add(x)
            #print(gradeA)
            print("Number of students has grade C = "+str(c2))
        elif float(x) >= 55: 
            print(txt+"D+")
            d1=d1+1
            gradeD.add(x)
            #print(gradeA)
            print("Number of students has grade D+ = "+str(d1))
        elif float(x) >= 50: 
            print(txt+"D")
            d2=d2+1
            gradeD2.add(x)
            #print(gradeA)
            print("Number of students has grade D = "+str(c2))
        else: 
            print(txt+"F")
            f=f+1
            gradeF.add(x)
            #print(gradeA)
            print("Number of students has grade F = "+str(f))
    elif x == 'print' :
        print(gradeA)
        print("จำนวนนักเรียนที่มีเกรด A = "+str(a))
        print(gradeB)
        print("จำนวนนักเรียนที่มีเกรด B+ = "+str(b1))
        print(gradeB2)
        print("จำนวนนักเรียนที่มีเกรด B = "+str(b2))
        print(gradeC)
        print("จำนวนนักเรียนที่มีเกรด C+ = "+str(c1))
        print(gradeC2)
        print("จำนวนนักเรียนที่มีเกรด C = "+str(c2))
        print(gradeD)
        print("จำนวนนักเรียนที่มีเกรด D+ = "+str(d1))
        print(gradeD2)
        print("จำนวนนักเรียนที่มีเกรด D = "+str(d2))
        print(gradeF)
        print("จำนวนนักเรียนที่มีเกรด F = "+str(f))
