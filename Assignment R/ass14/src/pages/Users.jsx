import { useContext } from "react";
import { DashboardContext } from "../context/DashboardContext";

const Users = () => {
  const { users, loading, error } =
    useContext(DashboardContext);

  if (loading) return <h3>Loading...</h3>;
  if (error) return <h3>{error}</h3>;

  return (
    <div>
      <h2>Users</h2>
      {users.map((user) => (
        <p key={user.id}>{user.name}</p>
      ))}
    </div>
  );
};

export default Users;