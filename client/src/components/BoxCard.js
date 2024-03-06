// src/components/BoxCard.js
import React from "react";

function BoxCard({ box }) {
  return (
    <div>
      <h4>{box.name}</h4>
      <p>{box.description}</p>
      <button>View Details</button>
    </div>
  );
}

export default BoxCard;
