'''from collections import Counter

n = int(input())
i = 0
lst = []
for i in range(n):
    a = int(input())
    lst.append(a)
#for x in lst:
   # print(x)
    #print("Occurs : ")
    #print(lst.count(x))
'''


'''    
d= {}
n = int(input('number of inputs?'))
for i in range(n):
    a = int(input())
    if a in d:
        d[a]+= 1
    else:
        d[a]= 1
print(d)
print()
print(d[max(d])
print(d[min(d)])
'''
#  lst = input().split()
# lst = [1,2,3,4,5,5]
'''lstnew = []
lst = [121,121,312,511,112,512212,512,11,52]
for x in lst:
    if x in lstnew:
        continue
    else:
        lstnew.append(x)
lstnew = sorted(lstnew)
n = int(input())
print(lstnew[n-1])
print(lstnew)

l = [1,2,3,4,5,5]
l = set(l)
k = int()
for i in range(k-1):
    l.remove(max(l))
print(max(l))
    '''

'''a = [5,7,3,4,37,9,18,24,0,1,24,23,6]
b = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
q = []
r = set(zip(a,b))

print(sorted(r))
#r = zip(a, b)
#print(*(p))
'''
'''col = 10
row = 10
r = [[0 for x in range(col)] for y in range(row)]
print(r)'''

# MATRIX SADANA BHAIYA SOLUTION

'''
col = int(input('col? : '))
row = int(input('row? : '))'''

'''n = int(input())
l = [[0 for x in range(n)] for y in range(n)]
for i in range(n):
    for j in range(n):
        l[i][j] = int(input())
for i in range(n):
    for j in range(n):
        if (i+j) >=n:
            l[i][j]=0
for i in range(n):
    for j in range(n):
        print(l[i][j], end = ' ')
    print()

'''

'''
class person:
    def __init__(self,name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        zipp= zip(name,gender,age)
        self.zip = zipp
    def display(self,zip):
        print(zip)
        return zip
a = person(input(),input(),input())
a.display(zip)
'''

'''
class car:
    def __init__(self,company, type, colour, mileage):
        self.company = company
        self.type = type
        self.colour = colour
        self.mileage = mileage

    def display(self):
        print(self.company, self.type, self.colour, self.mileage)

    def reqlitres(self,km):
        int(self.mileage)
        self.km = km
        int(km)
        print(km/self.mileage)

a = car('tt','suv','red',15)
a.display()
a.reqlitres(int(input('\n'+ 'KM to be covered? - ')))'''

# Q 1
'''class policeman:
    def __init__(self,name, age , post, color):
        self.name = name
        self.age = age
        self.post = post
        self.color = color
    
    def display(self):
        if self.post == 'inspector':
            self.color = 'green'
    
        elif self.post == 'comissioner':
            self.color = 'red'
    
        elif self.post == 'sho':
            self.color = 'blue'
    
        return self.name, self.age, self.post, self.color

a = policeman('rameam','2220','sho','')
print(a.display())'''

# Q 2

'''class calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
               
    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b
    def display(self):
        return self.add() , self.sub(), self.mul(), self.div()

a = calc(13,12)
print(a.display())'''

#Q3

'''
class students:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
lst = []
for x in range(9):
    lst.append(students(input('name? '),int(input('marks? \n'))))
print('')'''

'''
class a:
    def __init__(self, name):
        self.name = name

b = a('alefn')
b.age = 20
setattr(a,'age',2124)
print(b.age)
'''


# INHERITANCE

'''class a:
    def __init__(self,r):
        self.r = r
            
    def xyz(self):
        print('alefkn')
class b(a):
    def __init__(self):
        a.__init__(self,14)
class c(a,b):
    def __init__(self):
        a.__init__(self,14)
        b.__init__(self)
'''

# HYBRID INHERITANCE mysolution
'''
class a:
    def __init__(self):


class b(a):
    def __init__(self):
        a.__init__(self)


class c(b):
    def __init__(self):
        b.__init__(self)


class d(b):
    def __init__(self):
        b.__init__(self)
'''
'''class d:
    def __init__(self):
        print('kajefkaejbfa')
    def type(self):
        print('works')


class b(d):
    def __init__(self):
        d.__init__(self)
        print('aejfakejbf')
    def typee(self):
        print('worsksk')

class c(d):
    def __init__(self):
        d.__init__(self)
        print('akefaef')
    def typeee(self):
        print('workassasa')


class a(b,c):
    def __init__(self):
        b.__init__(self)
        c.__init__(self)
t = a()
print('')
t.type()
t.typee()
t.typeee()


'''
'''
class a:
    def _init_(self, m):
        self.k = m
class b(a):
    def _init_(self,l):
        a._init_(self, l)
        self.j=self.k
        self.n=l
class f(b):
    def _init_(self,q):
        b._init_(self, q)
        self.q=self.n
class c(b):
    def _init_(self,p):
        b._init_(self, p)
        self.t=p
class d(f,c):
    def _init_(self,i):
        f._init_(self, i )
        c._init_(self,i )
        self.o=i
class e(d):
    def _init_(self):
        d._init_(self, 7)
        pass
y=e()
print(y)'''

