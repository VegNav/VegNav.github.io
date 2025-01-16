import plotly.express as px
import pandas as pd

df = pd.read_csv("data.csv", sep = ";")

fig = px.scatter(df, x="Curricular units 1st sem (grade)", y="Curricular units 2nd sem (grade)", color="Target")

fig.update_layout(
    title = {
        "text": "Notas de ambos semestres, agrupadas por la decisión del alumno",
        "font": {"size": 20},
        "x": 0.5,
        "y": 0.95
        }

)
fig.write_html("graph2.html")
