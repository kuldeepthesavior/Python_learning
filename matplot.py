import matplotlib.pyplot as plt
import math

# import math
# x=[10,2,52,6,8,9,20,26]
# y=[20,5,26,32,45,12,63,62]
# plt.plot(x,y,'r')
# plt.show()

# plt.plot([1,2,3,4,10])
# plt.show()


import numpy as np

#
# x=np.arange(1,100,10)
x=range(5)
# logs=math.log(x,10)
# print(logs)

#  method one


plt.plot(x,[x1 for x1 in x] , label='linear plot')
plt.plot(x,[x1*x1 for x1 in x], label='square plot')
plt.plot(x,[x1*x1*x1 for x1 in x], label='cube plot')


# method two

# plt.plot(x,[x1**2 for x1 in x] ,x , [x2*4 for x2 in x] , x,[x1 for x1 in x])
plt.grid(True)
# plt.axis([0,5,0,10])
# plt.xlim(-1,5)
# plt.ylim(-1,10)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Learning matplotlib')
plt.legend()
plt.savefig('photo.png')
plt.show()


#  histogram graph

print(np.random.rand(2,3,5))

y=np.random.rand(50,2)

plt.hist(y)
plt.show()


# bar chart

plt.bar([1,2,3,4],[10,20,30,40] )
plt.title('bar chart')
plt.show()


# plotting of dictionary using bar chart

dict={'a':10,'b':25,'c':57,'d':90}
print(enumerate(dict))

#  method  without showing the key od dictionary in plot
for i,key in enumerate(dict):
    print(i,"ky  ",key)
    plt.bar(i,dict[key])

plt.show()


# method that show ghe key in plot also

#  method  without showing the key od dictionary in plot
for i,key in enumerate(dict):
    # print(i,"ky  ",key)
    plt.bar(i,dict[key])
plt.xticks(np.arange(len(dict)),dict.keys())
plt.show()


#  pie chart
pie_element=[42,18,10]
pie_labels=['cars','bikes','buses']
plt.figure(figsize=(3,3))
plt.pie(pie_element,labels=pie_labels)
plt.title('pie chart of vehicles ')
plt.show()

# scatter plot

xaxis=np.random.randn(1000)
yaxis=np.random.randn(1000)
plt.scatter(xaxis,yaxis)
plt.title('scatter plot')
plt.show()


# stlying color

values=np.arange(1,20)
plt.plot(values,'y')
plt.plot(values+5,'r')
plt.plot(values+10,'m')
plt.show()

#  styling line in plot

val=np.arange(1,100)
# plt.plot(val,'--')
# plt.plot(val*2,'*')
# plt.plot(val*5,'-.')


plt.plot(val,'--',val*2,'-.',val*10,'+')
plt.title('styling the plot')
plt.show()


# marker styling plots

y1=np.arange(1,3,0.2)
plt.plot(y1,'*',y1+0.5,'o',y1+1,'D',y1+2,'^',y1+3,'s')
plt.title('marker styling')
plt.show()



# graph of logrthmic function


a=np.arange(0.1 ,1000000,0.1)

b=[]
for i in a:
    b.append(math.log(i,10))

plt.plot(a,b)
plt.xlabel('a axis')
plt.ylabel('b axis')
plt.title('logrthemic graph')
plt.xlim(-1,1000000)
plt.ylim(-1,6.1)
plt.show()

print(math.log(1))