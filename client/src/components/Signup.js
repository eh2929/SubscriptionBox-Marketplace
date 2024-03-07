// src/components/SignUp.js
import React, { useState } from "react";
import { useHistory } from "react-router-dom";

function SignUp({ onSignUp }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const history = useHistory();

  function handleSubmit(e) {
    e.preventDefault();
    console.log("Username:", username); // This will be the username the user entered
    console.log("Password:", password); // This will be the password the user entered
    fetch("http://127.0.0.1:5555/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    })
      .then((r) => r.json())
      .then((user) => {
        console.log("User state after signup:", user);
        onSignUp(user);
      });
    history.push("/login");
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
      />
      <button type="submit">Sign Up</button>
    </form>
  );
}

export default SignUp;
