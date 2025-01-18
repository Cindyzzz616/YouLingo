import React, { useState, useEffect } from "react";
import VideoCard from "./components/VideoCard";
import { getVideos } from "./services/videoService";
import UserForm from "./components/UserForm";
import { useAuth0 } from '@auth0/auth0-react';
import { db, getDoc, setDoc, doc } from "./firebase-config"; 

const Home = () => {
  const [videos, setVideos] = useState({});
  const [userData, setUserData] = useState(null);
  const { user, isAuthenticated, isLoading } = useAuth0();

  useEffect(() => {
    const fetchVideos = async () => {
      if (userData?.themes && userData.themes.length > 0) {
        const videoData = {};
        for (const theme of userData.themes) {
          const fetchedVideos = await getVideos(theme);
          videoData[theme] = fetchedVideos;
        }
        setVideos(videoData);
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

  if (isLoading) {
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
