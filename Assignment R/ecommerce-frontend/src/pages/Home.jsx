import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div className="container">
      <h1>Welcome to My Store</h1>
      <Link to="/products" className="btn">View Products</Link>
    </div>
  );
};

export default Home;