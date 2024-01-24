from moviepy.editor import VideoFileClip
from moviepy.video.fx.speedx import speedx

def speed_up_video(input_path, output_path, speed_factor=10):
    # Load the video clip
    clip = VideoFileClip(input_path)
    
    # Speed up the video by the specified factor using speedx
    accelerated_clip = clip.fx(speedx, speed_factor)
    
    # Write the sped-up video to the output file
    accelerated_clip.write_videofile(output_path, codec='libvpx', audio_codec='libvorbis')
    
    # Close the video clip
    clip.close()

if __name__ == "__main__":
    # Input and output file paths
    input_video_path = "i.webm"
    output_video_path = "o.webm"
    
    # Speed up the video by 20 times
    speed_up_video(input_video_path, output_video_path)
