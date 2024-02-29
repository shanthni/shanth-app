import React from "react";
import "./App.css";
import MyNavbar from "./components/navbar";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/home/home";
import Cases from "./pages/criminalCases/criminalCases";

function App() {
  return (
    <Router>
      <MyNavbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/projects/criminal-cases" element={<Cases />} />
      </Routes>
    </Router>
  );
}

export default App;
