import sys

print(len(sys.argv))

if(len(sys.argv) > 1):
    print(sys.argv[1])
else:
    print("no args")