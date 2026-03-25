import { useState, useCallback } from "react";
import Sidebar from "../components/Sidebar";
import Header from "../components/Header";
import ProductForm from "../components/ProductForm";
import ProductTable from "../components/ProductTable";

const Products = () => {
  const [products, setProducts] = useState([]);

  // Add Product
  const addProduct = useCallback((product) => {
    setProducts((prev) => [...prev, product]);
  }, []);

  // Delete Product
  const deleteProduct = useCallback((index) => {
    setProducts((prev) => prev.filter((_, i) => i !== index));
  }, []);

  return (
    <div className="d-flex">
      <Sidebar />
      <div className="flex-grow-1">
        <Header />
        <div className="container mt-4">
          <ProductForm addProduct={addProduct} />
          <ProductTable
            products={products}
            deleteProduct={deleteProduct}
          />
        </div>
      </div>
    </div>
  );
};

export default Products;