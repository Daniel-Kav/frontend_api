
import axios from 'axios'
import { useEffect, useState } from 'react'

interface Recipe{
  id: number,
  title: string,
  description: string,
  instructions: string,
}

const App = () => {
  const[recipes, setRecipes] = useState([])

  const getRecipes = () => {
    axios.get('http://127.0.0.1:8000/api/recipes/')
    .then(res => setRecipes(res.data))
    .catch(error => {
      console.error('failed to get recipes',error)
    })
  }

  useEffect(() => {
    getRecipes()
  },[])

  return (
    <div>
      <h1>Recipes Garlour</h1>
      {recipes && recipes.map((recipe: Recipe) => (
        <li key={recipe.id}>
          <h3>{recipe.title}</h3>
          <p>{recipe.description}</p>
          <p>{recipe.instructions}</p>
        </li>
      )) }
    </div>
  )
}

export default App
