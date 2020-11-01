# Define server logic.

server <- function(input, output) {
    
    ########## FOURTH PAGE: ABOUT ##########
    
    output$katherine <- renderImage({
        list(src = "www/katherine.png", 
             width = 300, 
             height = 400)
    }, deleteFile = FALSE)
    
    output$justin <- renderImage({
        list(src = "www/person.png", # TODO: replace with headshot
             width = 300, 
             height = 400)
    }, deleteFile = FALSE)
    
    output$cindy <- renderImage({
        list(src = "www/person.png", # TODO: replace with headshot
             width = 300, 
             height = 400)
    }, deleteFile = FALSE)
    
    output$jacinta <- renderImage({
        list(src = "www/person.png", # TODO: replace with headshot
             width = 300, 
             height = 400)
    }, deleteFile = FALSE)
    
}