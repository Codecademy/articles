import React, {Component} from 'react';

class Hello extends React.Component {  
    constructor(){  
        super();  
        this.state = {  
            message: "Coding is fun!"  
        };  
        this.updateMessage = this.updateMessage.bind(this);  
    }
    updateMessage() {  
        this.setState({  
            message: " Coding is fun (from changed state)"  
        });  
    }
render() {  
         return (  
           <div>  
             <h1>Hello {this.state.message}!</h1>  
             <button onClick={this.updateMessage}>Click Here!</button>  
           </div>     
        );
    }  
}

export default Hello;
