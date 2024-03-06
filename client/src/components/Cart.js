// src/components/Cart.js
import React from "react";


function Cart({ orders }) {
  console.log("orders in Cart:", orders); // Log the orders
  return (
    <div className="cart">
      <h2>Your Orders</h2>
      {orders.map((order, index) => (
        <div key={index} className="order-item">
          <h3>{order.name}</h3>
          <p>Quantity: {order.quantity}</p>
          <p>Frequency: {order.frequency}</p>
        </div>
      ))}
    </div>
  );
}

export default Cart;
