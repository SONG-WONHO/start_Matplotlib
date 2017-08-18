#load matplotlib.pyplot as plt
import matplotlib.pyplot as plt

#load numpy as np
import numpy as np

#x range: [-pi, pi]
x = np.linspace(-np.pi, np.pi, 256, endpoint = True)

#y = sin(x)
y_sin = np.sin(x)
#y = cos(x)
y_cos = np.cos(x)

#Figure & subplot
fig = plt.figure(figsize = (12,8))
ax = fig.add_subplot(1,1,1)

#Graph
ax.plot(x, y_sin, 'r', linewidth = 2.0, label = 'sin')
ax.plot(x, y_cos, 'b', linewidth = 2.0, label = 'cos')

#Set limits
ax.set_xlim(-4,4)
ax.set_ylim(-1.5,1.5)

#Set ticks
ax.set_xticks(np.linspace(-np.pi, np.pi, 5, endpoint = True))
ax.set_yticks(np.linspace(-1.5, 1.5, 5, endpoint = True))

#Set spines
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

#Set labels
ax.set_title('trigonometric function')
ax.set_xlabel('X')
ax.set_ylabel('Y')

#Set legend
ax.legend(loc = 'best')

#no margin
plt.tight_layout()
plt.show() ## Figure_1
