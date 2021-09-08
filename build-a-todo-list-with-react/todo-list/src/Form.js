import React, {useState} from 'react';

function Form({addToDo}) {
    const [ formInput, setFormInput ] = useState('');

    const handleChange = (e) => {
        setFormInput(e.currentTarget.value)
    };

    const handleSubmit = (e) => {
       e.preventDefault();
       addToDo(formInput);
       setFormInput("");
   }

    return (
        <form onSubmit={handleSubmit}>
            <input value={formInput} type="text" onChange={handleChange} placeholder="Add a To Do List Item..."/>
            <button>Add To Do</button>
        </form>
    );
};

export default Form;