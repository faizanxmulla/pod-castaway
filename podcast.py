import os 
import re 
import requests 
import dateutil.parser
from bs4 import BeautifulSoup

# --------------------------------------------

class Podcast: 
    def __init__(self, name, rss_feed_url):
        # initialize a Podcast object with a name and RSS feed URL.
        self.name = name 
        self.rss_feed_url = rss_feed_url 

        # create download and transcript directories for this podcast.

        self.download_directory = f'./downloads/{name}'
        if not os.path.exists(self.download_directory):
            os.mkdir(self.download_directory)

        self.transcript_directory = f'./transcripts/{name}'
        if not os.path.exists(self.transcript_directory):
            os.mkdir(self.transcript_directory)


    def get_items(self, limit=None):
        # retrieve podcast items from the RSS feed.
        page = requests.get(self.rss_feed_url)
        soup = BeautifulSoup(page.text, 'xml')
        return soup.find_all('item')[:limit]


    def search_items(self, search, limit=None):
        # search for podcast items that matches a search query.
        matched_podcasts = []
        items = self.get_items()

        for podcast in items: 
            if re.search(search, podcast.find('description').text, re.I):
                matched_podcasts.append(podcast)

        return matched_podcasts[:limit]