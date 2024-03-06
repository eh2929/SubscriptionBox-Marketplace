// src/components/Home.js
import React from "react";
import BoxList from "./BoxList";
import SearchBar from "./SearchBar";
import SelectionContainer from "./SelectionContainer";

function Home() {
  return (
    <div>
      <h2>Welcome to our Subscription Box Marketplace!</h2>
      <SearchBar />
      <BoxList />
      <SelectionContainer />
    </div>
  );
}

export default Home;
