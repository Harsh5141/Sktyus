import { Outlet } from "react-router-dom";
import Sidebar from "../components/Sidebar";
import Header from "../components/Header";
import "../styles/dashboard.css";   // ✅ PUT IT HERE

const DashboardLayout = () => {
  return (
    <div className="dashboard">
      <Sidebar />
      <div className="main">
        <Header />
        <div className="content">
          <Outlet />
        </div>
      </div>
    </div>
  );
};

export default DashboardLayout;