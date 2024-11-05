import { useState } from "react"
import axios, { AxiosResponse } from 'axios'

type Task = {
  description: string
  title: string
}

const App = () => {
  const[tasks, setTasks] = useState<Task[]>([])

  const getTasks = () => {
    axios.get('http://127.0.0.1/tasks')
    .then((res: AxiosResponse) => {
      setTasks(res.data)
    })
  }

  return (
    <div>
      
    </div>
  )
}

export default App
