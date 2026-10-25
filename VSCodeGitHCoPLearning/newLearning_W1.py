print ("Hello world")
l= [1,4,3,6,7,25,16]
print ([x for x in l if x%2==0])
print ([x**2 if x%2==0 else "Not even" for x in l])