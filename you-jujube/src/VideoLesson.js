import React, { useState } from "react";
import { Form, FormGroup, Label, Input, Button } from "reactstrap";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const VideoLesson = () => {
  const [videoUrl, setVideoUrl] = useState("");
  const [videoInfo, setVideoInfo] = useState(null);
  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const url = formData.get("videoUrl");
    setVideoUrl(url);

    const videoId = extractVideoId(url);
    console.log(videoId);

    if (videoId) {
      try {
        const response = await axios.post("http://localhost:5000/check_video", {
          youtube_link: url,
        });
        const data = response.data;
        if (data.success) {
          setVideoInfo(data.data);
          console.log(videoInfo);
          // navigate(`/video/${videoId}`);
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

  const extractVideoId = (url) => {
    const regex =
      /(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})/;
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
