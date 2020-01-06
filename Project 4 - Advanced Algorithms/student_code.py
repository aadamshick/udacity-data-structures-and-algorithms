import math
import heapq
    
def shortest_path(M,start,goal):
    print("shortest path called")
    
    if start == goal:
        return [start]
    
    dist = {} #dictionary to store the distance from each intersection to the goal

    frontier = [] #min heap to store the frontier, represented as a tuple of the estimated cost and custom path class
    explored = {} #dictionary to store the explored intersections and the "best" custom path class
    
    #populate distance dictionary
    for x in M.intersections:
        dist[x] = distance(M.intersections[x][0], M.intersections[x][1], M.intersections[goal][0], M.intersections[goal][1])
        
    #heapify the frontier
    heapq.heapify(frontier)
    
    #put starting node in frontier
    path_cost = 0
    estimated_cost = path_cost + dist[start]
    path = Path(start, path_cost, None)
    heapq.heappush(frontier, (estimated_cost, path))
    
    #while the frontier is not empty...
    while len(frontier) > 0:
        
        #pop the tuple with the smallest total distance
        t = heapq.heappop(frontier)
        frontier_path = t[1]
        frontier_intersection = frontier_path.intersection
        explored_path = explored.get(frontier_intersection, None)
        
        #if the intersection hasn't been explored
        if explored_path == None:
            
            #update explored
            explored[frontier_intersection] = frontier_path
            
            #add children to frontier
            for child_intersection in M.roads[frontier_intersection]:
                path_cost = frontier_path.accumulated_cost + distance(M.intersections[frontier_intersection][0], M.intersections[frontier_intersection][1], M.intersections[child_intersection][0], M.intersections[child_intersection][1])
                estimated_cost = path_cost + dist[child_intersection]
                path = Path(child_intersection, path_cost, frontier_path)
                heapq.heappush(frontier, (estimated_cost, path))
                
        #if the intersection has been explored
        elif explored_path.accumulated_cost > frontier_path.accumulated_cost:
            
            #update explored
            explored[frontier_intersection] = frontier_path
    

    #return a list of the path corresponding to the goal in the explored dictionary
    output = []

    temp = explored[goal]
    
    while temp.previous_path:
        output = [temp.intersection] + output
        temp = temp.previous_path
    
    return [temp.intersection] + output

#custom path class, containing intersection, accumulated cost, and previous path
class Path:
    def __init__(self, intersection, accumulated_cost, previous_path = None):
        self.intersection = intersection
        self.accumulated_cost = accumulated_cost
        self.previous_path = previous_path

#custom distance function
def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist