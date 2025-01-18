export const getVideos = async (searchQuery) => {
  const API_KEY = process.env.REACT_APP_YOUTUBE_API_KEY;
  const apiUrl = `https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q=${searchQuery}&maxResults=6&key=${API_KEY}`;

  try {
    const response = await fetch(apiUrl);
    const data = await response.json();

    if (data.items && data.items.length > 0) {
      // Map API results to the desired format
      return data.items.map((item, index) => ({
        id: item.id.videoId || `placeholder-${index}`,
        title: item.snippet.title || "No Title",
        channel: item.snippet.channelTitle || "Unknown Channel",
        languageDifficulty: "Beginner", // TODO: Use API to get language difficulty
        description: item.snippet.description || "No Description",
        thumbnail:
          item.snippet.thumbnails?.default?.url ||
          "https://designshack.net/wp-content/uploads/placeholder-image-368x247.png",
      }));
    } else {
      console.error("No videos found.");
      return [];
    }
  } catch (error) {
    console.error("Error fetching videos:", error);
    return [];
  }
};