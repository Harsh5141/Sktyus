import { useContext } from "react";
import { CartContext } from "../context/CartContext";

const Cart = () => {
  const { cart, removeFromCart } = useContext(CartContext);

  if (cart.length === 0)
    return <h2 style={{textAlign:"center", marginTop:"50px"}}>Your Cart is Empty</h2>;

  return (
    <div className="cart-container">
      <h2>Cart Items</h2>
      {cart.map(item => (
        <div className="cart-item" key={item.id}>
          <span>{item.title}</span>
          <button className="btn" onClick={() => removeFromCart(item.id)}>
            Remove
          </button>
        </div>
      ))}
    </div>
  );
};

export default Cart;