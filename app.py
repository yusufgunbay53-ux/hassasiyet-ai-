import streamlit as st

st.set_page_config(page_title="Spotify Clone", layout="wide")

# Custom CSS for dark theme and hiding header
st.markdown("""
    <style>
    .main {
        background-color: #121212;
        color: white;
    }
    header {
        visibility: hidden;
    }
    .stApp {
        background-color: #121212;
    }
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #000000;
        width: 300px !important;
    }
    /* Player bar styling */
    .player-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #181818;
        padding: 15px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-top: 1px solid #282828;
        z-index: 999;
    }
    /* Track card styling */
    .track-card {
        background-color: #181818;
        padding: 15px;
        border-radius: 8px;
        transition: background-color 0.3s;
    }
    .track-card:hover {
        background-color: #282828;
    }
    </style>
    """, unsafe_allow_html=True)

# Sample Track Data
TRACKS = [
    {"id": 1, "title": "Blinding Lights", "artist": "The Weeknd", "image": "https://i.scdn.co/image/ab67616d0000b2738865770331a6137682d3856b"},
    {"id": 2, "title": "Shape of You", "artist": "Ed Sheeran", "image": "https://i.scdn.co/image/ab67616d0000b273ba5db46f4b0057b79d450824"},
    {"id": 3, "title": "Stay", "artist": "The Kid LAROI & Justin Bieber", "image": "https://i.scdn.co/image/ab67616d0000b27341e31f6ea1d493dd77937ee5"},
    {"id": 4, "title": "Starboy", "artist": "The Weeknd", "image": "https://i.scdn.co/image/ab67616d0000b2734718e2b124f79258be7bc452"},
    {"id": 5, "title": "Heat Waves", "artist": "Glass Animals", "image": "https://i.scdn.co/image/ab67616d0000b2739eeedcdc134f55a1d0d93134"},
]

def init_session_state():
    if 'current_track' not in st.session_state:
        st.session_state.current_track = None
    if 'is_playing' not in st.session_state:
        st.session_state.is_playing = False

def sidebar():
    with st.sidebar:
        st.title("Spotify")
        st.markdown("---")
        st.button("🏠 Ana Sayfa", use_container_width=True)
        st.button("🔍 Ara", use_container_width=True)
        st.button("📚 Kitaplığın", use_container_width=True)
        st.markdown("---")
        st.markdown("### Çalma Listelerin")
        st.write("Favorilerim")
        st.write("Chill Vibes")
        st.write("2024 Hit")

def track_card(track):
    with st.container():
        st.image(track["image"], use_container_width=True)
        st.markdown(f"**{track['title']}**")
        st.markdown(f"<span style='color: #b3b3b3; font-size: 0.9em;'>{track['artist']}</span>", unsafe_allow_html=True)
        if st.button("Oynat", key=f"play_{track['id']}", use_container_width=True):
            st.session_state.current_track = track
            st.session_state.is_playing = True
            st.rerun()

def player_bar():
    if st.session_state.current_track:
        track = st.session_state.current_track
        st.markdown(f"""
            <div class="player-bar">
                <div style="display: flex; align-items: center; gap: 15px; flex: 1;">
                    <img src="{track['image']}" width="56" height="56" style="border-radius: 4px;">
                    <div>
                        <div style="font-weight: bold; font-size: 0.9em;">{track['title']}</div>
                        <div style="color: #b3b3b3; font-size: 0.8em;">{track['artist']}</div>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 20px; flex: 1; justify-content: center;">
                    <span style="font-size: 1.5em; cursor: pointer;">⏮</span>
                    <span style="font-size: 2em; cursor: pointer;">{'⏸' if st.session_state.is_playing else '▶'}</span>
                    <span style="font-size: 1.5em; cursor: pointer;">⏭</span>
                </div>
                <div style="flex: 1; display: flex; justify-content: flex-end; align-items: center; gap: 10px;">
                    <span style="font-size: 1.2em; cursor: pointer;">🔊</span>
                    <div style="width: 100px; height: 4px; background-color: #4f4f4f; border-radius: 2px; position: relative;">
                        <div style="width: 70%; height: 100%; background-color: #1db954; border-radius: 2px;"></div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

def main():
    init_session_state()
    sidebar()

    # Player Bar at the bottom
    player_bar()

    # Main content
    st.header("İyi akşamlar")

    # Search Bar
    search_query = st.text_input("Ne dinlemek istiyorsun?", placeholder="Ne dinlemek istiyorsun?", label_visibility="collapsed")

    # Filtering logic
    filtered_tracks = [
        t for t in TRACKS
        if search_query.lower() in t["title"].lower() or search_query.lower() in t["artist"].lower()
    ]
    
    # Display tracks in a grid
    cols = st.columns(5)
    for i, track in enumerate(filtered_tracks):
        with cols[i % 5]:
            track_card(track)

if __name__ == "__main__":
    main()
