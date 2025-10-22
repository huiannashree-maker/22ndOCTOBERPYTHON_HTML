#Accept student marks in different subjects(3) maths science eng calculate the average and find the grade
# avg>=90 then grade A+
# avg>=80 grade A	+
# avg>=70 grade B	+
# avg >=60 grade C+
# grade D

# Step 1

name=input('enter student name....')
math=float(input('enter marks in maths(out of 100)'))
science=float(input('enter marks in science(out of 100)'))
eng=float(input('enter marks in Eng(out of 100)'))

# step 2

avg=(math+science+eng)/3

#step 3

if avg >=90: #Indentation Operator
    grade='A+'
elif avg>=80:
    grade='A'
elif avg>=70:
    grade='B'
elif avg>=60:
    grade='C'
elif avg>=50:
    grade='D'
else:
    grade='F'

#step 4

print("\n ===========RESULT===========\n")

print(f"Student name : {name}")
print(f"Average Marks: {avg}")
print(f"Grade is : {grade}")

#step 5
if grade!='F':
    print('status: PASS!!!!')
else:
     print('status: FAILED!!!!')

     