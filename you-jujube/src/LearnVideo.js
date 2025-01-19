import React, { useState, useEffect } from "react";
import {
  Container,
  Row,
  Col,
  Card,
  CardBody,
  CardTitle,
  CardText,
  Form,
  FormGroup,
  Label,
  Input,
  Button,
} from "reactstrap";
import YouTube from "react-youtube";
import { useParams, useLocation } from "react-router-dom";
import { useAuth0 } from "@auth0/auth0-react";
import { db, getDoc, setDoc, doc } from "./firebase-config";
import { updateDoc, increment } from "firebase/firestore";
import { fetchVideoCount } from "./services/viewCounterService";
import { getSecondHalfOfTranscript } from "./utils";
import axios from "axios";

const LearnVideo = () => {
  const { videoId } = useParams();
  const location = useLocation();
  const { videoInfo } = location.state || {};
  const { user, isAuthenticated, isLoading } = useAuth0();
  const [count, setCount] = useState(0);
  const [questions, setQuestions] = useState([]);
  const [responses, setResponses] = useState({});

  const transcript = videoInfo?.transcripts || "";
  const secondHalfTranscript = getSecondHalfOfTranscript(transcript);

  // YouTube player options
  const opts = {
    height: "390",
    width: "640",
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

        console.log(
          `Video ${videoId} watch history updated. Current count: ${history[videoId]}`
        );
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
    }
  }, [videoId, isAuthenticated, user?.sub]);

  useEffect(() => {
    const fetchQuestions = async () => {
      try {
        const response = await axios.post(
          "http://localhost:5000/find_questions",
          {
            transcript: secondHalfTranscript,
          }
        );
        setQuestions(response.data.questions.split("\n"));
      } catch (error) {
        console.error("Error fetching questions:", error);
      }
    };

    if (secondHalfTranscript) {
      fetchQuestions();
    }
  }, [secondHalfTranscript]);

  const handleResponseChange = (index, value) => {
    setResponses((prevResponses) => ({
      ...prevResponses,
      [index]: value,
    }));
  };

  const handleSubmit = async () => {
    try {
      const userRef = doc(db, "users", user.sub);
      const userDoc = await getDoc(userRef);

      if (userDoc.exists()) {
        const userData = userDoc.data();
        const videoResponses = userData.videoResponses || {};

        videoResponses[videoId] = {
          questions: questions,
          responses: responses,
        };

        await updateDoc(userRef, {
          videoResponses: videoResponses,
        });

        console.log("Responses saved successfully.");
      } else {
        console.log("User document does not exist.");
      }
    } catch (error) {
      console.error("Error saving responses:", error);
    }
  };

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <Container
      style={{
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        textAlign: "center",
      }}
    >
      <Row>
        <Col xs="12" md="8" className="mx-auto">
          <Card>
            <CardBody style={{ textAlign: "left" }}>
              <YouTube videoId={videoId} opts={opts} onEnd={recordHistory} />
              <CardText>
                <strong>Final Levels:</strong>
                {JSON.stringify(videoInfo?.final_levels)}
              </CardText>
              {/* TODO: use API for this */}
              <CardText>
                <strong>Times Watched:</strong> {count}
              </CardText>
              <CardTitle className="mt-4" style={{ fontWeight: "bold" }}>
                Transcript
              </CardTitle>
              <CardText>
                <pre>{secondHalfTranscript}</pre>
              </CardText>
              <CardTitle className="mt-4" style={{ fontWeight: "bold" }}>
                Questions
              </CardTitle>
              <Form>
                {questions.map((question, index) => (
                  <FormGroup key={index}>
                    <Label for={`question-${index}`}>{question}</Label>
                    <Input
                      type="text"
                      name={`question-${index}`}
                      id={`question-${index}`}
                      value={responses[index] || ""}
                      onChange={(e) =>
                        handleResponseChange(index, e.target.value)
                      }
                    />
                  </FormGroup>
                ))}
                <Button color="primary" onClick={handleSubmit}>
                  Submit
                </Button>
              </Form>
            </CardBody>
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default LearnVideo;
