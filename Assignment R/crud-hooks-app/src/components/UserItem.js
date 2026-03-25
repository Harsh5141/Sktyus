import React from "react";
import Button from "./Button";

function UserItem({ user, deleteUser, setEditUser }) {
  return (
    <div className="item">
      <div>
        <h3>{user.name}</h3>
        <p>{user.email}</p>
      </div>

      <div>
        <Button onClick={() => setEditUser(user)}>Edit</Button>
        <Button onClick={() => deleteUser(user.id)}>Delete</Button>
      </div>
    </div>
  );
}

export default UserItem;