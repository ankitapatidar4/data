#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px


# In[2]:


# Uses an External Stylesheet
# Use a css file from your GitHub Pages site 
external_stylesheets = ['https://ankitapatidar4.github.io/pythondash.github.io/new.css']


# In[3]:


# Creates the app to instantiate the content for the Dashboard and use the external_stylesheets
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# In[4]:


# Use a csv dataset from a repository in your GitHub account. Use the Raw URL to expose the data to the Python dataframe
df = pd.read_csv('https://raw.githubusercontent.com/ankitapatidar4/data/master/Placement_Data_Full_Class.csv')


# In[5]:


# Custom function used to generate a data table from a dataframe
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


# In[ ]:


# Add content to the app layout
# Begin all content DIV
app.layout=html.Div([
    # Add your HTML tags to the content - notice a comma is added between HTML elements
    html.H1('Placement Record of a Class'),
    html.Div([
        html.P('The data below provides an insight about the placement record of a class having 216 students.'),
    ]),
    # Begin of DIV surrounding both Tables
    html.Div([
    # Begin of First Table
    html.Table(style={'width':'100%'},
               # Begin of Table children
               children=[
                   #######################################################################
                   # Begin of First Tr
                 html.Tr(
                     #Begin Tr children
                     children=[
                         # Begin Th
                         
                         html.Th(style={'width':'60%'},
                             # Begin Th children
                             children=[
                                 html.H3('Number of students placed and not placed by gender')
                             # End of Th children   
                             ]
                         
                         # End of Th - Notice a comma is placed here to separate the next Th
                         ),
                         # Begin of Th
                         html.Th(style={'width':'70%'},
                             # Begin of Th children
                             children=[
#                                  html.H3('Global GDP for Fruits and Veggies')
                             # End of Th children    
                             ]
                         
                         # End of Th
                         )
                         
                     # End of Tr children    
                     ]
                 # End of First Tr - Notice a comma is placed here to separate the next Tr
                 ),
                 #########################################################################
                 # Begin of Second Tr
                 html.Tr(
                     #Begin Tr children
                     children=[
                         # Begin Td
                         html.Td(
                             # Begin Td children
                             children=[
                                    # Display bar graph
                                    dcc.Graph(
                                    id='example-graph',
                                    figure={
                                        'data': [
                                            {'x': ["M","F"], 'y': [101,48], 'type': 'bar', 'name': 'Placed'},
                                            {'x': ["M","F"], 'y': [40,29], 'type': 'bar', 'name': 'Not Placed'},
                                        ],
                                        'layout': {
                                            'title': 'Male Female ratio for placed and not placed'
                                        }
                                    }
                                # End of Chart 1
                                )
                        
                              # End of Td children   
                             ]
                         
                         # End of Td - Notice a comma is placed here to separate the next Th
                         ),
                         html.Th(style={'width':'70%'},
                             # Begin of Th children
                             children=[        
                                    html.H3('Top 10 records of students with their academic details')
                                                               
                             # End of Th children    
                             ]
                         # End of Th
                         ),
                         html.Td(
                             # Begin of Td children
                             children=[
                                    # Execute custom generate_table function and display data
                                    # Use data from dataframe df2
                                    generate_table(df)
                             # End of Td children    
                             ]
                         # End of Td
                         )
                     ]
                 )
                   ]),
               
# End of all content DIV
])
    ])

# Run the app on the web server
if __name__ == '__main__':
    # Set debug to False. Some configurations are not setup for Debug
    app.run_server(debug=False)

