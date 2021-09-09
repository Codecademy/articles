import React from 'react';
import ToDoListItem from './ToDoListItem'

function ToDoList({toDoList, completeToDo, removeToDo}) {

    return (
        <div>
            {toDoList.map((todolistitem, index) => {
               return (
                   <ToDoListItem 
                     todolistitem={todolistitem}
                     index={index}
                     completeToDo={completeToDo}
                     removeToDo={removeToDo}
                     key={index}
                   />
               )
           })}
        </div>
    );
}

export default ToDoList;