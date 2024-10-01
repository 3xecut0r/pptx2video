# PowerPoint to Video Converter with Audio Narration

This Python script converts a PowerPoint presentation (`.pptx`) into a video (`.mp4`) with each slide displayed for the duration of its corresponding narrated notes, which are generated using Google Text-to-Speech (`gTTS`).

## Features

- Converts each slide in a PowerPoint presentation to an image.
- Extracts slide notes and converts them into audio using `gTTS`.
- Combines slides and audio into a final video output (`.mp4`).
- Cleans up temporary files (images and audio) after video creation.

## Requirements

- Python 3.7+
- The following Python packages:
  - `gTTS`
  - `python-pptx`
  - `moviepy`
  - `Pillow`
  - `ffmpeg`

## Installation

1. Install FFmpeg:
   - **Ubuntu/Linux**:
     ```bash
     sudo apt update
     sudo apt install ffmpeg
     ```
   - **macOS** (using Homebrew):
     ```bash
     brew install ffmpeg
     ```
   - **Windows**: [Download FFmpeg](https://ffmpeg.org/download.html) and add it to your system PATH.


2. You can install the required dependencies using the following command:

    ```bash
    pip install python-pptx gTTS moviepy Pillow
    ```

## Usage

You can run the script with command-line arguments to specify the PowerPoint file, output video file, and the language for narration.

**language codes:**
- `en` - English
- `de` - Germany
- `fr` - French 

```bash
python main.py --pptx <path_to_presentation> --output <output_file.mp4> --lang <language_code>
```