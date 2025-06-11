Processes = [
    {"pid": "P1", "arrival_time": 0, "burst_time": 5},
    {"pid": "P2", "arrival_time": 1, "burst_time": 3},
    {"pid": "P3", "arrival_time": 2, "burst_time": 1}
]
time_quantum = 2


def round_robin(processes: list, q: int) -> None:
    queue = []
    ready = []
    exec_time = 0
    t = 0
    log = []

    while processes or queue:
        # append new processes
        ready = list(p for p in processes if p["arrival_time"] <= t)
        processes = processes[len(ready):]
        queue += ready

        # select next process
        p = queue[0]

        # run process
        p["burst_time"] -= 1
        exec_time += 1
        
        # time's up or process done
        if exec_time == q or p["burst_time"] == 0: 
            log.append(f"{p['pid']}({exec_time})")
            
            exec_time = 0
            
            # add processes to the back of the ready queue
            if p["burst_time"] > 0: processes.append(p)
            queue.pop(0)

            
        # increment time
        t += 1



    print(" -> ".join(log))


round_robin(Processes, time_quantum)