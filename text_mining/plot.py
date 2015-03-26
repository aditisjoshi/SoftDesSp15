# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: {{BASE_URL}}/python/getting-started
# Find your api_key here: {{BASE_URL}}/settings/api

import plotly.plotly as py
from plotly.graph_objs import *

from text_mining import *
#Using import * is generally not considered great style because it is not explicit what you are going to use. So I have no idea that comment_analysis comes from the text_mining module unless I've read through the text_mining module. Best to do from text_mining import comment_analysis, blah, etc.

men_sentiment, women_sentiment, men_word_count, women_word_count = comment_analysis(5000,['mean','boring', 'difficult','hard','nice','friendly','smart','fun','funny','rude','easy', 'strict', 'suppostive', 'unfair'])


#the following unpacks the sentiment dictionaries to get the average positivity rating and subjectivity rating for both men and women
men_sentiment_values_list = list(men_sentiment.viewvalues())
men_sentiment_values_dict = dict(men_sentiment_values_list)
men_sentiment_values = list(men_sentiment_values_dict.viewkeys())
men_subj_rating = list(men_sentiment_values_dict.viewvalues())
avg_men_sent = sum(men_sentiment_values)/len(men_sentiment_values)
avg_men_subj = sum(men_subj_rating)/len(men_subj_rating)

women_sentiment_values_list = list(women_sentiment.viewvalues())
women_sentiment_values_dict = dict(women_sentiment_values_list)
women_sentiment_values = list(women_sentiment_values_dict.viewkeys())
women_subj_rating = list(women_sentiment_values_dict.viewvalues())
avg_women_sent = sum(women_sentiment_values)/len(women_sentiment_values)
avg_women_subj = sum(women_subj_rating)/len(women_subj_rating)
#you're doing a lot of repetition here. Probably best to make a function!

print avg_women_subj, avg_women_sent, len(women_sentiment), avg_men_subj, avg_men_sent, len(men_sentiment)


#the next few lines normalize the data so that the graph shows the instances of usage not subjected by number of men/women
men_values = list(men_word_count.viewvalues())
print men_values, len(men_sentiment)
for i in range(0,len(men_values)):
    men_values[i] = men_values[i] / float(len(men_sentiment))

women_values = list(women_word_count.viewvalues())
print women_values, len(women_sentiment)
for i in range(0,len(women_values)):
    women_values[i] = women_values[i] / float(len(women_sentiment))
#kind of writing out the same chunk of code twice again, whenever you find yourself doing this you should write a function instead!


#I'd recommend separating out a lot of this formatting stuff into a separate python file called formatting.py or something that you can import this from and parameterize/fill in with values. It'd make this a lot cleaner and make the flow of logic visible and easier to follow.
trace1 = Bar(
    x=list(men_word_count.viewkeys()),
    y=men_values,
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
    y=women_values,
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
        title='Frequency of Use (normalized)',
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
