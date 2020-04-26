import sys

ogstd = sys.stdout

fh = open("test.txt","w")
sys.stdout = fh
print(4+5)
sys.stdout = ogstd

fh.close()