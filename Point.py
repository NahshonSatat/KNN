# 315823880- nahshon satat

import  math
import doctest as doctest

class Point():
    def __init__(self, x, gender, y):
        self.x = float(x)
        self.gender = int(gender)
        self.y = float(y)
        self.dis = float(0.0)


    def pr(self):
        print("First number = " + str(self.x))
        print("Second number = " + str(self.y))
        print("gender = " + str(self.gender))
        print("the dis ="+str(self.dis))

    def distance (self,index,point)-> float:
        """

        :param index: to choose the correct equation
        :param point: for to do distance between two points
        :return:distance of  correct equation
        >>> x =Point(1,1,2)
        >>> y =Point(7,1,6)
        >>> x.distance(1,y)
        10.0
        >>> x.distance(2,y)
        7.211102550927978
        >>> x.distance(3,y)
        6.0


        """
        if (index==1):
            sum = abs(self.x-point.x)+abs(self.y-point.y)

            return sum
        elif(index==2):
            sum = math.pow(abs(self.x-point.x),2)+math.pow(abs(self.y-point.y),2)
            sum = math.sqrt(sum)
            return sum
        else :

            return max(abs(self.x - point.x), abs(self.y - point.y))
    pass
#def sortbydis(point):
 #   return point.dis



if __name__ == '__main__':

        #        point = []
        #       with open('HC_Body_Temperature') as f:
        #            for line in f:
        #                a = line.strip().split()
        #                if a[1] == "2":
        #                    a[1] = -1
        #                b = Point(a[0],a[1],a[2])
        #                point.append(b)

        #        length = len(point)
        #        random.shuffle(point)
        #      c = Point(5,1,3)
        #     d = Point(1,1,4)
        #    e = Point(9,1,7)
        #   c.dis = 5
        #  d.dis = 3
        # e.dis = 4
        #list = []
        # list.append(c)
        # list.append(d)
        #        list.append(e)
        #        list.sort(key=sortbydis)
        #        for i in list:
        #            i.pr()

    (failures, tests) = doctest.testmod(report = True)
    print("{} failures, {} tests".format(failures, tests))