import { db, getDoc, doc } from "../firebase-config"; 

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