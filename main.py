import networkx as nx

def main():
    DG = nx.DiGraph()
    f = open("exampleInput.txt", "r")
    Lines = f.readlines()
    count = 0
    duration = 0
    numIntersections = 0
    numStreets = 0
    numCars = 0
    bonus = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        if count == 1:
            duration, numIntersections, numStreets, numCars, bonus = line.split()
            print("\n")
            print("-------------------------------------")
            print("duration is: ", duration)
            print("numIntersections is: ", numIntersections)
            print("numStreets is: ", numStreets)
            print("numCars is: ", numCars)
            print("bonus is: ", bonus)
            print("-------------------------------------")
        elif (count <= 1 + int(numStreets)):
            startIntersect, endIntersect, streetName, streetTime = line.split()
            print("streetName is: ", streetName)
            print("start intersection is: ", startIntersect)
            print("end intersection is: ", endIntersect)
            print("streetTime is: ", streetTime)
            DG.add_edge(startIntersect, endIntersect)
            DG[startIntersect][endIntersect]['weight'] = int(streetTime)
            DG[startIntersect][endIntersect]['name'] = streetName
        else:
            carInfo = line.split()
            numStreetsCarWantsToTravel = carInfo[0]
            print("number of streets car wants to travel is: ", numStreetsCarWantsToTravel)
            for i in range(1,len(carInfo)):
                print("streetName car wants to travel is: ", carInfo[i])
        print(f.read())

if __name__ == "__main__":
    main()