"""Module for creating charts to support analysis of fellowship data.
Created 6/25/2019  by Babila Lima"""

from data import dframe 
import pandas as pd
import  plotly.graph_objs as go


## TODO: style the chart use fmdview as guide
def total_spending_volume(dframe=dframe):
    """Function returns plotly chart figure object. Chart explores
    total spending & volume of city government fellows over time.
    
    Parameters
    ----------
    dframe:  Pandas Dataframe
           Dataframe on fellowship data from data.py module.
    
    Returns
    -------
    dict:  Returns Plotly chart figure object with keys: 'data' and 'layout'.
    
    Example
    -------
    >>> total_spending_volume()  # returns chart figure
    """ 
    
    trace1 = go.Bar(
        x = dframe.groupby(dframe.index)['fellow_cost'].sum().index,
        y = dframe.groupby(dframe.index)['fellow_cost'].sum().values,
        name = 'Spending'
    )
    trace2 = go.Scatter(
        x = dframe.groupby(dframe.index)['agency'].count().index,
        y = dframe.groupby(dframe.index)['agency'].count().values,
        name = 'Fellows',
        line = {'color':'darkgrey',
               'width':4,
               'dash':'dash'},
        yaxis = 'y2'
    )

    layout = {
        'legend':{'orientation':'h'},
        'title':'Something',
        'yaxis': {'title':'Fellowship Spending'},
        'yaxis2':{'title':'No. Fellows',
                 'titlefont':{'color':'darkgrey'},
                 'tickfont':{'color':'darkgrey'},
                 'overlaying':'y',
                 'side':'right'},
        'xaxis': {'tickmode':'auto',
                 'nticks': dframe.index.nunique()},
        'annotations':[
                {
                    'font':{'size':12,
                           'color':'darkgrey'},
                    'showarrow':False,
                    'text': 'Source: Data Provided by Baltimore Corps June 2019: https://github.com/brl1906/fellowship-analysis',
                    'xref':'paper',
                    'yref':'paper',
                    'x':.98,
                    'y':-.24}
            ]
    }

    fig = {'data':[trace1,trace2], 'layout':layout}
    return fig


## TODO: format colors
def usage_distribution_across_agencies(dframe=dframe):
    """Function returns plotly chart figure object. Chart explores
    the distribution of fellowship usage across agencies.
    
    Parameters
    ----------
    dframe:  Pandas Dataframe
           Dataframe on fellowship data from data.py module.
    
    Returns
    -------
    dict:  Returns Plotly chart figure object with keys: 'data' and 'layout'.
    
    Example
    -------
    >>> usage_distribution_across_agencies()  # returns chart figure
    """ 
    
    fig = {
        'data':[
            {
                'hole':.5,
                'labels': dframe.groupby('agency')['fellow_cost'].sum().index,
                'showlegend':False,
                'type':'pie',
                'domain':{'x': [0, .48]},
                'name':'total spending',
                'values':dframe.groupby('agency')['fellow_cost'].sum().values},
            {
                'hole':.5,
                'labels': dframe.groupby('funding')['fellow_cost'].sum().index,
                'showlegend':True,
                'type':'pie',
                'domain':{'x':[.52, 1]},
                'name':'funding sources',
                'values':dframe.groupby('funding')['fellow_cost'].sum().values}],

        'layout': {
        'title':'2014--2019 Fellowship Distribution<br>Utilization by Agency & Funding Type',
        'hovermode':'closest',
        'annotations': [
            {
                'font':{'size':12},
                'showarrow':False,
                'text':'{} Agencies<br>${:,.0f}'.format(dframe['agency'].nunique(),
                                                        dframe['fellow_cost'].sum()),
                'x':.197,
                'y':.5
            },
            {
                'font':{'size':12},
                'showarrow':False,
                'text':'<b>Placements</b>',
                'x':.10,
                'y':1.1
            },
            {
                'font':{'size':12},
                'showarrow':False,
                'text':'<b>Funding</b>',
                'x':.88,
                'y':1.1
            },
            {
                    'font':{'size':12,
                           'color':'darkgrey'},
                    'showarrow':False,
                    'text': 'Source: Data Provided by Baltimore Corps June 2019: https://github.com/brl1906/fellowship-analysis',
                    'x':.5,
                    'y':-.4}
                        ]}
    }

    return fig


