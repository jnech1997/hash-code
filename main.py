import networkx as nx

from submit import create_submit_file

# HashMap key: streets, val: # of times hit by any path
streetHits = {}
carStarts = {}
streetTimes = {}

def createGraph(filename):
    f = open(filename, "r")
    DG = nx.DiGraph()
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
            # print("\n")
            # print("-------------------------------------")
            # print("duration is: ", duration)
            # print("numIntersections is: ", numIntersections)
            # print("numStreets is: ", numStreets)
            # print("numCars is: ", numCars)
            # print("bonus is: ", bonus)
            # print("-------------------------------------")
        elif (count <= 1 + int(numStreets)):
            startIntersect, endIntersect, streetName, streetTime = line.split()
            # print("streetName is: ", streetName)
            # print("start intersection is: ", startIntersect)
            # print("end intersection is: ", endIntersect)
            # print("streetTime is: ", streetTime)
            DG.add_edge(startIntersect, endIntersect)
            DG[startIntersect][endIntersect]['weight'] = int(streetTime)
            DG[startIntersect][endIntersect]['name'] = streetName

            streetTimes[streetName] = streetTime
        else:
            carInfo = line.split()
            numStreetsCarWantsToTravel = carInfo[0]
            path = carInfo[1:]
            #print("number of streets car wants to travel is: ", numStreetsCarWantsToTravel)
            for i in range(len(path)):
                street = path[i]
                if i > 0:
                    if street in streetHits:
                        streetHits[street] += 1
                    else:
                        streetHits[street] = 1
                else:
                    if street in carStarts:
                        carStarts[street] += 1
                    else:
                        carStarts[street] = 1

    return DG
            
def main(filename):
    DG = createGraph(filename)
    # print("STREET HITS HASHMAP", streetHits)
    sortedStreetHits = sorted(streetHits.items(), key=lambda v: v[1], reverse=True)
    mostHits = sortedStreetHits[0][1]
    # print("FIRST 10 SORTED STREET HITS", sortedStreetHits[:10])
    sortedCarStarts = sorted(carStarts.items(), key=lambda v: v[1], reverse=True)
    mostStarts = sortedCarStarts[0][1]
    # print("FIRST 10 SORTED CAR STARTS", sortedCarStarts[:10])

    numNodes = DG.number_of_nodes()
    intersections = []
    incomingStreets = []
    orders = []
    for n in DG:
        intersections.append(n)
        numIncomingIntersections = 0
        orderList = []
        intersectionMaxCarStarts = 0
        intersectionMaxStreetHits = 0
        intersectionMaxStreetTime = 0
        for _, _, data in DG.in_edges(n, data=True):
            streetName = data['name']
            if streetName in streetHits:
                incomingEdgeStreetHits = streetHits[streetName]
            else:
                incomingEdgeStreetHits = 0
            if (incomingEdgeStreetHits > intersectionMaxStreetHits):
                intersectionMaxStreetHits = incomingEdgeStreetHits
            if streetName in carStarts:
                incomingEdgeCarStarts = carStarts[streetName]
            else: 
                incomingEdgeCarStarts = 0
            if (incomingEdgeCarStarts > intersectionMaxCarStarts):
                intersectionMaxCarStarts = incomingEdgeCarStarts
            incomingEdgeStreetTime = streetTimes[streetName]
            if (int(incomingEdgeStreetTime) > intersectionMaxStreetTime):
                intersectionMaxStreetTime = int(incomingEdgeStreetTime)
        for _, _, data in DG.in_edges(n, data=True):
            numIncomingIntersections += 1
            duration = str(assignTimeVal(data['name'], intersectionMaxCarStarts, incomingEdgeStreetHits, incomingEdgeStreetTime))
            orderList.append((data['name'], duration)) # assigning the time value to the street name for our output

        incomingStreets.append(numIncomingIntersections)
        orders.append(orderList)
    # print("intersections are: ", intersections)
    # print("incomingStreets are: ", incomingStreets)
    # print("orders are: ", orders)

    # create submission file
    # create_submit_file(filename, numNodes, intersections, incomingStreets, orders)

def assignTimeVal(streetName, maxCarStarts, maxStreetHits, maxStreetTime):
    if streetName in streetHits:
        hits = streetHits[streetName]
    else:
        hits = 0
    if streetName in carStarts:
        starts = carStarts[streetName]
    else: 
        starts = 0
    if maxCarStarts == 0:
        maxCarStarts = 1000000000
    if maxStreetHits == 0:
        maxStreetHits = 1000000000
    time = streetTimes[streetName]
    duration = int(int(starts)/int(maxCarStarts) * 1.5) +  int(int(hits)/int(maxStreetHits) * 5) + int(int(time)/int(maxStreetTime) * 3.5)
    if (duration < 1):
        duration = 1
    return duration


if __name__ == "__main__":
    # filenames = ["exampleInput.txt", "byTheOcean.txt", "checkmate.txt", "dailyCommute.txt", "etoile.txt", "foreverJammed.txt"]
    filenames = ["exampleInput.txt", "byTheOcean.txt"]
    for file in filenames: 
        main(file)