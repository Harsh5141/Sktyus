import React, { useState, useEffect, useRef } from "react";
import Button from "./Button";
import Input from "./Input";

function UserForm({ addUser, updateUser, editUser }) {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  const nameRef = useRef(); // 🔹 Uncontrolled + focus

  // Focus input on mount
  useEffect(() => {
    nameRef.current.focus();
  }, []);

  // When editUser changes
  useEffect(() => {
    if (editUser) {
      setName(editUser.name);
      setEmail(editUser.email);
    }
  }, [editUser]);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!name || !email) {
      alert("All fields required");
      return;
    }

    if (editUser) {
      updateUser({ id: editUser.id, name, email });
    } else {
      addUser({ name, email });
    }

    setName("");
    setEmail("");
  };

  return (
    <form onSubmit={handleSubmit} className="form">
      <Input
        ref={nameRef}
        placeholder="Enter Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <Input
        placeholder="Enter Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <Button type="submit">
        {editUser ? "Update" : "Add"} User
      </Button>
    </form>
  );
}

export default UserForm;