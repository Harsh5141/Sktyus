import { Link } from "react-router-dom";
import { useContext } from "react";
import { CartContext } from "../context/CartContext";

const ProductCard = ({ product }) => {
  const { addToCart } = useContext(CartContext);

  return (
    <div className="card">
      <img src={product.image} alt={product.title} />
      <h4>{product.title}</h4>
      <p>₹ {product.price}</p>

      {/* Buttons Container */}
      <div className="card-buttons">
        <Link to={`/product/${product.id}`} className="btn">
          View Product
        </Link>

        <button 
          className="btn btn-cart"
          onClick={() => addToCart(product)}
        >
          Add to Cart
        </button>
      </div>
    </div>
  );
};

export default ProductCard;