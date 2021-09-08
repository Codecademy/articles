import React, { useState } from 'react';
import './App.css';

import Header from './Header';
import Form from './Form';
import ToDoList from './ToDoList';
import data from './data.json';


function App() {
  const [ toDoList, setToDoList ] = useState(data);

  const addToDo = (formInput) => {
   const newToDoList = [...toDoList, { id: toDoList.length + 1, todo: formInput, done: false }];
   setToDoList(newToDoList);
  }

  const completeToDo = (i) => {
    const newToDoList = [...toDoList];
    newToDoList[i].done = true;
    setToDoList(newToDoList);
  }

  const removeToDo = (i) => {
    const newToDoList = [...toDoList];
    newToDoList.splice(i, 1);
    setToDoList(newToDoList);
  }

  return (
    <div className="App">
      <Header />
      <Form addToDo={addToDo}/>
      <ToDoList 
        toDoList={toDoList} 
        completeToDo={completeToDo} 
        removeToDo={removeToDo}/>
    </div>
  );
}

export default App;