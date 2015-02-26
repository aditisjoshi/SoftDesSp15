# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: {{BASE_URL}}/python/getting-started
# Find your api_key here: {{BASE_URL}}/settings/api

import plotly.plotly as py
from plotly.graph_objs import *

from text_mining import *

men_sentiment, women_sentiment, men_word_count, women_word_count = comment_analysis(500,['mean','boring','evil','difficult','hard','nice','friendly','smart','fun','funny','rude','ugly'])

trace1 = Bar(
    x=list(men_word_count.viewkeys()),
    y=list(men_word_count.viewvalues()),
    name='Men',
    error_y=ErrorY(
        color='rgb(0, 67, 88)',
        thickness=1,
        width=1
    ),
    error_x=ErrorX(
        copy_ystyle=True
    ),
    marker=Marker(
        color='#1f77b4',
        line=Line(
            color='#444',
            width=0
        )
    ),
    opacity=1,
    visible=True
)

trace2 = Bar(
    x=list(women_word_count.viewkeys()),
    y=list(women_word_count.viewvalues()),
    name='Women',
    error_y=ErrorY(
        color='rgb(31, 138, 112)',
        thickness=1,
        width=1
    ),
    error_x=ErrorX(
        copy_ystyle=True
    ),
    marker=Marker(
        color='rgb(214, 39, 40)',
        line=Line(
            color='#444',
            width=0
        )
    ),
    opacity=1
)
data = Data([trace1, trace2])
layout = Layout(
    title='Adjectives Used to Describe Professors on ratemyprofessor.com',
    titlefont=Font(
        family='"Open sans", verdana, arial, sans-serif',
        size=17,
        color='#444'
    ),
    font=Font(
        family='"Open sans", verdana, arial, sans-serif',
        size=12,
        color='#444'
    ),
    showlegend=True,
    autosize=True,
    width=1022,
    height=617,
    xaxis=XAxis(
        title='Adjective',
        titlefont=Font(
            family='"Open sans", verdana, arial, sans-serif',
            size=14,
            color='#444'
        ),
        range=[-0.5, 11.5],
        type='category',
        rangemode='normal',
        autorange=True,
        showgrid=False,
        zeroline=False,
        showline=False,
        autotick=True,
        nticks=0,
        ticks='',
        showticklabels=True,
        tick0=0,
        dtick=1,
        ticklen=6,
        tickcolor='rgba(0, 0, 0, 0)',
        tickangle='auto',
        tickfont=Font(
            family='"Open sans", verdana, arial, sans-serif',
            size=12,
            color='#444'
        ),
        exponentformat='B',
        showexponent='all',
        mirror='allticks',
        gridcolor='white',
        gridwidth=1,
        zerolinewidth=1,
        linecolor='rgb(34,34,34)',
        linewidth=1
    ),
    yaxis=YAxis(
        title='Frequency of Use',
        titlefont=Font(
            family='"Open sans", verdana, arial, sans-serif',
            size=14,
            color='#444'
        ),
        range=[0, 24.210526315789473],
        type='linear',
        rangemode='normal',
        autorange=True,
        showgrid=True,
        zeroline=True,
        showline=False,
        autotick=True,
        nticks=0,
        ticks='',
        showticklabels=True,
        tick0=0,
        dtick=1,
        ticklen=6,
        tickcolor='rgba(0, 0, 0, 0)',
        tickangle='auto',
        tickfont=Font(
            family='"Open sans", verdana, arial, sans-serif',
            size=12,
            color='#444'
        ),
        exponentformat='B',
        showexponent='all',
        mirror='allticks',
        gridcolor='#eee',
        gridwidth=1,
        zerolinecolor='#444',
        zerolinewidth=1,
        linecolor='rgb(34,34,34)',
        linewidth=1
    ),
    legend=Legend(
        x=1.02,
        y=1,
        traceorder='normal',
        font=Font(
            family='"Open sans", verdana, arial, sans-serif',
            size=12,
            color='#444'
        ),
        bgcolor='#fff',
        bordercolor='#444',
        borderwidth=0,
        xref='paper',
        yref='paper'
    ),
    paper_bgcolor='#fff',
    plot_bgcolor='#fff',
    hovermode='x',
    dragmode='zoom',
    separators='.,',
    bargap=0.2,
    bargroupgap=0,
    hidesources=False
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)