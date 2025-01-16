import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("data.csv", sep = ";")

course_dict = {
    33:"Biofuel Production Technologies",
    171: "Animation and Multimedia Design",
    8014: "Social Service",
    9003: "Agronomy",
    9070: "Communication Design",
    9085: "Veterinary Nursing",
    9119: "Informatics Engineering",
    9130: "Equinculture",
    9147: "Management",
    9238: "Social Service",
    9254: "Tourism",
    9500: "Nursing",
    9556: "Oral Hygiene",
    9670: "Advertising and Marketing Management",
    9773: "Journalism and Communication",
    9853: "Basic Education",
    9991: "Management" 
    }

# Pasamos de numéricas a categóricas
df["Course"]=df.Course.replace(course_dict)
df["Gender"]=df.Gender.replace({0:"Female", 1: "Male"})

# Dimensions
gender_dim = go.parcats.Dimension(values=df.Gender, label = "Gender")

course_dim = go.parcats.Dimension(values=df.Course, label = "Course")

outcome_dim = go.parcats.Dimension(values=df.Target, label="Outcome")

# Parcats trace

fig = go.Figure()

fig.add_trace(go.Parcats(dimensions=[gender_dim, course_dim, outcome_dim],
                         line={"color": df["Application order"],
                                "colorscale": "Viridis",
                                "showscale": True,
                                "colorbar": {"title": "Order"}},
                         hoveron="category",
                        hoverinfo="count+probability",
                        name="Application"))

fig.add_trace(go.Parcats(dimensions=[gender_dim, course_dim, outcome_dim],
                         visible = False,
                         line={"color": df["Age at enrollment"],
                               "colorscale":"Picnic",
                                "showscale": True,
                                "colorbar": {"title": "Age"}},
                         hoveron="category", hoverinfo="count+probability", name="Enrollment"))

fig.add_trace(go.Parcats(dimensions=[gender_dim, course_dim, outcome_dim],
                         visible = False,
                         line={"color": df["Previous qualification (grade)"],
                               "colorscale":"Jet",
                                "showscale": True,
                                "colorbar": {"title": "Qualification"}},
                         hoveron="category", hoverinfo="count+probability", name="Qualification"))



# Desplegable
fig.update_layout({"title" : {
                    "text": "Relaciones por orden de prioridad del curso",
                    "font": {"size": 20},
                    "x": 0.5,
                    "y": 0.95}})
fig.update_layout(
    updatemenus=[
        dict(
            buttons =[
                dict(label="Apllication Order",
                       method="update",
                       args=[{"visible": [True,False,False]},
                             {"title" : {
                                "text": "Relaciones por orden de prioridad del curso",
                                "font": {"size": 20},
                                "x": 0.5,
                                "y": 0.95}}]),
                dict(label="Age of enrollment",
                     method = "update",
                     args = [{"visible": [False, True, False]},
                             {"title" : {
                                "text": "Relaciones por edad a la que se matricularon",
                                "font": {"size": 20},
                                "x": 0.5,
                                "y": 0.95}}]),
                dict(label="Previous qualification",
                     method = "update",
                     args = [{"visible": [False, False, True]},
                             {"title" : {
                                "text": "Relaciones por la calificación de los estudios previos",
                                "font": {"size": 20},
                                "x": 0.5,
                                "y": 0.95}
                                            }]),
            ],
            direction = "down",
            showactive = True,
        )
    ]
)
fig.write_html("graph1.html")
