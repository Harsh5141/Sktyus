import React, { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);
  const LIMIT = 10;

  const increase = () => {
    if (count < LIMIT) {
      setCount(count + 1);
    }
  };

  const decrease = () => {
    if (count > 0) {
      setCount(count - 1);
    }
  };

  const reset = () => {
    setCount(0);
  };

  return (
    <div className="counter-container">
      <h2>Counter Value: {count}</h2>

      {/* Show warning when limit reached */}
      {count === LIMIT && (
        <p className="warning">⚠ Maximum limit reached (10)</p>
      )}

      <div className="buttons">
        {/* Disable Increase when count reaches LIMIT */}
        <button onClick={increase} disabled={count === LIMIT}>
          Increase
        </button>

        {/* Disable Decrease when count is 0 */}
        <button onClick={decrease} disabled={count === 0}>
          Decrease
        </button>

        <button onClick={reset}>Reset</button>
      </div>
    </div>
  );
}

export default Counter;