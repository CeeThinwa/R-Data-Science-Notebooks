library(shiny)
library(knitr)

rmdfiles <- c("SST 505 TAKE AWAY C.A.T.rmd")
sapply(rmdfiles, knit, quiet = T)

ui <- shinyUI(
    fluidPage(
        withMathJax(includeMarkdown("SST 505 TAKE AWAY C.A.T.md"))
  )
)
server <- function(input, output) { }

shinyApp(ui, server)
