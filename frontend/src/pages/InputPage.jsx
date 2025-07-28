import { useState } from "react";
import { useNavigate, Outlet } from "react-router-dom";
import "../styles/inputpage.css";

export default function InputPage() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    originCity: "",
    destinationCity: "",
    role: "",
    date: "",
  });

  const [suggestions, setSuggestions] = useState({
    originCity: [],
    destinationCity: [],
    role: []
  });
  
  const handleChange = async (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  
    if (["originCity", "destinationCity", "role"].includes(name) && value.length >= 2) {
      const url = `/api/suggest?field=${encodeURIComponent(name)}&input=${encodeURIComponent(value)}`;
      console.log("🔍 Fetching:", url);
  
      try {
        const res = await fetch(url);
        const text = await res.text();
        console.log("⚠️ Raw server response:", text);
  
        const data = JSON.parse(text);
        console.log("✅ Parsed suggestions:", data);
        setSuggestions((prev) => ({
          ...prev,
          [name]: data.suggestions,
        }));
      } catch (err) {
        console.error("🚨 Suggestion fetch error:", err.message);
      }
    }
  };  

  const handleSubmit = async (e) => {
    e.preventDefault();

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
      <Outlet />
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
            list="originSuggestions"
            required
          />
          <datalist id="originSuggestions">
            {suggestions.originCity.map((s, i) => (
              <option key={i} value={s} />
            ))}
          </datalist>
        </div>

        <div>
          <label>Destination City</label>
          <input
            type="text"
            name="destinationCity"
            value={formData.destinationCity}
            onChange={handleChange}
            placeholder="e.g. Austin"
            list="destinationSuggestions"
            required
          />
          <datalist id="destinationSuggestions">
            {suggestions.destinationCity.map((s, i) => (
              <option key={i} value={s} />
            ))}
          </datalist>
        </div>

        <div>
          <label>Desired Role</label>
          <input
            type="text"
            name="role"
            value={formData.role}
            onChange={handleChange}
            placeholder="e.g. Software Engineer"
            list="roleSuggestions"
          />
          <datalist id="roleSuggestions">
            {suggestions.role.map((s, i) => (
              <option key={i} value={s} />
            ))}
          </datalist>
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
