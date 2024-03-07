import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { ToastContainer } from "react-toastify";
import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Header from "./Header";
import Home from "./Home";
import Profile from "./Profile";
import Cart from "./Cart";
import Login from "./Login";
import Logout from "./Logout";
import BoxCreation from "./BoxCreation";
import Signup from "./Signup";


function App() {
  const [orders, setOrders] = useState([]);
  const [user, setUser] = useState(JSON.parse(localStorage.getItem("user")));
  const [currentUser, setCurrentUser] = useState({});

  function handleSignUp(user) {
    setCurrentUser(user);
  }

  const onLogin = (user) => {
    setUser(user);
    setCurrentUser(user);
    localStorage.setItem("user", JSON.stringify(user));
  };

  function handleLogout() {
    localStorage.removeItem("user");
    setUser(null);
    setCurrentUser(null);
    localStorage.removeItem("user");
    toast("You have been logged out");
  }

  useEffect(() => {
    if (user) {
      fetch("http://localhost:5555/orders")
        .then((response) => response.json())
        .then((data) => {
          const userOrders = data.filter((order) => order.user_id === user.id);
          setOrders(userOrders);
        });
    }
  }, [user]);

  useEffect(() => {
    // Load user data from localStorage
    const savedUser = localStorage.getItem("user");

    if (savedUser) {
      // Parse the user data and save it to state
      setUser(JSON.parse(savedUser));
    }
  }, []);

  return (
    <Router>
      <div>
        <ToastContainer />
        <Header />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/profile" render={() => <Profile user={user} />} />
          <Route path="/cart" render={() => <Cart orders={orders} />} />
          <Route path="/login" render={() => <Login onLogin={onLogin} />} />
          <Route path="/create-box" component={BoxCreation} />
          <Route
            path="/signup"
            render={() => <Signup onSignUp={handleSignUp} />}
          />
          <Route
            path="/logout"
            render={() => <Logout onLogout={handleLogout} />}
          />
        </Switch>
      </div>
    </Router>
  );
  }
export default App;
