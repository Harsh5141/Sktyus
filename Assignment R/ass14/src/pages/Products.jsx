import { useContext } from "react";
import { DashboardContext } from "../context/DashboardContext";

const Products = () => {
  const { products, loading, error } =
    useContext(DashboardContext);

  if (loading) return <h3>Loading...</h3>;
  if (error) return <h3>{error}</h3>;

  return (
    <div>
      <h2>Products</h2>
      {products.slice(0, 5).map((product) => (
        <p key={product.id}>{product.title}</p>
      ))}
    </div>
  );
};

export default Products;