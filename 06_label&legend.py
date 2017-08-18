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

fig, ax_list = plt.subplots(2,1,figsize = (12,8))

#label
ax_list[0].plot(x,sin_y, 'r')
ax_list[0].plot(x,cos_y, 'b')

ax_list[0].set_title('trigonometric function')
ax_list[0].set_xlabel('x')
ax_list[0].set_ylabel('y')

#legend
ax_list[1].plot(x,sin_y, 'r', label = 'sin')
ax_list[1].plot(x,cos_y, 'b', label = 'cos')

ax_list[1].legend(loc = 'best')

plt.tight_layout()
plt.show() ## Figure_1

'''
legend location options
    'best' = 0
    'upper right' = 1
    'upper left' = 2
    'lower right' = 3
    'lower left' = 4
    'right' = 5
    'center left' = 6
    'center right' = 7
    'lower center' = 8
    'upper center' = 9
    'center' = 10
'''
