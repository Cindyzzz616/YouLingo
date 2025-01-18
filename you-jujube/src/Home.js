import React, { useState, useEffect } from "react";
import VideoCard from "./components/VideoCard";
import { getVideos } from "./services/videoService";
import UserForm from "./components/UserForm";
import { useAuth0 } from '@auth0/auth0-react';
import { db, getDoc, setDoc, doc } from "./firebase-config"; 

const Home = () => {
  const [videos, setVideos] = useState([]);
  const [userData, setUserData] = useState(null);
  const { user, isAuthenticated, isLoading } = useAuth0();

  useEffect(() => {
    const fetchVideos = async () => {
      const videoData = await getVideos();
      setVideos(videoData);
    };

    fetchVideos();
  }, []);

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
      <div
        className="video-feed"
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(3, 1fr)",
          gap: "20px",
          padding: "20px",
        }}
      >
        {videos.map((video) => (
          <VideoCard key={video.id} video={video} />
        ))}
      </div>
    </div>
  );
};

export default Home;
