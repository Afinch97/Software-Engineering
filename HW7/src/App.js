import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';

function App() {
  const [fact, setFact] = useState("");
  const handleClick = () => {
    fetch("/funfact")
      .then(response => response.json())
      .then(data => setFact(data[Math.floor(Math.random() * 3)]))
  }
  return (
    <div className="App">
      <p>Fun Fact: {fact}</p>
      <button onClick={handleClick}>New Fact</button>
    </div>
  );
}

export default App;
