
import axios from 'axios'
import { useEffect, useState } from 'react'

interface Recipe{
  id: number,
  title: string,
  description: string,
  instructions: string,
  ingredients: string,
}

const App = () => {
  const[recipes, setRecipes] = useState([])
  const[newRecipe, setNewRecipe] = useState({title: '',description:'',instructions:'',ingredients:''})

  const getRecipes = () => {
    axios.get('http://127.0.0.1:8000/api/recipes/')
    .then(res => setRecipes(res.data))
    .catch(error => {
      console.error('failed to get recipes',error)
    })
  }

  const addRecipe = () => {
    axios.post('http://127.0.0.1:8000/api/recipes/', {...newRecipe,author: 1})
    .then(() => {
      getRecipes()
      setNewRecipe({title: '',description:'',instructions:'',ingredients:''})
    })
  }

  const deleteRecipe = () => {
    
  }

  useEffect(() => {
    getRecipes()
  },[])

  return (
    <div>
      <h1>Recipes Garlour</h1>
      <input type="text" 
        placeholder='title'
        value={newRecipe.title}
        onChange={(e) => setNewRecipe({...newRecipe, title: e.target.value})}
      />
      <input type="text" 
        placeholder='description'
        value={newRecipe.description}
        onChange={(e) => setNewRecipe({...newRecipe, description: e.target.value})}
      />
      <input type="text" 
        placeholder='ingredients'
        value={newRecipe.ingredients}
        onChange={(e) => setNewRecipe({...newRecipe, ingredients: e.target.value})}
      />
      <input type="text" 
        placeholder='instructions'
        value={newRecipe.instructions}
        onChange={(e) => setNewRecipe({...newRecipe, instructions: e.target.value})}
      />
      <button onClick={() => addRecipe()}>Add Recipe</button>

      {recipes && recipes.map((recipe: Recipe) => (
        <li key={recipe.id}>
          <h3>{recipe.title}</h3>
          <p>{recipe.description}</p>
          <p>{recipe.ingredients}</p>
          <p>{recipe.instructions}</p>
        </li>
      )) }
    </div>
  )
}

export default App
