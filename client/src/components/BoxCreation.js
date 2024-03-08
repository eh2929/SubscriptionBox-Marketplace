import React, { useState } from "react";


function BoxCreation({ onCreateBox }) {
  const [boxData, setBoxData] = useState({
    name: "",
    included_items: "",
    image_url: "",
    price: "",
  });

  const handleChange = (e) => {
    setBoxData({ ...boxData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // First, create the subscription
    fetch("http://localhost:5555/subscriptions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        price_per_box: parseInt(boxData.price),
        name: boxData.name,
      }),
    })
      .then((response) => response.json())
      .then((newSubscription) => {
        // Then, create the box with the new subscription_id
        fetch("http://localhost:5555/boxes", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            name: boxData.name,
            included_items: boxData.included_items,
            image_url: boxData.image_url,
            subscription_id: newSubscription.id,
          }),
        })
          .then((response) => response.json())
          .then((newBox) => {
            onCreateBox(newBox);
          });
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Name:</label>
        <input
          type="text"
          name="name"
          value={boxData.name}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label>Included Items:</label>
        <input
          type="text"
          name="included_items"
          value={boxData.included_items}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label>Image URL:</label>
        <input
          type="text"
          name="image_url"
          value={boxData.image_url}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label>Price Per Box:</label>
        <input
          type="number"
          name="price"
          value={boxData.price}
          onChange={handleChange}
          required
        />
      </div>
      <button type="submit">Create Box</button>
    </form>
  );
}

export default BoxCreation;
