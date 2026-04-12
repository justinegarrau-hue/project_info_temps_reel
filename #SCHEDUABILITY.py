#SCHEDUABILITY
#%%
from itertools import permutations
import matplotlib.pyplot as plt
import numpy as np
import math

#every tasks :
task = {"C1":(1.188, 10),"C2":(3,10),"C3":(2,20)}

#------3 tasks--------------------------------

#We take 3 tasks: we have 3! = 6 possibilities
task3 = list(task.keys())
hyperperiod = math.lcm(10,20)
print(f"hyperperiod: {hyperperiod}")
poss = list(permutations(task3))
print(f"{len(poss)} possibilities\n")

yes=[]

for priority_order in poss :
    current_time = 0
    scheduable = True  
    #we initialize a dictionnary to know when a task must be
    #executed
    next_activation = {name: 0 for name in task3}
    order = []

    while current_time<hyperperiod :
        found = False

        #we take the task which is ready to be executed
        for name in priority_order :
            wcet, period = task[name]

            #if time is over the period of the task (the deadline):
            if current_time>= next_activation[name]:
                deadline = next_activation[name] + period
                
                if current_time+wcet >deadline:
                    scheduable= False
                    break
                order.append((name, current_time, wcet))
                current_time+=wcet
                next_activation[name] += period
                found = True
                break
        if not scheduable :
            break

        if not found : #if no task is ready
            current_time+=0.1
    
    if scheduable:
        yes.append((priority_order,order))
print(f"Number of scheduable sets : {len(yes)}")

#---plot-------
#we choose the first one :
best_priority, best_order = yes[0]
print(f"schedule : {best_priority}")

colors_map = {"C1": "red", "C2": "orange", "C3": "blue", "C4": "purple", "C5": "green", "C6": "cyan", "C7": "magenta"}
fig, ax = plt.subplots(figsize=(15, 6))

for name, start_time, wcet in best_order:
    # task number
    y_pos = int(name[1:]) 
    ax.broken_barh([(start_time, wcet)], (y_pos - 0.4, 0.8), facecolors=colors_map[name])

ax.set_title(f"Non-Preemptive schedule")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Task")
ax.set_yticks([1, 2, 3])
ax.set_yticklabels(["C1", "C2", "C3"])
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_xlim(0, hyperperiod)
plt.show() 


#%%
#--------------4 tasks -------------
#We take 4 tasks: we have 4! = 24 possibilities

task = {"C1":(1.188, 10),"C2":(3,10),"C3":(2,20),"C4":(2,20)}
task4 = list(task.keys())
hyperperiod = math.lcm(10,20)
print(f"hyperperiod: {hyperperiod}")
poss = list(permutations(task4))
print(f"{len(poss)} possibilities\n")

yes=[]

for priority_order in poss :
    current_time = 0
    scheduable = True  
    #we initialize a dictionnary to know when a task must be
    #executed
    next_activation = {name: 0 for name in task4}
    order = []

    while current_time<hyperperiod :
        found = False

        #we take the task which is ready to be executed
        for name in priority_order :
            wcet, period = task[name]

            #if time is over the period of the task (the deadline):
            if current_time>= next_activation[name]:
                deadline = next_activation[name] + period
                
                if current_time+wcet >deadline:
                    scheduable= False
                    break
                order.append((name, current_time, wcet))
                current_time+=wcet
                next_activation[name] += period
                found = True
                break
        if not scheduable :
            break

        if not found : #if no task is ready
            current_time+=0.1
    
    if scheduable:
        yes.append((priority_order,order))
print(f"Number of scheduable sets : {len(yes)}")

#---plot-------
#we choose the first one :
best_priority, best_order = yes[0]
print(f"schedule : {best_priority}")

colors_map = {"C1": "red", "C2": "orange", "C3": "blue", "C4": "purple", "C5": "green", "C6": "cyan", "C7": "magenta"}
fig, ax = plt.subplots(figsize=(15, 6))

for name, start_time, wcet in best_order:
    # task number
    y_pos = int(name[1:]) 
    ax.broken_barh([(start_time, wcet)], (y_pos - 0.4, 0.8), facecolors=colors_map[name])

ax.set_title(f"Non-Preemptive schedule")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Task")
ax.set_yticks([1, 2, 3,4])
ax.set_yticklabels(["C1", "C2", "C3","C4"])
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_xlim(0, hyperperiod)
plt.show() 

# %%
#-----------------5 tasks---------------
#We take 5 tasks: we have 5! = 120 possibilities
task = {"C1":(1.188, 10),"C2":(3,10),"C3":(2,20),"C4":(2,20),"C5":(2,40)}
task5 = list(task.keys())
hyperperiod = math.lcm(10,20,40)
print(f"hyperperiod: {hyperperiod}")
poss = list(permutations(task5))
print(f"{len(poss)} possibilities\n")

