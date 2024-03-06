// src/components/SelectionContainer.js
import React from "react";
import SelectedProduct from "./SelectedProduct";

function SelectionContainer() {
  // Dummy data for demonstration
  const selectedProduct = {
    name: "Selected Box",
    description: "Description for Selected Box",
  };

  return (
    <div>
      <h3>Selected Box:</h3>
      <SelectedProduct product={selectedProduct} />
    </div>
  );
}

export default SelectionContainer;
