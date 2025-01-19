import React, { useState, useEffect } from "react";
import ViewedVideoCard from "./components/ViewedVideoCard";
import VideoCard from "./components/VideoCard";
import placeholderVideos from "./data/placeholderVideos";
import { fetchHistory } from "./services/viewCounterService";
import { useAuth0 } from '@auth0/auth0-react';

const MyVideos = () => {
  const { user, isAuthenticated } = useAuth0();
  const [videoHistory, setVideoHistory] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const getHistory = async () => {
      try {
        const historyData = await fetchHistory(user.sub);
        if (historyData) {
          setVideoHistory(historyData);
          console.log("historyData", historyData);
        } else {
          setVideoHistory([]);
        }
      } catch (error) {
        console.error("Error fetching history:", error);
        setVideoHistory([]);
      } finally {
        setLoading(false);
      }
    };

    if (user) {
      getHistory();
    }
  }, [user]);

  if (!isAuthenticated) return <p>Please log in to view your videos.</p>;
  if (loading) return <p>Loading...</p>;

  return (
    <div style={{ maxWidth: "1200px", margin: "0 auto" }}>
      <div
        className="video-feed"
        style={{
          padding: "20px",
          display: "grid",
          gridTemplateColumns: "repeat(3, 2fr)",
          gap: "20px",
        }}
      >
        {videoHistory.map((video) => (
          <VideoCard key={video.id} video={video} />
        ))}
      </div>
    </div>
  );
};

export default MyVideos;
