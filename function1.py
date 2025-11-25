#def fun():
 #   print:("this is funtionl")

#def sum(a, b):
 #     print (a+b)

#v= input("enter a number:")
#var=int(v)
#if var>10:
 #   print("greater than 10")
#else:
 #   print("les than 10")

#st1= "hello world"
#print(st1[0:5])
#print(st1[1:-1])

#st2= "Hi"
#st3 = st1 + st2
#print(st3)

#count = 1
#while count <= 10:
 #    print (count)
  #   count = count + 1

def print_table(input):
    for i in range(1,11):
        print("{input}*{i}", i*input)

def print_tableR(input):
    for i in range(10,0,-1):
        print("{input}*{i}", i*input)

while True:
    var = input("enter a number.\n")
    if var.isdigit():
        var = int(var)
        break
    print("Wrong input.")

var = input ("enter a number.\n")
var = int(var)
if var>0:
    print_table(var)
