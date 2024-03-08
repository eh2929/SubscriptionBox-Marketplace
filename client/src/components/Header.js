// src/components/Header.js
import React from "react";
import './Header.css';
import { Link } from "react-router-dom";


function Header({}) {
  return (
    <div className="header">
      <h1>Welcome to the Subscription Box Marketplace</h1>
      <nav className="navbar">
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>

          <>
            <li>
              <Link to="/profile">Profile</Link>
            </li>
            <li>
              <Link to="/cart">Cart</Link>
            </li>
            <li>
              <Link to="/logout">Logout</Link>
            </li>
            <li>
              <Link to="/login">Login</Link>
            </li>
            <li>
              <Link to="/signup">Sign Up</Link>
            </li>
          </>
        </ul>
      </nav>
    </div>
  );
}

export default Header;
