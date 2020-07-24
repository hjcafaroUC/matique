

def procboolstr(s):
    #replace i,j,k with x1,x2,x3

    s1 = s[::]
    ind = 0

    trkStrEsc = 0
    while(ind < len(s1)):
        if(s1[ind] == "'"):
            trkStrEsc = (trkStrEsc + 1)%2

        if(trkStrEsc == 0):
            if(s1[ind] == "i"):
                s1 = s1[:ind] + "x1" + s1[ind+1:]
            if (s1[ind] == "j"):
                s1 = s1[:ind] + "x2" + s1[ind + 1:]
            if (s1[ind] == "k"):
                s1 = s1[:ind] + "x3" + s1[ind + 1:]

        ind = ind +1

    ind = 0
    

    return s1





