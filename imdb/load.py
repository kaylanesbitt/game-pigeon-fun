from datasets import load_dataset
from collections import Counter

ds = load_dataset("MrbBakh/Rotten_Tomatoes")

#print(ds.data)

#print(ds.cache_files)

#print(ds.num_columns)

#print(ds.num_rows)

#print(ds.train)


labels = ds["train"]["label"]
freqs = Counter(labels)
print(freqs)


# This is more efficient than a list comprehension
texts = ds["train"]["text"]



