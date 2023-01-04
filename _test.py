import plotly.offline as py
import plotly.graph_objs as go
from plotly.io import to_html

# Create a line chart
trace = go.Scatter(x=[1, 2, 3, 4], y=[10, 15, 13, 17])
data = [trace]
layout = go.Layout(title='Line Chart', 
                   template='plotly_dark',
                   annotations=[
                        dict(
                            templateitemname="draft watermark",
                            text="erfan.ai",
                        )
                    ]
                   
                   )
fig = go.Figure(data=data, layout=layout)

# Save the chart as an HTML file
py.plot(fig, filename='line-chart.html', auto_open=False)


plot_html = to_html(fig, full_html=False, div_id='tt-aa-id', include_plotlyjs=False)
print(plot_html)