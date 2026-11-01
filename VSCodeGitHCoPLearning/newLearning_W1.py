import numpy as np
l= [1,4,3,6,7,25,16]
print ([x for x in l if x%2==0])
print ([x**2 if x%2==0 else "Not even" for x in l])

l2=[2,5,1,7,10,4,5]
print (sum([x for x in l2 if str(x).isdigit()])) 
print (np.sum(np.array(l2)))
print (sum(l2))


print ("Hello world")
print ("Hello"," world", sep="---")
print ("Hello world", end="::::")
print ("Hello there")
name="Aswathy"
title="Ms"
ageLimit=18
print (f"Hello {title}.{name}! How are you?")
print ("Hello {title}.{name}! How are you?".format(title=title, name=name))
print ("Hello %s.%s! Are you above %d?" % (title, name, ageLimit))
