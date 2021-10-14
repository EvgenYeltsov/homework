import sys

params = sys.argv[1]

fd = open("test_1_9_3.txt", "a")
fd.write(params + '\n')
fd.close
