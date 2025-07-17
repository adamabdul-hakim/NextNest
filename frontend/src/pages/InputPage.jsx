import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function InputPage() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    originCity: "",
    destinationCity: "",
    role: "",
    date: "",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    await fetch("http://127.0.0.1:5001/api/history", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        origin_city: formData.originCity,
        destination_city: formData.destinationCity,
        role: formData.role,
        travel_date: formData.date,
      }),
    });

    navigate("/results", {
      state: {
        originCity: formData.originCity,
        destinationCity: formData.destinationCity,
        date: formData.date,
        field: formData.role,
      },
    });
  };

  return (
    <div className="input-container">
      <h1>Tell us about your move</h1>
      <form onSubmit={handleSubmit} className="input-form">
        <div>
          <label>Origin City</label>
          <input
            type="text"
            name="originCity"
            value={formData.originCity}
            onChange={handleChange}
            placeholder="e.g. Los Angeles"
            required
          />
        </div>
        <div>
          <label>Destination City</label>
          <input
            type="text"
            name="destinationCity"
            value={formData.destinationCity}
            onChange={handleChange}
            placeholder="e.g. Austin"
            required
          />
        </div>
        <div>
          <label>Desired Role</label>
          <input
            type="text"
            name="role"
            value={formData.role}
            onChange={handleChange}
            placeholder="e.g. Software Engineer"
          />
        </div>
        <div>
          <label>Planned Travel Date</label>
          <input
            type="date"
            name="date"
            value={formData.date}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">See Results</button>
      </form>
    </div>
  );
}
