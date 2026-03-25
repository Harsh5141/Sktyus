import React, { useState } from "react";
import BlogList from "./components/BlogList";
import BlogDetail from "./components/BlogDetail";
import "./App.css";

function App() {
  const [blogs] = useState([
    {
      id: 1,
      title: "Introduction to React",
      author: "Harsh Patel",
      content: "React is a JavaScript library for building user interfaces."
    },
    {
      id: 2,
      title: "Understanding Props",
      author: "Harsh Patel",
      content: "Props allow data to be passed from parent to child components."
    },
    {
      id: 3,
      title: "React State",
      author: "Harsh Patel",
      content: "State is used to manage dynamic data inside a component."
    }
  ]);

  const [selectedBlog, setSelectedBlog] = useState(null);

  return (
    <div className="container">
      <h1>📝 Simple Blog App</h1>

      {selectedBlog ? (
        <BlogDetail blog={selectedBlog} goBack={() => setSelectedBlog(null)} />
      ) : (
        <BlogList blogs={blogs} onSelect={setSelectedBlog} />
      )}
    </div>
  );
}

export default App;