// components/SearchFilter.jsx

import React, { useEffect, useRef } from "react";

const SearchFilter = ({
  searchTerm,
  setSearchTerm,
  category,
  setCategory,
  products,
}) => {
  const inputRef = useRef(null);

  // Auto focus input
  useEffect(() => {
    inputRef.current.focus();
  }, []);

  // Get unique categories
  const categories = [...new Set(products.map((p) => p.category))];

  return (
    <div className="search-filter">
      <input
        ref={inputRef}
        type="text"
        placeholder="Search product..."
        value={searchTerm}            // ✅ Controlled
        onChange={(e) => setSearchTerm(e.target.value)}
      />

      <select
        value={category}              // ✅ Controlled
        onChange={(e) => setCategory(e.target.value)}
      >
        <option value="">All Categories</option>
        {categories.map((cat, index) => (
          <option key={index} value={cat}>
            {cat}
          </option>
        ))}
      </select>
    </div>
  );
};

export default SearchFilter;