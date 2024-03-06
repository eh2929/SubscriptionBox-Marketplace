import React, { useState } from "react";

const BoxCreation = () => {
  const [formData, setFormData] = useState({
    name: "",
    description: "",
    price: "",
    // Add more fields as needed
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Add your logic here to handle form submission
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
          <label>Description:</label>
          <textarea
            name="description"
            value={formData.description}
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
        {/* Add more form fields as needed */}
        <button type="submit">Create Box</button>
      </form>
    </div>
  );
};

export default BoxCreation;
