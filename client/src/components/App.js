// src/components/App.js
import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import Header from "./Header";
import Home from "./Home";
import Profile from "./Profile";
import Cart from "./Cart";
import Login from "./Login";
import Logout from "./Logout";
import BoxCreation from "./BoxCreation";

function App() {
  return (
    <Router>
      <div>
        <Header />
        <Route path="/" exact component={Home} />
        <Route path="/profile" component={Profile} />
        <Route path="/cart" component={Cart} />
        <Route path="/login" component={Login} />
        <Route path="/logout" component={Logout} />
        <Route path="/create-box" component={BoxCreation} />
      </div>
    </Router>
  );
}

export default App;
