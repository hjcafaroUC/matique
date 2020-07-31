from smartInput import *


import sys; print(sys.version)
#check if user wants to input commands in standard input or through text file?
print("Standard input 's' or text file 't'?")
inputMethod = input()
lines=[]
textIndex = 0
if(inputMethod=="t"):
    print("Enter name of text file to parse input from")
    textAddress = input()
    f=open(textAddress,'r')
    lines = f.read().split(sep="\n")


print("Standard output 's' or text file 't'?")
outputMethod = input()
outputFileAddress = ""
if(outputMethod == "t"):
    print("Enter address of text file to print to")
    #should .cpp be appended? ill assume user handles it for now
    outputFileAddress = input()




def inputWrapper():
    if(inputMethod=='s'):
        return input()
    if(inputMethod=='t'):
        global textIndex
        #check if current line is a comment-starting with ;
        textIndex = 1+textIndex
        while (lines[textIndex-1][0]==";"):
            textIndex = textIndex+1
        return lines[textIndex-1]






#get dimensions of underlying problem-typically 1,2, or at most 3

print("What is the dimensionality of your problem?")

dpdim = int(inputWrapper())

dpdims = []
print("Enter the maximum bounds on each dimension:")
#global multidimensional array will be allocated with these bounds

for i in range(dpdim):
    dpdims.append(int(inputWrapper()))

datadim = 0
datadims = []
print("Enter the dimensionality of your data")
s = inputWrapper()
if(s == "sm"):
    datadim = dpdim
    datadims = dpdims[::]
else:
    datadim = int(s)
    print("Enter the maximum bounds on each dimension of data:")
    # data array will be allocated with these dimensions

    for i in range(datadim):
        datadims.append(int(inputWrapper()))

print("Enter the number of constants, or 0:")
numConstants = int(inputWrapper())



dpPlacehold= "dp"
fPlacehold = "f("
aPlacehold = "a"

for i in range(1,datadim+1):
    aPlacehold = aPlacehold + "[x" + str(i) + "]"

for i in range(1,dpdim+1):
    dpPlacehold = dpPlacehold + "[x" + str(i) + "]"
    fPlacehold = fPlacehold + "x" + str(i) + ","
fPlacehold = fPlacehold[:-1] + ")"

#these are useful placeholder strings: the dp one is dp[x1], or dp[x1][x2], etc.
# the f one is f(x1), or f(x1,x2), etc

#To do: add changing variable names

#header includes dependencies, allocates variables
headerString = "//generated with matiquepro, Henry Cafaro \n# include <iostream>\n#define ll long long\nusing namespace std;\nll int a"
for i in range(datadim):
    headerString = headerString + "[" + str(datadims[i]+5) + "]"

headerString = headerString + ";\nll int dp"
for i in range(dpdim):
    headerString = headerString + "[" + str(dpdims[i]+5) + "]"

headerString = headerString + ";\n"
if(numConstants > 0):
    headerString = headerString + "ll int "

    for i in range(1,numConstants):
        headerString = headerString + "c" + str(i) + ","
    headerString = headerString + "c" + str(numConstants) + ";\n"








#this section builds the input function f which will interact with the dp array
#just builds a bunch of switch statements; can interact with variables, dp array, or underlying data array

print("Enter the rule for your dp")

dpRuleString = inputWrapper()

cases = []

if dpRuleString == "sw":
    while(True):
        print("Input case boolean")
        caseBoolean = procboolstr(inputWrapper())
        print("Input rule")
        caseRule = procboolstr(inputWrapper())
        if(caseBoolean != "el"):
            cases.append("if(" + caseBoolean + "){\n" + dpPlacehold + " = "  + caseRule + ";\n}\n")
            if(len(cases) > 1):
                cases[-1] = "else " + cases[-1]
        else:
            cases.append("else{\n" + dpPlacehold + " = " + caseRule + ";\n}\n")

        if(caseBoolean == "el"):
            break

functionString = "ll int f("
for i in range(1,dpdim):
    functionString = functionString + "int x" + str(i) + ","
functionString = functionString + "int x" + str(dpdim) + "){\n"
functionString = functionString + "if(" + dpPlacehold + "==-1){\n"

if(len(cases) > 1):
    for i in cases:
        functionString  =functionString + i


else:
    #no switch
    print()

functionString = functionString + "}\n return " + dpPlacehold + ";}\n"

print("What input type?")
inputType = inputWrapper()
#builds input parameters from user, can either fill a data array or just take in variables to evaluate answer at

cinString = ""
for i in range(1,datadim):
    headerString = headerString + "ll int y" + str(i) + ";\n"

headerString = headerString + "ll int y" + str(datadim) + ";\n"
cinString = cinString + "cin >> "
for i in range(1,datadim):
    cinString = cinString + "y" + str(i) + " >> "
cinString = cinString + "y" + str(datadim) + ";\n"

constInString = ""
if(numConstants > 0):
    for i in range(1,numConstants):
        constInString = constInString + "c" + str(i) + " >> "
    constInString = constInString + "c" + str(numConstants) + ";\n"

cinString = cinString + constInString

dpSetString1 = ""

dpSetString2 = ""

for i in range(1,dpdim+1):
    dpSetString1 = dpSetString1 + "for(int x" + str(i) + "=0; x" + str(i) + " < " + str(dpdims[i-1]) + "; x" + str(i) + "++){\n"

    dpSetString2 = dpSetString2 + "}\n"

dataCinString1 = ""

dataCinString2 = ""

for i in range(1,datadim+1):
    dataCinString1 = dataCinString1 + "for(int x" + str(i) + "=0; x" + str(i) + " < y" + str(i) + "; x" + str(i) + "++){\n"

    dataCinString2 = dataCinString2 + "}\n"

if ((inputType == "standard") or (inputType == "st")):

    totalInputString = cinString + dpSetString1 + dpPlacehold + "=-1;\n" + dpSetString2 + dataCinString1 + "cin >> " + aPlacehold + ";\n" + dataCinString2
elif ((inputType == "str") or (inputType == "string")):
    totalInputString = cinString +"cin >> s;\n"+ dpSetString1 + dpPlacehold + "=-1;\n" + dpSetString2
    headerString = headerString + "string s;\n"
elif ((inputType == "strauto") or (inputType == "stringauto")):
    #assumes 1-dimensional data
    totalInputString = "cin >> s;\ny1 =s.size();\n"+ dpSetString1 + dpPlacehold + "=-1;\n" + dpSetString2
    headerString = headerString + "string s;\n"

elif(inputType == "no"):
    totalInputString = cinString + dpSetString1 + dpPlacehold + "=-1;\n" + dpSetString2

#builds evaluation and answer printing statement
#right now, can either take max of dp elements or evaluate f() at a single point
print("Evaluation type")

evalType = inputWrapper()

evalString = ""
if(evalType == "mx"):
    evalString = "ll int mx = 0;\n" + dataCinString1 + "mx = max(mx," + fPlacehold + ");\n" + dataCinString2 + "cout << mx << endl;\n"
elif(evalType == "eval"):
    evalString = "cout << f("
    for i in range(1,dpdim):
        print("Input variable " + str(i))
        evalString = evalString + inputWrapper() + ","
    print("Input variable " + str(dpdim))
    evalString = evalString + inputWrapper() + ") << endl;\n"



mainString = "int main() {\n" + totalInputString + evalString + "}"





totalString = headerString + functionString + mainString

if(outputMethod == "s"):
    print(totalString)
elif(outputMethod == "t"):
    outputFile = open(outputFileAddress,"w")
    outputFile.write(totalString)
    outputFile.close()



















