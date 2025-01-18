import React from "react";
import { Card, CardImg, CardBody, CardTitle, CardText } from "reactstrap";
import { Link } from "react-router-dom";

const VideoCard = ({ video }) => {
  return (
    <Link
    to={`/video/${video.id}`} 
    style={{
      textDecoration: "none", 
      display: "block",      
    }}
    >
    <Card className="video-card">
      <CardImg top width="100%" src={video.thumbnail} alt={video.title} />
      <CardBody>
        <CardTitle tag="h5">{video.title}</CardTitle>
        <CardText>Channel: {video.channel}</CardText>
        <CardText>Language Difficulty: {video.languageDifficulty}</CardText>
        <CardText>{video.description}</CardText>
      </CardBody>
    </Card>
    </Link>
  );
};

export default VideoCard;
