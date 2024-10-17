from moviepy.editor import VideoFileClip, CompositeVideoClip
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def combine_videos():
    presentation_video = VideoFileClip('presentation_video.mp4')
    duration = 0
    audio_videos = []
    for i in range(2):
        try:
            video_clip = VideoFileClip(f'{i}/output_v{i}.mp4')
            if video_clip.size[0] > 0 and video_clip.size[1] > 0:
                audio_videos.append(video_clip)
            else:
                logger.error(f'Video {i} has invalid size: {video_clip.size}')
        except Exception as e:
            logger.error(f'Error processing video {i}: {e}')


    for i, video in enumerate(audio_videos):
        video = video.set_position(('left', 'bottom')).set_start(duration).set_duration(video.duration)
        duration += video.duration
        presentation_video = CompositeVideoClip([presentation_video, video])

    presentation_video.write_videofile('final_presentation_video.mp4', fps=24)

if __name__ == '__main__':
    combine_videos()
