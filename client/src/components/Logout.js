// src/components/Logout.js
import React from "react";
import { useHistory } from "react-router-dom";

function Logout({ setUser }) {
  const history = useHistory();

  function handleLogout() {
    console.log("Logout button clicked"); // Log when the logout button is clicked
    // Clear user from state
    setUser(null);
    console.log("User state after logout"); // Log when the user has been set to null
    // Redirect to login page
    history.push("/login");
  }

  return <button onClick={handleLogout}>Logout</button>;
}

export default Logout;
