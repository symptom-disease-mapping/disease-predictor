
import './App.css'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import DropdownComponent from './components/Search.jsx'
import HeroPage from './pages/heroPage'
import InfoPage from './pages/infoPage'
import InputPage from './pages/inputPage'
import QuestionPage from './pages/questionPage'
import Search2 from './components/Search2.jsx'
function App() {
 

  return (
    <Router>
    <Routes>
    {/* <HeroPage/> */}
    {/* <InfoPage/> */}
    {/* <InputPage/> */}
    
      <Route path="/" element={<DropdownComponent/>} />
      <Route path="/Search2" element={<Search2/>} />
    
    {/* <QuestionPage/> */}
    </Routes>
    </Router>
  )
}

export default App;