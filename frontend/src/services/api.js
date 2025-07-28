import { BASE_URL } from "../config";

export async function fetchFlights(originCity, destinationCity, date) {
  const res = await fetch(
    `${BASE_URL}/api/flights?origin=${encodeURIComponent(
      originCity
    )}&destination=${encodeURIComponent(
      destinationCity
    )}&date=${encodeURIComponent(date)}`
  );
  if (!res.ok) throw new Error("Flights API failed");
  return await res.json();
}

export async function fetchJobs(field, location) {
  const res = await fetch(
    `${BASE_URL}/api/jobs?field=${encodeURIComponent(
      field
    )}&location=${encodeURIComponent(location)}`
  );
  if (!res.ok) throw new Error("Jobs API failed");
  return await res.json();
}

export async function fetchCitySummary(city) {
  const res = await fetch(
    `${BASE_URL}/api/city-summary?city=${encodeURIComponent(city)}`
  );
  if (!res.ok) throw new Error("City Summary API failed");
  return await res.json();
}


export async function fetchTransportationSummary(city) {
  const res = await fetch(
    `${BASE_URL}/api/transportation?city=${encodeURIComponent(city)}`
  );
  if (!res.ok) throw new Error("City Summary API failed");
  return await res.json();
}