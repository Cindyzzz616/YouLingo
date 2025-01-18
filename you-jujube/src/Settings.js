import React, { useState, useEffect } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { db, getDoc, setDoc, doc } from "./firebase-config";
import UserForm from "./components/UserForm";
import "./App.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faGear } from "@fortawesome/free-solid-svg-icons";

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
    const newName = prompt("Add an interest");
    if (newName) {
        const updatedData = {...userData, name: newName};
        setUserData(updatedData)
        await handleFormSubmit(updatedData);
    }
  }

  function renderInterests() {
    const container = document.getElementById('interests-container');
    const statusElement = document.getElementById('interest-status');
  
    if (userData.themes && userData.themes.length > 0) {
      statusElement.textContent = '';  // Clear the "Not set" text
      container.innerHTML = ''; // Clear any existing content
  
      userData.themes.forEach(interest => {
        const interestBox = document.createElement('div');
        interestBox.classList.add('interest-box');
        interestBox.textContent = interest;
        container.appendChild(interestBox);
      });
    } else {
      statusElement.textContent = "Not set";  // Show "Not set" if no themes
      container.innerHTML = '';  // Clear any existing content
    }
  }

  if (isLoading) return <p>Loading...</p>;
  if (!isAuthenticated) return <p>Please log in to view your settings.</p>;

  return (
    <div className="settings-container">
    <h1>Settings</h1>
      {userData ? (
        <div>
            <h2>User</h2>
            <p><strong>Name:</strong> {userData.name || user.name || "Not set"}</p>
            <p><strong>Email:</strong> {userData.email || user.email || "Not set"}</p>
            <h3>You're learning <strong>{userData.language || "Not set"}</strong></h3>
            <p><strong>Level:</strong> {userData.level || "Not set"}</p>
            <p><strong>Interests:</strong> {userData.themes || "Not set"}</p>
            <div class="interests-container">
                <div class="interest-box">Sports</div>
                <div class="interest-box">Music</div>
                <div class="interest-box">Traveling</div>
                <div class="interest-box">Technology</div>
            </div>
        </div>
      ) : (
        <p>Loading user information...</p>
      )}
      <button onClick={handleThemeChange}>Add an interest</button>
    </div>
  );
};

export default Settings;
