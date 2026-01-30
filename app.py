import streamlit as st
import requests

st.set_page_config(page_title="PUBG Kod Bulucu")
st.title("🎯 PUBG Hassasiyet")

api_key = st.secrets.get("API_KEY")
user_input = st.text_input("Ünlü İsmi:", placeholder="Örn: Ersin Yekin")

if st.button("GETİR"):
    if user_input:
        with st.spinner('Bağlanılıyor...'):
            # DİKKAT: En kararlı kapı olan v1'i ve her yerde çalışan gemini-1.5-flash'ı zorluyoruz
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
            
            payload = {
                "contents": [{"parts": [{"text": f"PUBG Mobile {user_input} sensitivity code only 21 digits."}]}]
            }
            
            try:
                r = requests.post(url, json=payload)
                res = r.json()
                
                if "candidates" in res:
                    st.code(res["candidates"][0]["content"]["parts"][0]["text"])
                    st.success("Kod bulundu!")
                else:
                    # Hata varsa, dünyadaki en eski/sağlam model olan gemini-pro'ya sığın
                    url_pro = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
                    r_pro = requests.post(url_pro, json=payload)
                    res_pro = r_pro.json()
                    
                    if "candidates" in res_pro:
                        st.code(res_pro["candidates"][0]["content"]["parts"][0]["text"])
                    else:
                        st.error(f"Google kapıları kapattı: {res.get('error', {}).get('message', 'Bilinmeyen hata')}")
            except Exception as e:
                st.error(f"Bağlantı hatası: {e}")
                
