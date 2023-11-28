def median(num_list):
    sorted_list = sorted(num_list)
    n=len(num_list)
    if n % 2 == 1:
        return  num_list[n//2]
    # //为向下取整 3//2=1
    else:
        return (num_list[n//2-1]+num_list[n//2])/2
print(median([69,124,-32,27,217]))

import statistics
print(statistics.median([69,124,-32,27,217]))