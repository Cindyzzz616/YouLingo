import React, { useState } from "react";
import { Form, FormGroup, Label, Input, Button } from "reactstrap";

const VideoLesson = () => {
  const [videoUrl, setVideoUrl] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    setVideoUrl(formData.get("videoUrl"));
    console.log("Video URL:", videoUrl);
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
