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
            setUserData(userDoc.data());
          } else {
            console.log("No user data found in Firebase.");
          }
        } catch (error) {
          console.error("Error fetching user data from Firebase:", error);
        }
      }
    };

    fetchUserData();
  }, [isAuthenticated, user]);

  const handleFormSubmit = async (data) => {
    try {
      const userRef = doc(db, "users", user.sub);
      await setDoc(userRef, data, { merge: true });
      console.log("User data saved to Firebase");
      setUserData(data);
    } catch (error) {
      console.error("Error saving user data to Firebase:", error);
    }
  };

  const handleThemeChange = async () => {
    const newTheme = prompt("Add an interest:");
    if (newTheme) {
      const updatedThemes = userData.themes
        ? [...userData.themes, newTheme]
        : [newTheme];
      const updatedData = { ...userData, themes: updatedThemes };
      setUserData(updatedData);
      await handleFormSubmit(updatedData);
    }
  };

  const handleRemoveTheme = async (index) => {
    if (userData?.themes) {
      const themeToRemove = userData.themes[index];
      const updatedThemes = userData.themes.filter((_, i) => i !== index);
      const updatedData = { ...userData, themes: updatedThemes };
      setUserData(updatedData);

      try {
        const userRef = doc(db, "users", user.sub);
        await updateDoc(userRef, {
          themes: arrayRemove(themeToRemove),
        });
        console.log("Theme removed from Firebase");
      } catch (error) {
        console.error("Error removing theme from Firebase:", error);
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
                <strong>Email:</strong>{" "}
                {userData.email || user.email || "Not set"}
              </p>
              <p>
                <strong>Language:</strong>{" "}
                {userData.language || "Not set"}
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
                        onClick={() => handleRemoveTheme(index)}
                    >
                        {theme} <span style={{ marginLeft: "5px" }}>x</span>
                    </Button>
                  ))
                ) : (
                  <p>No interests set yet.</p>
                )}
              </div>
              <button className="add-interest-btn" onClick={handleThemeChange}>
                Add an interest
              </button>
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
