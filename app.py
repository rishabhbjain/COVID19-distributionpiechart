import plotly.express as px
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html

df = pd.read_csv("owid-covid-data.csv")
df.drop(['iso_code', 'new_cases', 'total_deaths', 'new_deaths', 'total_cases_per_million', 'new_cases_per_million', 'total_deaths_per_million', 'new_deaths_per_million', 'total_tests', 'new_tests', 'total_tests_per_thousand', 'new_tests_per_thousand', 'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'tests_units', 'stringency_index', 'population', 'population_density', 'median_age', 'aged_65_older', 'aged_70_older', 'gdp_per_capita', 'extreme_poverty', 'cvd_death_rate', 'diabetes_prevalence', 'female_smokers', 'male_smokers', 'handwashing_facilities', 'hospital_beds_per_100k'], axis=1, inplace=True)
df = df.loc[df['date'] == '2020-05-30']
df = df.loc[df['location'] != 'World']
df.drop(['date'], axis=1, inplace=True)
fig = px.pie(df, values='total_cases', names='location', title='Countrywise - Distribution of COVID - 19 (data - till 5/31/2020)')
fig.show()

app = dash.Dash()

server = app.server

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)