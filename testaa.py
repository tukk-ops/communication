import numpy as np
class ScoreAnalyzer:
    def __init__(self,ss):
        self.scores = np.array(ss)
    def get_max(self):
        return np.max(self.scores, axis =1)
    def get_avg(self):
        avg =  np.mean(self.scores, axis =0)
        return np.round(avg, 1)
data = input().split()
n,m  = map (int, data)
all_s = []
for i in range(n):
    line = list(map(int, input().split()))
    all_s.append(line)
    test = ScoreAnalyzer(all_s)

maxs = test.get_max()
print(*(maxs))
avgs = test.get_avg()
print(*(f"{x:.1f}"for x in avgs))