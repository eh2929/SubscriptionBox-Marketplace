// src/components/BoxList.js
import React, { useEffect, useState } from "react";

function BoxList() {
  const [boxes, setBoxes] = useState([]);

  //fetch to our back-end server
  useEffect(() => {
    fetch("http://localhost:5555/boxes") 
      .then((response) => response.json())
      .then((data) => setBoxes(data));
  }, []);

  return (
    <div>
      {boxes.map((box) => (
        <div key={box.id}>
          <h2>{box.name}</h2>
          <p>{box.included_items}</p>
          {/* Add more box properties here */}
        </div>
      ))}
    </div>
  );
}

export default BoxList;
