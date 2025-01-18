import React, { useState, useEffect } from "react";
import VideoCard from "./components/VideoCard";
import { getVideos } from "./services/videoService";

const Home = () => {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    const fetchVideos = async () => {
      const videoData = await getVideos();
      setVideos(videoData);
    };

    fetchVideos();
  }, []);

  return (
    <div>
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
