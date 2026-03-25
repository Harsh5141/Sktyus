import { useParams } from "react-router-dom";
import { useEffect, useState, useContext } from "react";
import axios from "axios";
import { CartContext } from "../context/CartContext";
import Loader from "../components/Loader";
import Error from "../components/Error";

const ProductDetail = () => {
  const { id } = useParams();
  const { addToCart } = useContext(CartContext);

  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    axios.get(`${process.env.REACT_APP_API_URL}/products/${id}`)
      .then(res => {
        setProduct(res.data);
        setLoading(false);
      })
      .catch(() => {
        setError("Failed to load product");
        setLoading(false);
      });
  }, [id]);

  if (loading) return <Loader />;
  if (error) return <Error message={error} />;

  return (
    <div className="detail">
      <img src={product.image} alt={product.title} width="200" />
      <h2>{product.title}</h2>
      <p>{product.description}</p>
      <h3>₹ {product.price}</h3>
      <button onClick={() => addToCart(product)}>Add to Cart</button>
    </div>
  );
};

export default ProductDetail;