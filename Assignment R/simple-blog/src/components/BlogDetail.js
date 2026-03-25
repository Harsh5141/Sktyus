import React from "react";

function BlogDetail({ blog, goBack }) {
  return (
    <div className="blog-detail">
      <h2>{blog.title}</h2>
      <p><strong>Author:</strong> {blog.author}</p>
      <p>{blog.content}</p>

      <button onClick={goBack}>Back</button>
    </div>
  );
}

export default BlogDetail;