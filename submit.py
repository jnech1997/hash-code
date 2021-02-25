'''
  1. num_schedule_intersections --> number of intersections we provide a schedule for (eg. 3)
  2. intersections --> list of intersections we provide a schedule for (eg. [1,0,2])
  3. num_incoming_streets --> list of number of incoming streets provided by the schedule for the intersection at intersections[i] (eg. [2,1,1])
  4. orders --> list of lists of tuples of (streetID, time) representing the order and duration of green lights 
                     (eg. [[('rue-d-athenes',2), ('rue-d-amsterdam', 1)], [('rue-de-londres', 2)], [('rue-de-moscou', 1)] ] )
'''




def create_submit_file(num_schedule_intersections, intersections, num_incoming_streets, orders):
    filename = 'submission.txt'

    file = open(filename,"w")

    file.write(str(num_schedule_intersections)+'\n')
    
    for i in range(num_schedule_intersections):
        file.write(str(intersections[i])+'\n')
        file.write(str(num_incoming_streets[i])+ '\n')
        order = orders[i]
        for o in order:
            file.write(str(o[0]) + ' ' + str(o[1]) + '\n')
    
    file.close()

        
if __name__ == "__main__":
    n = 3
    ints = [1,0,2]
    nis = [2,1,1]
    orders = [[('rue-d-athenes',2), ('rue-d-amsterdam', 1)], [('rue-de-londres', 2)], [('rue-de-moscou', 1)] ]
    create_submit_file(n,ints,nis,orders)