print ("Hello world")

text="Hello world"
def helloworld(*args,**kwargs):
    print(args)
    for k,v in kwargs.items():
        print(k, v )

helloworld("Hi","Hello","Hey",a="Mira", b="Hira", c="Jira")




import numpy as np
l=np.arange(1,10,1)
li=[x for x in l if x%2==0]
print(li)
