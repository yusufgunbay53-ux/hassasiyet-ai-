import streamlit as st
import google.generativeai as genai
import time

# Sayfa Ayarları
st.set_page_config(page_title="PUBG Kod Bulucu", page_icon="🎯")

st.title("🎯 PUBG Mobile Hassasiyet Sorgu")
st.write("Sadece ünlü ismini girin.")

# API Anahtarı
try:
    API_KEY = st.secrets["API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception:
    st.error("Hata: Secrets kısmında API_KEY bulunamadı!")
    st.stop()

# Cooldown (3 Dakika)
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
        with st.spinner('Modeller deneniyor, lütfen bekleyin...'):
            # Google'ın kabul edebileceği tüm olası isimleri sırayla deniyoruz
            denenecek_modeller = [
                'models/gemini-1.5-flash-latest',
                'models/gemini-1.5-pro-latest',
                'gemini-1.5-flash',
                'gemini-pro'
            ]
            
            basarili = False
            for model_adi in denenecek_modeller:
                try:
                    model = genai.GenerativeModel(model_adi)
                    sistem_komutu = f"PUBG Mobile hassasiyet kodu uzmanısın. {user_input} için sadece 21 haneli rakam kodu ver (Örn: 1111-2222-3333-4444-555). Başka hiçbir şey yazma."
                    response = model.generate_content(sistem_komutu)
                    
                    if response.text:
                        st.session_state.last_request_time = current_time
                        st.success(f"{user_input} için kod bulundu!")
                        st.code(response.text)
                        basarili = True
                        break
                except Exception:
                    continue # Bu model çalışmazsa bir sonrakine geç
            
            if not basarili:
                st.error("Ücretsiz API limitiniz dolmuş veya model ismi değişmiş olabilir. Lütfen 5 dakika sonra tekrar deneyin.")
    else:
        st.warning("Lütfen bir isim girin.")
        
