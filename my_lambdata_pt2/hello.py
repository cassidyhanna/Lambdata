from pandas import DataFrame
from my_lambdata_pt2.my_mod import enlarge

print("Hello")

print(enlarge(8))

df = DataFrame({"state": ["OR","CA","CT","TX"]})
print(df.head())
