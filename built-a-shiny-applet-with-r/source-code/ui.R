library(shiny)
# The user interface is defined
shinyUI(pageWithSidebar(
  
  # Title of the application
  headerPanel("Analyze Data"),
  
  # Provide the side bar view of caption, number of observations and selection of dataset
  sidebarPanel(
    textInput("caption", "Caption:", "Summary"),
    
    selectInput("dataset", "Choose a dataset:", 
                choices = c("rock", "pressure", "cars")),
    
    numericInput("obs", "Number of observations to view:", 10)
  ),

  # View the summary with given dataset that showed in the HTML table format
  mainPanel(
    h3(textOutput("caption")), 
    
    verbatimTextOutput("summary"), 
    
    tableOutput("view")
  )
))
