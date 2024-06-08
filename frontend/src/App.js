import React, { useState } from 'react';
import { handleRegister, handleLogin, handleSendCaptcha } from './services/auth';
import './App.css';  // 新增的 CSS 文件

function App() {
  const [isRegister, setIsRegister] = useState(false);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [passwordConfirm, setPasswordConfirm] = useState('');
  const [mail, setMail] = useState('');
  const [captcha, setCaptcha] = useState('');
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(false);

  const toggleMode = () => {
    setIsRegister(!isRegister);
    setMessage('');
  };

  return (
    <div className="container">
      <h1>{isRegister ? 'User Registration' : 'User Login'}</h1>
      {isRegister && (
        <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
      )}
      <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
      {isRegister && (
        <>
          <input type="password" placeholder="Confirm Password" value={passwordConfirm} onChange={(e) => setPasswordConfirm(e.target.value)} />
          <input type="email" placeholder="Email" value={mail} onChange={(e) => setMail(e.target.value)} />
          <input type="text" placeholder="CAPTCHA" value={captcha} onChange={(e) => setCaptcha(e.target.value)} />
          <button onClick={() => handleSendCaptcha(username, password, passwordConfirm, mail, setMessage, setLoading)} disabled={loading}>
            {loading ? 'Sending CAPTCHA...' : 'Send CAPTCHA'}
          </button>
          <button onClick={() => handleRegister(username, password, passwordConfirm, mail, captcha, setMessage, setLoading)} disabled={loading}>
            {loading ? 'Registering...' : 'Register'}
          </button>
        </>
      )}
      {!isRegister && (
        <>
          <input type="email" placeholder="Email" value={mail} onChange={(e) => setMail(e.target.value)} />
          <button onClick={() => handleLogin(mail, password, setMessage, setLoading)} disabled={loading}>
            {loading ? 'Logging in...' : 'Login'}
          </button>
        </>
      )}
      <button onClick={toggleMode}>
        {isRegister ? 'Switch to Login' : 'Switch to Register'}
      </button>
      <p>{message}</p>
    </div>
  );
}

export default App;
