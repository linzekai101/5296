import pandas as pd
import time
for i in range(20):
    t1=time.time()
    train = pd.read_csv('train.csv', delimiter='\t')
    t2=time.time()
    print(t2-t1)