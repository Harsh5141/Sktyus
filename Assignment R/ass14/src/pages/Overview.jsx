import { useContext } from "react";
import { DashboardContext } from "../context/DashboardContext";
import Card from "../components/Card";

const Overview = () => {
  const { users, products, loading, error } =
    useContext(DashboardContext);

  if (loading) return <h3>Loading dashboard data...</h3>;
  if (error) return <h3>{error}</h3>;

  return (
    <div className="card-grid">
      <Card title="Total Users" value={users.length} />
      <Card title="Total Products" value={products.length} />
      <Card title="Revenue" value="₹ 45,000" />
    </div>
  );
};

export default Overview;