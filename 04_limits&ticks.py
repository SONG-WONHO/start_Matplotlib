#load matplotlib.pyplot as plt
import matplotlib.pyplot as plt

#Let`s make trigonometric function

#To make trigonometric function, load numpy as np
import numpy as np

#x range: [-pi, pi]
x = np.linspace(-np.pi, np.pi, 256, endpoint = True)

#y = sin(x)
sin_y = np.sin(x)
#y = cos(x)
cos_y = np.cos(x)

fig, ax_list = plt.subplots(3, 1, figsize = (12,10))

#default sin & cos function
ax_list[0].plot(x, sin_y, 'r', linewidth = 2)
ax_list[0].plot(x, cos_y, 'b', linewidth = 2)

#set x,y limits
ax_list[1].plot(x, sin_y, 'r', linewidth = 2)
ax_list[1].plot(x, cos_y, 'b', linewidth = 2)

ax_list[1].set_xlim(-4,4)
ax_list[1].set_ylim(-2,2)

#set x,y ticks
ax_list[2].plot(x, sin_y, 'r', linewidth = 2)
ax_list[2].plot(x, cos_y, 'b', linewidth = 2)

ax_list[2].set_xticks(np.linspace(-np.pi, np.pi, 5, endpoint = True))
ax_list[2].set_yticks(np.linspace(-1, 1, 3, endpoint = True))

#no margin
plt.tight_layout()
plt.show() ## Figure_1
