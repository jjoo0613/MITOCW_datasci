import pandas as pd
#---- Question A1 ----- 
def load_cows(filename):
    cow_df = pd.read_csv(filename, header=None)
    return dict(zip(cow_df[0],cow_df[1]))

cowdata1=load_cows('ps1_cow_data.txt')
#print(cowdata1)

#---- Question A2 -----  
def greedy_cow_transport(cowdata,limit=10):
    cow_sorted = dict(sorted(cowdata.items(), reverse= True, key=lambda x: x[1]))
    cowname = list(cow_sorted.keys())
    result = []
    
    while len(cowname) > 0:
        weight = 0
        trip = []
        for n in cowname:
            if cowdata[n] + weight <= limit: #cowdata is a dict, will return cowdata.value('n') 
                trip.append(n)
                weight += cowdata[n]
                cowname.remove(n)
        result.append(trip)
    return result

#greedy_cow_transport(cowdata1)



#---- Question A3 ----- 
# From codereview.stackexchange.com """                    
def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b

def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition] # """           
            #get_partitions(cowdata1)        
            # >>> [['Moo Moo', 'Henrietta', 'Lola', 'Betsy', 'Millie', 'Maggie', 'Oreo', 'Herman', 'Florence', 'Milkshake']]
            # >>> [['Moo Moo', 'Henrietta', 'Lola', 'Betsy', 'Millie', 'Oreo', 'Herman', 'Florence', 'Milkshake'], ['Maggie']]
            # >>> [['Moo Moo', 'Henrietta', 'Lola', 'Betsy', 'Millie', 'Maggie', 'Oreo', 'Florence', 'Milkshake'], ['Herman']]
            # ... and more... 
#####

def brute_force_cow_transport(cows,limit=10):
    result = []
    for item in get_partitions(cows):  #single line: [['Moo Moo', 'Henrietta', 'Lola', 'Betsy', 'Millie', 'Maggie', 'Oreo', 'Florence', 'Milkshake'], ['Herman']]
        for cowtrip in item:  #single trip: ['Moo Moo', 'Henrietta', 'Lola', 'Betsy', 'Millie', 'Maggie', 'Oreo', 'Florence', 'Milkshake'] or ['Herman']
            weight = 0 #assigned to the trip
            tripscore = 0 #assigned to the trip
            for cowname in cowtrip: #Moo Moo in cowtrip ['Moo Moo', 'Henrietta', 'Lola', 'Betsy', 'Millie', 'Maggie', 'Oreo', 'Florence', 'Milkshake'] 
                weight += cows[cowname] #add each cow's weight per weight of "cowtrip"
            if weight > 10: 
                tripscore = 1 #bool -> if have any weight >10 in cowtrip, the tripscore of the cowtrop =1 --> will be excluded 
        if tripscore == 0:
            result.append(item)
            
    return result

#---- Question A4 ----- 
# Problem 4
import time 

def compare_cow_transport_algorithms(limit=10):
    cowdata = load_cows('ps1_cow_data.txt')
    print('==Greedy Cow Algorithm ==')
    start = time.time()
    greedy=greedy_cow_transport(cowdata, limit)
    end = time.time()
    print('Greedy cow transport time:', end-start)
    print('Number of Possible Trips ', len(greedy))
    print('\n')
    print('==Brute force Cow Algorithm ==')
    start1 = time.time()
    brute=brute_force_cow_transport(cowdata, limit)
    end1 = time.time()
    print('Brute force transport time:', end1-start1)
    print('Number of Possible Trips ', len(brute))
compare_cow_transport_algorithms()
