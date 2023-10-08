
# **Pod Crawler**

Do you love podcasts but find yourself spending more time searching for the perfect episode than actually enjoying them?

Podcast content offers a **diverse range of topics**, from thought-provoking dialogues with world-class chess enthusiasts to deep-dive conversations with tech visionaries like Bill Gates. It even extends to captivating interviews with renowned figures, reminiscent of engaging discussions featuring the iconic artist Prince – all encapsulated within a single podcast series.

I often found myself **endlessly scrolling** through podcast directories, searching for the **perfect episode** to listen to. 

That's when I decided to create a program that automates this process. With just a click of a button, this program can:

 1. **Search** through all your favorite podcasts.

 2. **Scan** through all their episodes.
 3. **Identify** and select the episodes you'll find most interesting.
 4. **Download** those episodes.
 5. **Transcribe** the audio content.
 6. **Save** everything neatly on your local machine.

---

## **Table of Contents**

- [Getting Started](#getting-started)

- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [Support my work](#support-my-work)

## 


## **Getting Started**
To get started, follow these steps:

1. **Fork and Clone Repository**: Fork this repository on GitHub and then clone it locally to your computer. You can do this using Git commands or GitHub Desktop. If you're new to forking and cloning, you can find instructions [here](https://docs.github.com/en/get-started/quickstart/fork-a-repo).


2. **Install Dependencies**: Make sure you have all the required Python libraries installed. You can do this by running the following command:

```
pip install -r requirements.txt
```

3. **Configure Podcasts**: Open the **download.py** and **transcripts.py** files and edit the podcast_list located at the bottom of each file.

- For each podcast you want to download and transcribe, create a Podcast object by providing a *"name"* and the *"URL of the podcast's RSS feed"*. For example:

```

podcast_list = [
    Podcast('lex-fridman', 'https://lexfridman.com/feed/podcast/'),
    Podcast('another-podcast', 'https://example.com/feed/podcast/')
]

```

You can add as many podcasts as you want by creating additional Podcast objects.

- **Discover Podcast RSS Feeds**: In order to obtain RSS feed url's, you can use services like [getrssfeed.com](https://getrssfeed.com). It helps us to discover and extract RSS feeds from various sources, including Apple Podcasts, Google Podcasts, SoundCloud, and blogs/websites. Once you have the RSS feed URL for a podcast, you can proceed to configure the program.





4. **Set Limits and Search Terms**: You can specify how many podcast episodes you want to download from each podcast by modifying the **"limit"** variable. 

Additionally, you can customize the search term to filter which types of episodes you want to download.

- In my implementation, the search term is set to **'zuckerberg'**, and the limit is set to **'1'**. Modify these values to suit your preferences.


5. **Run the Bash Script**: Execute the bash script **run_all.sh** to initiate the download and transcription process for your selected podcasts.

That's it! You're now ready to enjoy an automated way of downloading and transcribing your favorite podcasts.

## 


## **Usage**

Upon running the scripts, you will see the following information:

- In the *download.py* script, you will see the progress of downloading podcast episodes, including the file path of the downloaded files and the total time taken for downloading.

- In the *transcripts.py* script, you will see the progress of uploading podcast episodes for transcription and the corresponding transcription IDs. The script will wait until the transcription is complete and then save the transcriptions both as metadata and locally.

## 
## **Customization**

This project is flexible and can be *customized to download and transcribe podcasts* from different hosts and on various topics. You can adapt it by following the steps outlined in the **"Getting Started"** section.

##

## **Contributing**

Contributions are always welcome !!

If you would like to contribute to the project, please fork the repository and make a pull request.



## **Support my work** 
Do ⭐ the repository, if it inspired you, gave you ideas for your own project or helped you in any way !!!
