// src/components/Cart.js
import React, { useEffect, useState } from "react";
import "./Cart.css";

function Cart() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5555/orders")
      .then((response) => response.json())
      .then((data) => setOrders(data));
  }, []);

  const frequencyFactorMap = {
    Weekly: 4,
    Biweekly: 2,
    Monthly: 1,
  };

  const handleUpdateClick = (orderId, order) => {
    const quantity = document.getElementById(`quantity-${orderId}`).value;
    const frequency = document.getElementById(`frequency-${orderId}`).value;

    const pricePerBox = order.price_per_box;
    const frequencyFactor = frequencyFactorMap[frequency];
    const newTotalMonthlyPrice =
      pricePerBox * parseInt(quantity) * frequencyFactor;

    const url = `http://localhost:5555/orders/${orderId}`;

    fetch(url, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        quantity: parseInt(quantity),
        frequency: frequency,
        total_monthly_price: newTotalMonthlyPrice,
      }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((updatedOrder) => {
        setOrders(
          orders.map((order) => (order.id === orderId ? updatedOrder : order))
        );
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };
  console.log("orders in Cart:", orders);

  const handleDeleteClick = (orderId) => {
    const url = `http://localhost:5555/orders/${orderId}`;

    fetch(url, {
      method: "DELETE",
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        setOrders(orders.filter((order) => order.id !== orderId));
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  return (
    <div className="cart">
      <h2>Active Orders</h2>
      {orders.map((order, index) => (
        <div key={index} className="order-item">
          <h3>Order ID: {order.id}</h3>
          <p>Subscription: {order.subscription.description}</p>
          <label>
            Quantity:
            <input
              type="number"
              defaultValue={order.quantity}
              id={`quantity-${order.id}`}
            />
          </label>
          <label>
            Frequency:
            <select defaultValue={order.frequency} id={`frequency-${order.id}`}>
              <option value="Weekly">Weekly</option>
              <option value="Biweekly">Biweekly</option>
              <option value="Monthly">Monthly</option>
            </select>
          </label>
          <p>Status: {order.status}</p>
          <p>
            Total Monthly Price:{" "}
            {order.total_monthly_price
              ? order.total_monthly_price.toLocaleString("en-US", {
                  style: "currency",
                  currency: "USD",
                })
              : "Not available"}
          </p>
          <button onClick={() => handleUpdateClick(order.id, order)}>
            Update Order
          </button>
          <button onClick={() => handleDeleteClick(order.id)}>
            Delete Order
          </button>
        </div>
      ))}
    </div>
  );
}

export default Cart;
