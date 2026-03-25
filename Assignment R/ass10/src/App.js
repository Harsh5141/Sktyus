// src/App.jsx

import React, { useEffect, useState } from "react";
import ProductList from "./components/ProductList";
import { fetchProducts } from "./services/api";
import "./App.css";

function App() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadProducts = async () => {
      try {
        const data = await fetchProducts();
        setProducts(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    loadProducts();
  }, []);

  if (loading) return <h2 className="status">Loading products...</h2>;
  if (error) return <h2 className="status error">{error}</h2>;

  return (
    <div className="app">
      <h1>🛍 Product Store</h1>
      <ProductList products={products} />
    </div>
  );
}

export default App;