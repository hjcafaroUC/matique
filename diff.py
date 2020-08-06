#diff utility for checking correctness of code-check against earlier versions


print("Enter 1st file")
f1 = open(input(),"r")

print("Enter 2nd file")
f2 = open(input(),"r")

lines1 = f1.read().split(sep="\n")
lines2 = f2.read().split(sep="\n")

if(len(lines1) != len(lines2)):
    print("Lengths differ : " + str(len(lines1)) + " " + str(len(lines2)))

for i in range(min(len(lines1),len(lines2))):
    if(lines1[i] !=lines2[i]):
        print("Difference on line " + str(i))
        print(lines1[i])
        print(lines2[i])

print("Diff is complete")
