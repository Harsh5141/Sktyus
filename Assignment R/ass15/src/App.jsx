import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Suspense, lazy } from "react";
import Dashboard from "./pages/Dashboard";

const Products = lazy(() => import("./pages/Products"));

function App() {
  return (
    <Router>
      <Suspense fallback={<div className="text-center mt-5">Loading...</div>}>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/products" element={<Products />} />
        </Routes>
      </Suspense>
    </Router>
  );
}

export default App;