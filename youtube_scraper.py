from googleapiclient.discovery import build

# Ganti dengan API Key YouTube
API_KEY = "AIzaSyAvfSoEoYhHXPZroCuSgj2ZVUP5D4qK520"

# Inisialisasi YouTube API
youtube = build("youtube", "v3", developerKey=API_KEY)

# ID channel yang mau diambil datanya
CHANNEL_ID = "gsbKelrwWCzayija"

# Ambil daftar video dari channel
def get_videos(channel_id):
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=10,  # Ambil 10 video terakhir
        order="date"
    )
    response = request.execute()

    for item in response["items"]:
        video_id = item["id"]["videoId"]
        title = item["snippet"]["title"]
        print(f"Judul: {title} - Link: https://www.youtube.com/watch?v={video_id}")

# Jalankan fungsi
get_videos(CHANNEL_ID)