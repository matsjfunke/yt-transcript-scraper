"""
matsjfunke
"""

import re

from youtube_transcript_api import YouTubeTranscriptApi

def main(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    if match:
        video_id = match.group(1)

        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # Iterate over all available transcripts
        for transcript in transcript_list:
            # Print metadata
            print(f"Video ID: {transcript.video_id}\n")
            print(f"Language: {transcript.language}\n")
            print(f"Is Generated: {transcript.is_generated}\n")
            print(f"Is translatable: {transcript.is_translatable}\n")
            print(f"Translations: {[entry["language"] for entry in transcript.translation_languages]}\n")

            try:
                # Fetch and translate the transcript to English
                translated_transcript = transcript.translate("en").fetch()

                # Join transcript segments into a single string
                full_transcript = ""
                for segment in translated_transcript:
                    full_transcript += segment["text"] + "\n"

                # Write translated transcript to a text file
                with open(f"{video_id}_en.txt", "w", encoding="utf-8") as txt_file:
                    txt_file.write(full_transcript)

                print(f"Translated transcript saved as {video_id}_en.txt")

            except Exception as e:
                print(f"Error processing transcript: {e}")

    else:
        print("Invalid url")
    return True


if __name__ == "__main__":
    url = input("Enter video url: ")
    main(url)
