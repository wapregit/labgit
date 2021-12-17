dataset = {45,25,48,75,62,82,91,26,52,96,40,60,61,82,72,60}
a = 0
b = 0
c = 0
d = 0
f = 0

for x in dataset:
    if x >= 80:
        a=a+1
    elif x >= 70 and x <= 79:
        b=b+1
    elif x >= 60 and x <= 69:
        c=c+1
    elif x >= 50 and x <= 59:
        d=d+1
    else:
        f=f+1


print("จำนวนนักเรียนที่ได้เกรด A = " + str(a))
print("จำนวนนักเรียนที่ได้เกรด B = " + str(b))
print("จำนวนนักเรียนที่ได้เกรด C = " + str(c))
print("จำนวนนักเรียนที่ได้เกรด D = " + str(d))
print("จำนวนนักเรียนที่ได้เกรด F = " + str(f))