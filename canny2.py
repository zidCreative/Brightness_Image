import streamlit as st
from PIL import Image, ImageEnhance

st.sidebar.image("zidCreative_putih.png")

st.title("Program Pengatur Kecerahan Gambar by zidCreative")
gamb = st.file_uploader("Upload gambar yang ingin anda konversi", type=['jpg' , 'jpeg', 'png' ])

if gamb is not None :
    fileg = Image.open(gamb)
    atur = st.slider("Atur tingkat kecerahan", 0.0, 5.0)
    col1, col2 = st.columns(2)
    col1.text("Gambar Asli")
    col1.image(fileg)
    
    enhancer = ImageEnhance.Brightness(fileg)
    bar = enhancer.enhance(atur)
    
    col2.text("Gambar Penyesuaian")
    col2.image(bar)
    
    if atur > 0.1:
        st.success("Selamat, kecerahan berhasil diatur. klil kanan pada gambar untuk menyimpan")