import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Card, CardBody, CardTitle, CardText } from 'reactstrap';
import YouTube from 'react-youtube';
import { useParams } from 'react-router-dom';
import { useAuth0 } from '@auth0/auth0-react';
import { db, getDoc, setDoc, doc } from "./firebase-config"; 
import { updateDoc, increment } from "firebase/firestore";
import { fetchVideoCount } from './services/viewCounterService';

const LearnVideo = () => {
  const { videoId } = useParams();
  console.log(videoId);
  const { user, isAuthenticated, isLoading } = useAuth0();
  const [count, setCount] = useState(0);

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

  const recordHistory = async () => {
    console.log(`Recording video ${videoId} watch history...`);

    try {
      const userRef = doc(db, "users", user.sub); 
      const userDoc = await getDoc(userRef); 

      if (userDoc.exists()) {
        const history = userDoc.data().history || {}; 
  
        if (history[videoId]) {
          history[videoId] += 1;
        } else {
          history[videoId] = 1;
        }
  
        await updateDoc(userRef, {
          history: history, 
        });
  
        console.log(`Video ${videoId} watch history updated. Current count: ${history[videoId]}`);
        setCount(history[videoId]);
      } else {
        console.log("User document does not exist.");
      }
    } catch (error) {
      console.error("Error updating watch history:", error);
    }
  };

  useEffect(() => {
    if (isAuthenticated && user?.sub) {
      const getVideoCount = async () => {
        const videoCount = await fetchVideoCount(user.sub, videoId); // Use the imported function
        setCount(videoCount); // Set the count from the fetched data
      };

      getVideoCount();
    };

  }, [videoId, isAuthenticated, user?.sub]);

  if (isLoading) {
    return <div>Loading...</div>; 
  }

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
              <YouTube 
                videoId={videoId} 
                opts={opts} 
                onEnd={recordHistory}
              />
              <CardText>
                <strong>Language Difficulty Level:</strong> Intermediate
              </CardText>
              {/* TODO: use API for this */}
              <CardText>
                <strong>Times Watched:</strong> {count}
              </CardText>
              <CardTitle className="mt-4" style={{ fontWeight: 'bold' }}>Transcript</CardTitle>
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
