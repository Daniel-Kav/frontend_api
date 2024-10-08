import React, { useEffect, useState}  from 'react'
import axios from 'axios'


const App = () => {

  const[books , setBooks ]= useState([])

  const getBooks = () => {
    axios.get('http://localhost:8000/api/books')
    .then(response => setBooks(response.data))
    .catch(error => {
      consle.error('There was an error fetching books', error)
    })
  }
  return (
    <div>
      <h1> My frontend </h1>
    </div>
  )
}

export default App
