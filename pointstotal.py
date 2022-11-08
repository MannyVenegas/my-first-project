def points(games):
    lrgstring = "".join(games)
    removedoublepts = lrgstring.split(":")
    joinednums = "".join(removedoublepts)
    myteamgoals = joinednums[::2]
    awayteamgoals = joinednums[1::2]
    myteamlist = [i for i in myteamgoals]
    awaylist = [i for i in awayteamgoals]
    #print(myteamlist)
    #print(awaylist)
    total = 0
    length = len(myteamlist)
    for i in range(length):
        if myteamlist[i] > awaylist[i]:
            total += 3
        elif myteamlist[i] < awaylist[i]:
            total += 0
        else:
            total += 1
    #print(total)
#todo puede ser resumido a esto 
#def points(games):
    #count = 0
    #for match in games:
        #x = match.split(":")
        #if x[0] > x[1]:
            #count += 3
        #elif x[0] == x[1]:
            #count += 1
    #return count


points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3'])