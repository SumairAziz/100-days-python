# import yt_dlp

# url = "https://youtu.be/wII2JhNACJE?si=CQQg2NJEW6yxS1-E"

# # Options for downloading the best video and audio separately and then merging them
# ydl_opts = {
#     'format': 'bestvideo+bestaudio/best', 
#     'merge_output_format': 'mp4',   
#     'outtmpl': 'downloaded_video3.%(ext)s',
# }

# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download([url])

# print("Video downloaded successfully!")

# import yt_dlp

# def print_available_formats(info):
#     print("Available video formats:")
#     formats = info.get('formats', [])
#     for i, f in enumerate(formats):
#         print(f"{i + 1}. Format ID: {f['format_id']}, Resolution: {f.get('height', 'N/A')}p")

# def get_user_choice(num_options):
#     while True:
#         try:
#             choice = int(input(f"Select a quality (1-{num_options}): "))
#             if 1 <= choice <= num_options:
#                 return choice - 1
#             else:
#                 print(f"Please select a number between 1 and {num_options}.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")

# def main():
#     url = input("Enter the YouTube video URL: ")

#     # Step 1: Get available formats
#     ydl_opts = {
#         'format': 'bestaudio/best',  # Temporarily download best audio to check formats
#         'outtmpl': 'temp_audio.%(ext)s',
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(url, download=False)
#         print_available_formats(info)
        
#         choice = get_user_choice(len(info['formats']))

#         selected_format = info['formats'][choice]['format_id']
#         print(f"You selected format ID: {selected_format}")

#     # Step 2: Download video and audio in selected format
#     ydl_opts = {
#         'format': f'{selected_format}+bestaudio/best',  # Download selected video format and best audio
#         'merge_output_format': 'mp4',  # Merge into MP4 format
#         'outtmpl': 'downloaded_video.%(ext)s',
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])

#     print("Video downloaded successfully!")

# if __name__ == "__main__":
#     main()
import yt_dlp
import re

def print_available_formats(info):
    print("Available video formats:")
    formats = info.get('formats', [])
    for i, f in enumerate(formats):
        print(f"{i + 1}. Format ID: {f['format_id']}, Resolution: {f.get('height', 'N/A')}p")

def get_user_choice(num_options):
    while True:
        try:
            choice = int(input(f"Select a quality (1-{num_options}): "))
            if 1 <= choice <= num_options:
                return choice - 1
            else:
                print(f"Please select a number between 1 and {num_options}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def sanitize_filename(title):
    # Replace invalid characters in filenames with an underscore
    return re.sub(r'[<>:"/\\|?*\x00-\x1F]', '_', title)

def main():
    url = input("Enter the YouTube video URL: ")

    # Step 1: Get available formats
    ydl_opts = {
        'format': 'bestaudio/best',  # Temporarily download best audio to check formats
        'outtmpl': 'temp_audio.%(ext)s',
        'quiet': True  # Suppress output during format extraction
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        print_available_formats(info)
        
        choice = get_user_choice(len(info['formats']))

        selected_format = info['formats'][choice]['format_id']
        print(f"You selected format ID: {selected_format}")

    # Extract video title and sanitize for use in filename
    video_title = info.get('title', 'downloaded_video')
    sanitized_title = sanitize_filename(video_title)
    output_filename = f"{sanitized_title}.%(ext)s"

    # Step 2: Download video and audio in selected format
    ydl_opts = {
        'format': f'{selected_format}+bestaudio/best',  # Download selected video format and best audio
        'merge_output_format': 'mp4',  # Merge into MP4 format
        'outtmpl': output_filename,     # Use the sanitized title as the filename
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Video downloaded successfully!")

if __name__ == "__main__":
    main()
