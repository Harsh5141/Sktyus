import React from "react";

function BlogCard({ blog, onSelect }) {
  return (
    <div className="blog-card" onClick={() => onSelect(blog)}>
      <h2>{blog.title}</h2>
      <p>Author: {blog.author}</p>
    </div>
  );
}

export default BlogCard;