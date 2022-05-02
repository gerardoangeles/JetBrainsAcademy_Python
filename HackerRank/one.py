def fx(job, k):
    j = 0
    for _ in range(0, k):
        job[j] = job[j] + 1
        j = j + 1
        if j >= len(job):
            j = 0
    
    n_min = min(job)
    n_max = max(job)
    print(job)
    print(n_max - n_min)

def a(job, k):
    p = 1
    while p <= k:
        min_value = min(job)
        for i, j in enumerate(job):
            if j == min_value:
                job[i] = job[i] + 1
                break
        p = p + 1
        
    print(job)
            

a([4, 3, 2, 2, 2], 10)
