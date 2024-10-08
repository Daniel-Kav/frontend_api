import React, { useEffect, useState}  from 'react'
import axios from 'axios'


const App = () => {

  const[books , setBooks ]= useState([])
  const[newBook, setnewBook] = useState({ title: '', description :'', read : false})

  const getBooks = () => {
    axios.get('http://127.0.0.1:8000/api/books/')
    .then(response => setBooks(response.data))
    .catch(error => {
      console.error('There was an error fetching books', error)
    })
  }

  const addBook = () => {
    axios.post('http://localhost:8000/api/books/', newBook)
    .then(()=> {
      getBooks()
      setnewBook({ title: '', description: '', read: false})
    })
    .catch( error => {
      console.error( 'Error adding book ', error)
    })
  }

  useEffect(() => {
    getBooks()
  },[])
  return (
    <div>
      <h1> My frontend </h1>
      <h2>Add Book</h2>
      <input type="text" 
        placeholder='Title'
        value={newBook.title}
        onChange={(e) => setnewBook({...newBook, title: e.target.value})}
      />

      <input type="text" 
        placeholder='description'
        value={newBook.description}
        onChange={(e) => setnewBook({...newBook, description: e.target.value})}
      />
      <label htmlFor="">
        <input type="checkbox" 
          checked = {newBook.checked}
          onChange={(e) => setnewBook({...newBook, read: e.target.checked})}
        />
        Read
      </label>
      <button onClick={() => addBook()}>Add Book</button>
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
