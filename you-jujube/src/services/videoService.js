import { db, addDoc, collection } from "../firebase-config";
import { getDocs, query, where } from "firebase/firestore";

export const getVideos = async (searchQuery) => {
  console.log(`Fetching videos for ${searchQuery}...`);
  const API_KEY = process.env.REACT_APP_YOUTUBE_API_KEY;
  const apiUrl = `https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q=${searchQuery}&videoDuration=short&maxResults=6&key=${API_KEY}`;

  const videosCollection = collection(db, "videos");

  const q = query(
    videosCollection,
    where("theme", "==", searchQuery) 
  );

  try {
    const querySnapshot = await getDocs(q);
    const existingVideos = [];

    querySnapshot.forEach((doc) => {
      existingVideos.push(doc.data()); 
    });

    if (existingVideos.length > 0) {
      console.log(`Found ${existingVideos.length} videos in the database.`);
      return existingVideos;
    }
  
    const response = await fetch(apiUrl);
    const data = await response.json();

    if (data.items && data.items.length > 0) {
      // Map API results to the desired format
      return data.items.map(async (item, index) => {
        const videoData = {
          id: item.id.videoId || `placeholder-${index}`,
          title: item.snippet.title || "No Title",
          channel: item.snippet.channelTitle || "Unknown Channel",
          languageDifficulty: "Beginner", // TODO: Use API to get language difficulty
          description: item.snippet.description || "No Description",
          theme: searchQuery,
          thumbnail:
            item.snippet.thumbnails?.default?.url ||
            "https://designshack.net/wp-content/uploads/placeholder-image-368x247.png",
        };
      
        try {
          // Upload video data to Firestore
          await addDoc(videosCollection, videoData);
          console.log(`Video ${videoData.title} uploaded successfully`);
        } catch (e) {
          console.error("Error adding video: ", e);
        }
      });
    } else {
      console.error("No videos found.");
      return [];
    }
  } catch (error) {
    console.error("Error fetching videos:", error);
    return [];
  }
};