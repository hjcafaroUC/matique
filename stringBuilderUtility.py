def buildLoopString(ranges, interior = ""):
    #ranges should look like [[0,1000],[0,3]] or [[0,"y1"],[0,3]]
    #either integers or strings will be accepted
    n =  len(ranges)
    part1 = ""
    part2 = ""

    for i in range(n):
        part1 = part1 + "for(int x" + str(i+1) + "=" + str(ranges[i][0]) + "; x" + str(i+1) + " < " + str(ranges[i][1]) + "; x" + str(i+1) + "++){\n"
        part2 = part2  + "}\n"

    return [part1,part2]

    #returns 2-element list [first part,last part]