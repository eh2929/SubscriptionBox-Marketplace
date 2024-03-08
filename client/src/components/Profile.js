import React, { useEffect, useState } from "react";
import "./Profile.css";

function Profile({ user }) {
  const [userInfo, setUserInfo] = useState(null);

  useEffect(() => {
    if (user) {
      fetch(`http://localhost:5555/users/${user.id}`)
        .then((response) => response.json())
        .then((data) => setUserInfo(data));
    }
  }, [user]);

  const handleUpdateClick = () => {
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const address = document.getElementById("address").value;
    const fullName = document.getElementById("full-name").value;
    const phoneNumber = document.getElementById("phone-number").value;

    const url = `http://localhost:5555/users/${user.id}`;

    fetch(url, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username,
        email,
        address,
        full_name: fullName,
        phone_number: phoneNumber,
      }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((updatedUser) => {
        setUserInfo(updatedUser);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  if (!userInfo) {
    return <h2>Please log in to view your profile.</h2>;
  }

  return (
    <div className="profile-container">
      <div className="profile">
        <h2>Your Profile</h2>
        <p>Username: {userInfo.username}</p>
        <p>Email: {userInfo.email}</p>
        <p>Delivery Address: {userInfo.address}</p>
        <p>Full Name: {userInfo.full_name}</p>
        <p>Phone Number: {userInfo.phone_number}</p>
      </div>
      <div>
        <form className="form">  
          <label>Username:</label>
          <input type="text" defaultValue={userInfo.username} id="username" />
          
          <label>Email:</label>
          <input type="email" defaultValue={userInfo.email} id="email" />
          
          <label>Address:</label>
          <input type="text" defaultValue={userInfo.address} id="address" />
          
          <label>Full Name:</label>
          <input type="text" defaultValue={userInfo.full_name} id="full-name" />
          
          <label>Phone Number:</label>
          <input type="text" defaultValue={userInfo.phone_number} id="phone-number" />
          
          <button onClick={handleUpdateClick}>Update Profile</button> 
        </form>
      </div>
    </div>
  );
}

export default Profile;
