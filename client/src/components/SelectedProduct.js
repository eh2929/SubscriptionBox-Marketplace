// src/components/SelectedProduct.js
import React from "react";
import "./SelectedProduct.css";

function SelectedProduct({
  box,
  onRemoveClick,
  onQuantityChange,
  onFrequencyChange,
  onCreateOrderClick,
}) {
  // Check if box is defined before trying to access its properties
  return (
    <div className="selected-product">
      <h3>{box.name}</h3>
      <p>{box.included_items}</p>
      <img src={box.image_url} alt={box.name} />
      <label>
        Quantity:
        <input
          type="number"
          min="1"
          value={box.quantity}
          onChange={(e) => onQuantityChange(box.id, e.target.value)}
        />
      </label>
      <label>
        Frequency:
        <select
          value={box.frequency}
          onChange={(e) => onFrequencyChange(box.id, e.target.value)}
        >
          <option value="weekly">Weekly</option>
          <option value="biweekly">Biweekly</option>
          <option value="monthly">Monthly</option>
        </select>
      </label>
      <button onClick={onCreateOrderClick}>Create Order</button>
      <button onClick={() => onRemoveClick(box)}>Start Over</button>
    </div>
  );
}

export default SelectedProduct;
