// src/components/BoxList.js
// BoxList.js
import React, { useEffect, useState } from "react";
import "./BoxList.css"; // Import the CSS file
import BoxCreation from "./BoxCreation";

function BoxList() {
  const [boxes, setBoxes] = useState([]);
  const [selectedBoxes, setSelectedBoxes] = useState([]); // State to hold the selected boxes
  const [orders, setOrders] = useState([]); // State to hold the orders
  const [subscriptions, setSubscriptions] = useState([]); // State to hold the subscriptions

  useEffect(() => {
    fetch("http://localhost:5555/boxes")
      .then((response) => response.json())
      .then((data) => setBoxes(data));

    fetch("http://localhost:5555/orders")
      .then((response) => response.json())
      .then((data) => setOrders(data));

    fetch("http://localhost:5555/subscriptions")
      .then((response) => response.json())
      .then((data) => setSubscriptions(data));
  }, []);

  const handleAddClick = (box, quantity, frequency) => {
    console.log("handleAddClick is being called"); // Add this line
    console.log(`Type of box.id: ${typeof box.id}`);
    console.log(`Type of quantity: ${typeof quantity}`);
    console.log(`Type of frequency: ${typeof frequency}`);

    setSelectedBoxes((prevBoxes) => [...prevBoxes, box]);
    const url = "http://localhost:5555/orders"; // URL

    const requestBody = {
      box_id: box.id,
      quantity: parseInt(quantity),
      frequency: frequency,
    };

    console.log(requestBody);

    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        box_id: box.id,
        quantity: parseInt(quantity),
        frequency: frequency,
      }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log(data);
        setOrders((prevOrders) => [...prevOrders, data]);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  const onCreateBox = (box) => {
    setBoxes((boxes) => [...boxes, box]);
  };

  return (
    <div>
      <BoxCreation onCreateBox={onCreateBox} />
      <div className="box-grid">
        {boxes.map((box) => {
          const subscription = subscriptions.find(
            (sub) => sub.id === box.subscription_id
          );
          return (
            <div key={box.id} className="box-item">
              <h2>{box.name}</h2>
              <p>{box.included_items}</p>
              {subscription && (
                <p>Price per box: ${subscription.price_per_box}</p>
              )}
              <img src={box.image_url} alt={box.name} />
              <label>
                Quantity:
                <input
                  type="number"
                  defaultValue="1"
                  id={`quantity-${box.id}`}
                />
              </label>
              <label>
                Frequency:
                <select defaultValue="Weekly" id={`frequency-${box.id}`}>
                  <option value="Weekly">Weekly</option>
                  <option value="Biweekly">Biweekly</option>
                  <option value="Monthly">Monthly</option>
                  {/* Add more options as needed */}
                </select>
              </label>
              <button
                onClick={() =>
                  handleAddClick(
                    box,
                    document.getElementById(`quantity-${box.id}`).value,
                    document.getElementById(`frequency-${box.id}`).value
                  )
                }
              >
                Start Subscription!
              </button>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default BoxList;
