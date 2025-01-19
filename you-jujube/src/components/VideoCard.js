import React, { useState, useEffect } from "react";
import { Card, CardImg, CardBody, CardTitle, CardText } from "reactstrap";
import { Link } from "react-router-dom";
import { fetchVideoCount } from '../services/viewCounterService';
import { useAuth0 } from '@auth0/auth0-react';
import { useNavigate } from "react-router-dom";
import axios from "axios";
import he from 'he';

const VideoCard = ({ video }) => {
  const { user, isAuthenticated, isLoading } = useAuth0();
  const [count, setCount] = useState(0);
  const [videoInfo, setVideoInfo] = useState(null);
  const navigate = useNavigate();
  console.log("video", video);

  const convertToCEFR = (level) => {
    const intLevel = parseInt(level, 10);
    const levels = ["A1", "A2", "B1", "B2", "C1", "C2", "Unknown"];
    return levels[intLevel] || "Unknown";
  };  

  useEffect(() => {
    if (isAuthenticated && user?.sub) {
      const getVideoCount = async () => {
        const videoCount = await fetchVideoCount(user.sub, video.id); // Use the imported function
        setCount(videoCount); // Set the count from the fetched data
      };

      getVideoCount();
    };

  }, [video.id, isAuthenticated, user?.sub]);

  const handleVideoClick = async (video) => {
    const videoId = video.id;
    if (videoId) {
      try {
        const response = await axios.post("http://localhost:5000/check_video", {
          youtube_link: "https://www.youtube.com/watch?v=" + videoId,
        });
        const data = response.data;
        if (data.success) {
          setVideoInfo(data.data);
          console.log(videoInfo);
          navigate(`/video/${videoId}`, { state: { videoInfo: data.data } });
        } else {
          console.error("Error fetching video info:", data.error);
        }
      } catch (error) {
        if (error.response) {
          // The request was made and the server responded with a status code
          // that falls out of the range of 2xx
          console.error("Response error:", error.response.data);
        } else if (error.request) {
          // The request was made but no response was received
          console.error("Request error:", error.request);
        } else {
          // Something happened in setting up the request that triggered an Error
          console.error("Error:", error.message);
        }
        console.error("Config error:", error.config);
      }
    } else {
      console.error("Invalid URL");
    }
  };

  if (isLoading) {
    return <div>Loading...</div>; 
  }

  return (
  //   <Link
  //   to={{
  //     pathname: `/video/${video.id}`,
  //     state: { videoInfo: video }
  //   }}
  //   style={{
  //     textDecoration: "none",
  //     display: "block",
  //   }}
  // >
    <button
    onClick={() => handleVideoClick(video)}
    style={{
      background: "none",
      border: "none",
      padding: 0,
      cursor: "pointer",
      display: "block",
      textDecoration: "none",
    }}
  >
    <Card 
      className="video-card"
      style={{
        backgroundColor: count > 0 ? "#FFF9C4": "white", // Set the background color conditionally
      }}
    >
      <CardImg top width="100%" src={video.thumbnail} alt={video.title} />
      <CardBody>  
        <CardTitle tag="h5">{he.decode(video.title)}</CardTitle>
        <CardText>Channel: {video.channel}</CardText>
        <CardText>Language Difficulty: {convertToCEFR(video.final_levels.general_level)}</CardText>
        <CardText>Times Watched: {count}</CardText>
        <CardText><i>{video.description}</i></CardText>
      </CardBody>
    </Card>
    </button>
  );
};

export default VideoCard;