def cost_components(dframe=dframe):
    """Function returns plotly chart figure object. Chart explores
    the fellowship cost components.
    
    Parameters
    ----------
    dframe:  Pandas Dataframe
           Dataframe on fellowship data from data.py module.
    
    Returns
    -------
    dict:  Returns Plotly chart figure object with keys: 'data' and 'layout'.
    
    Example
    -------
    >>> cost_components()  # returns chart figure
    """
    
    labels = ['stipend','fringe','unemployment','BaltCorps_fee','StrongCity_fee']
    values = []
    for label in labels:
        values.append(dframe[label].sum())

    text = []
    for label,value in zip(labels,values):
        text.append('{}<br>${:,.0f}'.format(label.capitalize(),value))

    fig = {
        'data':[
            {'labels': labels,
            'values': values,
             'name': 'cost components',
             'hole': .4,
             'type': 'pie',
             'text': text,
             'hoverinfo':'text+percent'
            }],
        'layout': {
            'hovermode': 'closest',
            'annotations': [
                {
                    'font':{'size':12},
                    'showarrow':False,
                    'text': '<b>Fellowship Cost Components</b>',
                    'x':.94,
                    'y':.9},
                {
                    'font':{'size':12},
                    'showarrow':False,
                    'text': '5yr Fees: ${:,.0f}'.format(dframe['BaltCorps_fee'].sum() + dframe['StrongCity_fee'].sum()),
                    'x':.94,
                    'y':.8},
                {
                    'font':{'size':12},
                    'showarrow':False,
                    'text': '5yr OPCs: ${:,.0f}'.format(dframe['fringe'].sum() + dframe['unemployment'].sum()),
                    'x':.94,
                    'y':.7},
                {
                    'font':{'size':12,
                           'color':'darkgrey'},
                    'showarrow':False,
                    'text': 'Source: Data Provided by Baltimore Corps June 2019:<br>https://github.com/brl1906/fellowship-analysis',
                    'x':.5,
                    'y':-.2},

            ]
        }
    }

    return fig


## TODO: set color scheme and style consistent with other charts, add hovertext as agency, fellows, spending
def utilization_changes_overtime_by_agency(dframe=dframe):
    """Function returns plotly chart figure object. Chart explores
    the changes in fellowship utilization and cost by agency overtime.
    
    Parameters
    ----------
    dframe:  Pandas Dataframe
           Dataframe on fellowship data from data.py module.
    
    Returns
    -------
    dict:  Returns Plotly chart figure object with keys: 'data' and 'layout'.
    
    Example
    -------
    >>> utilization_changes_overtime_by_agency()  # returns chart figure
    """
    
    traces = []

    for agncy in dframe['agency'].unique():
        traces.append(go.Bar(
            x = (dframe[dframe['agency'] == agncy].
                 groupby(dframe[dframe['agency'] == agncy].
                         index)['fellows_count'].mean().index),
            y = (dframe[dframe['agency'] == agncy].
                 groupby(dframe[dframe['agency'] == agncy].
                         index)['fellows_count'].mean().values),
            name = agncy,


        ))

    fig = {
        'data':traces,
        'layout': {
            'title': 'Fellowship Use & Cost Overtime: Agency Level',
            'hovermode':'closest',
            'barmode': 'stack',
            'xaxis':{'nticks':dframe.index.nunique()},
            'legend':{'orientation':'v'},
            'annotations':[
                {
                    'font':{'size':12,
                           'color':'darkgrey'},
                    'showarrow':False,
                    'text': 'Source: Data Provided by Baltimore Corps June 2019: https://github.com/brl1906/fellowship-analysis',
                    'xref':'paper',
                    'yref':'paper',
                    'x':.5,
                    'y':-.24}
            ]
        }}

    return fig


chart1 = total_spending_volume()
chart2 = usage_distribution_across_agencies()
chart3 = cost_components()
chart4 = utilization_changes_overtime_by_agency()