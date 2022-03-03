import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';

function App() {
  const [fact, setFact] = useState("");
  const handleClick = () => {
    fetch("/funfact")
      .then(response => response.json())
      .then(data => console.log(data))
    setFact("done")
  }
  return (
    <div className="App">
      <p>Fun Fact: {fact}</p>
      <button onClick={handleClick}></button>
    </div>
  );
}

export default App;
