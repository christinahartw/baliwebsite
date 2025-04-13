import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './App.css'
import Register from './pages/Register'
import PublicItinerary from './pages/PublicItinerary'
import PersonalItinerary from './pages/PersonalItinerary'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Register />} />
        <Route path="/public-itinerary" element={<PublicItinerary />} />
        <Route path="/personal-itinerary" element={<PersonalItinerary />} />
      </Routes>
    </Router>
  )
}

export default App
