import streamlit as st
import requests

st.title("🎯 PUBG Hassasiyet")

api_key = st.secrets.get("API_KEY")
user_input = st.text_input("Ünlü İsmi:")

if st.button("GETİR"):
    if user_input:
        # Hesabın Gemini 3 olduğu için doğrudan bu yolu deniyoruz
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash:generateContent?key={api_key}"
        
        payload = {
            "contents": [{"parts": [{"text": f"{user_input} PUBG Mobile sensitivity code only 21 digits."}]}]
        }
        
        try:
            r = requests.post(url, json=payload)
            res = r.json()
            if "candidates" in res:
                st.code(res["candidates"][0]["content"]["parts"][0]["text"])
                st.success("Kod bulundu!")
            else:
                # Eğer Gemini 3 henüz API üzerinden açılmadıysa 1.5 Flash'ı dene
                url_alt = url.replace("gemini-3-flash", "gemini-1.5-flash")
                r_alt = requests.post(url_alt, json=payload)
                res_alt = r_alt.json()
                if "candidates" in res_alt:
                    st.code(res_alt["candidates"][0]["content"]["parts"][0]["text"])
                else:
                    st.error(f"Google Yanıtı: {res.get('error', {}).get('message', 'Model hatası')}")
        except Exception as e:
            st.error(f"Bağlantı hatası: {e}")
            
