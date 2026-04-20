
#%%
from itertools import permutations
import matplotlib.pyplot as plt
import numpy as np
import math

#set of tasks :
task = {"C1":(1.188, 10),"C2":(3,10),"C3":(2,20),"C4":(2,20),"C5":(2,40),"C6":(2,40),"C7":(3,80)}

#%%
#Case number 1 : 

#please choose the number of desired tasks to do computation
#between 3 and 7 :
nb_tasks = 7
if nb_tasks<3 or nb_tasks>7 :
    print("Please choose between 3 and 7 !")
print(f"Number if tasks: {nb_tasks}")
#We calculate the hyperperiod :
if nb_tasks == 3 or nb_tasks==4:
    hyperperiod = math.lcm(10,20)
if nb_tasks ==5 or nb_tasks==6:
    hyperperiod = math.lcm(10,20,40)
if nb_tasks ==7 :
    hyperperiod = math.lcm(10,20,40,80)
print(f"hyperperiod: {hyperperiod}s")

#we convert into a list for the name of the tasks 
#and choose only the desired tasks:
tasks = list(task.keys())
tasks = tasks[0:nb_tasks]

#permutations of the set :
poss = list(permutations(tasks))
print(f"{len(poss)} possibilities\n") # = nb_tasks !

yes=[]

for priority_order in poss :
    current_time = 0
    scheduable = True  
    #we initialize a dictionnary to know when a task must be
    #executed
    next_activation = {name: 0 for name in tasks}
    #we initialize an other to stock the response time for each task:
    response_times = {name: [] for name in tasks} 

    order = []
    idle_periods = []
    total_waiting_time = 0

    while current_time<hyperperiod :
        found = False

        #we take the task which is ready to be executed
        for name in priority_order :
            wcet, period = task[name]

            #if time is over the period of the task (the deadline):
            if current_time>= next_activation[name]:

                #calculation of the response time :
                finish_time = current_time + wcet
                response_time = finish_time - next_activation[name]
                response_times[name].append(response_time)

                deadline = next_activation[name] + period
                
                if current_time+wcet >deadline:
                    scheduable= False
                    break

                waiting_time = current_time - next_activation[name]
                total_waiting_time+=waiting_time

                order.append((name, current_time, wcet))
                current_time+=wcet
                next_activation[name] += period
                found = True
                break

        if not scheduable :
            break

        if not found : #if no task is ready
            idle_periods.append((current_time, 0.1))
            current_time+=0.1
    
    if scheduable:
        wcrt = {n: max(times) for n, times in response_times.items()}
        yes.append((priority_order,order, idle_periods, total_waiting_time,wcrt))
print(f"Number of scheduable sets : {len(yes)}")

#---plot-------
#we order the list in increasing order of total_waiting_time :
ordered_yes = sorted(yes, key=lambda x: x[3])

idx = 0
wait_shorter = ordered_yes[0][3]
for prio, order, idle, wait, wcrt in ordered_yes:
    if wait == wait_shorter:
        idx += 1
    else :
        break
print(f"total waiting time: {wait_shorter}s")
#print the number of index with the shortest waiting time
print(f"number of sets with a minimized waiting time: {idx}") 

print(f"Response time: {ordered_yes[0][4]}s")


for i in range(idx) :
    best_priority, best_order, idle, total_waiting_time , wcrt= ordered_yes[i]
    print(f"schedule : {best_priority}")

    colors_map = {"C1": "red", "C2": "orange", "C3": "blue", "C4": "purple", "C5": "green", "C6": "cyan", "C7": "magenta"}
    fig, ax = plt.subplots(figsize=(15, 6))

    for name, start_time, wcet in best_order:
        # task number
        y_pos = int(name[1:]) 
        ax.broken_barh([(start_time, wcet)], (y_pos - 0.4, 0.8), facecolors=colors_map[name])

    for start_idle, duration in idle:
        ax.broken_barh([(start_idle, duration)], (0 - 0.4, 0.8), facecolors="black")

    ax.set_title(f"Non-Preemptive schedule")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Task")
    ax.set_yticks([0,1, 2, 3,4,5,6,7])
    ax.set_yticklabels(["idle","C1", "C2", "C3","C4","C5","C6","C7"])
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_xlim(0, hyperperiod)
    plt.show() 
# %%

# Case number 2 : 
#task 5 is allowed to miss a deadline and the total 
# wainting time is minimize
#We take 7 tasks: we have 7! = 5040 possibilities

task7 = list(task.keys())
hyperperiod = math.lcm(10,20,40,80)
print(f"hyperperiod: {hyperperiod}")
poss = list(permutations(task7))
print(f"{len(poss)} possibilities\n")

yes=[]

for priority_order in poss :
    current_time = 0
    scheduable = True  
    #we initialize a dictionnary to know when a task must be
    #executed
    next_activation = {name: 0 for name in task7}
    order = []
    idle_periods = []
    total_waiting_time = 0

    while current_time<hyperperiod :
        found = False

        #we take the task which is ready to be executed
        for name in priority_order :
            wcet, period = task[name]

            #if time is over the period of the task (the deadline):
            if current_time>= next_activation[name]:
                deadline = next_activation[name] + period
                
                #if the deadline is missed is not scheduable, except for the task 5 :
                if current_time+wcet >deadline :
                    if name != 'C5':
                        scheduable= False
                        break

                waiting_time = current_time - next_activation[name]
                total_waiting_time+=waiting_time

                order.append((name, current_time, wcet))
                current_time+=wcet
                next_activation[name] += period
                found = True
                break

        if not scheduable :
            break

        if not found : #if no task is ready
            idle_periods.append((current_time, 0.1))
            current_time+=0.1
    
    if scheduable:
        yes.append((priority_order,order, idle_periods, total_waiting_time))
print(f"Number of scheduable sets : {len(yes)}")

#---plot-------
#we order the list in increasing order of total_waiting_time :
ordered_yes = sorted(yes, key=lambda x: x[3])

#we check the waiting time for each possibility
idx = 0
wait_shorter = ordered_yes[0][3]
for prio, order, idle, wait in ordered_yes:
    if wait == wait_shorter:
        idx += 1
    else :
        break
print(f"total waiting time: {wait_shorter}s")
print(f"number of sets with a minimized waiting time: {idx}") #print the number of index with the shortest waiting time


for i in range(idx) :
    best_priority, best_order, idle, total_waiting_time = ordered_yes[i]
    print(f"schedule : {best_priority}")

    colors_map = {"C1": "red", "C2": "orange", "C3": "blue", "C4": "purple", "C5": "green", "C6": "cyan", "C7": "magenta"}
    fig, ax = plt.subplots(figsize=(15, 6))

    for name, start_time, wcet in best_order:
        # task number
        y_pos = int(name[1:]) 
        ax.broken_barh([(start_time, wcet)], (y_pos - 0.4, 0.8), facecolors=colors_map[name])

    for start_idle, duration in idle:
        ax.broken_barh([(start_idle, duration)], (0 - 0.4, 0.8), facecolors="black")

    ax.set_title(f"Non-Preemptive schedule")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Task")
    ax.set_yticks([0,1, 2, 3,4,5,6,7])
    ax.set_yticklabels(["idle","C1", "C2", "C3","C4","C5","C6","C7"])
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_xlim(0, hyperperiod)
    plt.show() 


# %%
