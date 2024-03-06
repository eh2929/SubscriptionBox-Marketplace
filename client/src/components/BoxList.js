// src/components/BoxList.js
import React from "react";
import BoxCard from "./BoxCard";

function BoxList() {
  // Dummy data for demonstration
  const boxes = [
    { id: 1, name: "Box 1", description: "Description for Box 1" },
    { id: 2, name: "Box 2", description: "Description for Box 2" },
    { id: 3, name: "Box 3", description: "Description for Box 3" },
  ];

  return (
    <div>
      <h3>Available Subscription Boxes:</h3>
      <div>
        {boxes.map((box) => (
          <BoxCard key={box.id} box={box} />
        ))}
      </div>
    </div>
  );
}

export default BoxList;
