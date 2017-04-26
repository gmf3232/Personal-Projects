import random

# Creates random strategies by randomly allocating high values to high districts
def RandoStrat(init, n, w):
    strats = []
    potential = []
    while len(strats) < w:
        res = init
        i = 0
        while i < n-1:
            rand = random.randint(0,res)
            potential.append(rand)
            res -= rand
            i += 1
        potential.append(res)
        strats.append(potential)
        potential = []
    return strats

#Ensures that each distict gets at least one vote and a maximum of 40 votes
def RandoStrat2(init, n, w):
    strats = []
    potential = []
    while len(strats) < w:
        res = init
        i = 0
        while i < n-1:
            ran = min(res, 40)
            rand = random.randint(0,ran)
            rand = min(rand,res-n+i+1)
            rand = max(rand,1)
            potential.append(rand)
            res -= rand
            i += 1
        potential.append(res)
        strats.append(potential)
        potential = []
    return strats

#Ensures that each district gets at least 2 votes
def RandoStrat3(init, n, w):
    strats = []
    potential = []
    while len(strats) < w:
        res = init
        i = 0
        while i < n-1:
            ran = min(res, 40)
            rand = random.randint(0,ran)
            rand = min(rand,res - 2*(n-i-1))
            rand = max(rand,2)
            potential.append(rand)
            res -= rand
            i += 1
        potential.append(res)
        strats.append(potential)
        potential = []
    return strats

# At least 3 in each
def RandoStrat4(init, n, w):
    strats = []
    potential = []
    while len(strats) < w:
        res = init
        i = 0
        while i < n-1:
            ran = min(res, 40)
            rand = random.randint(0,ran)
            rand = min(rand,res - 3*(n-i-1))
            rand = max(rand,3)
            potential.append(rand)
            res -= rand
            i += 1
        potential.append(res)
        strats.append(potential)
        potential = []
    return strats

# Cap at 30
def RandoStrat5(init, n, w):
    strats = []
    potential = []
    while len(strats) < w:
        res = init
        i = 0
        while i < n-1:
            ran = min(res, 30)
            rand = random.randint(0,ran)
            rand = min(rand,res - 3*(n-i-1))
            rand = max(rand,3)
            potential.append(rand)
            res -= rand
            i += 1
        potential.append(res)
        strats.append(potential)
        potential = []
    return strats

def BlottoGame(strat1, strat2, n):
    p1score = 0
    p2score = 0

    for i in range(n):
        if strat1[i] > strat2[i]:
            p1score += n-i
        elif strat1[i] < strat2[i]:
            p2score += n-i

    return (p1score,p2score)

def simResults(strats):
    results = []
    j = 0
    while j < len(strats):
        sum_of_scores = 0
        i = 0
        while i < len(strats):
            sum_of_scores += BlottoGame(strats[j], strats[i], len(strats[j]))[0]
            i += 1
        avg_score = round(sum_of_scores / (len(strats)-1), 2)
        results.append( (avg_score, j) )
        j += 1
    return results

def AverageStrat4(init, n, w):
    strats = RandoStrat4(init, n, w)
    totals = []
    i = 0
    while i < n:
        j = 0
        district_sum = 0
        while j < len(strats):
            district_sum += strats[j][i]
            j += 1
        totals.append(district_sum)
        i += 1
    average = [int(round(x/w)) for x in totals]
    return average
"""
strats = RandoStrat(100,10,5) # put money in big districts, 0-4
strats += RandoStrat2(100,10,5) # cap districts at 40, at least 1 in each, 5-9
strats += RandoStrat3(100,10,5) # cap districts at 40, at least 2 in each, 10-14
strats += RandoStrat4(100,10,5) # 40 cap, at least 3 in each, 15-19
strats += [[10]*10]*5 # all 10's, 20-24
strats += [[30,30,30,4] + [1]*6]*5 # 30,30,30,4,and the rest are 1's, 25-29
strats += [[5,30,5,20,15,10,10,2,2,1]]*5 # 30-34
strats += [[30,3,20,20,11,5,3,3,2,3]]*5 # 35-39
strats += [[20,18,16,14,12,10,6,2,1,1]]*5 # 40-44
strats += [[4,6,18,21,15,16,12,4,2,2]]*5 #45 - 49
strats += [[35,29,25,0,0,0,11,0,0,0]]*5 #50-54
strats += RandoStrat5(100,10,5) # 30 cap, at least 3 on each, 55-59
strats += [AverageStrat4(100,10,300)] # 60
strats += [[32,0,15,18,20,15,0,0,0,0]]*5 # 61-65
strats += [[3,29,25,25,3,3,3,3,3,3]]*5 # 66-70

for i in range(len(strats)):
    print("%s: %s" % (i,strats[i]))

example = simResults(strats)
sorted_example = sorted(example, reverse=True)
print(sorted_example)
#s1 = results[0]
#s2 = results[1]
# print(RandoStrat4(100,10,1)[0])



sample_average = AverageStrat4(100,10,50)
print("Strategy 4 average: %s" % sample_average)
winner_index = sorted_example[0][1]
print("Winner: %s" % strats[winner_index])
Avg_vs_winner = BlottoGame(sample_average, strats[winner_index], 10)
print("Average vs winner: {0}".format(Avg_vs_winner))
"""
def RandoStratFloat(init, n, w):
    strats = []
    potential = []
    while len(strats) < w:
        res = init
        i = 0
        while i < n-1:
            ran = min(res, 40)
            rand = random.uniform(0,ran)
            rand = min(rand,res - 4*(n-i-1))
            rand = max(rand,4)
            potential.append(rand)
            res -= rand
            i += 1
        potential.append(res)
        strats.append(potential)
        potential = []
    return strats

strats2 = RandoStratFloat(100,10,5)
strats2 += RandoStrat3(100,10,5) # cap districts at 40, at least 2 in each, 10-14
strats2 += RandoStrat4(100,10,5) # 40 cap, at least 3 in each, 15-19
strats2 += [[10]*10]*5 # all 10's, 20-24
strats2 += [[30,30,30,4] + [1]*6]*5 # 30,30,30,4,and the rest are 1's, 25-29
strats2 += [[5,30,5,20,15,10,10,2,2,1]]*5 # 30-34
strats2 += [[30,3,20,20,11,5,3,3,2,3]]*5 # 35-39
strats2 += [[20,18,16,14,12,10,6,2,1,1]]*5 # 40-44
strats2 += [[4,6,18,21,15,16,12,4,2,2]]*5 #45 - 49
strats2 += [[35,29,25,0,0,0,11,0,0,0]]*5 #50-54
strats2 += RandoStrat5(100,10,5) # 30 cap, at least 3 on each, 55-59
strats2 += [AverageStrat4(100,10,300)] # 60
strats2 += [[32,0,15,18,20,15,0,0,0,0]]*5 # 61-65
strats2 += [[3,29,25,25,3,3,3,3,3,3]]*5 # 66-70

for i in range(len(strats2)):
    print("%s: %s" % (i,strats2[i]))
example2 = simResults(strats2)
sorted_example2 = sorted(example2, reverse=True)
print(sorted_example2)
