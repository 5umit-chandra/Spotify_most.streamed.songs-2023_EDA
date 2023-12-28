import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Function to get album art URL using Spotipy
def get_album_art(track_name, artist_name):
    client_credentials_manager = SpotifyClientCredentials(client_id='<-paste_your_client_id_here->', client_secret='<-paste_your_client_secret_here->')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    # Search for the track
    print(f"Searching for album art for '{track_name}' by '{artist_name}'...")
    results = sp.search(q=f'track:{track_name} artist:{artist_name}', type='track')
    
    # Extract album art URL
    if results['tracks']['items']:
        album_art_url = results['tracks']['items'][0]['album']['images'][0]['url']
        print(f"Album art found: {album_art_url}")
        return album_art_url
    else:
        print("Album art not found.")
        return None

# Read the CSV file into a DataFrame with encoding
df = pd.read_csv('updated-spotify-2023.csv', encoding='utf-8')

# Add a new column for album art URLs
df['album_art_url'] = df.apply(lambda row: get_album_art(row['track_name'], row['artist(s)_name']), axis=1)

# Save the updated DataFrame to a new CSV file
output_file = 'updated-Art-spotify-2023'
df.to_csv(output_file, index=False)

print(f"Processing completed. Updated DataFrame saved to '{output_file}'.")