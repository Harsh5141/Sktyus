import Sidebar from "../components/Sidebar";
import Header from "../components/Header";
import Card from "../components/Card";

const Dashboard = () => {
  return (
    <div className="d-flex">
      <Sidebar />
      <div className="flex-grow-1">
        <Header />
        <div className="container mt-4">
          <div className="row">
            <div className="col-md-4">
              <Card title="Total Products" value="20" />
            </div>
            <div className="col-md-4">
              <Card title="Total Users" value="10" />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;