class task4b:
    listOfCoordinates = list()
        
    def calcArea():
        if len(task4b.listOfCoordinates)<1:
            task4b.enterFileName()
        for i in task4b.listOfCoordinates:
            coordinates = list(map(int,i.split()))
            x = coordinates[::2]
            y = coordinates[1::2]
            area = 0
            n = len(x)-1
            for j in range(n):
                area += (x[j]*y[j+1]) - (x[j+1]*y[j])
            area+=(x[n]*y[0]) - (x[0]*y[n])
            print("The area of the polygon is "+str(area/2))
        task4b.listOfCoordinates.close()

    def enterFileName():
        try:
            task4b.listOfCoordinates = open(input("Enter the file path "), 'r')
        except:
            print("Path not valid")
            exit()      

    def task4b_usage():
        print("Enter file name where file contains\nlist of space seperated coordinate values\neg.. x1 y1 x2 y2 ... xn yn")
        


        
if __name__ == "__main__":
    task4b.task4b_usage()
    task4b.calcArea()
