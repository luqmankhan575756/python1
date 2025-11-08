x = 100
name = "python"
print(f"this is value of x:{x} and this is values of name :{name}")

l = [1,2,3,5,0]
print("list before adding items :", l )
print(l[3])

l = ["Alex", "John", "Ali"]
print (l)
print (l[1])

l = ["Alex", 1, 2.5]
l[1] = "John"
print (l)

l.append(34)
print("list after adding items :",l)
print(len(l))
l.pop(1)
print("lists afterremoving items :",l)
print(len(l))

l.insert(1,2.5)
print("list after inserting items :", l)

l1 = [2.5, "Doe"]
l.append(l1)
print("list after adding list as item :",l)

l.remove(2.5)
print("list after removing item 2.5 :",l)

for i in l:
    print("items in the list are :", i)

for i in l:
    if type(i) is list:
        for j in i:
            print("items in nested list are :", j)
            
sepList = [j for i in l if type(i) is list for j in i]
print("separeted nestes list items are : " , sepList)

marks = [80,56,63,54,95]
newMarks = []
for i in marks:
    if i >60:
        newMarks.append(i)
        print(newMarks)

      #  newMarks2 = [i for i in marks if i>60]
       # print(newMarks2)



