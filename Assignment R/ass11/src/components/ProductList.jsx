// components/ProductList.jsx

import React from "react";
import ProductCard from "./ProductCard";

const ProductList = ({ products }) => {
  if (products.length === 0) {
    return <h2>No products found</h2>;
  }

  return (
    <div className="product-list">
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
};

export default ProductList;