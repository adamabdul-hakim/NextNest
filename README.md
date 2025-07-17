# 🏠 NextNest

**NextNest** helps you explore what life might look like if you moved to another city.  
Enter your current city, desired destination, travel date, and the type of job you’re interested in — and we’ll give you insights to help you plan your next move.

## ✨ Features

- ✅ Cheapest flights – Get real‑time flight data (via Amadeus API) between your chosen cities.  
- ✅ Job opportunities – See available jobs in your desired field and location (via Adzuna API).  
- ✅ AI‑powered insights – Gemini AI provides closest airport codes and a friendly city summary.  
- ✅ Search history – All your searches are stored in an SQLite database and can be viewed or cleared on the History page.  
- ✅ Interactive UI – Built with React and Vite for a clean, modern frontend.

## 🛠️ Tech Stack

- **Frontend:** React + Vite  
- **Backend:** Flask (Python)  
- **Database:** SQLite (for search history)  
- **APIs:** Amadeus, Adzuna, Gemini

## 📂 Project Structure

```text
NextNest/
├── backend/
│   ├── routes/
│   ├── services/
│   ├── app.py
│   └── search_history.db
└── frontend/
    ├── src/pages/
    ├── src/styles/
    └── main.jsx
```

## 🚀 Getting Started

### Prerequisites

- Python 3
- Download Nodejs
- API keys for Amadeus, Adzuna, Gemini

Create a `.env` file in `backend/` with:

```
AMADEUS_API_KEY=your_amadeus_key  
AMADEUS_API_SECRET=your_amadeus_secret  
ADZUNA_APP_ID=your_adzuna_id  
ADZUNA_APP_KEY=your_adzuna_key  
GEMINI_API_KEY=your_gemini_key  
```

---

### Run Backend
```bash
cd backend
pip install -r requirements.txt
python db_setup.py
python app.py
```
Backend runs on: http://127.0.0.1:5001

### Run Frontend
```bash
cd frontend
npm install
npm run dev
```
Frontend runs on http://localhost:5173


## 📌 Pages

- Welcome Page – Introduction to the app  
- Input Page – Enter origin, destination, date, and job role  
- Results Page – See flight, jobs, and city insights  
- History Page – Review or clear past searches

## ✅ Roadmap / Future Ideas

- [ ] Add cost of living data  
- [ ] Improve weather history with monthly averages  
- [ ] Add authentication to save personal favorites  
- [ ] Autocomplete for cities and airports

## 📜 License

MIT License © 2025 NextNest Team
