import re 
import time
import requests 
import dateutil.parser 

from podcast import Podcast

# --------------------------------------------

def get_episodes_metadata(podcasts_items):
    # extract metadata (URL, title, release date) from podcast items.
    episodes_urls = [podcast.find('enclosure')['url'] for podcast in podcasts_items]    
    episodes_titles = [podcast.find('title').text for podcast in podcasts_items]    
    episodes_release_dates = [podcast.find('pubDate') for podcast in podcasts_items]    

    return list(zip(episodes_urls, episodes_titles, episodes_release_dates))


def parse_date(date): 
    return dateutil.parser(date).strftime('%b-%d-%Y')


def get_mp3_file(url):
    # download MP3 file from a URL.
    redirect_url = requests.get(url).url
    file = requests.get(redirect_url)
    return file


def save_mp3_url(file, filepath):
    # save MP3 file to a specified filepath.
    with open(filepath, 'wb') as f:
        f.write(file.content)


def sanitize_title(title):
    # sanitize a title to make it suitable for use as a filename.
    filename = re.sub(r'[\\/:*?"<>|]', '', title)
    return filename


if __name__ == '__main__':
    print('\n----- Downloading Podcasts ... -----\n')

    podcast_list = [Podcast('lex-fridman', 'https://lexfridman.com/feed/podcast/')]

    for podcast in podcast_list:
        podcast_items = podcast.search_items('zuckerberg', limit=1)
        episodes_metadata = get_episodes_metadata(podcast_items)
        total_episodes = len(episodes_metadata)  

        start_time = time.time()

        for i, episode in enumerate(episodes_metadata, start=1):
            url, title, release_date = episode
            sanitized_title = sanitize_title(title)

            file = get_mp3_file(url)
            filepath = f'{podcast.download_directory}/{sanitized_title}.mp3'

            print(f'Downloaded "{filepath}"...')

            save_mp3_url(file, filepath)
            print(f'Downloaded {i}/{total_episodes} episodes\n') 

        end_time = time.time()
        total_time = end_time - start_time  

        print(f'Download complete !!!')
        print(f'Total time taken for downloading : {total_time:.2f} seconds\n')


