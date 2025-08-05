import React, { useEffect } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { Button } from "reactstrap";
import { db, getDoc, setDoc, doc } from "../firebase-config";

export const LoginButton = () => {
  const {
    loginWithPopup,
    getAccessTokenSilently,
    user,
    isAuthenticated,
  } = useAuth0();

  const addUserToFirebase = async (user) => {
    const userRef = doc(db, "users", user.sub);
    const userSnapshot = await getDoc(userRef);

    if (!userSnapshot.exists()) {
      await setDoc(userRef, {
        name: user.name || "",
        email: user.email || "",
        picture: user.picture || "",
        createdAt: new Date().toISOString(),
        history: {},
      });
      console.log("✅ User added to Firebase!");
    } else {
      console.log("ℹ️ User already exists.");
    }
  };

  const handleLogin = async () => {
    console.log("🔐 Logging in...");
    await loginWithPopup();

    try {
      const token = await getAccessTokenSilently();
      console.log("🔑 Access Token:", token);
    } catch (err) {
      console.error("❌ Failed to get token:", err.message);
    }

    console.log("✅ Logged in.");
  };

  useEffect(() => {
    if (isAuthenticated && user) {
      addUserToFirebase(user);
    }
  }, [isAuthenticated, user]);

  return (
    <Button color="primary" onClick={handleLogin}>
      Log In
    </Button>
  );
};