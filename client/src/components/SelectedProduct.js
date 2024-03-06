// src/components/SelectedProduct.js
import React from "react";

function SelectedProduct({ product }) {
  return (
    <div>
      <h4>{product.name}</h4>
      <p>{product.description}</p>
      <button>Start Subscription</button>
    </div>
  );
}

export default SelectedProduct;
