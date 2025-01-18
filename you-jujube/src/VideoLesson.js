import React, { useState } from "react";
import { Form, FormGroup, Label, Input, Button } from "reactstrap";
import { useNavigate } from "react-router-dom"; 

const VideoLesson = () => {
  const [videoUrl, setVideoUrl] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const url = formData.get("videoUrl");
    setVideoUrl(url);
    
    const videoId = extractVideoId(url);
    console.log(videoId);

    if (videoId) {
      navigate(`/video/${videoId}`);
    } else {
      console.error("Invalid URL");
    }
  };

  const extractVideoId = (url) => {
    const regex = /(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})/;
    const match = url.match(regex);
    return match ? match[1] : null;
  };

  return (
    <div style={{ maxWidth: "600px", margin: "0 auto", paddingTop: "20px" }}>
      <Form onSubmit={handleSubmit}>
        <FormGroup>
          <Label for="videoUrl">What video would you like to watch?</Label>
          <Input
            type="url"
            name="videoUrl"
            id="videoUrl"
            placeholder="Enter video URL"
            required
            style={{ width: "400px" }}
          />
        </FormGroup>
        <Button type="submit">Submit</Button>
      </Form>
      {videoUrl && (
        <div style={{ marginTop: "20px" }}>
          <h2>Selected Video URL:</h2>
          <p>{videoUrl}</p>
        </div>
      )}
    </div>
  );
};

export default VideoLesson;
