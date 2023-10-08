import os
import re
import json
import time
import requests 

from podcast import Podcast

# --------------------------------------------


def create_transcripts(podcast_list, **kwargs):
	# create transcripts for podcast episodes.
    all_transcripts_metadata = {}

    for podcast in podcast_list:
        podcast_metadata = {}
        downloads = os.listdir(podcast.download_directory)
        
        for download in downloads: 
            print('\n----- Uploading Podcasts ... -----\n')
			
            # upload audio file to AssemblyAI and transcribe it.
            filepath = f'{podcast.download_directory}/{download}'

            content_url = upload_to_assembly_ai(filepath)
            transcription_id = transcribe_podcast(content_url, **kwargs)

            podcast_metadata[download] = transcription_id 

        all_transcripts_metadata[podcast.name] = podcast_metadata.copy()

    return all_transcripts_metadata


def upload_to_assembly_ai(file_path):
	headers = {'authorization': os.environ['ASSEMBLY_AI_KEY']}
	endpoint = 'https://api.assemblyai.com/v2/upload'
	
	response = requests.post(endpoint, headers=headers, data=read_file(file_path))
	
	upload_url = response.json()['upload_url']
	return upload_url


def transcribe_podcast(url, **kwargs):
	headers = {
        "authorization": os.environ['ASSEMBLY_AI_KEY'],
        "content-type": "application/json"
	}
	
	json = {
		'audio_url': url,
    }
	
	for key, value in kwargs.items():
		json[key] = value
	
	endpoint = 'https://api.assemblyai.com/v2/transcript'
	response = requests.post(endpoint, headers=headers, json=json)

	transcription_id = response.json()['id']
	return transcription_id


def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data


def save_transcriptions_metadata(metadata, file_path='./transcripts/metadata.json'):
	with open(file_path,'w') as f:
		json.dump(metadata, f)


def load_transcriptions_metadata(file_path='./transcripts/metadata.json'):
	with open(file_path) as json_file:
		metadata = json.load(json_file)

	return metadata


def save_transcriptions_locally(podcast_list):
	metadata = load_transcriptions_metadata()
	
	for podcast in podcast_list:
		podcast_transcripts = metadata[podcast.name]
		
		for episode, transcription_id in podcast_transcripts.items():
			episode_name = os.path.splitext(episode)[0]
			output_path = f'{podcast.transcript_directory}/{episode_name}.txt'
			
			print('Trying to save !!! :  \n', output_path)
			
			transcription = wait_and_get_assembly_ai_transcript(transcription_id)
			
			with open(output_path, 'w') as f:
				f.write(transcription['text'])


def get_assembly_ai_transcript(transcription_id):
	headers = {'authorization': os.environ['ASSEMBLY_AI_KEY']}
	endpoint = f'https://api.assemblyai.com/v2/transcript/{transcription_id}'
	
	response = requests.get(endpoint, headers=headers)
	return response.json()


def wait_and_get_assembly_ai_transcript(transcription_id):
	while True:
		response = get_assembly_ai_transcript(transcription_id)
		
		if response['status'] == 'completed':
			print("Transcription Complete !!!\n")
			break
		
		elif response['status'] == 'error':
			print("Error getting transcript !!!\n ")
			break
		
		else:
			print("Transcript is not available, will try again in 2 minutes ...\n")
			time.sleep(120) 

	return response


# --------------------------------------------

if __name__ == "__main__":
    print('\n----- Transcribing Podcasts ... -----\n')

    podcast_list = [Podcast('lex-fridman', 'https://lexfridman.com/feed/podcast/')]

    total_transcribed = 0
    start_time = time.time()

    for podcast in podcast_list:
        podcast_items = podcast.search_items('zuckerberg', limit=1)
        total_episodes = len(podcast_items)

        metadata = create_transcripts(podcast_list, audio_start_from=900000, audio_end_at=1200000)

        end_time = time.time()
        total_time = end_time - start_time

        print(f'Upload Complete: {total_transcribed}/{total_episodes} episodes uploaded.')
        print(f'Total time taken: {total_time:.2f} seconds\n')

    print('Transcription Complete !!!')

    # Save transcripts' metadata and transcripts locally.
    save_transcriptions_metadata(metadata)
    save_transcriptions_locally(podcast_list)







