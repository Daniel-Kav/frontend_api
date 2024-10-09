import { useEffect, useState } from "react"
import axios from "axios"

const App = () => {
  const[drinks, setDrinks] = useState([])

  const  getDrinks = () => {
    axios.get('http://localhost:8000/api/drinks/')
    .then(response => setDrinks(response.data))
    .catch(errors => {
      console.error('Failed to fetch drinks', errors)
    })
  }

  useEffect(()=> {
    getDrinks()
  }, [])

  return (
    <div>
      <h1>Drink parlour</h1>
    </div>
  )
}

export default App
