import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

newplot_input = html.Div(
    [
        dbc.Label("New Plot"),
        dbc.Input(type="text", id="newplot-input1", placeholder="Enter New Plot Name"),
        dbc.FormText(
            "Enter unique name for your plot",
            color="secondary",
        ),
    ],
)


email_input = html.Div(
    [
        dbc.Label("Email", html_for="example-email"),
        dbc.Input(type="email", id="example-email", placeholder="Enter email"),
        dbc.FormText(
            "Are you on email? You simply have to be these days",
            color="secondary",
        ),
    ],
)

password_input = html.Div(
    [
        dbc.Label("Password", html_for="example-password"),
        dbc.Input(
            type="password",
            id="example-password",
            placeholder="Enter password",
        ),
        dbc.FormText(
            "A password stops mean people taking your stuff", color="secondary"
        ),
    ],
    className="mb-3",
)

#### email & password form

emailform_title = html.Div(html.P(children='Please Login', className = "NOPADDING_CONTENT FORM_TITLE"))


enter_emailandpassword  = dbc.Row(
    [
        dbc.Col(
            [
                dbc.Label("Email", html_for="example-email-grid", className="FORM_TEXT"),
                dbc.Input(
                    type="email",
                    id="example-email-grid",
                    placeholder="Enter email",
                ),
            ],
            width=6,
        ),
        dbc.Col(
            [
                dbc.Label("Password", html_for="example-password-grid", className="FORM_TEXT"),
                dbc.Input(
                    type="password",
                    id="example-password-grid",
                    placeholder="Enter password",
                ),
            ],
            width=6,
        ),
    ],
    className="g-3",
)

#submit_button =  dbc.Col(dbc.Button("Submit", color="primary"), width="auto")

create_button =  html.Div(dbc.Button("Create", color="primary"), className = "FORM_CREATE_BUTN")

submit_button =  html.Div(dbc.Button("Submit", color="primary"), className = "FORM_SUBMIT_BUTN")

cancel_button =  html.Div(dbc.Button("Cancel", color="secondary"), className = "FORM_CANCEL_BUTN")

#cancel_button =  dbc.Col(dbc.Button("Cancel", color="secondary"), width="auto")

login_form = html.Div(
    #[newplot_title,newplot_input3],
    [emailform_title, enter_emailandpassword, submit_button, cancel_button],
    className = "NOPADDING_CONTENT CENTRE_FORM"
)


#newplotform = dbc.Form([newplot_input, newplot_input2, email_input, password_input, input_groups])

newplot_input2 = dbc.Row(
    [
        html.Div(children="New Plot", className="FORM_TEXT"),
        dbc.Col([
            dbc.Label("Name", width=2),
            dbc.Input(
                type="text",
                id="newplot-input2",
                placeholder="Enter New Plot Name",
                style={"width": "25vh", "height": "5vh", "color": "blue"},
            ),]
        ),
    ],
)


#######################################


newplot_title = html.Div(html.P(children='New Plot', className = "NOPADDING_CONTENT FORM_TITLE"))

label_1 = html.Div(dbc.Label("Name", align="center", className="FORM_TEXT"))

newplot_input3 = html.Div(
    [
        dbc.Col(dbc.Label("Name", align="end", className="FORM_TEXT"),width=2),
        dbc.Col(
            dbc.Input(
                type="text", id="newplot-input3",
                placeholder="Enter New Plot Name",
            ),
            width=4,
        ),
    ],
    className="row",
)

#newplotform = html.Div([newplot_title , newplot_input3], style={"padding":"0px", "margin":"0px", "background-color":"red"})

newplotform = html.Div(
    #[newplot_title,newplot_input3],
    [newplot_title, label_1],
    className = "NOPADDING_CONTENT CENTRE_FORM"
)

################################################

