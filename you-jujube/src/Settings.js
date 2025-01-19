import React, { useState, useEffect } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { db, getDoc, setDoc, doc } from "./firebase-config";
import { updateDoc, arrayRemove } from "firebase/firestore";
import "./App.css";
import { Button } from "reactstrap";

const Settings = () => {
  const [userData, setUserData] = useState(null);
  const { user, isAuthenticated, isLoading } = useAuth0();

  useEffect(() => {
    const fetchUserData = async () => {
      if (isAuthenticated && user) {
        try {
          const userRef = doc(db, "users", user.sub);
          const userDoc = await getDoc(userRef);
          
          if (userDoc.exists()) {
            const fetchedData = userDoc.data();
            if (!fetchedData.language) {
              await setDoc(userRef, { language: "English" }, { merge: true });
              fetchedData.language = "English";
            }
            if (!fetchedData.level || fetchedData.level === "NA") {
              // Set default level if not already set or is "NA"
              await setDoc(userRef, { level: "A1" }, { merge: true });
              fetchedData.level = "A1";
            }
            setUserData(fetchedData);
          } else {
            // Initialize user data for new users
            const initialData = { language: "English", level: "A1" };
            await setDoc(userRef, initialData);
            setUserData(initialData);
          }          
        } catch (error) {
          console.error("Error fetching user data:", error);
        }
      }
    };

    fetchUserData();
  }, [isAuthenticated, user]);

  const saveUserData = async (data) => {
    try {
      const userRef = doc(db, "users", user.sub);
      await setDoc(userRef, data, { merge: true });
      setUserData(data);
      console.log("User data saved successfully.");
    } catch (error) {
      console.error("Error saving user data:", error);
    }
  };

  const addInterest = async () => {
    const newInterest = prompt("Enter a new interest:");
    if (newInterest) {
      const updatedInterests = userData.themes
        ? [...userData.themes, newInterest]
        : [newInterest];
      const updatedData = { ...userData, themes: updatedInterests };
      await saveUserData(updatedData);
    }
  };

  const removeInterest = async (index) => {
    if (userData?.themes) {
      const themeToRemove = userData.themes[index];
      const updatedThemes = userData.themes.filter((_, i) => i !== index);
      const updatedData = { ...userData, themes: updatedThemes };
      try {
        const userRef = doc(db, "users", user.sub);
        await updateDoc(userRef, {
          themes: arrayRemove(themeToRemove),
        });
        setUserData(updatedData);
        console.log("Interest removed successfully.");
      } catch (error) {
        console.error("Error removing interest:", error);
      }
    }
  };

  if (isLoading) return <p>Loading...</p>;
  if (!isAuthenticated) return <p>Please log in to view your settings.</p>;

  return (
    <div className="settings-page">
      <div className="settings-bar">
        <h1>Settings</h1>
      </div>
      <div className="settings-container">
        {userData ? (
          <div className="settings-content">
            <div className="user-info">
              <h2>User Details</h2>
              <p>
                <strong>Name:</strong> {userData.name || user.name || "Not set"}
              </p>
              <p>
                <strong>Email:</strong> {userData.email || user.email || "Not set"}
              </p>
              <p>
                <strong>Language:</strong> {userData.language || "English"}
              </p>
              <p>
                <strong>Level:</strong> {userData.level || "Not set"}
              </p>
            </div>

            <div className="user-interests">
              <h2>Interests</h2>
              <div className="interests-container">
                {userData.themes && userData.themes.length > 0 ? (
                  userData.themes.map((theme, index) => (
                    <Button
                      key={index}
                      color="primary"
                      outline
                      style={{ marginRight: "5px", marginBottom: "5px" }}
                      onClick={() => removeInterest(index)}
                    >
                      {theme} <span style={{ marginLeft: "5px" }}>x</span>
                    </Button>
                  ))
                ) : (
                  <p>No interests set yet.</p>
                )}
              </div>
              <Button
                className="add-interest-btn"
                color="secondary"
                onClick={addInterest}
              >
                Add an Interest
              </Button>
            </div>
          </div>
        ) : (
          <p>Loading user information...</p>
        )}
      </div>
    </div>
  );
};

export default Settings;
