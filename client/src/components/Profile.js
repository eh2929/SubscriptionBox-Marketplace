// src/components/Profile.js
import React from "react";

function Profile({ user }) {
  if (!user) {
    return <h2>Please log in to view your profile.</h2>;
  }

  return (
    <div className="profile">
      <h2>Your Profile</h2>
      <p>Username: {user.username}</p>
      <p>Email: {user.email}</p>
      <p>Address: {user.address}</p>
      {/* Add more fields as needed */}
    </div>
  );
}

export default Profile;
