def fine_busiest_intersectiopns(intersections_list):
    busiest =[] #create list to use for store list of busiest intersection
    if (len(intersections_list) == 0): #check if enter empty list
        return busiest  #return empty list if enter empty list
    busiestValue = intersections_list[0] #set value to record highest value
    intersectionNo = 0  #name the intersection
    for intersection in intersections_list: #use for loop to compare intersection
        if intersection > busiestValue: #if found higher
            busiestValue =intersection  #set as record
            busiest = [intersectionNo]  #reset businest to have only new record
        elif intersection == busiestValue: #check if found same highest value
             busiest.append(intersectionNo) #add new member
        intersectionNo+=1     #create new name dor next intersection
    return busiest  #return businest intersection list



intersections_list = [] #example for test
busiest_intersection = fine_busiest_intersectiopns(intersections_list)  #use the function
if (len(busiest_intersection)) == 1:    #summary
    print("The busiest intersection is intersection no.:", busiest_intersection[0])
else:
    print("The businest intersection are intersection no.:", busiest_intersection)