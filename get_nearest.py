import glob
import numpy as np
from horapy import BruteForceIndex
dimension = 512
index = BruteForceIndex(dimension, "usize")
file_list = glob.glob("../OI-Wiki/docs/**/*.npy", recursive=True)
# for (i, v) in enumerate(file_list):
#   print(i, v)
vec_list = []
for (i, v) in enumerate(file_list):
  tmp = np.load(v)
  index.add(tmp, i)
  vec_list.append(tmp)

index.build("euclidean")
target = 214
res = index.search(vec_list[target], 10)
print("res for {} :".format(file_list[target]))
for i in res[1:]:
  print(file_list[i][:-13])
