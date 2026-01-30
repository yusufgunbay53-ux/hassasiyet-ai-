import streamlit as st
import requests
import json

st.set_page_config(page_title="PUBG Kod Bulucu")
st.title("🎯 PUBG Mobile Hassasiyet Sorgu")

# API Anahtarını al
api_key = st.secrets.get("API_KEY")

user_input = st.text_input("Ünlü İsmi:", placeholder="Örn: Ersin Yekin")

if st.button("KODU GETİR"):
    if not api_key:
        st.error("Secrets kısmında API_KEY bulunamadı!")
    elif user_input:
        with st.spinner('Doğrudan Google sunucularına bağlanılıyor...'):
            # Adresi biz elle yazıyoruz (v1 sürümü), yanlış kapıya gitme şansı yok!
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
            
            payload = {
                "contents": [{
                    "parts": [{"text": f"PUBG Mobile {user_input} hassasiyet kodu sadece 21 haneli rakam ver."}]
                }]
            }
            headers = {'Content-Type': 'application/json'}
            
            try:
                response = requests.post(url, headers=headers, data=json.dumps(payload))
                result = response.json()
                
                if "candidates" in result:
                    kod = result["candidates"][0]["content"]["parts"][0]["text"]
                    st.success(f"{user_input} için kod bulundu!")
                    st.code(kod)
                else:
                    # Hata mesajını detaylı görelim
                    error_msg = result.get('error', {}).get('message', 'Bilinmeyen hata')
                    st.error(f"Google Yanıtı: {error_msg}")
                    if "404" in str(result):
                        st.info("Eğer hala 404 alıyorsan, Google AI Studio'dan 'Gemini 1.5 Flash' modelinin aktif olup olmadığını kontrol et.")
            except Exception as e:
                st.error(f"Bağlantı hatası: {e}")
    else:
        st.warning("Lütfen bir isim girin.")
        
