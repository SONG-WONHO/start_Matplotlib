#load matplotlib.pyplot as plt
import matplotlib.pyplot as plt

#Simple graph
#plt.plot() makes simple graph

#Example_1
x = range(10,15)
y = range(10,15)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(x,y)

plt.show() ## Figure_1

#Example_2
y = range(10,15)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(y)

plt.show() ## Figure_2

#Example_3
x = range(1,6)
y = range(1,6)

fig, ax_list = plt.subplots(4, 4, figsize = (16,8))

ax_list[0][0].plot(x, y, color = 'r')
ax_list[0][1].plot(x, y, color = 'b')
ax_list[0][2].plot(x, y, color = 'g')
ax_list[0][3].plot(x, y, color = 'c')

ax_list[1][0].plot(x, y, linestyle = '-')
ax_list[1][1].plot(x, y, linestyle = '--')
ax_list[1][2].plot(x, y, linestyle = '-.')
ax_list[1][3].plot(x, y, linestyle = ':')

ax_list[2][0].plot(x, y, linewidth = 1)
ax_list[2][1].plot(x, y, linewidth = 2)
ax_list[2][2].plot(x, y, linewidth = 4)
ax_list[2][3].plot(x, y, linewidth = 8)

ax_list[3][0].plot(x, y, 'r-', linewidth = 1)
ax_list[3][1].plot(x, y, 'b--', linewidth = 2)
ax_list[3][2].plot(x, y, 'g-.', linewidth = 4)
ax_list[3][3].plot(x, y, 'c:', linewidth = 8)

plt.show() ## Figure_3

'''
color
    'b' : blue
    'g' : green
    'r' : red
    'c' : cyan
    'm' : magenta
    'y' : yellow
    'k' : black
    'w' : white

line styles or markers
    '-' : solid line
    '--' : dashed line
    '-.' : dash-dot line
    ':' : dotted line
    'o' : circle
    '^' : triangle up
    'v' : triangle down
    '<' : triangle left
    '>' : triangle right
    '+' : plus
    'x' : cross

'''
