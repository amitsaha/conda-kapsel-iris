import os
import pandas as pd
from bokeh.plotting import Figure
from bokeh.io import curdoc

iris_csv = os.getenv("IRIS_CSV")

flowers = pd.read_csv(iris_csv)

colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
colors = [colormap[x] for x in flowers['species']]

p = Figure(title = "Iris Morphology")
p.xaxis.axis_label = 'Petal Length'
p.yaxis.axis_label = 'Petal Width'

p.circle(flowers["petal_length"], flowers["petal_width"],color=colors, fill_alpha=0.2, size=10)

curdoc().title = "Iris Example"
curdoc().add_root(p)
