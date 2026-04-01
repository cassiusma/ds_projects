def summary_stats(vector:list)->dict:
    n = len(vector)
    mean = sum(vector)/n
    variance = sum( (x - mean)**2 for x in vector )/(n-1)
    std = variance**0.5
    sortvector = sorted(vector)
    if (n%2==0):
        median = (sortvector[n//2-1]+sortvector[n//2])/2
    else:
        median = sortvector[n//2]
    return {"n":n, "mean":round(mean,4), "variance":round(variance,4), "std":round(std,4), "median":median}