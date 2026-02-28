
import webbrowser
def open_application(app_name):
    app_name = app_name.lower().strip()

    APP_URLS = {
        "spotify": "https://open.spotify.com",
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "gmail": "https://mail.google.com",
        "linkedin": "https://linkedin.com",
        "instagram": "https://instagram.com",
        "facebook": "https://facebook.com",
        "twitter": "https://twitter.com",
        "github": "https://github.com",
        "chatgpt": "https://chat.openai.com"
    }
    if app_name in APP_URLS:
        webbrowser.open(APP_URLS[app_name])
        return f"{app_name.capitalize()} opened in browser."

    return f"Application {app_name} not supported yet."


# SPOTIFY SEARCH
def open_spotify_search(song_name):
    query = song_name.replace(" ", "%20")
    url = f"https://open.spotify.com/search/{query}"
    webbrowser.open(url)
    return f"Playing {song_name} on Spotify."
# YOUTUBE SEARCH
def open_youtube_search(song_name):
    query = song_name.replace(" ", "%20")
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    return f"Playing {song_name} on YouTube."
