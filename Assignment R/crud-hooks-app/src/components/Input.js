import React, { forwardRef } from "react";

const Input = forwardRef((props, ref) => {
  return <input className="input" ref={ref} {...props} />;
});

export default Input;