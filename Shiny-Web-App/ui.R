########## ########## PREP ##########

# Load necessary libraries.

library(shiny)
library(shinythemes)

# Define UI.

ui <- navbarPage(
    theme = shinytheme("yeti"), # other options: sandstone, flatly, united, slate
    tags$b("Analyzing Harvard Commencement Speeches"),
    
    ########## FIRST PAGE: OVERVIEW ##########
    
    tabPanel("Overview",
             fluidPage(
                 fluidRow(column(1), column(10,
                                            br(),
                                            br(),
                                            h1(tags$b("Analyzing Harvard Commencement Speeches"), 
                                               align = "center"),
                                            h4(tags$b("Looking at trends in Harvard commencement speeches
                              over the years."),
                                               align = "center"),
                                            br(),
                                            br()
                 ))
             )
    ),
    
    ########## SECOND PAGE: ANALYSIS ##########
    
    tabPanel("Analysis",
             fluidPage(
                 br(),
                 br(),
                 fluidRow(column(1), column(10,
                                            h3(tags$b("Analysis")),
                                            br(),
                                            br()
                 ))
             )
    ),
    
    ########## THIRD PAGE: ABOUT ##########
    
    tabPanel("About", 
             fluidPage(
                 br(),
                 br(),
                 fluidRow(column(1), column(10,
                                            h3(tags$b("About Our Project"),
                                               align = "center"),
                                            p(
                                                "This was a project for the",
                                                a("Harvard Open Data Project", href="https://hodp.org/"),
                                                "comp.",
                                                align = "center"
                                            ),
                                            p(
                                                "This project's GitHub repository lives",
                                                a("here", href="https://github.com/Someone-1243/HODP-Commencement-Speeches-Project"),
                                                ".",
                                                align = "center"
                                            ),
                                            br(),
                                            h3(tags$b("About Our Team"),
                                               align = "center")
                 )),
                 fluidRow(column(3), column(9,
                                            fluidRow(
                                                column(5, imageOutput("katherine")),
                                                column(5, offset = 0, 
                                                       h4(tags$b("Katherine McPhie")), br(), 
                                                       p("Hi, I'm Katherine! I'm a first-year undergraduate at Harvard pursuing a concentration in Computer Science. On campus I am involved in Harvard Computer Society, Women in Computer Science, and Harvard Open Data Project. I also sing alto for University Choir, and  play trumpet in the Wind Ensemble! You can reach me at",
                                                         a("katherinemcphie@college.harvard.edu",
                                                           href="mailto:katherinemcphie@college.harvard.edu?Subject=Commencement%20Speeches%20Project"
                                                         ),
                                                         ".")),
                                            ),
                                            br(),
                                            fluidRow(
                                                column(5, imageOutput("justin")),
                                                column(5, offset = 0, 
                                                       h4(tags$b("Justin Ye")), br(), 
                                                       p("You can reach me at",
                                                         a("____@college.harvard.edu",
                                                           href="mailto:____@college.harvard.edu?Subject=Commencement%20Speeches%20Project"
                                                         ),
                                                         ".")),
                                            ),
                                            br(),
                                            fluidRow(
                                                column(5, imageOutput("cindy")),
                                                column(5, offset = 0, 
                                                       h4(tags$b("Cindy Liu")), br(), 
                                                       p("You can reach me at",
                                                         a("____@college.harvard.edu",
                                                           href="mailto:____@college.harvard.edu?Subject=Commencement%20Speeches%20Project"
                                                         ),
                                                         ".")),
                                            ),
                                            br(),
                                            fluidRow(
                                                column(5, imageOutput("jacinta")),
                                                column(5, offset = 0, 
                                                       h4(tags$b("Jacinta Olonilua")), br(), 
                                                       p("You can reach me at",
                                                         a("____@college.harvard.edu",
                                                           href="mailto:____@college.harvard.edu?Subject=Commencement%20Speeches%20Project"
                                                         ),
                                                         ".")),
                                            ),
                                            br(),
                                            br()
                 ))
             )
    )
)
