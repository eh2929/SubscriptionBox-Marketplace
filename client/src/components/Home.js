// src/components/Home.js
import React from "react";
import BoxList from "./BoxList";
import SearchBar from "./SearchBar";

function Home() {
  return (
    <div>
      <SearchBar />
      <BoxList />
    </div>
  );
}

export default Home;
