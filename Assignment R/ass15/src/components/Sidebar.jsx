import { Link } from "react-router-dom";

const Sidebar = () => {
  return (
    <div className="bg-dark text-white p-3 vh-100" style={{ width: "250px" }}>
      <h4>Admin Panel</h4>
      <ul className="nav flex-column mt-4">
        <li className="nav-item">
          <Link className="nav-link text-white" to="/">Dashboard</Link>
        </li>
        <li className="nav-item">
          <Link className="nav-link text-white" to="/products">Products</Link>
        </li>
      </ul>
    </div>
  );
};

export default Sidebar;