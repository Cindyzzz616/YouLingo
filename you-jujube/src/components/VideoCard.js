import React from "react";
import { Card, CardImg, CardBody, CardTitle, CardText } from "reactstrap";

const VideoCard = ({ video }) => {
  return (
    <Card className="video-card">
      <CardImg top width="100%" src={video.thumbnail} alt={video.title} />
      <CardBody>
        <CardTitle tag="h5">{video.title}</CardTitle>
        <CardText>Channel: {video.channel}</CardText>
        <CardText>Language Difficulty: {video.languageDifficulty}</CardText>
        <CardText>{video.description}</CardText>
      </CardBody>
    </Card>
  );
};

export default VideoCard;
