
def procMultirangeStr(s):
    #should be formatted like:
    # "y1,1" or "100000,5,5"
    q = s.split(",")
    mRange = [[0,str(i)] for i in q]
    return mRange


def procboolstr(s):
    #replace i,j,k with x1,x2,x3

    s1 = s[::]
    ind = 0

    trkStrEsc = 0
    #track if we're inside a char or string-don't want to replace i,j,k in that case"
    while(ind < len(s1)):
        if(s1[ind] == "'"):
            trkStrEsc = (trkStrEsc + 1)%2

        if(trkStrEsc == 0):
            if(s1[ind] == "i"):
                if(ind>0):
                    if(s1[ind-1]!="m"):
                        s1 = s1[:ind] + "x1" + s1[ind+1:]
                else:
                    s1 = s1[:ind] + "x1" + s1[ind + 1:]

            if (s1[ind] == "j"):
                s1 = s1[:ind] + "x2" + s1[ind + 1:]
            if (s1[ind] == "k"):
                s1 = s1[:ind] + "x3" + s1[ind + 1:]

        ind = ind +1

    ind = 1

    #replace = with ==

    while(ind < len(s1)-1):
        if (s1[ind] == "=" and (s1[ind+1] not in "=<>!" and s1[ind-1] not in  "=<>!")):
            s1 = s1[:ind] + "==" + s1[ind+1:]
        else:
            ind = ind + 1

    #auto filling in of parentheses or brackets
    #start by only doing this for one-dimensional stuff
    ind = 0
    while(ind < len(s1)):
        if(s1[ind] == "a" and s1[ind+1] not in "[x"):
            lastInd = ind
            s1 = s1[:ind+1] + "[" + s1[ind+1:]
            ind = ind + 2
            while(ind < len(s1) and s1[ind] != " "):
                ind = ind + 1
            if(ind == len(s1)):
                s1 = s1 + "]"
            else:
                s1 = s1[:ind] + "]" + s1[ind:]
            ind = lastInd + 1
        elif (s1[ind] == "f" and s1[ind+1] != "("):
            lastInd = ind
            s1 = s1[:ind + 1] + "(" + s1[ind + 1:]
            ind = ind + 2
            while (ind < len(s1) and s1[ind] != " "):
                ind = ind + 1
            if (ind == len(s1)):
                s1 = s1 + ")"
            else:
                s1 = s1[:ind] + ")" + s1[ind:]
            ind = lastInd + 1

        else:
            ind = ind + 1
    

    return s1





