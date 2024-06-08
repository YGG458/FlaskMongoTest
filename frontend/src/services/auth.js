import { register, login, sendCaptcha } from '../api';

export const handleRegister = async (username, password, passwordConfirm, mail, captcha, setMessage, setLoading) => {
  setLoading(true);
  try {
    const response = await register({ username, password, passwordConfirm, mail, code: captcha });
    if (response && response.data) {
      setMessage(response.data.message);
      if (response.status === 201) {
        alert('Registration Successful');
      }
    } else {
      setMessage('An error occurred while processing your request.');
    }
  } catch (error) {
    setMessage(error.response?.data?.message || 'An error occurred');
  } finally {
    setLoading(false);
  }
};

export const handleLogin = async (mail, password, setMessage, setLoading) => {
  setLoading(true);
  try {
    const response = await login({ mail, password });
    if (response && response.data) {
      setMessage(response.data.message);
      if (response.data.message === 'Login successful') {
        alert('Login Successful');
      }
    } else {
      setMessage('An error occurred while processing your request.');
    }
  } catch (error) {
    setMessage(error.response?.data?.message || 'An error occurred');
  } finally {
    setLoading(false);
  }
};

export const handleSendCaptcha = async (username, password, passwordConfirm, mail, setMessage, setLoading) => {
  setLoading(true);
  try {
    const response = await sendCaptcha({ username, password, passwordConfirm, mail });
    if (response && response.data) {
      setMessage(response.data.message);
      if (response.status === 201) {
        alert('CAPTCHA sent successfully');
      }
    } else {
      setMessage('An error occurred while processing your request.');
    }
  } catch (error) {
    setMessage(error.response?.data?.message || 'An error occurred');
  } finally {
    setLoading(false);
  }
};
