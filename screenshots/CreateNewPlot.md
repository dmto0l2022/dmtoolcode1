# Row 1
    Header
    Need Help
    FAQ
    Found A Bug
    What's New
# Row 2
    Plots
    Data
  
# All Plots

# New Plot
    Name : Enter Plot Name
# Code

        newplot_input = dbc.Row(
            [
                dbc.Label("New Plot", width=2),
                dbc.Col(
                    [dbc.Input(
                        type="text", id="newplot_input", placeholder="Enter New Plot Name"
                    ),
                    dbc.FormText("Enter unique name for your plot",color="secondary")],
                    width=10,
                    style={"height": "100%","background-color": "blue", "padding":"0px", "margin":"0px"},
                ),
            ],
        style={"height": "50%"},
        )
        
        newplotform = dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.P("New Plot"),
                            width=12,
                            style={"height": "100%","background-color": "red","padding":"0px", "margin":"0px"},
                        ),
                    ],
                    #className="h-25",
                    style={"height": "50%"},
                ),
                newplot_input,
            ],
            style={"height": "50px"},
        )
