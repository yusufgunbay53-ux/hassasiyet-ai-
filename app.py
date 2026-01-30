import streamlit as st
import google.generativeai as genai

# Sayfa Ayarları
st.set_page_config(page_title="PUBG Kod Bulucu")
st.title("🎯 PUBG Mobile Hassasiyet Sorgu")

# API Yapılandırması
if "API_KEY" in st.secrets:
    # transport='rest' kalsın, bu en stabil yoldur
    genai.configure(api_key=st.secrets["API_KEY"], transport='rest')
else:
    st.error("Secrets içine API_KEY eklenmemiş!")
    st.stop()

user_input = st.text_input("Ünlü İsmi:")

if st.button("KODU GETİR"):
    if user_input:
        with st.spinner('Sorgulanıyor...'):
            try:
                # DİKKAT: Model isminin önüne 'models/' ekledik. 
                # 404 hatasını bu şekilde bypass ediyoruz.
                model = genai.GenerativeModel('models/gemini-1.5-flash')
                
                prompt = f"{user_input} PUBG Mobile sensitivity code only 21 digits."
                response = model.generate_content(prompt)
                
                if response.text:
                    st.success("Kod bulundu!")
                    st.code(response.text)
            except Exception as e:
                # Eğer flash yine hata verirse, en eski/kararlı olan 'gemini-pro'yu dene
                try:
                    model = genai.GenerativeModel('models/gemini-pro')
                    response = model.generate_content(prompt)
                    st.success("Kod bulundu (Pro sürüm)!")
                    st.code(response.text)
                except Exception as e2:
                    st.error(f"Google hala kapıyı açmıyor. Hata: {e2}")
                    
