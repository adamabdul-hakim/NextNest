# 🏠 NextNest

**NextNest** helps you explore what life might look like if you moved to another city.  
Enter your current city, destination, travel date, and job field — we’ll return real insights to help you plan your next move.

---

## ✨ Features

- ✅ **Flight prices** – Get real‑time cheapest flights using the Amadeus API
- ✅ **Job listings** – See open roles via the Adzuna API
- ✅ **City summaries** – Gemini AI gives weather and lifestyle summaries
- ✅ **Save your searches** – Signed-in users can save/view/delete search history
- ✅ **Guest access** – Use the app without signing in (limited features)
- ✅ **Secure login** – Supabase handles auth, sessions, and user data
- ✅ **Flight booking** – Link to book flights via Google Flights
- ✅ **Interactive UI** – Built with React + Vite for a modern experience
- ✅ **Dashboard** – Post-login landing with user options and tips

---

## 🛠️ Tech Stack

- **Frontend:** React (Vite)
- **Backend:** Flask (Python)
- **Database:** Supabase PostgreSQL (replaces SQLite)
- **Auth:** Supabase Auth
- **APIs:** Amadeus, Adzuna, Gemini (Google AI), OpenAI

---

## 📂 Project Structure

```text
NextNest/
├── backend/
│   ├── routes/
│   ├── services/
│   └── app.py
└── frontend/
    ├── src/
    │   ├── components/
    │   ├── pages/
    |   ├── services/
    │   ├── styles/
    │   └── context/
    └── main.jsx
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Node.js + npm
- Supabase project (with anon key and JWT secret)
- API keys for Amadeus, Adzuna, Gemini, OpenAI

---

### Backend Setup

Create `.env` in `/backend`:

```
AMADEUS_API_KEY=your_amadeus_key
AMADEUS_API_SECRET=your_amadeus_secret
ADZUNA_APP_ID=your_adzuna_id
ADZUNA_APP_KEY=your_adzuna_key
GEMINI_API_KEY=your_gemini_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
SUPABASE_JWT_SECRET=your_supabase_jwt_secret
```

Install and run backend:

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Runs at: `http://127.0.0.1:5001`

---

### Frontend Setup

Create `.env` in `/frontend`:

```
VITE_SUPABASE_URL=your_supabase_project_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
```

Install and run frontend:

```bash
cd frontend
npm install
npm run dev
```

Runs at: `http://localhost:5173`

---

## 📌 App Flow

1. Landing Page – Intro + Get Started
2. Auth Page – Sign in, Sign up, or Continue as Guest
3. Dashboard – Choose to search or view history
4. Input Page – Enter travel + job info
5. Results Page – Flights, jobs, city info + book/save
6. History Page – (if signed in) View past searches

---

## ✅ Roadmap

- [ ] Add cost of living API
- [ ] Add map visualizations
- [ ] Social login (Google, GitHub)

---

## 📜 License

MIT License © 2025 NextNest Team
