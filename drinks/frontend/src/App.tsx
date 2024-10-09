import { useEffect, useState } from "react"
import axios from "axios"

type Drink = {
  id: number,
  name: string,
  description: string
}

const App = () => {
  const[drinks, setDrinks] = useState([])
  const[newdrink, setNewDrink] = useState({ name : '',description: ''})

  const  getDrinks = () => {
    axios.get('http://localhost:8000/api/drinks/')
    .then(response => setDrinks(response.data))
    .catch(errors => {
      console.error('Failed to fetch drinks', errors)
    })
  }

  const addDrink = () => {
    axios.post('http://localhost:8000/api/drinks/')
    .then(() => {
      getDrinks()
      setNewDrink({ name: '', description: ''})
    })
    .catch(error => {
      console.error('Failed to add book', error)
    })
  }

  useEffect(()=> {
    getDrinks()
  }, [])

  return (
    <div>
      <h1>Drink parlour</h1>

      <input type="text" 
        placeholder="add a drink"
        value={newdrink.name}
        onChange={(e) => {...newdrink, name: e.target.value}}
      />

      <ul>
        {drinks && drinks.map((drink : Drink)=> (
          <li key={drink.id}>
            <h2>{drink.name}</h2>
            <p>{drink.description}</p>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App
