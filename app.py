import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="PUBG Kod Bulucu")
st.title("🎯 PUBG Mobile Hassasiyet Sorgu")

# API Anahtarını al ve yapılandır
if "API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["API_KEY"])
else:
    st.error("API_KEY Secrets içine eklenmemiş!")
    st.stop()

user_input = st.text_input("Ünlü İsmi:")

if st.button("KODU GETİR"):
    if user_input:
        with st.spinner('Sorgulanıyor...'):
            try:
                # Grafikte hata veren sürüm yerine en kararlı olanı zorluyoruz
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"{user_input} PUBG Mobile sensitivity code only 21 digits.")
                
                if response.text:
                    st.success("Kod bulundu!")
                    st.code(response.text)
            except Exception as e:
                st.error(f"Google Hatası: {e}")
                st.info("Eğer 404 alıyorsan, lütfen Google AI Studio'dan YENİ BİR KEY alıp Secrets'a yapıştır.")
                
