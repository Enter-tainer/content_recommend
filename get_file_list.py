import glob
file_list = glob.glob("../OI-Wiki/docs/**/*.npy", recursive=True)
for (i, v) in enumerate(file_list):
  print(i, v)
