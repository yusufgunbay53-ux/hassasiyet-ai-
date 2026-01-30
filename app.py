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

if 'last_request_time' not in st.session_state:
    st.session_state.last_request_time = 0

current_time = time.time()
cooldown = 60 # Deneme amaçlı 1 dakikaya düşürdüm

user_input = st.text_input("Ünlü İsmi:", placeholder="Örn: Ersin Yekin")

if st.button("KODU GETİR"):
    elapsed = current_time - st.session_state.last_request_time
    if elapsed < cooldown:
        st.warning(f"Lütfen {int(cooldown - elapsed)} saniye bekleyin.")
    elif user_input:
        with st.spinner('Kod aranıyor...'):
            # Ücretsiz planda çalışan tüm varyasyonlar
            modeller = ['gemini-1.5-flash', 'gemini-1.5-flash-latest', 'gemini-pro']
            basari = False
            
            for m_adi in modeller:
                try:
                    # Hem normal hem models/ ön ekiyle deniyoruz
                    for prefix in ["", "models/"]:
                        try:
                            model = genai.GenerativeModel(prefix + m_adi)
                            response = model.generate_content(f"PUBG Mobile {user_input} hassasiyet kodu sadece 21 hane rakam ver.")
                            if response.text:
                                st.success(f"{user_input} için kod bulundu!")
                                st.code(response.text)
                                st.session_state.last_request_time = current_time
                                basari = True
                                break
                        except:
                            continue
                    if basari: break
                except:
                    continue
            
            if not basari:
                st.error("Google şu an yanıt vermiyor. Lütfen API anahtarınızı Google AI Studio'dan kontrol edin veya yeni bir tane oluşturun.")
    else:
        st.warning("Lütfen bir isim girin.")
        
