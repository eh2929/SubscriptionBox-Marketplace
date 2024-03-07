// Logout.js
import React from "react";

function Logout({ onLogout }) {
  const handleLogoutClick = () => {
    onLogout();
    // Redirect the user to the login page after logging out
    window.location.href = "/login";
  };

  return <button onClick={handleLogoutClick}>Logout</button>;
}

export default Logout;
