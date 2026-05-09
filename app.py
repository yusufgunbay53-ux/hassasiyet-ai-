import streamlit as st

# Page configuration
st.set_page_config(page_title="Spotify Clone", page_icon="🎵", layout="wide")

# Custom CSS to mimic Spotify's look
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #121212;
        color: #FFFFFF;
    }
    
    /* Hide Streamlit header */
    header {visibility: hidden;}

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #000000 !important;
        width: 250px !important;
    }

    section[data-testid="stSidebar"] .stMarkdown {
        color: #B3B3B3;
    }

    /* Card styling */
    .song-card {
        background-color: #181818;
        padding: 15px;
        border-radius: 8px;
        transition: background-color 0.3s ease;
        margin-bottom: 20px;
    }

    .song-card:hover {
        background-color: #282828;
    }

    .song-card img {
        width: 100%;
        border-radius: 4px;
        margin-bottom: 10px;
    }

    .song-title {
        font-size: 16px;
        font-weight: 700;
        margin-bottom: 5px;
        color: white;
    }

    .artist-name {
        font-size: 14px;
        color: #B3B3B3;
    }

    /* Green play button styling */
    .stButton>button {
        background-color: #1DB954;
        color: white;
        border-radius: 500px;
        border: none;
        padding: 10px 24px;
        font-weight: 700;
    }

    .stButton>button:hover {
        background-color: #1ed760;
        color: white;
        transform: scale(1.05);
    }

    /* Audio player styling */
    div[data-testid="stAudio"] {
        background-color: #181818;
        border-radius: 50px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/26/Spotify_logo_with_text.svg", width=130)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🏠 Home")
    st.markdown("### 🔍 Search")
    st.markdown("### 📚 Your Library")
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("#### PLAYLISTS")
    st.markdown("❤️ Liked Songs")
    st.markdown("🎹 Focus Flow")
    st.markdown("🎸 Rock Classics")

# Mock Data
songs = [
    {
        "title": "Starboy",
        "artist": "The Weeknd",
        "cover": "https://picsum.photos/id/1/300/300",
        "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    },
    {
        "title": "Blinding Lights",
        "artist": "The Weeknd",
        "cover": "https://picsum.photos/id/10/300/300",
        "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
    },
    {
        "title": "Levitating",
        "artist": "Dua Lipa",
        "cover": "https://picsum.photos/id/20/300/300",
        "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
    },
    {
        "title": "Stay",
        "artist": "The Kid LAROI & Justin Bieber",
        "cover": "https://picsum.photos/id/30/300/300",
        "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"
    }
]

# Main Area
st.title("Good Morning")

st.write("### Made For You")
cols = st.columns(4)

for i, song in enumerate(songs):
    with cols[i % 4]:
        st.markdown(f"""
            <div class="song-card">
                <img src="{song['cover']}">
                <div class="song-title">{song['title']}</div>
                <div class="artist-name">{song['artist']}</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Play", key=f"btn_{i}"):
            st.session_state.current_song = song

# Player Footer (sticky-ish at the bottom)
st.markdown("---")
if "current_song" in st.session_state:
    curr = st.session_state.current_song
    c1, c2, c3 = st.columns([1, 2, 1])
    with c1:
        st.write(f"**{curr['title']}**")
        st.caption(curr['artist'])
    with c2:
        st.audio(curr['url'])
    with c3:
        st.empty()
else:
    st.info("Select a song to start listening!")
    # Just a placeholder audio
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
