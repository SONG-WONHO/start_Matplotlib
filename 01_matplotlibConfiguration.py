#load matplotlib.pyplot as plt
import matplotlib.pyplot as plt

#Configuration
#Figure ==> Axes(Subplot) ==> Xaxis, Yaxis

#Figure
fig = plt.figure()
print(type(fig)) ## <class 'matplotlib.figure.Figure'>

#Axes(Subplot)
ax = fig.add_subplot(1,1,1)
print(type(ax)) ## <class 'matplotlib.axes._subplots.AxesSubplot'>

#Xaxis, Yaxis
print(type(ax.xaxis)) ## <class 'matplotlib.axis.XAxis'>
print(type(ax.yaxis)) ## <class 'matplotlib.axis.YAxis'>

plt.show() ## Figure_1

#Example_1
fig = plt.figure()

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

plt.show() ## Figure_2

#Eample_2
fig = plt.figure()

ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

plt.show() ## Figure_3

#Example_3
fig = plt.figure()

ax1 = fig.add_subplot(3,3,1)
ax2 = fig.add_subplot(3,3,2)
ax3 = fig.add_subplot(3,3,3)
ax4 = fig.add_subplot(3,3,4)
ax5 = fig.add_subplot(3,3,5)
ax6 = fig.add_subplot(3,3,6)
ax7 = fig.add_subplot(3,3,7)
ax8 = fig.add_subplot(3,3,8)
ax9 = fig.add_subplot(3,3,9)

plt.show() ## Figure_4

#Same
fig, ax_list = plt.subplots(3,3)

plt.show() ## Figure_5

print(type(fig)) ## <class 'matplotlib.figure.Figure'>
print(type(ax_list)) ## <class 'numpy.ndarray'>
print(type(ax_list[0][0])) ## <class 'matplotlib.axes._subplots.AxesSubplot'>
print(type(ax_list[0][1])) ## <class 'matplotlib.axes._subplots.AxesSubplot'>
print(type(ax_list[0][2])) ## <class 'matplotlib.axes._subplots.AxesSubplot'>
print(type(ax_list[1][0])) ## <class 'matplotlib.axes._subplots.AxesSubplot'>
print(type(ax_list[1][1])) ## <class 'matplotlib.axes._subplots.AxesSubplot'>
print(type(ax_list[1][2])) ## <class 'matplotlib.axes._subplots.AxesSubplot'>
print(type(ax_list[2][0])) ## <class 'matplotlib.axes._subplots.AxesSubplot'>
print(type(ax_list[2][1])) ## <class 'matplotlib.axes._subplots.AxesSubplot'>
print(type(ax_list[2][2])) ## <class 'matplotlib.axes._subplots.AxesSubplot'>
