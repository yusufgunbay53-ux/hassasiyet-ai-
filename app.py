import streamlit as st

# Page configuration
st.set_page_config(page_title="Spotify Clone", page_icon="🎵", layout="wide")

# Custom CSS for Spotify-like UI
st.markdown("""
<style>
    /* Dark theme colors */
    :root {
        --background-base: #121212;
        --background-highlight: #1a1a1a;
        --background-press: #000;
        --text-base: #fff;
        --text-subdued: #a7a7a7;
        --spotify-green: #1db954;
    }

    .stApp {
        background-color: var(--background-base);
        color: var(--text-base);
    }

    /* Hide Streamlit elements */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #000000 !important;
        border-right: 1px solid #282828;
    }

    /* Sidebar Content */
    .sidebar-item {
        padding: 8px 16px;
        color: var(--text-subdued);
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 16px;
        cursor: pointer;
        transition: color 0.2s;
    }

    .sidebar-item:hover {
        color: var(--text-base);
    }

    .sidebar-item.active {
        color: var(--text-base);
    }

    /* Main content grid */
    .song-card {
        background-color: #181818;
        padding: 16px;
        border-radius: 8px;
        transition: background-color 0.3s ease;
        margin-bottom: 20px;
    }

    .song-card:hover {
        background-color: #282828;
    }

    .song-card img {
        width: 100%;
        aspect-ratio: 1/1;
        object-fit: cover;
        border-radius: 4px;
        margin-bottom: 16px;
        box-shadow: 0 8px 24px rgba(0,0,0,.5);
    }

    .song-title {
        font-weight: 700;
        font-size: 16px;
        margin-bottom: 4px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .song-artist {
        color: var(--text-subdued);
        font-size: 14px;
    }

    /* Player bar */
    .player-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        height: 90px;
        background-color: #000000;
        border-top: 1px solid #282828;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 16px;
        z-index: 1000;
    }

    .now-playing {
        display: flex;
        align-items: center;
        gap: 14px;
        width: 30%;
    }

    .now-playing img {
        width: 56px;
        height: 56px;
        border-radius: 4px;
    }

    .player-controls {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 8px;
        width: 40%;
    }

    .control-buttons {
        display: flex;
        align-items: center;
        gap: 24px;
    }

    .play-button {
        background-color: #fff;
        border: none;
        border-radius: 50%;
        width: 32px;
        height: 32px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
    }

    .progress-container {
        width: 100%;
        max-width: 500px;
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 11px;
        color: var(--text-subdued);
    }

    .progress-bar {
        flex-grow: 1;
        height: 4px;
        background-color: #4d4d4d;
        border-radius: 2px;
        position: relative;
    }

    .progress-fill {
        width: 30%;
        height: 100%;
        background-color: var(--text-base);
        border-radius: 2px;
    }

    .volume-controls {
        width: 30%;
        display: flex;
        justify-content: flex-end;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for playback
if 'current_track' not in st.session_state:
    st.session_state.current_track = None
if 'is_playing' not in st.session_state:
    st.session_state.is_playing = False

# Sample track data
tracks = [
    {"id": 1, "title": "Blinding Lights", "artist": "The Weeknd", "image": "https://upload.wikimedia.org/wikipedia/en/e/e6/The_Weeknd_-_Blinding_Lights.png"},
    {"id": 2, "title": "Starboy", "artist": "The Weeknd", "image": "https://upload.wikimedia.org/wikipedia/en/3/39/The_Weeknd_-_Starboy.png"},
    {"id": 3, "title": "Save Your Tears", "artist": "The Weeknd", "image": "https://upload.wikimedia.org/wikipedia/en/4/4c/The_Weeknd_-_Save_Your_Tears.png"},
    {"id": 4, "title": "Die For You", "artist": "The Weeknd", "image": "https://upload.wikimedia.org/wikipedia/en/4/41/The_Weeknd_-_Starboy.png"},
    {"id": 5, "title": "The Hills", "artist": "The Weeknd", "image": "https://upload.wikimedia.org/wikipedia/en/e/e0/The_Weeknd_-_The_Hills.png"},
    {"id": 6, "title": "Can't Feel My Face", "artist": "The Weeknd", "image": "https://upload.wikimedia.org/wikipedia/en/b/bd/The_Weeknd_-_Can%27t_Feel_My_Face.png"},
]

def play_track(track):
    st.session_state.current_track = track
    st.session_state.is_playing = True

# Sidebar
with st.sidebar:
    st.markdown('<div style="padding: 24px 0 18px 0;"><h2 style="color: white; margin-left: 16px;">Spotify</h2></div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-item active">🏠 Ana Sayfa</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-item">🔍 Ara</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-item">📚 Kitaplığın</div>', unsafe_allow_html=True)
    
    st.markdown('<div style="margin-top: 24px;" class="sidebar-item">➕ Çalma Listesi Oluştur</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-item">❤️ Beğenilen Şarkılar</div>', unsafe_allow_html=True)

# Main Content
st.markdown('<h1 style="font-size: 32px; margin-bottom: 24px;">İyi günler</h1>', unsafe_allow_html=True)

# Song Grid
cols = st.columns(3)
for i, track in enumerate(tracks):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="song-card">
            <img src="{track['image']}">
            <div class="song-title">{track['title']}</div>
            <div class="song-artist">{track['artist']}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"Oynat: {track['title']}", key=f"play_{track['id']}"):
            play_track(track)

# Player Bar (Sticky at bottom)
if st.session_state.current_track:
    track = st.session_state.current_track
    st.markdown(f"""
    <div class="player-bar">
        <div class="now-playing">
            <img src="{track['image']}">
            <div>
                <div class="song-title" style="font-size: 14px;">{track['title']}</div>
                <div class="song-artist" style="font-size: 11px;">{track['artist']}</div>
            </div>
        </div>
        <div class="player-controls">
            <div class="control-buttons">
                <span style="color: var(--text-subdued);">⏮️</span>
                <span style="font-size: 24px;">{'⏸️' if st.session_state.is_playing else '▶️'}</span>
                <span style="color: var(--text-subdued);">⏭️</span>
            </div>
            <div class="progress-container">
                <span>0:45</span>
                <div class="progress-bar">
                    <div class="progress-fill"></div>
                </div>
                <span>3:24</span>
            </div>
        </div>
        <div class="volume-controls">
            <span style="color: var(--text-subdued);">🔊</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Simple controls overlay (Streamlit doesn't support easy JS for this UI yet)
    c1, c2, c3 = st.columns([1,1,1])
    with c2:
        if st.button("Durdur/Oynat" if st.session_state.is_playing else "Oynat"):
            st.session_state.is_playing = not st.session_state.is_playing
            st.rerun()

# Add padding for bottom bar
st.markdown('<div style="height: 100px;"></div>', unsafe_allow_html=True)
