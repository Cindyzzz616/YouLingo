import axios from "axios";

export const checkVideoDifficulty = async (videoId) => {
  try {
    const response = await axios.post("http://localhost:5000/check_video", {
      youtube_link: "https://www.youtube.com/watch?v=" + videoId,
    });
    return response.data.data.final_levels;
  } catch (error) {
    console.error("Error fetching video info:", error);
    throw error;
  }
};

// export default { checkVideoDifficulty };
