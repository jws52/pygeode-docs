import pylab as pyl
import pygeode as pyg, numpy as np
#import matplotlib as mpl
#import matplotlib.pyplot as plt

from pygeode.tutorial import t1

#fig,mplax = plt.subplots(1,2)

pyl.ion()
ax1 = pyg.plot.AxesWrapper()

pyg.showvar(t1.Temp, axes=ax1)

# This resizes the figure that will be rendered, including axes positioning
#ax1.size=(3,3)

#pyl.ion()

# Why is this not showing the colorbar in the output window?
ax1.render(1)

#ax.render(fig=fig)

# Now you can modify matplotlib figure instance, e.g.:
#fig.set_size_inches(2,2)
