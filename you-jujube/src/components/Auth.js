import React from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { Button } from "reactstrap";

export const LoginButton = () => {
  const { loginWithPopup } = useAuth0();

  return (
    <Button color="primary" onClick={() => loginWithPopup()}>
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
