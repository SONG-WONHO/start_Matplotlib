#load matplotlib.pyplot as plt
import matplotlib.pyplot as plt

#To make trigonometric function, load numpy as np
import numpy as np

#x range: [-pi, pi]
x = np.linspace(-np.pi, np.pi, 256, endpoint = True)

#y = sin(x)
sin_y = np.sin(x)
#y = cos(x)
cos_y = np.cos(x)

fig, ax_list = plt.subplots(3, 4, figsize = (12,8))

for i in range(3):
    for j in range(4):
        ax_list[i][j].plot(x, sin_y, 'r')
        ax_list[i][j].plot(x, cos_y, 'b')

#set spine color
ax_list[0][0].spines['bottom'].set_color('none')
ax_list[0][1].spines['right'].set_color('none')
ax_list[0][2].spines['top'].set_color('none')
ax_list[0][3].spines['left'].set_color('none')

#set spine position
ax_list[1][0].spines['bottom'].set_position(('data',0))
ax_list[1][1].spines['right'].set_position(('data',0))
ax_list[1][2].spines['top'].set_position(('data',0))
ax_list[1][3].spines['left'].set_position(('data',0))

#set tick position
ax_list[2][0].xaxis.set_ticks_position('bottom')
ax_list[2][1].xaxis.set_ticks_position('top')
ax_list[2][2].yaxis.set_ticks_position('left')
ax_list[2][3].yaxis.set_ticks_position('right')

plt.tight_layout()
plt.show() # Figure_1

#Example_1
fig = plt.figure(figsize = (10,6))
ax = fig.add_subplot(1,1,1)

ax.plot(x, sin_y, 'r')
ax.plot(x, cos_y, 'b')

ax.set_xlim(-4,4)
ax.set_ylim(-1.5,1.5)

ax.set_xticks(np.linspace(x.min(), x.max(), 5, endpoint = True))
ax.set_yticks(np.linspace(-1, 1, 3, endpoint = True))

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))

plt.tight_layout()
plt.show() # Figure_2
