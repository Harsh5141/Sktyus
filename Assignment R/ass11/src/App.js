// App.jsx

import React, { useEffect, useState } from "react";
import ProductList from "./components/ProductList";
import SearchFilter from "./components/SearchFilter";
import { fetchProducts } from "./services/api";
import "./App.css";

function App() {
  const [products, setProducts] = useState([]);
  const [filteredProducts, setFilteredProducts] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [category, setCategory] = useState("");

  // Fetch Products
  useEffect(() => {
    const loadProducts = async () => {
      const data = await fetchProducts();
      setProducts(data);
      setFilteredProducts(data);
    };
    loadProducts();
  }, []);

  // 🔥 Filtering Logic
  useEffect(() => {
    let updatedProducts = products;

    // Search filter
    if (searchTerm) {
      updatedProducts = updatedProducts.filter((product) =>
        product.title.toLowerCase().includes(searchTerm.toLowerCase())
      );
    }

    // Category filter
    if (category) {
      updatedProducts = updatedProducts.filter(
        (product) => product.category === category
      );
    }

    setFilteredProducts(updatedProducts);
  }, [searchTerm, category, products]);

  return (
    <div className="app">
      <h1>🛍 Product Store</h1>

      <SearchFilter
        searchTerm={searchTerm}
        setSearchTerm={setSearchTerm}
        category={category}
        setCategory={setCategory}
        products={products}
      />

      <ProductList products={filteredProducts} />
    </div>
  );
}

export default App;