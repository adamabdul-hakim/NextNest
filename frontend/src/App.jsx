import { useNavigate, Outlet} from 'react-router-dom';
import './App.css'

function App() {
  const navigate = useNavigate();

  const handleStart = () => {
    navigate('/InputForm');
  };

  return (

    <>
      <Outlet />
      <h1>Welcome to NextNest</h1>
      <h5>Explore what life would be like in another state</h5>
      <button onClick={handleStart}>Get Started</button>
    </>
  )
}

export default App
