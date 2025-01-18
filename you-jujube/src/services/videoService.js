import React, { useState, useEffect } from "react";

export const getVideos = (videoId) => {
  const [video, setVideo] = useState(null);

  useEffect(() => {
    const fetchVideo = async () => {
      const apiKey = process.env.REACT_APP_YOUTUBE_API_KEY;
      const apiUrl = `https://www.googleapis.com/youtube/v3/videos?part=snippet&id=${videoId}&key=${apiKey}`; // paste diff url

      try {
        const response = await fetch(apiUrl);
        const data = await response.json();

        if (data.items && data.items.length > 0) {
          const videoSnippet = data.items[0].snippet;
          setVideo({
            id: videoSnippet.videoId,
            title: videoSnippet.title,
            channel: videoSnippet.channelTitle,
            description: videoSnippet.description,
            thumbnail: videoSnippet.thumbnails.default.url,
          });
        } else {
          console.error("Video not found.");
        }
      } catch (error) {
        console.error("Error fetching video:", error);
      }
    };

    fetchVideo();
  }, [videoId]);

  if (!video) {
    return <p>Loading...</p>;
  }

  return (
    <div>
      <h1>{video.title}</h1>
      <p>Channel: {video.channel}</p>
      <p>{video.description}</p>
      <img src={video.thumbnail} alt={video.title} />
    </div>
  );
};

// export default getVideos;

// export const getVideos = async () => {
//   // Replace with actual API call to fetch videos
//   return [
//     {
//       id: "1",
//       title: "Hi",
//       channel: "Bye",
//       languageDifficulty: "Beginner",
//       description: "Greetings",
//       thumbnail:
//         "https://designshack.net/wp-content/uploads/placeholder-image-368x247.png",
//     },
//     {
//       id: "2",
//       title: "Advanced React Patterns",
//       channel: "ReactPro",
//       languageDifficulty: "Advanced",
//       description: "Deep dive into advanced React patterns.",
//       thumbnail:
//         "https://designshack.net/wp-content/uploads/placeholder-image-368x247.png",
//     },
//     {
//       id: "3",
//       title: "JavaScript Fundamentals",
//       channel: "JSWorld",
//       languageDifficulty: "Beginner",
//       description: "Learn the basics of JavaScript.",
//       thumbnail:
//         "https://designshack.net/wp-content/uploads/placeholder-image-368x247.png",
//     },
//     {
//       id: "4",
//       title: "Node.js Crash Course",
//       channel: "NodeMaster",
//       languageDifficulty: "Intermediate",
//       description: "A comprehensive guide to Node.js.",
//       thumbnail:
//         "https://designshack.net/wp-content/uploads/placeholder-image-368x247.png",
//     },
//     {
//       id: "5",
//       title: "CSS Grid Layout",
//       channel: "CSSWizard",
//       languageDifficulty: "Intermediate",
//       description: "Master CSS Grid layout with this tutorial.",
//       thumbnail:
//         "https://designshack.net/wp-content/uploads/placeholder-image-368x247.png",
//     },
//     {
//       id: "6",
//       title: "CSS Grid Layout",
//       channel: "CSSWizard",
//       languageDifficulty: "Intermediate",
//       description: "Master CSS Grid layout with this tutorial.",
//       thumbnail:
//         "https://designshack.net/wp-content/uploads/placeholder-image-368x247.png",
//     },
//     // Add more video objects as needed
//   ];
// };
