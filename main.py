import networkx as nx

from submit import create_submit_file

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
        else:
            carInfo = line.split()
            numStreetsCarWantsToTravel = carInfo[0]
            #print("number of streets car wants to travel is: ", numStreetsCarWantsToTravel)
            #for i in range(1,len(carInfo)):
                #print("streetName car wants to travel is: ", carInfo[i])
    return DG
            
def main(filename):
    DG = createGraph(filename)
    numNodes = DG.number_of_nodes()
    intersections = []
    incomingStreets = []
    orders = []
    for n in DG:
        #print("node id is: ", n)
        intersections.append(n)
        numIncomingIntersections = 0
        orderList = []
        for u, v, data in DG.in_edges(n, data=True):
            numIncomingIntersections += 1
            orderList.append((data['name'], 1))
            #print("--------------------")
            #print("start intersection is: ", u)
            #print("end intersection is: ", v)
            #print("data is: ", data)
            #print("--------------------")
        # print("numIncoming intersections for node is: ", numIncomingIntersections)
        incomingStreets.append(numIncomingIntersections)
        orders.append(orderList)
    #print("DG is", DG.number_of_nodes())
    print("intersections are: ", intersections)
    print("incomingStreets are: ", incomingStreets)
    print("orders are: ", orders)

    # create submission file
    create_submit_file(filename, numNodes, intersections, incomingStreets, orders)



if __name__ == "__main__":
    filenames = ["exampleInput.txt", "byTheOcean.txt", "checkmate.txt", "dailyCommute.txt", "etoile.txt", "foreverJammed.txt"]
    for file in filenames: 
        main(file)