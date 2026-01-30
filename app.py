import streamlit as st
import requests
import json

st.set_page_config(page_title="PUBG Kod Bulucu")
st.title("🎯 PUBG Mobile Hassasiyet Sorgu")

api_key = st.secrets.get("API_KEY")
user_input = st.text_input("Ünlü İsmi:", placeholder="Örn: Ersin Yekin")

if st.button("KODU GETİR"):
    if not api_key:
        st.error("API_KEY bulunamadı!")
    elif user_input:
        with st.spinner('Bağlanılıyor...'):
            # DİKKAT: En kararlı model olan gemini-pro'ya dönüyoruz
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
            
            payload = {
                "contents": [{
                    "parts": [{"text": f"PUBG Mobile {user_input} hassasiyet kodu sadece 21 haneli rakam ver."}]
                }]
            }
            
            try:
                response = requests.post(url, json=payload)
                result = response.json()
                
                if "candidates" in result:
                    kod = result["candidates"][0]["content"]["parts"][0]["text"]
                    st.success(f"{user_input} için kod bulundu!")
                    st.code(kod)
                else:
                    # Hata varsa burada göreceğiz
                    msg = result.get('error', {}).get('message', 'Model henüz aktif değil.')
                    st.error(f"Google Yanıtı: {msg}")
            except Exception as e:
                st.error(f"Bağlantı hatası: {e}")
                
