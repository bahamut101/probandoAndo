# pip install opencv-python

import streamlit as st
import pandas as pd 
import cv2
import time
import os


@st.dialog("Video")
def subeVideo(palabra):
    provincia = st.selectbox("Selecciona una provincia", provincias)

    # Crear una carpeta "videos" si no existe
    os.makedirs("videos", exist_ok=True)

    st.title("Sube un video y guárdalo en el disco")

    # Usar el file uploader para que el usuario seleccione un archivo
    uploaded_file = st.file_uploader("Elige un archivo de video", type=["mp4", "avi", "mov", "mkv"])

    # Si el usuario sube un archivo
    if uploaded_file is not None:
        # Guardar el archivo en el disco
        file_path = os.path.join("videos", uploaded_file.name)
        
        # Escribir el contenido del archivo subido en el disco
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"El video ha sido guardado en: {file_path}")
        st.video(file_path)  # Mostrar el video en la app Streamlit


def grabaVideo(palabra):
    provincia = st.selectbox("Selecciona una provincia", provincias)

    # Crear la carpeta "videos" si no existe
    os.makedirs("videos", exist_ok=True)

    # Configura la cámara
    cap = cv2.VideoCapture(0)

    # Configura el códec para MP4 (usando H264)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' es para MP4 comprimido
    output_file = f"videos/{palabra}.mp4"  # Ruta personalizada

    # Crear el objeto VideoWriter
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

    st.subheader("Graba un video corto (5 segundos) de la palabra")

    # Graba el video por 5 segundos
    start_time = time.time()
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Muestra el video en Streamlit
        st.image(frame, channels="BGR", use_column_width=True)

        # Escribe el frame en el archivo de salida
        out.write(frame)

        # Detener después de 5 segundos
        if time.time() - start_time > 5:
            break

    # Liberar los recursos
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    st.success(f"Video grabado con éxito 🥳")



UA="Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
url="https://dle.rae.es/{}?m=31"
url_video = "https://fundacioncnse-dilse.org/bddilse/images/stories/"


st.set_page_config(page_title="Diccionario de signos por povincias", page_icon=":hand:") 
st.title("Diccionario de signos por provincias")
 
letras = ['a', 'á', 'b', 'c', 'd', 'e', 'é', 'f', 'g', 'h', 'i', 'í', 'j', 'k', 'l', 'm',
             'n', 'ñ', 'o', 'ó', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'ü', 'v', 'w', 'x', 'y', 'z']

provincias=['Álava','Albacete','Alicante','Almería','Asturias','Ávila','Badajoz','Barcelona','Burgos','Cáceres','Cádiz','Cantabria','Castellón','Ciudad Real','Córdoba','Cuenca','Gerona','Granada','Guadalajara','Guipúzcoa','Huelva','Huesca','Islas Baleares','Jaén','La Coruña','La Rioja','Las Palmas','León','Lérida','Lugo','Madrid','Málaga','Murcia','Navarra','Orense','Palencia','Pontevedra','Salamanca','Segovia','Sevilla','Soria','Tarragona','Santa Cruz de Tenerife','Teruel','Toledo','Valencia','Valladolid','Vizcaya','Zamora','Zaragoza','Ceuta','Melilla']

df = pd.read_csv('palabras.csv', encoding='ISO-8859-1') 

palabra = st.text_input("Introduce una palabra")
palabra = palabra.lower()

col1,col2 = st.columns(2)

if palabra != "":
    col1.video(f"https://fundacioncnse-dilse.org/bddilse/images/stories/{palabra}.mov")
    if st.button("Añadir variante"):
        #grabaVideo(palabra)
        subeVideo(palabra)
    
else:
    st.warning("Introduce una palabra")