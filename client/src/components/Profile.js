import React, { useEffect, useState } from "react";

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
    <div className="profile">
      <h2>Your Profile</h2>
      <p>Username: {userInfo.username}</p>
      <p>Email: {userInfo.email}</p>
      <p>Delivery Address: {userInfo.address}</p>
      <p>Full Name: {userInfo.full_name}</p>
      <p>Phone Number: {userInfo.phone_number}</p>
      <label>
        Username:
        <input type="text" defaultValue={userInfo.username} id="username" />
      </label>
      <label>
        Email:
        <input type="email" defaultValue={userInfo.email} id="email" />
      </label>
      <label>
        Address:
        <input type="text" defaultValue={userInfo.address} id="address" />
      </label>
      <label>
        Full Name:
        <input type="text" defaultValue={userInfo.full_name} id="full-name" />
      </label>
      <label>
        Phone Number:
        <input
          type="text"
          defaultValue={userInfo.phone_number}
          id="phone-number"
        />
      </label>
      <button onClick={handleUpdateClick}>Update Profile</button>
    </div>
  );
}

export default Profile;
