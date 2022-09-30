import time

start=time.time()
for o in range (1,100,2):
    print(o)
    
end = time.time()
print(end-start)

print("-----------------")

inici = time.time()
for i in range (0,200):
    if i%2==0:
        print(i)
        
fi=time.time()
print(inici-fi)