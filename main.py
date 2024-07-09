def fine_busiest_intersectiopns(intersections_list):
    busiest =[]
    busiestValue = 0
    intersectionNo = 0
    for intersection in intersections_list:
        if intersection > busiestValue:
            busiestValue =intersection
            busiest = [intersectionNo]
        elif intersection == busiestValue:
             busiest.insert(intersectionNo)
        intersectionNo+=1     
    return [busiest]



intersections_list = [1,2,3,1,4,5,]
busiest_intersection = fine_busiest_intersectiopns(intersections_list)
if (len(busiest_intersection)) == 1:
    print("The busiest intersection is intersection no.:", busiest_intersection)
else:
    print("The businest intersection are intersection no.:", busiest_intersection)