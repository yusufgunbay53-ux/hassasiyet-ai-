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

# Cooldown
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
            # En geniş kapsamlı model ismi
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            
            sistem_komutu = f"PUBG Mobile hassasiyet kodu uzmanısın. {user_input} için sadece 21 haneli rakam kodu ver (Örn: 1234-5678-9012-3456-789). Başka yazı yazma."
            
            with st.spinner('Sorgulanıyor...'):
                response = model.generate_content(sistem_komutu)
                st.session_state.last_request_time = current_time
                st.success(f"{user_input} için kod bulundu:")
                st.code(response.text)
        except Exception as e:
            # Hata devam ederse alternatif modele geçiş yapıyoruz
            try:
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content(sistem_komutu)
                st.success(f"{user_input} için kod bulundu (Alt Mod):")
                st.code(response.text)
            except Exception as e2:
                st.error(f"Sistem şu an meşgul, lütfen 3 dakika sonra tekrar deneyin. (Hata: {e2})")
    else:
        st.warning("Lütfen bir isim girin.")
        
