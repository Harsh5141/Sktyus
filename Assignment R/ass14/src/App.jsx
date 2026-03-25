import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import DashboardLayout from "./pages/DashboardLayout";
import Overview from "./pages/Overview";
import Products from "./pages/Products";
import Users from "./pages/Users";


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/dashboard/overview" />} />
        <Route path="/dashboard" element={<DashboardLayout />}>
          <Route path="overview" element={<Overview />} />
          <Route path="products" element={<Products />} />
          <Route path="users" element={<Users />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;   // ✅ THIS LINE MUST EXIST