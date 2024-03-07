// src/components/BoxList.js
// BoxList.js
import React, { useEffect, useState } from "react";
import "./BoxList.css"; // Import the CSS file
import SelectionContainer from "./SelectionContainer";
import Cart from "./Cart";

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

  const handleAddClick = (box) => {
    setSelectedBoxes([...selectedBoxes, { ...box, quantity: 1, frequency: 1 }]);
  };

  const handleRemoveClick = (boxToRemove) => {
    setSelectedBoxes(selectedBoxes.filter((box) => box.id !== boxToRemove.id));
  };

  const handleQuantityChange = (id, quantity) => {
    setSelectedBoxes(
      selectedBoxes.map((box) => (box.id === id ? { ...box, quantity } : box))
    );
  };

  const handleFrequencyChange = (id, frequency) => {
    setSelectedBoxes(
      selectedBoxes.map((box) => (box.id === id ? { ...box, frequency } : box))
    );
  };

  const handleCreateOrderClick = () => {
    setOrders([...orders, ...selectedBoxes]);
    setSelectedBoxes([]); // Clear the selected boxes
  };

  console.log("orders in BoxList:", orders); // Log the orders
  return (
    <div>
      <div className="box-grid">
        {boxes.map((box) => {
          const subscription = subscriptions.find(
            (sub) => sub.id === box.subscription_id
          );
          return (
            <div key={box.id} className="box-item">
              <h2>{box.name}</h2>
              <img src={box.image_url} alt={box.name} />
              <p>{box.included_items}</p>
              {subscription && (
                <p>Price per box: ${subscription.price_per_box}</p>
              )}
              <button onClick={() => handleAddClick(box)}>
                Start Subscription!
              </button>
            </div>
          );
        })}
      </div>
      <SelectionContainer
        selectedBoxes={selectedBoxes}
        onRemoveClick={handleRemoveClick}
        onQuantityChange={handleQuantityChange}
        onFrequencyChange={handleFrequencyChange}
        onCreateOrderClick={handleCreateOrderClick}
      />
      <button onClick={handleCreateOrderClick}>Create Order</button>
      
    </div>
  );
}

export default BoxList;
