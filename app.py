import math
import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import altair as alt
import io
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os



st.title("FFR Chart Template")
df = pd.read_csv('datas.csv')
df = df.replace(to_replace=r'\N', value='0')
df=df.replace('00:00:00.000','',regex=True)
df2=df
dfc = pd.read_csv('datasc.csv')
dfc = dfc.replace(to_replace=r'\N', value='0')
dfc=dfc.replace('00:00:00.000','',regex=True)
dfc2=dfc
dfr = pd.read_csv('datasr.csv')
dfr = dfr.replace(to_replace=r'\N', value='0')
dfr=dfr.replace('00:00:00.000','',regex=True)
dfr2=dfr
with st.container():
    col_x, col_y = st.columns(2)
    with col_x:
        nivel = st.selectbox("Level_1",['Region','City Portfolio','City'])
#################################################################################################################################

        if str(nivel) == 'City Portfolio':
            pais = st.selectbox("City_Portfolio_1", sorted(df['city_name'].unique()))
            data_filtrada = df[df['city_name'] == pais]

            fecha = st.selectbox("Month_1", sorted(data_filtrada['month'].unique(),reverse=True))
            data_filtrada = data_filtrada[data_filtrada['month'] == fecha]
            # Fixing random state for reproducibility
            plt.rcdefaults()
            fig, ax = plt.subplots()
            # Example data
            df= data_filtrada
            people= df.columns.values[3:24]
            y_pos = np.arange(len(people))
            aux=df.values[0][3:24]
            suma = 0
            for j in range(len(aux)):
                suma= suma + np.int(aux[j])
            for i in range(len(aux)):
                aux[i] = round(np.int(aux[i])/suma*100,2)
            performance = (aux)
            ax.barh(y_pos, performance, align='center',color="red")
            ax.set_yticks(y_pos)
            ax.set_yticklabels(people)
            ax.invert_yaxis()  # labels read top-to-bottom
            ax.set_xlabel('Sessions')
            dx = performance.max() / 200
            for i, (value, name) in enumerate(zip(performance,people)):
                   ax.text(value+dx, i, str(value) + "%",  size=10, ha='left',  va='center')
            plt.box(False)
            st.pyplot(plt)
#################################################################################################################################

        elif str(nivel) == 'City':
            pais = st.selectbox("City_1", sorted(dfc['city_name'].unique()))
            data_filtrada = dfc[dfc['city_name'] == pais]

            fecha = st.selectbox("MONTH_1", sorted(data_filtrada['month'].unique(),reverse=True))
            data_filtrada = data_filtrada[data_filtrada['month'] == fecha]
            # Fixing random state for reproducibility
            plt.rcdefaults()
            fig, ax = plt.subplots()
            # Example data
            df= data_filtrada
            people= df.columns.values[3:24]
            y_pos = np.arange(len(people))
            aux=df.values[0][3:24]
            suma = 0
            for j in range(len(aux)):
                suma= suma + np.int(aux[j])
            for i in range(len(aux)):
                aux[i] = round(np.int(aux[i])/suma*100,2)
            performance = (aux)
            ax.barh(y_pos, performance, align='center',color="red")
            ax.set_yticks(y_pos)
            ax.set_yticklabels(people)
            ax.invert_yaxis()  # labels read top-to-bottom
            ax.set_xlabel('Sessions')
            dx = performance.max() / 200
            for i, (value, name) in enumerate(zip(performance,people)):
                   ax.text(value+dx, i, str(value) + "%",  size=10, ha='left',  va='center')
            plt.box(False)
            st.pyplot(plt)
#################################################################################################################################

        else:

            fecha = st.selectbox("Month_1", sorted(dfr['month'].unique(),reverse=True))
            data_filtrada = dfr[dfr['month'] == fecha]
            # Fixing random state for reproducibility
            plt.rcdefaults()
            fig, ax = plt.subplots()
            # Example data
            df= data_filtrada
            people= df.columns.values[3:24]
            y_pos = np.arange(len(people))
            aux=df.values[0][3:24]
            suma=0
            for j in range(len(aux)):
                suma= suma + np.int(aux[j])
            for i in range(len(aux)):
                aux[i] = round(np.int(aux[i])/suma*100,2)
            performance = (aux)
            ax.barh(y_pos, performance, align='center',color="red")
            ax.set_yticks(y_pos)
            ax.set_yticklabels(people)
            ax.invert_yaxis()  # labels read top-to-bottom
            ax.set_xlabel('Sessions')
            dx = performance.max() / 200
            for i, (value, name) in enumerate(zip(performance,people)):
                   ax.text(value+dx, i, str(value) + "%",  size=10, ha='left',  va='center')
            plt.box(False)
            st.pyplot(plt)
