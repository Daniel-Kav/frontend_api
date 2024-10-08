import React, { useEffect, useState } from 'react';
import axios from 'axios';

const App = () => {
  const [books, setBooks] = useState([]);
  const [newBook, setNewBook] = useState({ title: '', description: '', read: false });
  const [editBookId, setEditBookId] = useState(null);

  const getBooks = () => {
    axios.get('http://localhost:8000/api/books/')
      .then(res => setBooks(res.data))
      .catch(error => {
        console.error('There was an error fetching books', error);
      });
  };

  const addBook = () => {
    axios.post('http://localhost:8000/api/books/', newBook)
      .then(() => {
        getBooks();
        setNewBook({ title: '', description: '', read: false });
      })
      .catch(error => {
        console.error('There was an error adding the book', error);
      });
  };

  const updateBook = (id) => {
    axios.put(`http://localhost:8000/api/books/${id}/`, newBook)
      .then(() => {
        getBooks();
        setEditBookId(null);
        setNewBook({ title: '', description: '', read: false });
      })
      .catch(error => {
        console.error('There was an error updating the book', error);
      });
  };

  const deleteBook = (id) => {
    axios.delete(`http://localhost:8000/api/books/${id}/`)
      .then(() => {
        getBooks();
      })
      .catch(error => {
        console.error('There was an error deleting the book', error);
      });
  };

  useEffect(() => {
    getBooks();
  }, []);

  return (
    <div>
      <h1>Kavatha's Bookshop</h1>
      
      <h2>{editBookId ? 'Edit Book' : 'Add Book'}</h2>
      <input
        type="text"
        placeholder="Title"
        value={newBook.title}
        onChange={(e) => setNewBook({ ...newBook, title: e.target.value })}
      />
      <input
        type="text"
        placeholder="Description"
        value={newBook.description}
        onChange={(e) => setNewBook({ ...newBook, description: e.target.value })}
      />
      <label>
        <input
          type="checkbox"
          checked={newBook.read}
          onChange={(e) => setNewBook({ ...newBook, read: e.target.checked })}
        />
        Read
      </label>
      <button onClick={editBookId ? () => updateBook(editBookId) : addBook}>
        {editBookId ? 'Update' : 'Add'}
      </button>

      <ul>
        {books.map(book => (
          <li key={book.id}>
            <h2>{book.title}</h2>
            <p>{book.description}</p>
            <p>{book.read ? 'Read' : 'Not Read'}</p>
            <button onClick={() => {
              setEditBookId(book.id)
              setNewBook({ title: book.title, description: book.description, read: book.read })
            }}>Edit</button>
            <button onClick={() => deleteBook(book.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;
