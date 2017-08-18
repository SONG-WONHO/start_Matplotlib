#load matplotlib.pyplot as plt
import matplotlib.pyplot as plt

#All subplots have same size
fig, ax_list = plt.subplots(2,2,figsize = (10,10))
plt.show() ## Figure_1

#So, how we can have different size?
#Subplot to grid !
fig = plt.figure(figsize = (10,10))

#(4,4) 크기의 격자 중 (0,0)부터 행 1개, 열 4개
ax1 = plt.subplot2grid((4,4), (0,0), rowspan = 1, colspan = 4)

#(4,4) 크기의 격자 중 (1,0)부터 행 3개, 열 3개
ax2 = plt.subplot2grid((4,4), (1,0), rowspan = 3, colspan = 3)

#(4,4) 크기의 격자 중 (1,3)부터 행 3개, 열 1개
ax3 = plt.subplot2grid((4,4), (1,3), rowspan = 3, colspan = 1)

plt.show() ## Figure_2
