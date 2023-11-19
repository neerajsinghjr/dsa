import os
from moviepy.editor import VideoFileClip



def convert_video(input_path, output_path, codec='libx264', audio_codec='aac', bitrate='5000k', preset='medium'):
    """
    Convert a video from one format to another and reduce file size without changing resolution.

    Parameters:
    - input_path (str): Path to the input video file.
    - output_path (str): Path to the output video file.
    - codec (str): Video codec to use (default is 'libx264').
    - audio_codec (str): Audio codec to use (default is 'aac').
    - bitrate (str): Video bitrate for output file (default is '5000k').
    - preset (str): Preset for encoding speed and quality (default is 'medium').
    """
    # Load the video clip
    video_clip = VideoFileClip(input_path)

    # Write the video to the output file with specified codecs, bitrate, and preset
    video_clip.write_videofile(output_path, codec=codec, audio_codec=audio_codec, bitrate=bitrate, preset=preset)


if __name__ == "__main__":
    folder_path = "/media/neeraj/bin/.aevil/hongkongdoll"

    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Print the list of files
    for file in os.listdir(folder_path):
        filepath = os.path.join(folder_path, file)
        if os.path.isfile(filepath):
            try:
                count = 1
                output = f"/home/neeraj/Downloads/hongkongdoll/{file}"
                convert_video(filepath, output)
                count += 1
            except Exception as ex:
                import traceback
                print("Erorr : ", traceback.format_exc())
                break