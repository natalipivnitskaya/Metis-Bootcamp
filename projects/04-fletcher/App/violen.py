import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot

data = pd.read_csv('data/for_violen.csv', sep = ',', index_col = 0)

list_of_colleges = data['college'].unique().tolist()
list_of_colleges.sort()


def draw_violen(first, second):
    #fields = ['Accommodation', 'Job Prospects', 'Course and Lecturers', 'college']
    fields = fields = ['Clubs and Societies', 'Job Prospects', 'Student Support', 'college']
    vio = data[(data['college'] == first) | (data['college'] == second)][fields]
    
    x = vio['college']

    field0 = fields[0]
    trace0 = go.Box(
        y=vio[field0],
        x=x,
        name='Student Support',
        marker=dict(
            color= 'lightblue'
        )
    )
    field1 = fields[1]
    trace1 = go.Box(
        y= vio[field1],
        x=x,
        name='Job Prospects',
        marker=dict(
            color='darkgrey'
        )
    )
    field2 = fields[2]
    trace2 = go.Box(
        y=vio[field2],
        x=x,
        name='Social Life',
        marker=dict(
            color='cornflowerblue'
        )
    )

    plot_data = [trace0, trace1, trace2]
    layout = go.Layout(
        yaxis=dict(
            title='Rating',
            zeroline=False
        ),
        boxmode='group'
    )
    
    fig = go.Figure(data=plot_data, layout=layout)

    return plot(fig, filename='static/comparison.html', auto_open=False)
