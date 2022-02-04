library(shiny)
library(datasets)
# Put the server logic to obtain the dataset
shinyServer(function(input, output) {
  
  datasetInput <- reactive({
    switch(input$dataset,
           "rock" = rock,
           "pressure" = pressure,
           "cars" = cars)
  })
output$caption <- renderText({
    input$caption
  })
  
    output$summary <- renderPrint({
    dataset <- datasetInput()
    summary(dataset)
  })
  
  output$view <- renderTable({
    head(datasetInput(), n = input$obs)
  })
})
