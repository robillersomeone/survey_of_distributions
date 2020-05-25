import os, sys
sys.path.append(os.path.abspath('../.'))
import distributions as ds
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
# x range here
x_gamma_values= np.arange(0, 20, .05)[1:]
# start value for shape slider
k0 =2
# start value for slider frequency
# f0 = 3
theta0 = 2
# how big the amp slider goes to?
delta_f = 5.0

# initial pdf
distr = ds.int_gamma_distribution(x_gamma_values, k0, theta0)

# plot the pdf
l, = plt.plot(x_gamma_values, distr, lw=2)
ax.margins(x=0)

# slider bar
axcolor = 'lightgoldenrodyellow'
# param 1 size
axshape = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
# param 2 size
axscale = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

# param 1 slider bar
s_shape = Slider(axshape, 'shape', 0.1, 10.0, valinit=k0, dragging=True)
# param 2 slider bar
s_scale = Slider(axscale, 'scale', 0.1, 10.0, valinit=theta0, dragging=True)


def update(val):
    # update shape
    shape = s_shape.val
    # update scale
    scale = s_scale.val
    l.set_ydata(ds.int_gamma_distribution(x_gamma_values, shape, scale))
    fig.canvas.draw_idle()

# when param 1 slider bar changes call update with new value
s_shape.on_changed(update)
# when param 2 slider bar changes call update with new value
s_scale.on_changed(update)

# aesthetic
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    s_shape.reset()
    s_scale.reset()
button.on_clicked(reset)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)


def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()
radio.on_clicked(colorfunc)

plt.show()