import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Admin from './pages/Admin';
import Librarian from './pages/Librarian';
import Member from './pages/Member';
import Login from './components/Login';
import Register from './components/Register';

function App() {
    return (
        <Router>
            <div>
                <Routes>
                    <Route path="/" exact element={<Home/>} />
                    <Route path="/admin" element={<Admin/>} />
                    <Route path="/librarian" element={<Librarian/>} />
                    <Route path="/member" element={<Member/>} />
                    <Route path="/login" element={<Login/>} />
                    <Route path="/register" element={<Register/>} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
