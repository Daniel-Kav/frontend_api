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
  const[editDrinkId, setEditDrinkId] = useState(0)

  const  getDrinks = () => {
    axios.get('http://localhost:8000/api/drinks/')
    .then(response => setDrinks(response.data))
    .catch(errors => {
      console.error('Failed to fetch drinks', errors)
    })
  }

  const addDrink = () => {
    axios.post('http://localhost:8000/api/drinks/', newdrink)
    .then(() => {
      getDrinks()
      setNewDrink({ name: '', description: ''})
    })
    .catch(error => {
      console.error('Failed to add book', error)
    })
  }

  const updateDrink = (id: Number) => {
    axios.put(`http://127.0.0.1:8000/api/drinks/${id}`, newdrink)
    .then(() => {
      getDrinks()
      setNewDrink({ name:'', description: ''})
      setEditDrinkId(0)
    })
  }

  const deleteDrink = (id: Number) => {
    axios.delete(`http://127.0.0.1:8000/api/drinks/${id}`)
    .then(() => getDrinks())
    .catch(error => {
      console.error('Failed to delete drink', error)
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
        onChange={(e) => setNewDrink({...newdrink, name: e.target.value})}
      />

      <input type="text" 
        placeholder="description"
        value={newdrink.description}
        onChange={(e) => setNewDrink({ ...newdrink, description: e.target.value})}
      />
      <button onClick={editDrinkId ? () => updateDrink(editDrinkId) : addDrink}>{editDrinkId ? 'Update' : 'Update' }</button>
      <ul>
        {drinks && drinks.map((drink : Drink)=> (
          <li key={drink.id}>
            <h2>{drink.name}</h2>
            <p>{drink.description}</p>
            <button onClick={ () => {
              setEditDrinkId(drink.id)
              setNewDrink({ name : drink.name, description: drink.description})
            }}>Edit</button>
            <button onClick={() => deleteDrink(drink.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App
