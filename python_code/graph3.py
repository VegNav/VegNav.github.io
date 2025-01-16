import plotly.express as px
import pandas as pd

df = pd.read_csv("data.csv", sep = ";")

nation ={1:"Portuguese",
        2: "German",
        6: "Spanish",
        11: "Italian",
        13: "Dutch",
        14: "English",
        17: "Lithuanian",
        21: "Angolan",
        22: "Cape Verdean",
        24: "Guinean",
        25: "Mozambican",
        26: "Santomean",
        32: "Turkish",
        41: "Brazilian",
        62: "Romanian",
        100: "Moldova (Republic of)",
        101: "Mexican",
        103: "Ukrainian",
        105: "Russian",
        108: "Cuban",
        109: "Colombian"}

df["Nacionality"]=df.Nacionality.replace(nation)
df["Gender"]=df.Gender.replace({0:"Female", 1: "Male"})

fig = px.sunburst(df, path=["Gender", "Target", "Nacionality"], color="Target")

fig.update_layout(
    title = {
        "text": "Número de alumnos por nacionalidad según decidamos la raíz entre género y decisión",
        "font": {"size": 20},
        "x": 0.5,
        "y": 0.95
        })

fig.write_html("graph3.html")



