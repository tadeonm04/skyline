import matplotlib.pyplot as plt 
import numpy as np
import random

n=int(input('Introduce number of buildings: '))
buildx=[]
buildy=[]
SKYLINE1=[]
SKYLINE2=[]
#THIS FIRST SCRIPT SHOW ONLY THE SILLHOUETTE OF BUILDINGS

def skyrandlr(a,b):
    l=random.randint(a,b)
    r=random.randint(a,b)
    R=max(l,r)
    L=min(l,r)
    buildingsx=[L,L,R,R]
    yield buildingsx

def skyrandh(a,b):
	H=random.randint(a,b)
	buildingsy=[0,H,H,0]
	yield buildingsy

def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)

print('Introduce interval where random numbers will be created: ')
a=int(input('Min: '))
b=int(input('Max: '))

for i in range(n):
	for j in range(4):
		buildx.append(next(skyrandlr(a,b)))
		buildy.append(next(skyrandh(a,b)))
		BUILDX=[buildx[i][j]]
		BUILDY=[buildy[i][j]]
		SKYLINE1.append(BUILDX)
		SKYLINE2.append(BUILDY)


print('x', buildx,'y', buildy)
print('EEE',BUILDX,BUILDY)
print('sss',SKYLINE1,'ppp',SKYLINE2)
#plt.figure(figsize=(a,b))
plt.title('Skyline')
plt.xlabel('Longitud')
plt.ylabel('Altura')
plt.plot(SKYLINE1,SKYLINE2)
plt.show()

