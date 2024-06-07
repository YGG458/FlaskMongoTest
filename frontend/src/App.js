import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleRegister = async () => {
    try {
      const response = await axios.post('http://localhost:5000/register', { username, password });
      if (response && response.data) {
        setMessage(response.data.message);
        if (response.status === 201) {
          alert('Registration Successful');
        }
      } else {
        setMessage('An error occurred while processing your request.');
      }
    } catch (error) {
      setMessage(error.response.data.message);
    }
  };
  
  const handleLogin = async () => {
    try {
      const response = await axios.post('http://localhost:5000/login', { username, password });
      if (response && response.data) {
        setMessage(response.data.message);
        if (response.data.message === 'Login successful') {
          alert('Login Successful');
        }
      } else {
        setMessage('An error occurred while processing your request.');
      }
    } catch (error) {
      setMessage(error.response.data.message);
    }
  };

  return (
    <div>
      <h1>User Registration and Login</h1>
      <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
      <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
      <button onClick={handleRegister}>Register</button>
      <button onClick={handleLogin}>Login</button>
      <p>{message}</p>
    </div>
  );
}

export default App;
