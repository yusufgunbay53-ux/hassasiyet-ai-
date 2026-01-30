import streamlit as st
import google.generativeai as genai
import time

st.set_page_config(page_title="PUBG Kod Bulucu", page_icon="🎯")

st.title("🎯 PUBG Mobile Hassasiyet Sorgu")
st.write("Sadece ünlü ismini girin.")

# API ANAHTARI
API_KEY = st.secrets["API_KEY"]

if 'last_request_time' not in st.session_state:
    st.session_state.last_request_time = 0

current_time = time.time()
cooldown = 180 

user_input = st.text_input("Ünlü İsmi:", placeholder="Örn: Ersin Yekin")

if st.button("KODU GETİR"):
    elapsed = current_time - st.session_state.last_request_time
    if elapsed < cooldown:
        kalan_sure = int((cooldown - elapsed) / 60)
        st.warning(f"Lütfen tekrar istek atmak için {kalan_sure + 1} dakika bekleyin.")
    elif user_input:
        try:
            genai.configure(api_key=API_KEY)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            sistem_komutu = f"Sen sadece PUBG Mobile hassasiyet kodu bulmakla görevli bir yapay zekasın. Kullanıcı ismi: {user_input}. Sadece 21 rakamdan oluşan X-XXXX-XXXXX-XXXX-XXXX-XXXX formatındaki kodu ver. Başka bir şey yazma."
            
            with st.spinner('Sorgulanıyor...'):
                response = model.generate_content(sistem_komutu)
                st.session_state.last_request_time = current_time
                st.code(response.text)
        except Exception as e:
            st.error(f"Hata detayı: {e}")
    else:
        st.warning("Lütfen bir isim girin.")

st.markdown("---")
st.caption("Not: Her 3 dakikada bir 1 istek atma hakkınız vardır.")
