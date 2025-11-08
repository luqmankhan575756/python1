movies = []
mov1=input("enter first movie:")
mov2=input("enter second movie:")
mov3=input("enter third movie:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

# but we also write in this way
movies.append(input("enter first movie: "))
movies.append(input("enter second movie:"))
movies.append(input("enter third movie:"))

print(movies)