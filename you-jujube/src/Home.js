import React, { useState, useEffect } from "react";
import VideoCard from "./components/VideoCard";
import { getVideos } from "./services/videoService";
import UserForm from "./components/UserForm";

const Home = () => {
  const [videos, setVideos] = useState([]);
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    const fetchVideos = async () => {
      const videoData = await getVideos("cats"); // TODO: Replace with user's selected theme
      setVideos(videoData);
    };

    fetchVideos();
  }, []);

  const handleFormSubmit = (data) => {
    setUserData(data);
  };

  if (!userData) {
    return (
      <div style={{ maxWidth: "1200px", margin: "0 auto" }}>
        <UserForm onSubmit={handleFormSubmit} />
      </div>
    );
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
