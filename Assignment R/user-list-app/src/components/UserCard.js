import React from "react";

const UserCard = ({ user, toggleStatus, removeUser }) => {
  return (
    <div className={`card ${user.isActive ? "active" : "inactive"}`}>
      <h3>{user.name}</h3>
      <p>{user.email}</p>
      <p>Status: {user.isActive ? "Active" : "Inactive"}</p>

      <div className="btn-group">
        <button onClick={() => toggleStatus(user.id)}>
          Toggle Status
        </button>

        <button 
          className="delete-btn"
          onClick={() => removeUser(user.id)}
        >
          Remove
        </button>
      </div>
    </div>
  );
};

export default UserCard;