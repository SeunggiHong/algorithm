credit = 0
grade = 0
for i in range(20):
    subject, c, g = map(str, input().split())
    if g != 'P':
        credit += float(c)
        if g == 'A+':
            grade += 4.5*float(c)
        elif g == 'A0':
            grade += 4.0*float(c)
        elif g == 'B+':
            grade += 3.5*float(c)
        elif g == 'B0':
            grade += 3.0*float(c)
        elif g == 'C+':
            grade += 2.5*float(c)
        elif g == 'C0':
            grade += 2.0*float(c)
        elif g == 'D+':
            grade += 1.5*float(c)
        elif g == 'D0':
            grade += 1.0*float(c)
        elif g == 'F':
            grade += 0.0*float(c)

print(grade/credit)