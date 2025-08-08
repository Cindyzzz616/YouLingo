import requests
import tiktok_scraper

def download_tiktok_video(video_data, filename="tiktok_video.mp4"):
    # Get the best quality video URL (first in list is usually best)
    # video_url = video_data['video']['PlayAddrStruct']['UrlList'][0]
    video_url = "https://www.tiktok.com/@kickclipper_/video/7533858154757623062"
    
    # Optional: override with highest bitrate from bitrateInfo if needed
    # if 'bitrateInfo' in video_data['video']:
    #     best_quality = max(video_data['video']['bitrateInfo'], key=lambda x: x['Bitrate'])
    #     video_url = best_quality['PlayAddr']['UrlList'][0]

    print(f"Downloading from: {video_url}")

    response = requests.get(video_url, stream=True)

    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Download complete: {filename}")
    else:
        print("Failed to download. Status code:", response.status_code)

# Example usage
# Paste your TikTokApi.video(id='...') dictionary here as `video_info`
video_info = tiktok_scraper.video_dict

download_tiktok_video(video_info)
