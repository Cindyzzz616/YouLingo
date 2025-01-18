import React from "react";
import ViewedVideoCard from "./components/ViewedVideoCard";
import placeholderVideos from "./data/placeholderVideos";

const MyVideos = () => {
  return (
    <div style={{ maxWidth: "1200px", margin: "0 auto" }}>
      <div
        className="video-feed"
        style={{
          padding: "20px",
          display: "grid",
          gridTemplateColumns: "repeat(2, 2fr)",
          gap: "20px",
        }}
      >
        {placeholderVideos.map((video) => (
          <ViewedVideoCard key={video.id} video={video} />
        ))}
      </div>
    </div>
  );
};

export default MyVideos;
