import numpy as np

with np.load('data/Data2.npz') as X:
    mtx, dist, rvecs, tvecs = [X[i] for i in ('arr_0', 'arr_1', 'arr_2', 'arr_3')]
    print mtx
    print dist
    print tvecs[0][:][:]
