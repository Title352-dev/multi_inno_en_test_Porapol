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