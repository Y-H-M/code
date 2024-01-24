import imageio
import cv2

def extract_frames(input_path, output_path, fps=10):
    # Read the input video
    input_video = imageio.get_reader(input_path)

    # Get video properties
    total_frames = input_video.get_length()
    frame_rate = input_video.get_meta_data()['fps']

    # Calculate frame indices to extract
    frame_indices = [int(i * frame_rate) for i in range(1, total_frames // frame_rate + 1, 5)]

    # Create a VideoWriter object for the output
    output_video = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'VP80'), fps, (input_video.get_meta_data()['size'][1], input_video.get_meta_data()['size'][0]))

    # Extract and write frames to the output video
    for idx in frame_indices:
        frame = input_video.get_data(idx)
        output_video.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    # Release resources
    input_video.close()
    output_video.release()

if __name__ == "__main__":
    input_file = "i.webm"
    output_file = "o.webm"
    fps = 10

    extract_frames(input_file, output_file, fps)
    print("Frames extracted successfully.")
