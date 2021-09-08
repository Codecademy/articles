import React from 'react';

function ToDoListItem({todolistitem, completeToDo, removeToDo, index}) {
    return (
        <div className="todo-item">
            <span className={todolistitem.done ? "done" : ""}>
              {todolistitem.todo}
            </span>
            <button onClick={() => completeToDo(index)}>Done</button>
            <button onClick={() => removeToDo(index)}>Remove</button>
        </div>
    )
}

export default ToDoListItem;