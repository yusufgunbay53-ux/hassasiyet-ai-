import streamlit as st
import google.generativeai as genai

# Sayfa Ayarları
st.set_page_config(page_title="PUBG Kod Bulucu")
st.title("🎯 PUBG Mobile Hassasiyet Sorgu")

# API Anahtarı ve v1 Kararlı Sürüm Zorlaması
if "API_KEY" in st.secrets:
    # Burada v1 sürümünü zorlayarak 404 hatasını bypass ediyoruz
    genai.configure(api_key=st.secrets["API_KEY"], transport='rest')
else:
    st.error("Secrets içine API_KEY eklenmemiş!")
    st.stop()

user_input = st.text_input("Ünlü İsmi:")

if st.button("KODU GETİR"):
    if user_input:
        with st.spinner('Sorgulanıyor...'):
            try:
                # Model ismini EN SADE haliyle yazıyoruz
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"{user_input} PUBG Mobile sensitivity code only 21 digits.")
                
                if response.text:
                    st.success("Kod bulundu!")
                    st.code(response.text)
            except Exception as e:
                st.error(f"Teknik Hata: {e}")
                
