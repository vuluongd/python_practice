import plotly.express as px
import plotly.io as pio

pio.renderers.default = 'browser'

country = input("Enter the country name: ")
data = {
    'country':[country],
    'values':[100]
}
fig = px.choropleth (
    data,
    locations='country',
    locationmode='country names',
    color = 'values',
    color_continuous_scale='Inferno',
    title=f'Country map highlighting {country}'
)

fig.show()