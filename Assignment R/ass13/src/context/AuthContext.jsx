import { createContext, useState, useEffect } from "react";

// ✅ MUST export AuthContext
export const AuthContext = createContext(null);

// ✅ MUST export AuthProvider
export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const storedUser = localStorage.getItem("user");
    if (storedUser) {
      setUser(JSON.parse(storedUser));
    }
  }, []);

  const login = async (username, password) => {
    if (username === "admin" && password === "123") {
      const fakeUser = { username: "admin" };
      setUser(fakeUser);
      localStorage.setItem("user", JSON.stringify(fakeUser));
      return true;
    } else {
      return false;
    }
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem("user");
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};