import { useForm } from "react-hook-form";

const ProductForm = ({ addProduct }) => {
  const { register, handleSubmit, formState: { errors }, reset } = useForm();

  const onSubmit = (data) => {
    addProduct(data);
    reset();
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="card p-4 mb-4">
      <h5>Add Product</h5>

      <input
        className="form-control mb-2"
        placeholder="Product Name"
        {...register("name", { required: "Name is required" })}
      />
      {errors.name && <small className="text-danger">{errors.name.message}</small>}

      <input
        type="number"
        className="form-control mb-2"
        placeholder="Price"
        {...register("price", { required: "Price is required" })}
      />
      {errors.price && <small className="text-danger">{errors.price.message}</small>}

      <button className="btn btn-primary mt-2">Add</button>
    </form>
  );
};

export default ProductForm;