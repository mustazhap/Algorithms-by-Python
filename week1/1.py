number = input("Enter numbers [1 and 0]: ")
counter = 0
l = []

for i in number:
    if (i == "1" and counter !=  0):
        l.append(counter)
        counter =  0
    elif (i == "0" ):
        counter += 1;
    
if (number[-1] == "0"):
    l.append(counter)


print("Samo bolwoe kolichestvo ", max(l))
print("s leva ", l.index(max(l))+1)