#################################################################################################################################


    with col_y:
        nivel = st.selectbox("Level_2",['Region','City Portfolio','City'])
#################################################################################################################################

        if str(nivel) == 'City Portfolio':
            pais = st.selectbox("City_Portfolio_2", sorted(df2['city_name'].unique()))
            data_filtrada = df2[df2['city_name'] == pais]

            fecha = st.selectbox("MONTH_2", sorted(data_filtrada['month'].unique(),reverse=True))
            data_filtrada = data_filtrada[data_filtrada['month'] == fecha]
            # Fixing random state for reproducibility
            plt.rcdefaults()
            fig, ax = plt.subplots()
            # Example data
            df= data_filtrada
            people= df.columns.values[3:24]
            y_pos = np.arange(len(people))
            aux=df.values[0][3:24]
            suma = 0
            for j in range(len(aux)):
                suma= suma + np.int(aux[j])
            for i in range(len(aux)):
                aux[i] = round(np.int(aux[i])/suma*100,2)
            performance = (aux)
            ax.barh(y_pos, performance, align='center',color="red")
            ax.set_yticks(y_pos)
            ax.set_yticklabels(people)
            ax.invert_yaxis()  # labels read top-to-bottom
            ax.set_xlabel('Sessions')
            dx = performance.max() / 200
            for i, (value, name) in enumerate(zip(performance,people)):
                   ax.text(value+dx, i, str(value) + "%",  size=10, ha='left',  va='center')
            plt.box(False)
            st.pyplot(plt)
#################################################################################################################################

        elif str(nivel) == 'City':
            pais = st.selectbox("City_2", sorted(dfc2['city_name'].unique()))
            data_filtrada = dfc2[dfc2['city_name'] == pais]

            fecha = st.selectbox("Month_2", sorted(data_filtrada['month'].unique(),reverse=True))
            data_filtrada = data_filtrada[data_filtrada['month'] == fecha]
            # Fixing random state for reproducibility
            plt.rcdefaults()
            fig, ax = plt.subplots()
            # Example data
            df= data_filtrada
            people= df.columns.values[3:24]
            y_pos = np.arange(len(people))
            aux=df.values[0][3:24]
            suma = 0
            for j in range(len(aux)):
                suma= suma + np.int(aux[j])
            for i in range(len(aux)):
                aux[i] = round(np.int(aux[i])/suma*100,2)
            performance = (aux)
            ax.barh(y_pos, performance, align='center',color="red")
            ax.set_yticks(y_pos)
            ax.set_yticklabels(people)
            ax.invert_yaxis()  # labels read top-to-bottom
            ax.set_xlabel('Sessions')
            dx = performance.max() / 200
            for i, (value, name) in enumerate(zip(performance,people)):
                   ax.text(value+dx, i, str(value) + "%",  size=10, ha='left',  va='center')
            plt.box(False)
            st.pyplot(plt)
#################################################################################################################################

        else:

            fecha = st.selectbox("Month_2", sorted(dfr2['month'].unique(),reverse=True))
            data_filtrada = dfr2[dfr2['month'] == fecha]
            # Fixing random state for reproducibility
            plt.rcdefaults()
            fig, ax = plt.subplots()
            # Example data
            df= data_filtrada
            people= df.columns.values[3:24]
            y_pos = np.arange(len(people))
            aux=df.values[0][3:24]
            suma=0
            for j in range(len(aux)):
                suma= suma + np.int(aux[j])
            for i in range(len(aux)):
                aux[i] = round(np.int(aux[i])/suma*100,2)
            performance = (aux)
            ax.barh(y_pos, performance, align='center',color="red")
            ax.set_yticks(y_pos)
            ax.set_yticklabels(people)
            ax.invert_yaxis()  # labels read top-to-bottom
            ax.set_xlabel('Sessions')
            dx = performance.max() / 200
            for i, (value, name) in enumerate(zip(performance,people)):
                   ax.text(value+dx, i, str(value) + "%",  size=10, ha='left',  va='center')
            plt.box(False)
            st.pyplot(plt)
