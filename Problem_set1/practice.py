import pandas as pd
#---- Question A1 ----- 
def load_cows(filename):
    cow_df = pd.read_csv(filename, header=None)
    return dict(zip(cow_df[0],cow_df[1]))

cowdata1=load_cows('ps1_cow_data.txt')
#print(cowdata1)

#---- Question A2 ----- 
def greedy_cow_transport(data, limit=10): 
    cow_sorted = dict(sorted(data.items(), reverse= True, key=lambda x: x[1]))
    cowname_list = list(cow_sorted.keys())
    cowweight_list = list(cow_sorted.values())
    
    result = []
    index=0
    trip=[]
    
    while len(cow_sorted)>0: #keep iterating until we've added all cows to a single trip
        weight= 0        
        trip.append([])
        for i in range(len(cow_sorted)):  
            if weight + cowweight_list[i] <= limit : 
                trip[index].append (cowname_list[i])
                weight+=cowweight_list[i]
                
            index+=1        
            result.append([trip])
    return result
     

    
##Example 1
def greedy_cow_transport(cows,limit=10):
   
    trips = []
     
    cows_copy = cows.copy()
 
    cows_sorted = dict(sorted(cows_copy.items(), reverse=True, key=lambda x: x[1]))       
    total_weight = 0
    
    list_index = 0
    #Keep iterating until we've added all cows to a trip
    while len(cows_sorted) > 0:        
        total_weight = 0  
        trips.append([])       
        for (cow, weight) in cows_sorted.copy().items(): 
            if total_weight + weight <= limit:
                trips[list_index].append(cow)
                total_weight = total_weight + weight 
                del cows_sorted[cow]
        list_index += 1
               
    return trips  

## Example 2
def greedy_cow_transport(cows,limit=10):
 # TODO: Your code here
    cows_copy = sorted(cows, key=cows.get, reverse=True) # cows.get apply to all the key in cows
    result = []
    while len(cows_copy) > 0:
        totalWeight = 0
        trip = []
        for name in cows_copy[:]:
            if cows[name] + totalWeight <= limit:
                trip.append(name)
                totalWeight = totalWeight + cows[name]
                cows_copy.remove(name)
        result.append(trip)
    return result
greedy_cow_transport(cowdata1)

#### Demo
hello2 = []
for j in range(1,6):
    trip = []
    for i in range(4):
        trip.append(i+j)
    hello2.append(trip)
    
    
