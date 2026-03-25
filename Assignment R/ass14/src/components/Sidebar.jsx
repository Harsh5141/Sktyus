import { NavLink } from "react-router-dom";

const Sidebar = () => {
  return (
    <div className="sidebar">
      <h2>Admin Panel</h2>
      <NavLink to="overview">Overview</NavLink>
      <NavLink to="products">Products</NavLink>
      <NavLink to="users">Users</NavLink>
    </div>
  );
};

export default Sidebar;