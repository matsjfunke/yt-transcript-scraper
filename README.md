# Usage

1. clone repo

```sh
git clone git@github.com:matsjfunke/yt-transcript-scraper.git
```

2. call script with arguments

```sh
python get_transcript.py <YouTube Video URL> [--lang <Language Code>]
```

**Arguments**
url: The URL of the YouTube video. This is a required positional argument.
--lang: The language code for translation. This is an optional argument. If not provided, it defaults to 'en' (English).

Example
To fetch the transcript of a YouTube video and translate it to German:

```sh
python get_transcript.py "https://www.youtube.com/watch?v=jDe5BAsT2-Y" --lang de
```

# API docs

check https://github.com/jdepoix/youtube-transcript-api for docs

# TODOs

- structuring output in txt
