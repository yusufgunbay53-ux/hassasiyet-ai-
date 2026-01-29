import streamlit as st
import google.generativeai as genai

# Sayfa tasarımı
st.set_page_config(page_title="PUBG AI Hassasiyet", page_icon="🎮")
st.title("🎯 PUBG Pro Hassasiyet Bulucu")

# API Anahtarını buraya tırnak içine yapıştır
API_KEY = "AIzaSyC1SjL_kcah61pvh8Buxgj1lalHmO-v32A"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

query = st.text_input("Hangi yayıncının ayarlarını arıyorsun?", placeholder="Örn: Ersin Yekin güncel hassasiyet")

if st.button("Ayarları Getir"):
    if query:
        with st.spinner('Yapay zeka araştırıyor...'):
            try:
                response = model.generate_content(f"{query} PUBG Mobile oyuncusunun en güncel hassasiyet kodlarını ve ayarlarını tablo olarak göster.")
                st.markdown(response.text)
            except:
                st.error("Bir hata oluştu")
    else:
        st.warning("Lütfen bir isim yazın!")
