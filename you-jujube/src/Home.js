import React, { useState, useEffect } from "react";
import VideoCard from "./components/VideoCard";
import { getVideos } from "./services/videoService";
import UserForm from "./components/UserForm";
import { useAuth0 } from '@auth0/auth0-react';
import { db, getDoc, setDoc, doc } from "./firebase-config";
import { checkVideoDifficulty } from "./services/videoDifficultyService";

const Home = () => {
  const [videos, setVideos] = useState({});
  const [userData, setUserData] = useState(null);
  const { user, isAuthenticated, isLoading } = useAuth0();
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchUserData = async () => {
      if (isAuthenticated && user) {
        try {
          const userRef = doc(db, "users", user.sub);
          const userSnap = await getDoc(userRef);
          if (userSnap.exists()) {
            setUserData(userSnap.data());
          } else {
            console.log("No user data found. Please fill the form.");
          }
        } catch (error) {
          console.error("Error fetching user data from Firebase:", error);
        }
      }
    };

    fetchUserData();
  }, [isAuthenticated, user]);

  useEffect(() => {
    const fetchVideos = async () => {
      if (userData?.themes && userData.themes.length > 0) {
        const videoData = {};
        for (const theme of userData.themes) {
          console.log("Fetching videos for theme:", theme);
          const fetchedVideos = await getVideos(theme);
          // await new Promise(resolve => setTimeout(resolve, 1000));
          console.log("Fetched videos:", fetchedVideos);
          for (const video of fetchedVideos) {
            try {
              console.log("Video:", video);
              console.log("Checking video difficulty for video:", video.id);
              video.final_levels = await checkVideoDifficulty(video.id);
              console.log("Video difficulty:", video.final_levels);
            } catch (error) {
              video.final_levels = "unknown";
            }
          }
          videoData[theme] = fetchedVideos;
        }
        setVideos(videoData);
        setLoading(false);
      }
    };

    fetchVideos();
  }, [userData]);

  const handleFormSubmit = async (data) => {
    setUserData(data);
    console.log(data);

    try {
      const userRef = doc(db, "users", user.sub);
      await setDoc(userRef, data, { merge: true });
      console.log("User data saved to Firebase");
    } catch (error) {
      console.error("Error saving user data to Firebase:", error);
    }
  };

  if (!userData) {
    return (
      <div style={{ maxWidth: "1200px", margin: "0 auto" }}>
        <UserForm onSubmit={handleFormSubmit} />
      </div>
    );
  };

  if (isLoading || loading) {
    return <div>Loading ...</div>;
  }

  return (
    <div style={{ maxWidth: "1200px", margin: "0 auto" }}>
      {Object.keys(videos).map((theme) => (
        <div key={theme}>
          <h2 style={{ 
              textTransform: "capitalize",
              margin: "20px 0",
              fontSize: "1.8rem",
              fontWeight: "600",
              color: "#2c3e50",
              borderBottom: "2px solid #3498db",
              paddingBottom: "10px",
              width: "fit-content"
           }}>{theme}</h2>
        <div
          className="video-feed"
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(3, 1fr)",
            gap: "20px",
            padding: "20px",
          }}
        >
        {videos[theme].map((video) => (
          <VideoCard key={video.id} video={video} />
        ))}
        </div>
      </div>
    ))}
  </div>
  );
};

export default Home;
