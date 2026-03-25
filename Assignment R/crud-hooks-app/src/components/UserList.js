import React from "react";
import UserItem from "./UserItem";

function UserList({ users, deleteUser, setEditUser }) {
  return (
    <div className="list">
      {users.length === 0 && <p>No Users Found</p>}

      {users.map((user) => (
        <UserItem
          key={user.id}
          user={user}
          deleteUser={deleteUser}
          setEditUser={setEditUser}
        />
      ))}
    </div>
  );
}

export default UserList;