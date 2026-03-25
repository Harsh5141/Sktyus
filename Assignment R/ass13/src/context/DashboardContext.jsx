import { createContext, useState, useEffect } from "react";
import axios from "axios";

export const DashboardContext = createContext();

export const DashboardProvider = ({ children }) => {
  const [users, setUsers] = useState([]);
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      try {
        const userRes = await axios.get(
          "https://jsonplaceholder.typicode.com/users"
        );

        const productRes = await axios.get(
          "https://fakestoreapi.com/products"
        );

        setUsers(userRes.data);
        setProducts(productRes.data);
        setLoading(false);
      } catch (err) {
        setError("Failed to fetch dashboard data");
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <DashboardContext.Provider
      value={{ users, products, loading, error }}
    >
      {children}
    </DashboardContext.Provider>
  );
};