import { db, getDoc, doc } from "../firebase-config"; 
import { where, collection, query, getDocs } from "firebase/firestore";

export const fetchVideoCount = async (userId, videoId) => {
    try {
      const userRef = doc(db, 'users', userId);
      const userDoc = await getDoc(userRef);
      
      if (userDoc.exists()) {
        const history = userDoc.data().history || {};
        return history[videoId] || 0; 
      } else {
        console.log('User document does not exist.');
        return 0;
      }
    } catch (error) {
      console.error('Error fetching watch history:', error);
      return 0;
    }
};

export const fetchHistory = async (userId) => {
    try {
        const userRef = doc(db, 'users', userId);
        const userDoc = await getDoc(userRef);
    
        if (userDoc.exists()) {
        const history = userDoc.data().history || {};
        const videoIds = Object.keys(history); // Extract video IDs from the history object
    
        if (videoIds.length === 0) {
            console.log('No videos watched.');
            return [];
        }
    
        // Fetch video details for each video in history
        const videoDataPromises = videoIds.map(async (videoId) => {
            const videoRef = collection(db, 'video');
            const q = query(videoRef, where('videoId', '==', videoId)); // Assuming 'id' is the field for video ID
            const querySnapshot = await getDocs(q);
            
            if (!querySnapshot.empty) {
            const videoDoc = querySnapshot.docs[0]; // Assuming only one match
            const videoData = videoDoc.data(); // Get video data
    
            // Return video data in the desired format
            return {
                videoId: videoData.videoId,
                title: videoData.title,
                description: videoData.description,
                final_levels: videoData.final_levels,
                channel: videoData.channel,
                thumbnail: videoData.thumbnail || "https://designshack.net/wp-content/uploads/placeholder-image-368x247.png", // Fallback thumbnail
                difficultWords: videoData.difficultWords || [], // Assuming 'difficultWords' exists in the video data
                watchedCount: history[videoId], // Add watch count from history
            };
            } else {
            console.log(`Video with ID ${videoId} not found in 'video' collection.`);
            return null; // Handle case where video is not found
            }
        });
    
        const videoData = await Promise.all(videoDataPromises);
        return videoData.filter(video => video !== null); // Remove null results
    
        } else {
        console.log('User document does not exist.');
        return null;
        }
    } catch (error) {
        console.error('Error fetching watch history:', error);
        return null;
    }
};