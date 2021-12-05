import tensorflow
import tensorflow_hub as hub
import tensorflow_text
import numpy as np
import glob
from tqdm import tqdm

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual/3")

file_list = glob.glob("../OI-Wiki/docs/**/*.stripped", recursive=True)

for i in tqdm(file_list):
  # print("processing " + i)
  with open(i) as f:
    content = f.read()
    vec = embed(content).numpy().reshape(512)
    np.save(i + '.npy', vec)
