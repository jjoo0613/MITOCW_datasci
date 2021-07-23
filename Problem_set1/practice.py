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


def brute_force_cow_transport(cows,limit=10):
    result = []
    for item in get_partitions(cows): 
        for cowtrip in item: 
            weight = 0
            tripscore = 0
            for cowname in cowtrip:
                weight += cows[cowname]
            if weight > 10: 
                tripscore += 1
        if tripscore == 0:
            result.append(item)
            
    return result
