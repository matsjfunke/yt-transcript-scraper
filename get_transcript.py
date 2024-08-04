"""
matsjfunke
"""

import argparse
import re

from youtube_transcript_api import YouTubeTranscriptApi


def main(url, lang):
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
            print(f"Translation Codes: {[entry["language_code"] for entry in transcript.translation_languages]}\n")
            if lang in [entry["language_code"] for entry in transcript.translation_languages]:

                try:
                    # Fetch and translate the transcript to English
                    translated_transcript = transcript.translate(lang).fetch()

                    # Join transcript segments into a single string
                    full_transcript = ""
                    for segment in translated_transcript:
                        full_transcript += segment["text"] + "\n"

                    # Write translated transcript to a text file
                    file_name = f"{video_id}_{lang}.txt"
                    with open(file_name, "w", encoding="utf-8") as txt_file:
                        txt_file.write(full_transcript)

                    print(f"Translated transcript saved as {file_name}")

                except Exception as e:
                    print(f"Error processing transcript: {e}")

            else:
                print("Invalid language argument")

    else:
        print("Invalid url")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch and translate YouTube transcript.")
    parser.add_argument("url", type=str, help="YouTube video URL")
    parser.add_argument("--lang", type=str, default="en", help="Language code for translation (default: 'en')")
    args = parser.parse_args()

    main(args.url, args.lang)
