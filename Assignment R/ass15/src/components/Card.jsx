import React from "react";

const Card = ({ title, value }) => {
  return (
    <div className="card p-3 shadow-sm">
      <h5>{title}</h5>
      <h3>{value}</h3>
    </div>
  );
};

export default React.memo(Card);