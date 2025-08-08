from TikTokApi import TikTokApi
import asyncio
import os

ms_token = os.environ.get("9agZfRzrUK-2ouAjRG-z8HXRs30AiRL1aP0mN6I6Ciz5YUt6FM6zAKn50Ps_3HQ0RmrU7S2gAvIemwj9upxvEa4HAvSW23Kyil_aBjSrZ10Nk0G4SLOpQFTknenqCo5FnYgwllwNygl_bIQf7VpHqH9X", None) # get your own ms_token from your cookies on tiktok.com
# ms_token = "9agZfRzrUK-2ouAjRG-z8HXRs30AiRL1aP0mN6I6Ciz5YUt6FM6zAKn50Ps_3HQ0RmrU7S2gAvIemwj9upxvEa4HAvSW23Kyil_aBjSrZ10Nk0G4SLOpQFTknenqCo5FnYgwllwNygl_bIQf7VpHqH9X"

async def trending_videos():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, browser=os.getenv("TIKTOK_BROWSER", "chromium"))
        async for video in api.trending.videos(count=1):
            # print(video)
            # print(video.as_dict)
            return video.as_dict

video_dict = asyncio.run(trending_videos())

if __name__ == "__main__":
    print(video_dict)