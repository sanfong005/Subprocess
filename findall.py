from re import findall
from subprocess import Popen, PIPE
import re

def ping (host,ping_count, buffer):
    max_rtt = 0
    for ip in host:
        data = ""
        output= Popen(f"ping {ip} -n {ping_count} -l {buffer}", stdout=PIPE, encoding="utf-8")

        for line in output.stdout:
            data = data + line
            ping_test = findall("TTL", data)

        if ping_test:
            print(f"{ip} : Successful Ping")
            avgRTT=re.search("Minimum = (\d+)ms, Maximum = (\d+)ms, Average = (\d+)", str(data))
            print(avgRTT)
            print(avgRTT[2])
            max_rtt = avgRTT[2]
        else:
            print(f"{ip} : Failed Ping")
    return max_rtt

#--------------------------------------------------------------------
nodes = ["192.168.191.100"]
#nodes = ["8.8.8.8"]
buffer = ["2048"]

ii = 0
rtt_list = []
s_n = 5
f_n = 12
s_l = 4
f_l = 22
i_l = 2
rtt_list = [[0]*(((f_l - s_l)/i_l)+1)]*((f_n - s_n) + 1)     # #cols * #rows
print(rtt_list)

print(xdfdf)
while ii < 30:
    for i in range(s_n, f_n):  # 8
        for j in range(s_l, f_l, i_l):   # 10
            bf = 2**i
            print('Loop : ', i)
            rtt_list.append(int(ping(nodes,j,bf)))
    ii = ii + 1
print(rtt_list)

def Average(lst):
    return sum(lst) / len(lst)

Driver Code
average = Average(rtt_list)

# Printing average of the list
print("Average of the list =", round(average, 2))

import numpy as np
import scipy.stats

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    # print(data)
    # print(a)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return round(m,2), round(m-h,2), round(m+h,2)

print(mean_confidence_interval(rtt_list))