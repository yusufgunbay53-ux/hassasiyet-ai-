import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="PUBG Kod Bulucu")
st.title("🎯 PUBG Mobile Hassasiyet Sorgu")

if "API_KEY" in st.secrets:
    # transport='rest' kalsın, bu en güvenli yol
    genai.configure(api_key=st.secrets["API_KEY"], transport='rest')
else:
    st.error("Secrets içine API_KEY eklenmemiş!")
    st.stop()

user_input = st.text_input("Ünlü İsmi:")

if st.button("KODU GETİR"):
    if user_input:
        with st.spinner('Sorgulanıyor...'):
            try:
                # DİKKAT: Burada model isminin önüne 'models/' ekledik 
                # ve en eski/stabil sürüm olan 'gemini-pro'yu deniyoruz
                model = genai.GenerativeModel('models/gemini-pro')
                
                response = model.generate_content(f"{user_input} PUBG Mobile sensitivity code only 21 digits.")
                
                if response.text:
                    st.success("Kod bulundu!")
                    st.code(response.text)
            except Exception as e:
                # Eğer gemini-pro da olmazsa flash'ı 'models/' ön ekiyle dene
                try:
                    model = genai.GenerativeModel('models/gemini-1.5-flash')
                    response = model.generate_content(f"{user_input} PUBG Mobile sensitivity code only 21 digits.")
                    st.success("Kod bulundu!")
                    st.code(response.text)
                except Exception as e2:
                    st.error(f"Google hala kapıyı açmıyor. Hata: {e2}")
                    
