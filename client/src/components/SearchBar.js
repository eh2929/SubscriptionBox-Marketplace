// src/components/SearchBar.js
import React from "react";

function SearchBar() {
  return (
    <div className='serach-bar-container'>
      <div className="search-bar">
        <input type="text" placeholder="Search subscription boxes" />
        <button>Search</button>
      </div>
    </div>
  );
}

export default SearchBar;
