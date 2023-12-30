# Import necessary libraries
import os
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from tqdm import tqdm

# Function to retrieve album art URL from Spotify using track and artist names
def get_album_art(track_name, artist_name):
    # Set up Spotify client credentials
    client_credentials_manager = SpotifyClientCredentials(client_id='<-paste_your_client_id_here->', client_secret='<-paste_your_client_secret_here->')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    # Search for the track on Spotify
    results = sp.search(q=f'track:{track_name} artist:{artist_name}', type='track')
    
    # Check if there are any matching tracks
    if results['tracks']['items']:
        # Retrieve the album art URL from the first matching track
        album_art_url = results['tracks']['items'][0]['album']['images'][0]['url']
        return album_art_url
    else:
        # Return None if no matching track is found
        return None

# Function to verify and update missing album art URLs in the DataFrame
def verify_album_art(df):
    # Clear the console screen
    os.system('cls')
    
    # Identify rows with missing album art URLs
    missing_albums = df[pd.isna(df['album_art_url'])]
    
    # Check if there are any missing album art URLs
    if not missing_albums.empty:
        print("The following songs have missing album art:")
        # Display the missing songs
        for index, row in missing_albums.iterrows():
            print(f" - '{row['track_name']}' by '{row['artist(s)_name']}'")
        
        # Pause execution to allow the user to view the missing songs
        os.system('echo.')
        os.system('pause')
        
        # Set a placeholder URL for missing album art
        new_url = ("_not found_")
        
        # Update the DataFrame with the placeholder URL for missing album art
        df.loc[missing_albums.index, 'album_art_url'] = new_url
        
        # Return the placeholder URL
        return new_url
    else:
        # If no missing album art URLs are found, display a message
        print("All album arts are found. No updates needed.")
        return None

# Read the input DataFrame from a CSV file
df = pd.read_csv('updated-spotify-2023.csv', encoding='utf-8')

# Use tqdm to show progress while applying the get_album_art function to each row
tqdm.pandas(desc="Processing", unit="row")
df['album_art_url'] = df.progress_apply(lambda row: get_album_art(row['track_name'], row['artist(s)_name']), axis=1)

# Verify and update missing album art URLs in the DataFrame
new_url = verify_album_art(df)
df['album_art_url'] = df['album_art_url'].fillna(new_url)

# Save the updated DataFrame to a new CSV file
output_file = 'updated-Art-spotify-2023.csv'
df.to_csv(output_file, index=False)

# Display a completion message
print(f"Processing completed. Updated DataFrame saved to '{output_file}'.")
