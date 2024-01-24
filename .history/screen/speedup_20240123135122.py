from moviepy.editor import VideoFileClip

def speed_up_video(input_path, output_path, speed_factor=20):
    # Load the video clip
    clip = VideoFileClip(input_path)
    
    # Speed up the video by the specified factor
    accelerated_clip = clip.fx(VideoFileClipspeedx, speed_factor)
    
    # Write the sped-up video to the output file
    accelerated_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
    
    # Close the video clip
    clip.close()

if __name__ == "__main__":
    # Input and output file paths
    input_video_path = "input_video.mp4"
    output_video_path = "output_video.mp4"
    
    # Speed up the video by 20 times
    speed_up_video(input_video_path, output_video_path)
