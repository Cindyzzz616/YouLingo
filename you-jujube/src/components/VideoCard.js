import React, { useState, useEffect } from "react";
import { Card, CardImg, CardBody, CardTitle, CardText } from "reactstrap";
import { Link } from "react-router-dom";
import { fetchVideoCount } from '../services/viewCounterService';
import { useAuth0 } from '@auth0/auth0-react';
import he from 'he';

const VideoCard = ({ video }) => {
  const { user, isAuthenticated, isLoading } = useAuth0();
  const [count, setCount] = useState(0);
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

  if (isLoading) {
    return <div>Loading...</div>; 
  }

  return (
    <Link
    to={{
      pathname: `/video/${video.id}`,
      state: {
        videoInfo: video,
      },
    }} 
    style={{
      textDecoration: "none", 
      display: "block",      
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
    </Link>
  );
};

export default VideoCard;
