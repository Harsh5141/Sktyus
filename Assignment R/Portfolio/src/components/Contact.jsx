import { useState } from "react";

const Contact = () => {
  const [form, setForm] = useState({ name: "", email: "", message: "" });
  const [error, setError] = useState("");

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!form.name || !form.email || !form.message) {
      setError("⚠️ Please fill all fields");
      return;
    }

    setError("");
    alert("✅ Message Sent Successfully");
  };

  return (
    <section id="contact" className="card">
      <h2>Contact Me</h2>

      <form onSubmit={handleSubmit}>
        {error && <p className="error">{error}</p>}

        <input name="name" placeholder="Name" onChange={handleChange} />
        <input name="email" placeholder="Email" onChange={handleChange} />
        <textarea
          name="message"
          placeholder="Message"
          onChange={handleChange}
        ></textarea>

        <button className="primary">Send Message</button>
      </form>
    </section>
  );
};

export default Contact;
