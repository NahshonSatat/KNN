# 315823880- nahshon satat

from Point import Point
import doctest as doctest
import random

# this function for the sort
def sortbydis(point):
    return point.dis

def knn (laern,k,pl,point)->int:
    for i in laern :
        i.dis = point.distance(pl, i)
    laern.sort(key=sortbydis)
    sum = 0
    for i in range (0,k) :
        sum += laern[i].gender
    if sum >= 0:
        return 1
    else:
        return -1

def play (list,numtime,k):
    listOdd = odd(k+1)

    for i in listOdd:
        for j in range(1,4):
            Grade=0
            for u in range(numtime):
                 laern,test = shaffel(list)
                 Score = 0
                 for point in laern:
                     if knn(test, i, j, point) == point.gender:
                         Score += 1
                 Grade += (Score / len(test) * 100)

            Grade /= numtime
            print("the Grade of {} neighbors (neighbors == k) and pl (pl== p) {} is {}  ".format(i, j, Grade))

# This function is because I learned my mistake in the Previous assignment
# that I created full lists without deleting and because of this my algorithm runs slowly
# there is no doubt that you learn from mistakes
#
def shaffel (list) :
    learn = []
    test = []
    numtime = len(list)
    start = int(numtime / 2)
    random.shuffle(list)
    for i in range(0, numtime):
        if (i < start):
            learn.append(point[i])
        else:
            test.append(point[i])

    return learn,test
def odd (x) :

    list =[]
    if x == 1 :
        list.append(x)
        return list
    else :
        i=1
    for i in range(i,x,2):
        list.append(i)
    return list

if __name__ == '__main__':

        point =[]

        with open('HC_Body_Temperature') as f:
            for line in f:
                a = line.strip().split()
                if (a[1] == "2"):
                    a[1] = -1
                b = Point(a[0], a[1], a[2])
                point.append(b)

        length = len(point)
        random.shuffle(point)
#        list = odd(10) this was as a check for function odd
#        for i in list:
#            print(i)
        play(point,500,9)

        (failures, tests) = doctest.testmod(report=True)
        print("{} failures, {} tests".format(failures, tests))