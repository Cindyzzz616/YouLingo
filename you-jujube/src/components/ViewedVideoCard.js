import React from "react";
import {
  Card,
  CardImg,
  CardBody,
  CardTitle,
  CardText,
  ListGroup,
  ListGroupItem,
} from "reactstrap";

const ViewedVideoCard = ({ video }) => {
  return (
    <Card className="viewed-video-card" style={{ width: "100%" }}>
      <CardImg top width="100%" src={video.thumbnail} alt={video.title} />
      <CardBody>
        <CardTitle tag="h5">{video.title}</CardTitle>
        <CardText>{video.description}</CardText>
        <CardText>Language Difficulty: {video.languageDifficulty}</CardText>
        <CardText>Channel: {video.channel}</CardText>
        <CardText>Difficult Words:</CardText>
        <ListGroup>
          {video.difficultWords.map((word, index) => (
            <ListGroupItem key={index}>{word}</ListGroupItem>
          ))}
        </ListGroup>
      </CardBody>
    </Card>
  );
};

export default ViewedVideoCard;
