import React from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { Button } from "reactstrap";

// import { initializeApp } from "firebase/app";
// import { getFirestore, doc, getDoc, setDoc } from "firebase/firestore";
import { db, getDoc, setDoc, doc } from "../firebase-config"; 

export const LoginButton = () => {
  const { loginWithPopup, getIdTokenClaims, user, isAuthenticated } = useAuth0();
  console.log("user", user);

  const addUserToFirebase = async (user) => {
    console.log("Adding user to Firebase...");
    console.log("isAuthenticated", isAuthenticated);
    console.log("user", user);
    if (user) {
      const userRef = doc(db, "users", user.sub); 
      const userSnapshot = await getDoc(userRef);

      if (!userSnapshot.exists()) {
        await setDoc(userRef, {
          name: user.name || "",
          email: user.email || "",
          picture: user.picture || "",
          createdAt: new Date().toISOString(),
        });
        console.log("User added to Firebase!");
      } else {
        console.log("User already exists in Firebase.");
      }
    }
  };

  const handleLogin = async () => {
    console.log("logging in");
    await loginWithPopup();
    const userData = await getIdTokenClaims(); 
    console.log("User data:", userData);
    console.log("logged in");
    if (userData) {
      await addUserToFirebase(userData);
    } else {
      console.log("No user data available after login.");
    }
  }

  return (
    <Button color="primary" onClick={() => handleLogin()}>
      Log In
    </Button>
  );
};

export const LogoutButton = () => {
  const { logout } = useAuth0();

  return (
    <Button
      color="danger"
      onClick={() =>
        logout({ logoutParams: { returnTo: window.location.origin } })
      }
    >
      Log Out
    </Button>
  );
};

export const Profile = () => {
  const { user, isAuthenticated, isLoading } = useAuth0();

  if (isLoading) {
    return <div>Loading ...</div>;
  }

  return (
    isAuthenticated && (
      <div className="d-flex align-items-center p-2">
        <img
          src={user.picture}
          alt={user.name}
          style={{ width: "30px", borderRadius: "50%", marginRight: "10px" }}
        />
        <span>{user.name}</span>
      </div>
    )
  );
};
