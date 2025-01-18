import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Card, CardBody, CardTitle, CardText } from 'reactstrap';
import YouTube from 'react-youtube';
import { useParams } from 'react-router-dom';

const LearnVideo = () => {
  const { videoId } = useParams();
  console.log(videoId);

  const transcript = `
    This is the transcript of the video. You can replace this with actual content.
    It will display at the bottom of the video player.
    The transcript helps users follow along with the video.
    You can style this content and make it more interactive later.
  `;

  // YouTube player options
  const opts = {
    height: '390',
    width: '640',
    playerVars: {
      autoplay: 1, // Autoplay the video
    },
  };

  return (
    <Container 
      style={{
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        textAlign: 'center',
      }}>
      <Row>
        <Col xs="12" md="8" className="mx-auto">
          <Card>
            <CardBody>
              <YouTube videoId={videoId} opts={opts} />
              <CardTitle className="mt-3" style={{ fontWeight: 'bold' }}>Language Difficulty Level</CardTitle>
              <CardText>Intermediate</CardText>
              <CardTitle className="mt-4">Transcript</CardTitle>
              <CardText>
                <pre>{transcript}</pre>
              </CardText>
            </CardBody>
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default LearnVideo;
