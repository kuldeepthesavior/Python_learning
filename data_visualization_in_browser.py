from bokeh.plotting import output_file,show,figure

import pandas
dataset=pandas.DataFrame(columns=['x','y'])
dataset['x']=[1,2,3,4,5,6,7]
dataset['y']=[1,4,9,16,25,36,49]

p=figure(plot_width=500,plot_height=400)

p.circle(dataset['x'],dataset['y'],size=5)

output_file('data_visualization_plot.html')
show(p)


