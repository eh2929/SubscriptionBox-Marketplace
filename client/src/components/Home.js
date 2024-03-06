// src/components/Home.js
import React from "react";
import BoxList from "./BoxList";
import SearchBar from "./SearchBar";
import SelectionContainer from "./SelectionContainer";

function Home() {
  return (
    <div>
      <SearchBar />
      <BoxList />
      <SelectionContainer />
    </div>
  );
}

export default Home;
