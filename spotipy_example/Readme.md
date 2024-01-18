# **Spotipy_search_example.ipynb**

### The `[0]` in `['tracks']['items'][0]['album']['images'][0]` is used to access the first item in a list. In this specific context, it's navigating through the structure of the Spotify API response.

#### Let's break it down:
- `['tracks']:` This accesses the 'tracks' key in the dictionary. 
- `['items']:` This accesses the 'items' key within the 'tracks' dictionary. This is often a list of tracks.
- `[0]:` This accesses the first item in the list of tracks.
- `['album']:` This accesses the 'album' key within the first track.
- `['images']:` This accesses the 'images' key within the 'album' dictionary. This is often a list of images associated with the album cover.
- `[0]:` This accesses the first item in the list of images.

**So, `['tracks']['items'][0]['album']['images'][0]` is essentially specifying the details of the first image associated with the album of the first track in the search results. If there are multiple images, you might see `[1], [2]`, and so on to access additional images. The `[0]` is used to get the details of the first image in this case.this case.**

# **UPDATED_Album_Art_Python.py**
**Updated Script [UPDATED_Album_Art_Python.py](UPDATED_Album_Art_Python.py)**
1. Enhancements:
- You can now see how the script is doing with a progress bar.
- If there are songs with missing album art, the script tells you and waits for you to check them.
- For the missing album art, it puts `_not found_` in column.
2. Usage:
- Install required libraries: `pip install pandas spotipy tqdm`
- Save your Spotify API credentials `(client ID and client secret)` in the script.
- Replace `'updated-spotify-2023.csv'` with the path to your CSV file containing song information.
- Run: `python UPDATED_Album_Art_Python.py` in terminal.

