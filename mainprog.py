
import sys; print(sys.version)
#get dimensions of underlying problem-typically 1,2, or at most 3

print("What is the dimensionality of your problem?")

dim = int(input())

dims = []
print("Enter the maximum bounds on each dimension:")
#global multidimensional array will be allocated with these bounds

for i in range(dim):
    dims.append(int(input()))

dpPlacehold= "dp"
fPlacehold = "f("


for i in range(1,dim+1):
    dpPlacehold = dpPlacehold + "[x" + str(i) + "]"
    fPlacehold = fPlacehold + "x" + str(i) + ","
fPlacehold = fPlacehold[:-1] + ")"

#these are useful placeholder strings: the dp one is dp[x1], or dp[x1][2], etc.
# the f one is f(x1), or f(x1,x2), etc

#To do: add changing variable names






#this section builds the input function f which will interact with the dp array
#just builds a bunch of switch statements; can interact with variables, dp array, or underlying data array

print("Enter the rule for your dp")

dpRuleString = input()

cases = []

if dpRuleString == "sw":
    while(True):
        print("Input case boolean")
        caseBoolean = input()
        print("Input rule")
        caseRule = input()
        if(caseBoolean != "el"):
            cases.append("if(" + caseBoolean + "){\n" + dpPlacehold + " = "  + caseRule + ";\n}\n")
            if(len(cases) > 1):
                cases[-1] = "else " + cases[-1]
        else:
            cases.append("else{\n" + dpPlacehold + " = " + caseRule + ";\n}\n")

        if(caseBoolean == "el"):
            break

functionString = "ll int f("
for i in range(1,dim):
    functionString = functionString + "int x" + str(i) + ","
functionString = functionString + "int x" + str(dim) + "){\n"
functionString = functionString + "if(" + dpPlacehold + "==-1){\n"

if(len(cases) > 1):
    for i in cases:
        functionString  =functionString + i


else:
    #no switch
    print()

functionString = functionString + "}\n return " + dpPlacehold + ";}\n"

print("What input type?")
inputType = input()
#builds input parameters from user, can either fill a data array or just take in variables to evaluate answer at

cinString = "int "
for i in range(1,dim):
    cinString = cinString + "y" + str(i) + ","

cinString = cinString + "y" + str(dim) + ";\ncin >> "
for i in range(1,dim):
    cinString = cinString + "y" + str(i) + " >> "
cinString = cinString + "y" + str(dim) + ";\n"

arrCinString1 = ""

arrCinString2 = ""

for i in range(1,dim+1):
    arrCinString1 = arrCinString1 + "for(int x" + str(i) + "=0; x" + str(i) + " < y" + str(i) + "; x" + str(i) + "++){\n"

    arrCinString2 = arrCinString2 + "}\n"

if ((inputType == "standard") or (inputType == "st")):

    totalInputString = cinString + arrCinString1 + "cin >> a" + dpPlacehold[2:] + ";\n" + dpPlacehold + "=-1;\n" + arrCinString2
elif(inputType == "no"):
    totalInputString = cinString + arrCinString1 + dpPlacehold + "=-1;\n" + arrCinString2

#builds evaluation and answer printing statement
#right now, can either take max of dp elements or evaluate f() at a single point
print("Evaluation type")

evalType = input()

evalString = ""
if(evalType == "mx"):
    evalString = "ll int mx = 0;\n" + arrCinString1 + "mx = max(mx," + fPlacehold + ");\n" + arrCinString2 + "cout << mx << endl;\n"
elif(evalType == "eval"):
    evalString = "cout << f("
    for i in range(1,dim):
        print("Input variable " + str(i))
        evalString = evalString + input() + ","
    print("Input variable " + str(dim))
    evalString = evalString + input() + ") << endl;\n"


mainString = "int main() {\n" + totalInputString + evalString + "}"



#header includes dependencies, allocates variables 
headerString = "//generated with autodp, Henry Cafaro \n# include <iostream>\n#define ll long long\nusing namespace std;\nll int a"
for i in range(dim):
    headerString = headerString + "[" + str(dims[i]) + "]"

headerString = headerString + ";\nll int dp"
for i in range(dim):
    headerString = headerString + "[" + str(dims[i]) + "]"

headerString = headerString + ";\n"

totalString = headerString + functionString + mainString

print(totalString)
















