import pandas as pd
import time
import random
# t1=time.time()
# train = pd.read_csv('train.csv', delimiter='\t')
# t2=time.time()
# print(t2-t1)
train = pd.read_csv('train.csv', delimiter='\t')

for i in range(20):
    aa = str(random.randint(10000,20000))
    filename =aa+".csv"
    t1=time.time()
    train.to_csv(filename)
    t2=time.time()
    print(t2-t1)

