import os
# Kütüphane uyumsuzluğunu gidermek için zorunlu güncelleme
os.system("pip install --upgrade google-generativeai")

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
            genai.configure(api_key=API_KEY)
            
            # En eski ve en uyumlu model ismi formatı
            model = genai.GenerativeModel('gemini-pro')
            
            sistem_komutu = f"PUBG Mobile uzmanı olarak {user_input} isimli oyuncunun hassasiyet kodunu sadece 21 haneli rakam olarak ver. Örn: 1111-2222-3333-4444-555"
            
            with st.spinner('Sorgulanıyor...'):
                response = model.generate_content(sistem_komutu)
                st.session_state.last_request_time = current_time
                st.success(f"{user_input} için kod:")
                st.code(response.text)
        except Exception as e:
            st.error(f"Hata detayı: {e}")
    else:
        st.warning("Lütfen bir isim girin.")
        
