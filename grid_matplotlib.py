import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
fig = plt.figure()
gs = gridspec.GridSpec(3, 3)
ax1 = plt.subplot(gs[0, :],title='Plot1')
ax2 = plt.subplot(gs[1, :-1],title='Plot2')
ax3 = plt.subplot(gs[1:, -1],title='Plot3')
ax4 = plt.subplot(gs[-1, 0],title='Plot4')
ax5 = plt.subplot(gs[-1, -2],title='Plot5')
plt.show()

axes1 = plt.subplot(2, 2, (1,3), title='Plot1')
axes2 = plt.subplot(2, 2, 2, title='Plot2')
axes3 = plt.subplot(2, 2, 4, title='Plot3')
plt.show()

