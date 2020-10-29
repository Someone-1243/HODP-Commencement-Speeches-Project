# Define server logic.

server <- function(input, output) {
    
    ########## FIRST PAGE: OVERVIEW ##########
    
    ########## SECOND PAGE: ANALYSIS ##########
    
    ########## THIRD PAGE: ABOUT ##########
    
    output$katherine <- renderImage({
        list(src = "www/katherine.png", 
             width = 300, 
             height = 400)
    }, deleteFile = FALSE)
    
    output$justin <- renderImage({
        list(src = "www/person.png",
             width = 300, 
             height = 400)
    }, deleteFile = FALSE)
    
    output$cindy <- renderImage({
        list(src = "www/person.png",
             width = 300, 
             height = 400)
    }, deleteFile = FALSE)
    
    output$jacinta <- renderImage({
        list(src = "www/person.png",
             width = 300, 
             height = 400)
    }, deleteFile = FALSE)
    
}