// src/components/SelectionContainer.js
import React from "react";
import SelectedProduct from "./SelectedProduct";

function SelectionContainer({
  selectedBoxes,
  onRemoveClick,
  onQuantityChange,
  onFrequencyChange,
}) {
  return (
    <div className="selection-container">
      <h2>Selected Products</h2>
      {selectedBoxes.map((box, index) => (
        <SelectedProduct
          key={index}
          box={box}
          onRemoveClick={onRemoveClick}
          onQuantityChange={onQuantityChange}
          onFrequencyChange={onFrequencyChange}
        />
      ))}
    </div>
  );
}

export default SelectionContainer;
