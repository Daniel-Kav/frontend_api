
import axios from 'axios'
import { useState } from 'react'

const Login = () => {
    const[username, setUsername] = useState('')
    const[password, setPassword] = useState('')

    const handleSubmit = () => {
        axios.post('http://127.0.0.1:8000/api/token/', { username: username, password: password})
        .then(response => localStorage.setItem('tokens',JSON.stringify(response.data)))
        .catch(error => {
            console.error('Failed to Login', error)
        })
    }
  return (
    <div>
      <form action="" onSubmit={() => handleSubmit()}>
        <input type="text" 
            placeholder='Username'
            value={username}
            onChange={(e) => setUsername(e.target.value)}
        />
        <input type="password" 
            placeholder='password'
            value={password}
            onChange={(e) => setPassword(e.target.value)}
        />
        <button type='submit'>Login</button>
      </form>
    </div>
  )
}

export default Login
