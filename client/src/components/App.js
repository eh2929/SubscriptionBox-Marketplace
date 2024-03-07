// src/components/App.js
// comment
import React, {useEffect, useState} from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Header from "./Header";
import Home from "./Home";
import Profile from "./Profile";
import Cart from "./Cart";
import Login from "./Login";
import Logout from "./Logout";
import BoxCreation from "./BoxCreation";

function App() {
  const [user, setUser] = useState("")

  useEffect(() => {
    fetch("/check_session")
    .then(res => {
      if (res.ok) {
        res.json()
        .then(data => setUser(data))
      }
    })
  }, [])

  function onLogin(user) {
    setUser(user)
  }
  return (
    <Router>
      <div>
        <Header />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/profile" component={Profile} />
          <Route path="/cart" component={Cart} />
          <Route path="/login" component={Login} />
          <Route path="/logout" component={Logout} />
          <Route path="/create-box" component={BoxCreation} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
