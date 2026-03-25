import React from "react";

const ProductTable = ({ products, deleteProduct }) => {
  return (
    <div className="card p-3 shadow-sm">
      <h5>Product List</h5>

      <table className="table table-bordered mt-3">
        <thead>
          <tr>
            <th>Name</th>
            <th>Price</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          {products.length === 0 ? (
            <tr>
              <td colSpan="3" className="text-center">
                No products added
              </td>
            </tr>
          ) : (
            products.map((product, index) => (
              <tr key={index}>
                <td>{product.name}</td>
                <td>{product.price}</td>
                <td>
                  <button
                    className="btn btn-danger btn-sm"
                    onClick={() => deleteProduct(index)}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
};

export default React.memo(ProductTable);