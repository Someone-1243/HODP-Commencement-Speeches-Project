########## ########## PREP ##########

# Load necessary libraries.

library(shiny)
library(shinythemes)
library(reticulate)

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
                                            br(),
                                            h3(tags$b("Introduction & Question")),
                                            p("Every year, Harvard hosts a notable speaker to deliver a commencement speech as part of the graduation ceremony. In the last twenty years, icons from Bill Gates to Oprah Winfrey have spoken to the graduating students and have covered a variety of topics to jumpstart the class’ post-academic, “real world” lives. Our group sought to understand what, if any, correlation existed between these speakers’ words and the situation in the world at large: what is the final call to action, final image of what a Harvard student should be like and how does this change as the world changes?  An understanding of these ideas reflects not only which global topics are the most salient and pressing, but our responsibilities as students to act on them."),
                                            br(),
                                            h3(tags$b("Data & Methods")),
                                            p("Data was collected from commencement speech transcripts from 2000 - 2020, with the exclusion of 2001, 2003, and 2006, for which no accurate transcripts could be found. This was then quantified and analyzed using Text Analytics from Microsoft Azure. The data on speeches was compared to web-based search data, namely from Google Trends and",
                                              a("Wikipedia’s Timeline of the 21st Century",
                                                href = "https://en.wikipedia.org/wiki/Timeline_of_the_21st_century#2001"),
                                              "."
                                            )
                 ))
             )
    ),
    
    ########## SECOND PAGE: INSIGHTS ##########
    
    tabPanel("Insights",
             fluidPage(
                 br(),
                 br(),
                 fluidRow(column(1), column(10,
                                            h3(tags$b("Sentiment Analysis")),
                                            p("Each speech was first analyzed for sentiment, where the content was scored from 0 to 1, roughly as percentage for how positive, neutral, or negative the material was. As shown below, Harvard commencement speeches have been largely negative in tone, with only two speeches reaching a positivity score of 50%."),
                                            # image
                                            p("A subjective examination of Microsoft Azure’s sentiment analysis appears to show that the software flags controversial topics or words related to global problems as negative, even when presented in a hopeful manner. For instance, a passage describing a student who “has every reason to be cynical” who chose instead to follow a sense of purpose and “bring people along with him” would be seen as hopeful or positive by most viewers, but words describing the struggles he overcame resulted in a negativity score of 83%. Applying this to the speeches at large, the consistently high negativity scores may indicate that Harvard students must be made aware of global problems—not to apply an omnipresent pressure of pessimism, but as a chance to eliminate them and bring a better future forward."),
                                            p("To compare the sentiment of each speech to the general global environment at the time. To do this,",
                                              a("Wikipedia’s Timeline of the 21st Century",
                                                href = "https://en.wikipedia.org/wiki/Timeline_of_the_21st_century#2001"),
                                              "was used as a proxy for the past 20 years as it is relatively consistent in presentation and format, while Google search data was used for more recent years as well. The individual sentiment scores for every year of Wikipedia’s entries are shown below. Also, a comparison of the speech versus Wikipedia summary yields the following:"),
                                            # image
                                            # image
                                            p("There appears to be a slight negative correlation between the negativity of the speech and of the year. Speculatively, this may allude to a perceived responsibility on the part of the Harvard community to maintain a sense of optimism during difficult times; however, due to the small sample size, weak correlation, and lack of detail in Wikipedia’s summary necessitates that further research is conducted."),
                                            h3(tags$b("Text Analysis")),
                                            p("Each speech was then analyzed for key phrases using", 
                                              a("Text Analytics’",
                                                href = "https://azure.microsoft.com/en-ca/services/cognitive-services/text-analytics/"), 
                                              "key phrase extraction API. The API used natural language processing to identify and evaluate approximately 200 key words and phrases in each transcript."),
                                            p("To better understand this data, we began by looking for the key phrases that were repeated most often among the speeches. We wanted to learn whether certain words and ideas were universal to Harvard commencement speeches, regardless of the specific speaker. The word cloud below is a visual representation of the frequency of words and phrases that appeared in Harvard commencement speeches between 2000-2020. The word cloud provides a high-level snapshot of some of the important ideas, such as an outward focus on other people, the world, and the future, that Harvard wishes to instill in their students."),
                                            # image
                                            p("Next, we found the percentage of keywords in each of the speeches that were related to what was going on in the world. Again, we used", 
                                              a("Wikipedia’s Timeline of the 21st Century",
                                                href = "https://en.wikipedia.org/wiki/Timeline_of_the_21st_century#2001"),
                                              "to guide our comparison. We recognize the limitations of using Wikipedia as reference for real-world significance because Wikipedia’s summary only covers a narrow scope of the world’s events. As such, the graph below is more helpful for comparing the speeches relative to each other, rather than focusing on the individual percentages."),
                                            # image
                                            p("This analysis can be improved in the future by incorporating Google search data and other sources of media coverage to ensure a more comprehensive view of pertinent real-world events."),
                                            p("To incorporate such data from Google, we used an unofficial Google Trends API, where one feature is the ability to track the interest over time of specific words based on year and location. The phrase “interest over time” is represented through numbers from 0-100 that “represent search interest relative to the highest point on the chart”. For example, the term “American election” would perhaps reach a value of 100 during the month November, because that is the peak popularity for said term, whereas in another month, it may have a value of 50 because at that point in time the term is only half as popular. Finally, a score of 0 means that there wasn’t enough data present for the term."),
                                            p("We took the common key phrases from above and checked to see their interest over time for the year they were mentioned in the speech. We then took the average of these values and plotted them below:"),
                                            # image
                                            p("On average, the interest over time of phrases mentioned in the commencement speeches had a minimum value of about 56 and a maximum value of about 69. In other words, the topics said in these speeches were in some ways relevant to events occurring around the world. This makes sense, seeing as how these speeches are in a way, the formal greeting into the “real world” after college. It would only be fair to recap on important events that happened throughout the year as a guiding place for graduates to feel prepared at entering an entirely new environment."),
                                            p("There are some limits of using an unofficial API as Google themselves did not create it. Furthermore, we had to remove years prior to 2006, as the scope of data available in Google Trends was limited and did not accurately reflect major events of these years."),
                                            h3(tags$b("Unanswered Questions")),
                                            p("There are some questions left unanswered by our work because of the limitations of the resources we used. For example, the sentiment analysis software we used interpreted the presence of any words related to global problems as negative, even when it would be clear to a human reader that although the topic is negative, it is actually being presented in a hopeful manner. A more accurate or nuanced interpretation of the overall sentiment of each speech would therefore rely on more sophisticated software. With such software, it could be interesting to analyze the presence of different sentiments within the same speech to see if any patterns emerge, but this was beyond the scope of our research."),
                                            p("The slight negative correlation between the negativity of the speech and of the year that we found is also an ambiguous result that leads to further unanswered questions. The first question would be whether or not such a slight trend is actually relevant, and to answer this, it would be necessary to analyze more commencement speech data. The second question would be the reason for such a negative trend, if it exists. Although we might speculate that a slight negative trend might be representative of an urge to remain optimistic even during difficult times, ultimately this is just a prediction. The slight negative trend might also be indicative of something else entirely, and ultimately it would be necessary to conduct more research before drawing any definitive conclusions."),
                                            br(),
                                            br()
                 ))
             )
    ),
    
    ########## THIRD PAGE: CONCLUSION ##########
    
    tabPanel("Conclusion",
             fluidPage(
                 fluidRow(column(1), column(10,
                                            br(),
                                            br(),
                                            h3(tags$b("Conclusion")),
                                            h3(tags$b("Significance")),
                                            h3(tags$b("Future Work"))
                 ))
             )
    ),
    
    ########## FOURTH PAGE: ABOUT ##########
    
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
                                            br()
                 ))
             )
    )
)
