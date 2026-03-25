import React, { useState } from "react";
import UserCard from "./components/UserCard";
import "./App.css";

function App() {
  const [users, setUsers] = useState([
    { id: 1, name: "Harsh Patel", email: "harsh@gmail.com", isActive: true },
    { id: 2, name: "Amit Shah", email: "amit@gmail.com", isActive: false }
  ]);

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  // Toggle Status
  const toggleStatus = (id) => {
    const updatedUsers = users.map((user) =>
      user.id === id ? { ...user, isActive: !user.isActive } : user
    );
    setUsers(updatedUsers);
  };

  // Remove User
  const removeUser = (id) => {
    const filteredUsers = users.filter((user) => user.id !== id);
    setUsers(filteredUsers);
  };

  // Add User
  const handleSubmit = (e) => {
    e.preventDefault();

    if (!name.trim() || !email.trim()) {
      alert("All fields are required!");
      return;
    }

    const newUser = {
      id: Date.now(),
      name,
      email,
      isActive: true
    };

    setUsers([...users, newUser]);
    setName("");
    setEmail("");
  };

  return (
    <div className="container">
      <h1>User List App</h1>

      <form className="form" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <input
          type="email"
          placeholder="Enter Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <button type="submit">Add User</button>
      </form>

      {users.length === 0 ? (
        <p className="no-users">No users available</p>
      ) : (
        users.map((user) => (
          <UserCard
            key={user.id}
            user={user}
            toggleStatus={toggleStatus}
            removeUser={removeUser}
          />
        ))
      )}
    </div>
  );
}

export default App;