yes=[]

for priority_order in poss :
    current_time = 0
    scheduable = True  
    #we initialize a dictionnary to know when a task must be
    #executed
    next_activation = {name: 0 for name in task5}
    order = []

    while current_time<hyperperiod :
        found = False

        #we take the task which is ready to be executed
        for name in priority_order :
            wcet, period = task[name]

            #if time is over the period of the task (the deadline):
            if current_time>= next_activation[name]:
                deadline = next_activation[name] + period
                
                if current_time+wcet >deadline:
                    scheduable= False
                    break
                order.append((name, current_time, wcet))
                current_time+=wcet
                next_activation[name] += period
                found = True
                break
        if not scheduable :
            break

        if not found : #if no task is ready
            current_time+=0.1
    
    if scheduable:
        yes.append((priority_order,order))
print(f"Number of scheduable sets : {len(yes)}")

#---plot-------
#we choose the first one :
best_priority, best_order = yes[0]
print(f"schedule : {best_priority}")

colors_map = {"C1": "red", "C2": "orange", "C3": "blue", "C4": "purple", "C5": "green", "C6": "cyan", "C7": "magenta"}
fig, ax = plt.subplots(figsize=(15, 6))

for name, start_time, wcet in best_order:
    # task number
    y_pos = int(name[1:]) 
    ax.broken_barh([(start_time, wcet)], (y_pos - 0.4, 0.8), facecolors=colors_map[name])

ax.set_title(f"Non-Preemptive schedule")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Task")
ax.set_yticks([1, 2, 3,4,5])
ax.set_yticklabels(["C1", "C2", "C3","C4","C5"])
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_xlim(0, hyperperiod)
plt.show() 
# %%
#------------------6 tasks---------------
#We take 6 tasks: we have 6! = 720 possibilities
task = {"C1":(1.188, 10),"C2":(3,10),"C3":(2,20),"C4":(2,20),"C5":(2,40),"C6":(2,40)}
task6 = list(task.keys())
hyperperiod = math.lcm(10,20,40)
print(f"hyperperiod: {hyperperiod}")
poss = list(permutations(task6))
print(f"{len(poss)} possibilities\n")

yes=[]

for priority_order in poss :
    current_time = 0
    scheduable = True  
    #we initialize a dictionnary to know when a task must be
    #executed
    next_activation = {name: 0 for name in task6}
    order = []

    while current_time<hyperperiod :
        found = False

        #we take the task which is ready to be executed
        for name in priority_order :
            wcet, period = task[name]

            #if time is over the period of the task (the deadline):
            if current_time>= next_activation[name]:
                deadline = next_activation[name] + period
                
                if current_time+wcet >deadline:
                    scheduable= False
                    break
                order.append((name, current_time, wcet))
                current_time+=wcet
                next_activation[name] += period
                found = True
                break
        if not scheduable :
            break

        if not found : #if no task is ready
            current_time+=0.1
    
    if scheduable:
        yes.append((priority_order,order))
print(f"Number of scheduable sets : {len(yes)}")

#---plot-------
#we choose the first one :
best_priority, best_order = yes[1]
print(f"schedule : {best_priority}")

colors_map = {"C1": "red", "C2": "orange", "C3": "blue", "C4": "purple", "C5": "green", "C6": "cyan", "C7": "magenta"}
fig, ax = plt.subplots(figsize=(15, 6))

for name, start_time, wcet in best_order:
    # task number
    y_pos = int(name[1:]) 
    ax.broken_barh([(start_time, wcet)], (y_pos - 0.4, 0.8), facecolors=colors_map[name])

ax.set_title(f"Non-Preemptive schedule")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Task")
ax.set_yticks([1, 2, 3,4,5,6])
ax.set_yticklabels(["C1", "C2", "C3","C4","C5","C6"])
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_xlim(0, hyperperiod)
plt.show() 

# %%
#------------------7 tasks---------------
#We take 7 tasks: we have 7! = 5040 possibilities
task = {"C1":(1.188, 10),"C2":(3,10),"C3":(2,20),"C4":(2,20),"C5":(2,40),"C6":(2,40),"C7":(3,80)}
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
        yes.append((priority_order,order, idle_periods, total_waiting_time))
print(f"Number of scheduable sets : {len(yes)}")

#---plot-------
#we order the list in increasing order of total_waiting_time :
ordered_yes = sorted(yes, key=lambda x: x[3])

#we check the waiting time for each possibility
# waiting = []
# for prio, order, idle, wait in ordered_yes:
#     waiting.append(wait)
# print(waiting) # the top four is equal in total_waiting time


best_priority, best_order, idle, total_waiting_time = ordered_yes[0]#idx 0,1,2 and 3 are valid and minimize the total waiting time
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
