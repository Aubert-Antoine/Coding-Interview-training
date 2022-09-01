from pdb import find_function


p1WorkingTime = ['9:00','20:00']
p1Meeting = [['9:00','10:30'],['12:00','13:00'],['16:00','18:00']]

p2WorkingTime = ['10:00','18:30']
p2Meeting = [['10:00','11:30'],['12:30','14:30'],['14:30','15:00'],['16:00','17:00']]



def timeToInt(calendar):
    out = []
    if len(calendar) != 2:      #condition a chier
        for l in calendar:
            for t in l:
                t=t.replace(':','')
                t=int(t)
                out.append(t)
    else :
        for t in calendar:
                t=t.replace(':','')
                t=int(t)
                out.append(t)
    # print("Le type de out est {} et out est {}".format(type(out), out))
    return out
                
                
intLp1=timeToInt(p1Meeting)
intHp1=timeToInt(p1WorkingTime)

intLp2=timeToInt(p2Meeting)
intHp2=timeToInt(p2WorkingTime)

def findFreeTime(intList)  :
    # it will find free time for 1 of 2 poeple
    freeTimeList = []
    for i in range(2,len(intList),2):
        print(i)
        freeTimeList.append([intList[i-1],intList[i]])
    print(freeTimeList)
    return freeTimeList

p1FreeTime = findFreeTime(intLp1)


def FinalResults(FreeTimeSchedule, edtOthePeople):
    out = []
    for free in FreeTimeSchedule:
        for time in edtOthePeople:
            print("free = {}    time = {}".format(free,time))
            if free[0] >= time and 


FinalResults(p1FreeTime, intLp2)