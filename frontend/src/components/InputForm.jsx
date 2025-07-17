import { useState } from 'react';
import { Outlet } from 'react-router-dom';
import './App.css';
import axios from "axios";

function InputForm() {
  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  const [fieldOfInterest, setFieldOfInterest] = useState("");
  const[city, setCity] = useState("");
  const [dateOfTravel, setDateOfTravel] = useState("")

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    const formData = {
      name,
      age,
      fieldOfInterest,
      city,
      dateOfTravel,
    };
  
    try {
      const res = await axios.post(`http://localhost:5001/get_weather/${city}`, formData, {
        headers: {
          "Content-Type": "application/json",
        },
      });
  
      console.log("✅ Response from backend:", res.data);
    } catch (error) {
      console.error("🚫 Error submitting form:", error);
    }
  };

  return (
    <>
    <Outlet/>
      <form onSubmit={handleSubmit} className="signin-container">
        <h1>Input Form</h1>

        <input
        value={name} 
        onChange={(e) => setName(e.target.value)}
        placeholder="Name" 
        type="text" 
        />
        <input 
        value={age}
        onChange={(e)=> setAge(e.target.value)} 
        placeholder="Age"
        type="number"
        />
        <input 
        value={fieldOfInterest}
        onChange={(e)=> setFieldOfInterest(e.target.value)} 
        placeholder="Field of Interest"
        type="text"
        />
        <input 
        value={city}
        onChange={(e)=> setCity(e.target.value)} 
        placeholder="City"
        type="text"
        />
        <input
        value={dateOfTravel}
        onChange={(e)=> setDateOfTravel(e.target.value)}
        placeholder="City"
        type="date"
        />
        <button type="submit">
          Submit
        </button>
        </form>
    </>
  )
}

export default InputForm;
