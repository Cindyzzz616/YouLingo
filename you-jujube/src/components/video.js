import React, { useEffect, useState } from 'react';

const YouTubeVideos = () => {
  const [videos, setVideos] = useState([]);
  const SEARCH_QUERY = 'funny cats';
  const API_KEY = process.env.REACT_APP_YOUTUBE_API_KEY;

  useEffect(() => {
    // Fetch videos from YouTube API
    fetch(`https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q=${SEARCH_QUERY}&key=${API_KEY}`)
      .then(res => res.json())
      .then(data => {
        setVideos(data.items || []); // Update state with video items
      })
      .catch(error => {
        console.error('Error fetching videos:', error);
      });
  }, []);

  return (
    <div>
      <h1>YouTube Videos</h1>
      <section style={{ display: 'flex', flexWrap: 'wrap', gap: '1rem' }}>
        {videos.map(video => (
          <a
            key='7NbxfrnnWOk'
            target="_blank"
            rel="noopener noreferrer"
            href={`https://www.youtube.com/watch?v=7NbxfrnnWOk`}
            style={{
              textDecoration: 'none',
              color: 'inherit',
              width: '300px',
              boxShadow: '0 4px 8px rgba(0,0,0,0.1)',
              borderRadius: '8px',
              overflow: 'hidden',
              textAlign: 'center',
            }}
          >
            <img
              src={video.snippet.thumbnails?.maxres?.url || video.snippet.thumbnails?.default?.url}
              alt={video.snippet.title}
              style={{ width: '100%' }}
            />
            <h3 style={{ margin: '0.5rem 0' }}>{video.snippet.title}</h3>
          </a>
        ))}
      </section>
    </div>
  );
};

export default YouTubeVideos;