import React, { useState } from "react";

const BoxCreation = ({onCreateBox}) => {
  const [formData, setFormData] = useState({
    name: "",
    included_items: "",
    image_url: "",
    price: ""
    // Add more fields as needed
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
    console.log(e.target.name)
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('/boxes', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
      
    }).then(res => {
      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }
      else {
        return res.json()
      }
    })
      .then(data => {
        onCreateBox(data)})
    
    console.log(formData); // For testing, you can log the form data
  };

  return (
    <div>
      <h2>Create New Subscription Box</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:</label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>included_items:</label>
          <input
            name="included_items"
            value={formData.included_items}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Image URL:</label>
          <input
            type="text"
            name="image_url"
            value={formData.image_url}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Price:</label>
          <input
            type="number"
            name="price"
            value={formData.price}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Subscription ID:</label>
          <input
              type="number"
              name="subscription_id"
              value={formData.subscription_id}
              onChange={handleChange}
          />
        </div>
        {/* Add more form fields as needed */}
        <button type="submit">Create Box</button>
      </form>
    </div>
  );
};

export default BoxCreation;
