# Basics of Python

print("Hello World")
x=1.9
print(type(x))
# output:<class 'int'>


x=1000000000000000000000000000000000000000000000000000000000000000000000000000000
print(type(x))
# output:<class 'int'>


age=int(input("enter your age"))
print(type(age))
print(age)

age = int(input("enter the age "))
print(age)
print(type(age))

age1 = int(input("enter the age1 "))
print(age1)
print(type(age1))
print("The sum of the ages is ",age+age1)



krish = '1.2'
print(type(krish))


#Real and imag
c1 = 1
c2 = 2j
print("c1",c1 ,"c2",c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

# output:
# c1 1 c2 2j
# <class 'int'>
# <class 'complex'>
# 1
# 2.0


all_ok=True
print(all_ok)

all_okk=False
print(all_okk)

print(type(all_ok))

# output:
# True
# False
# <class 'bool'>



status=bool(input("is it okkk"))
print(status)
print(type(status))

# output1:
# is it okkk Yes
# True
# <class 'bool'>

# output2:
# is it okkk  -(no input)
# False
# <class 'bool'>



a=2
b=2
print(a**b)


x=2
print(x)
x+=3
print(x)
# output:
# 2
# 5



# Identition:

no = 12
if no>0:
 print(no)
 output:
 12



no = 12
if no>0:
print(no)
#  output:
#   File "C:\Users\ROHIT\PycharmProjects\pythonProject1\.venv\sample.py", line 103
#     print(no)
#     ^
# IndentationError: expected an indented block after 'if' statement on line 102




no=int(input("Enter a number:"))
if(no>0):
    print("Pos")
else:
    print("Neg")
# output:
# Enter a number:11
# Pos




no=int(input("Enter a number:"))
if(no==0):
    print("Print zero")
elif(no>0):
    print("Pos")
else:
    print("neg")
# output:
# Enter a number:4
# Pos


# Loops:
# While loop
count = 1
print("starting")
while count<=10:
    print(count)
    count+=1
# output:
# starting
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# for loop

for i in range(2,10):
    print(i)
    print("done")
#output:    C:\Users\ROHIT\PycharmProjects\pythonProject1\.venv\Scripts\python.exe C:\Users\ROHIT\PycharmProjects\pythonProject1\.venv\sample.py
# 2
# done
# 3
# done
# 4
# done
# 5
# done
# 6
# done
# 7
# done
# 8
# done
# 9
# done



print("print out")
num = int(input("enter no"))
for i in range(0,20):
    if i == num:
        break
    print(i)
    print("done")

# output:
# C:\Users\ROHIT\PycharmProjects\pythonProject1\.venv\Scripts\python.exe C:\Users\ROHIT\PycharmProjects\pythonProject1\.venv\sample.py
# print out
# enter no11
# 0
# done
# 1
# done
# 2
# done
# 3
# done
# 4
# done
# 5
# done
# 6
# done
# 7
# done
# 8
# done
# 9
# done
# 10
# done
# Process finished with exit code 0




