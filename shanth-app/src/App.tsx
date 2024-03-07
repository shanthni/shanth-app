import React from "react";
import "./App.css";
import MyNavbar from "./components/navbar";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/home/home";
import Cases from "./pages/criminalCases/criminalCases";
import Mortality from "./pages/mortalityUs/mortalityUs";

function App() {
  return (
    <Router>
      <MyNavbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/projects/criminal-cases" element={<Cases />} />
        <Route path="/projects/us-mortality" element={<Mortality />} />
      </Routes>
    </Router>
  );
}

export default App;
