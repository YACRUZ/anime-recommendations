import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

#Cache dataset
st.title('Anime recommendations')
DATA_URL = ('anime.csv')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data   

data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text('Done ! using cache...')


#Sidebar
sidebar = st.sidebar

sidebar.title("Yahir Jesus Jacome Cogco")
sidebar.write("zs20006732@estudiantes.uv.mx")
sidebar.image("ANIME.png")

#Mostrar todos
agree = sidebar.checkbox("Mostrar todos los animes")
if agree:
    st.header("Todos los animes")
    st.dataframe(data)

#Buscador
@st.cache_data
def load_data_byname(name):
    filtered_data_byname = data[data["Name"].str.contains(name, case=False)]
    return filtered_data_byname

myname = sidebar.text_input("Titulo del anime: ")
if(myname):
    filteredbyname = load_data_byname(myname)
    count_row = filteredbyname.shape[0]
    st.write(f"Total animes por titulo mostrados : {count_row}")


btfilm = sidebar.button('Buscar anime por nombre')
if(btfilm):
    st.dataframe(filteredbyname)

#Radio
selected_type = sidebar.radio("Selecciona tipo",
data['Type'].unique())
st.write("Tipo seleccionado: ", selected_type)
st.write(data.query(f"""Type==@selected_type"""))
st.markdown("___")

#Select
@st.cache_data
def load_data_byname(Studios):
    data = pd.read_csv(DATA_URL)
    data = load_data(1000)
    filtered_data_byname = data[data['Studios'] == Studios]

    return filtered_data_byname

selected_name =sidebar.selectbox('Seleccionar estudio ', data['Studios'].unique())
btndirector = sidebar.button('Buscar anime por estudio')

if(btndirector):
    filterbyname =load_data_byname(selected_name)
    count_row = filterbyname.shape[0]
    st.write(f"Total animes por estudio mostrados: {count_row}")

    st.dataframe(filterbyname)

#Multiselect
#Source = st.sidebar.multiselect("Selecciona origen",
#                                options=data['Source'].unique())

#df_selection=data.query("Source == @Source")
#st.write("Origen seleccionado", df_selection)

#Histograma
sidebar.title("Graficas:")
agree = sidebar.checkbox("Histograma")
if agree:
  fig, ax = plt.subplots()
  ax.hist(data['Score'])
  ax.set_ylabel("Cantidad")
  ax.set_xlabel("Nivel de score")
  st.header("Histograma del Score")
  st.write("Cantidad de animes que tiene cada nivel de Score")
  st.pyplot(fig)

st.markdown("___")

#Grafica de barras
#agree = sidebar.checkbox("Grafica de barras")
#if agree:
#   Type=data['Type']
#   Episodes=data['Episodes']
#   fig_barra=px.bar(data,
#                    x=Type,
#                    y=Episodes,
#                    orientation="v",
#                    title="Cantidad de capitulos que tiene cada tipo de anime",
#                    labels=dict(Episodes="Episodes", Type="Type"),
#                    color_discrete_sequence=["#7ECBB4"],
#                    template="plotly_white")
#   st.plotly_chart(fig_barra)

#Grafica de barras
if st.sidebar.checkbox('Grafica de barras popularidad'):

    fig, ax = plt.subplots()

    y_pos = data['Popularity']
    x_pos = data['Type']

    ax.bar(x_pos, y_pos,color = "red")
    ax.set_ylabel("Popularidad")
    ax.set_xlabel("Tipo de anime")
    ax.set_title('Grafica de barras popularidad')

    st.header("Grafica de barras popularidad")
    st.write("Nivel de popularidad que tiene cada tipo de anime")

    st.pyplot(fig)

st.markdown("___")

#Grafica scatter
if st.sidebar.checkbox('Grafica de scatter origen'):

    fig, ax = plt.subplots()

    x_pos = data['Type']
    y_pos = data['Source']


    ax.scatter(x_pos, y_pos,color = "blue")
    ax.set_ylabel("Origen")
    ax.set_xlabel("Tipo de anime")
    ax.set_title('Grafica de scatter origen')

    st.header("Grafica de scatter origen")
    st.write("Origen de cada tipo de anime")

    st.pyplot(fig)

st.markdown("___")

#grafica scatter
#st.header("Grafica Scatter")
#agree = sidebar.checkbox("Grafica scatter")
#if agree:
#    Type=data['Type']
#    Source=data['Source']
#    Episodes=data['Episodes']
#    fig_age=px.scatter(data,
#                   x=Type,
#                   y=Episodes,
#                   color=Source,
#                   title="Cantidad de episodios que tiene cada tipo de anime",
#                   labels=dict(Type="Type", Source="Source", Episodes="Episodes"),
#                   template="plotly_white")
#    st.plotly_chart(fig_age)