'''
class d(c,f):
    def __init__(self):
        c.__init__(self)
        f.__init__(self)
        print('class f')


class e(d):
    def __init__(self):
        a.__init__(self)
        d.__init__(self)
        print('class e')
r = e()
'''






'''

class a:
    def _init_(self,m):
        k= m
        
        
class b(a):
    
    def _init_(self,l):
        a._init_(self,9)
        j=self.m
        n=l


class f(b):

    def _init_(self,q):
        b._init_(self)
        q=self.n


class c(b):

    def _init_(self,p):
        b._init_(self)
        t=p


class d(f,c):

    def _init_(self, i):
        f._init_(self)
        c._init_(self)
        o=i


class e(d):

    def _init_(self,g,h,z,v,x):
        d._init_(self)
        pass
y=e(10,9,8,6,5)
print(y.k)'''
'''


import pandas as pd
import os
from sklearn.preprocessing import Imputer
import numpy as np

d = pd.read_csv('loan.csv')
numpyArray = d.values
imputerobject = Imputer(missing_values='NaN',strategy='mean',axis = 0)
imputerobject = imputerobject.fit(numpyArray[:,8:9])

numpyArray[:,8:9] = imputerobject.transform(numpyArray[:,8:9])
# object fit hota hai, transform dataset hota hai
newdata = pd.DataFrame(numpyArray)
file = open(str('C:\\Users\BHARAJ\PycharmProjects\ACMClasses\llon'), 'w')
file.write(newdata)
file.close()



imputerobject2 = Imputer(missing_values=0, strategy='median', axis = 0)
imputerobject2 = imputerobject2.fit(numpyArray[:,7:8])
import os
numpyArray[:,7:8] = imputerobject2.transform(numpyArray[:,7:8])
#object fit hota hai, transform dataset hota hai
newdata1 = pd.DataFrame(numpyArray)
print(newdata1)
'''
'''import pandas as pd
import numpy as np
import csv
import os
a = pd.read_csv('loan.csv')
#print(a.describe())
#print(a.head(10))
#print((a == 0).sum())
a.replace(0, np.NaN)
print(a)
a.fillna(a.mean(), inplace= True)
print(a[1:1:2])
'''
# ERROR
'''
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

dataset = pd.read_csv('loan.csv')

x = dataset.iloc[:,2]
le = LabelEncoder()
x[:,2] = le.fit_transform(x[:,2])'''
'''

from sklearn.preprocessing import OneHotEncoder, LabelEncoder, Imputer
import pandas as pd
import numpy as np
from numpy import array

data = pd.read_csv('data.csv')
x = data.values
#IMPUTER WALA PART
numpyArray = data.values
imputerobject = Imputer(missing_values='NaN',strategy='median',axis = 0)
imputerobject = imputerobject.fit(numpyArray[:,3])
x[:,3] = imputerobject.transform(x[:,3])


l = LabelEncoder()

x[:,3] = l.fit_transform(x[:,3])
x[:,0] = l.fit_transform(x[:,0]

o = OneHotEncoder(categorical_features=[0])
x = o.fit_transform(x).toarray()'''
#Make this shit work


# read Dummy variable trap why what when how

# solve a proble on kaggle , solve a problem on training , NaN ko solve karo, pehla column drop , use OHE.

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import random

pd.set_option('display.max_rows', 1000)
d = pd.read_csv('datta.csv')

#print(d.head())
#d_sex = pd.get_dummies(d.Sex).iloc[:,1:]
#d = pd.concat([d, d_sex], axis = 1)

desired_width=400

pd.set_option('display.width', desired_width)
pd.set_option('display.max_rows', 40)

pd.set_option('display.max_columns', 40)

d = pd.get_dummies(d, columns=['Sex', 'Embarked'], drop_first=True)
print(d)
sm = list(d['Age'])
sm[:] = [x - random.uniform(-0.121,0.121) for x in sm]

survive = list(d['Survived'])
survive[:] = [x - random.uniform(-0.121,0.121) for x in survive]

plt.scatter(sm, survive)
plt.show()

