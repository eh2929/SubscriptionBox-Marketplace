// src/components/Cart.js
import React from "react";

function Cart({ orders }) {
  console.log("orders in Cart:", orders); // Log the orders
  return (
    <div className="cart">
      <h2>Your Orders</h2>
      {orders.map((order, index) => (
        <div key={index} className="order-item">
          <h3>Order ID: {order.id}</h3>
          <p>Subscription: {order.subscription.description}</p>
          <p>Quantity: {order.quantity}</p>
          <p>Frequency: {order.frequency}</p>
          <p>Status: {order.status}</p>
          <p>Total Monthly Price: {order.total_monthly_price.toLocaleString('en-US', { style: 'currency', currency: 'USD' })}</p>
          <p>User: {order.user.username}</p>
          <p>User Address: {order.user.address}</p>
        </div>
      ))}
    </div>
  );
}

export default Cart;