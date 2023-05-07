import { useState } from 'react'
import { Routes, Route } from 'react-router-dom'
import Dashboard from './Dashboard/Dashboard'
import Navbar from '../components/Navbar/Navbar'

import './App.css'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Navbar />
      <Routes>
          <Route path='/' element={<Dashboard />} />
      </Routes>

    </>
  )
}

export default App


// <h1 className="text-2xl font-bold underline text-blue-600 ">
// Hello world!
// </h1>
// <div>

// </div>
// <h1>Vite + React</h1>
// <div className="card">
// <button onClick={() => setCount((count) => count + 1)}>
//   count is {count}
// </button>
// <p>
//   Edit <code>src/App.jsx</code> and save to test HMR
// </p>
// </div>
// <p className="read-the-docs">
// Click on the Vite and React logos to learn more
// </p>