newplot_input = dbc.Row(
    [
        dbc.Label("New Plot", width=2, style={"height": "40px"}),
        dbc.Col(
            [dbc.Input(
                type="text", id="newplot_input", placeholder="Enter New Plot Name"
            ),
            dbc.FormText("Enter unique name for your plot",color="secondary")],
            ##width=10,
            style={"height": "100%","background-color": "blue", "padding":"0px", "margin":"0px", "border": "2px solid black"},
        ),
    ],
style={"height": "75%", "width": "100%"},
)


newplotform_2 = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.P("New Plot"),
                    ##width=12,
                    style={"height": "40px","background-color": "red","padding":"0px", "margin":"0px", "border": "2px solid black"},
                ),
            ],
            #className="h-25",
            style={"height": "25%"},
        ),
        newplot_input,
    ],
    style={"height": "100%", "width": "100%", "border": "2px solid black"},
    ##style={"border": "5px solid", "margin": "auto", "width": "100%","height": "100%", "padding": "0px", "background-color": "red"}
)

newplotform_1 = html.Div([
        newplot_input,
    ],
    ##className = "container-fluid",
    style={"height": "100%", "width": "100%", "border": "5px solid", "background-color": "red"},
    ##style={"border": "5px solid", "margin": "auto", "width": "100%","height": "100%", "padding": "0px", "background-color": "red"}
)


###############
formcentrestyle_1 = {"width": "600px", "height": "600px",
                "position": "absolute", "top": "50%", "left": "50%", 
                "transform": "translate(-50%,-50%)",
                "-ms-transform": "translate(-50%, -50%)"}

#formcentrestyle = {"width": "1000px", "height": "1000px", "display": "inline-block" ,"vertical-align": "middle"}
formcentrestyle = {"width": "1000px", "height": "1000px", "display": "table-cell" ,"vertical-align": "middle"}


############################

email_input = html.Div(
    [
        dbc.Label("Email", html_for="example-email"),
        dbc.Input(type="email", id="example-email", placeholder="Enter email"),
        dbc.FormText(
            "Are you on email? You simply have to be these days",
            color="secondary",
        ),
    ],
    ##style={"border": "5px solid black", "margin": "auto", "width": "50%","height": "25%", "padding": "0px", "background-color": "green"}
    ##className="mb-3",
)



'''
.inner {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%,-50%);
  width: 200px;
  height: 200px;
}

display: inline-block;
  vertical-align: middle;

 margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);

'''

password_input = html.Div(
    [
        dbc.Label("Password", html_for="example-password"),
        dbc.Input(
            type="password",
            id="example-password",
            placeholder="Enter password",
        ),
        dbc.FormText(
            "A password stops mean people taking your stuff", color="secondary"
        ),
    ],
    ##style={"border": "5px solid black", "margin": "auto", "width": "50%","height": "25%", "padding": "0px", "background-color": "orange"}
    ##className="mb-3",
)

newplotform = html.Div(
                [dbc.Form([email_input, password_input])],
                #style={"border": "5px solid black", "margin": "auto", "width": "100%","height": "100%", "padding": "0px", "background-color": "red"}
                style = formcentrestyle
                )
                


###########################


input_groups = html.Div(
    [
        dbc.InputGroup(
            [dbc.InputGroupText("@"), dbc.Input(placeholder="Username")],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.Input(placeholder="Recipient's username"),
                dbc.InputGroupText("@example.com"),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("$"),
                dbc.Input(placeholder="Amount", type="number"),
                dbc.InputGroupText(".00"),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("Total:"),
                dbc.InputGroupText("$"),
                dbc.Input(placeholder="Amount", type="number"),
                dbc.InputGroupText(".00"),
                dbc.InputGroupText("only"),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("With textarea"),
                dbc.Textarea(),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.Select(
                    options=[
                        {"label": "Option 1", "value": 1},
                        {"label": "Option 2", "value": 2},
                    ]
                ),
                dbc.InputGroupText("With select"),
            ]
        ),
    ]
)
