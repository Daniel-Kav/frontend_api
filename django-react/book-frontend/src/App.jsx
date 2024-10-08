import React, { useEffect, useState}  from 'react'
import axios from 'axios'


const App = () => {

  const[books , setBooks ]= useState([])

  const getBooks = () => {
    axios.get('http://127.0.0.1:8000/api/books/')
    .then(response => setBooks(response.data))
    .catch(error => {
      console.error('There was an error fetching books', error)
    })
  }
  useEffect(() => {
    getBooks()
  },[])
  return (
    <div>
      <h1> My frontend </h1>
      <ul>
        { books.map(book =>(
          <li key={book.id}>
            <h3>{book.title}</h3>
            <p>{book.description}</p>
            <p>{book.read ? 'Read' : 'Not Read'}</p>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App
