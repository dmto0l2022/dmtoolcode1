import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc


######################### fields ######################


# Plot Name - Text

# X Range: Lower Bound - Text

# Upper Bound - Text

# Scale - Dropdown

# Trace Trace ID - Integer

# Trace Name - Text

# Trace Color - Dropdown Trace

# Symbol - Dropdown

# Trace Line Style - Dropdown

# Trace Fill Color - Dropdown

# Remove Site Address Check Box

# Upload XML File - Select File

# Load Limit from Uploaded File

# Help on XML File and Examples

# Data Label - Text - < 60 chars

# Data Reference - Big Text

# Data Comment - Big Text

# Experiment - Dropdown

# Date of Announcement - Date

# Year - Dropdown - Integer

# Y Rescale - Exponential

# X Rescale - Exponential

# Data Values - big text field

# Data Formatting Help

# Result Type - Dropdown

# Spin Dependency - Dropdown

# Measurement Type -

# Public Limit - Checkbox

# Other Users - CSV of Users

# Official - Dropdown

# Experiment Type - Dropdown

# Year - Dropdown

# Greatest Hits - Dropdown



##########################


################################################
## NEW PLOT FORM
################################################

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
    [newplot_title,newplot_input3],
    #[newplot_title, label_1],
    className = "NOPADDING_CONTENT CENTRE_FORM"
)

################################################

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


################################################
## EDIT EXISTING
################################################

## X RESCALE
xrescale_input = html.Div(
    [
        dbc.Label("Xrescale", html_for="example-Xrescale"),
        dbc.Input(type="Xrescale", id="example-Xrescale", placeholder="Enter Xrescale"),
        dbc.FormText(
            "Enter XRescale",
            color="secondary",
        ),
    ],
)

## DATA VALUE
datavalue_input = html.Div(
    [
        dbc.Label("Data Value", html_for="example-datavalue"),
        dbc.Input(type="DataValue", id="example-DataValue", placeholder="Enter Data Value"),
        dbc.FormText(
            "Enter Data Value",
            color="secondary",
        ),
    ],
)

resultype_input = html.Div(
    [
        dbc.Label("Result Type", html_for="example-resultype"),
        dbc.Input(type="ResultType", id="example-resultype", placeholder="Enter Result Type"),
        dbc.FormText(
            "Enter Result Type",
            color="secondary",
        ),
    ],
)

spindependency_input = html.Div(
    [
        dbc.Label("Spin Dependency", html_for="example-spindependency"),
        dbc.Input(type="SpinDependency", id="example-spindependency", placeholder="Enter Spin Dependency"),
        dbc.FormText(
            "Enter Spin Dependency",
            color="secondary",
        ),
    ],
)

measuretype_input = html.Div(
    [
        dbc.Label("Measure Type", html_for="example-measuretype"),
        dbc.Input(type="MeasureType", id="example-measuretype", placeholder="Enter Measure Type"),
        dbc.FormText(
            "Enter Measure Type",
            color="secondary",
        ),
    ],
)


public_input = html.Div(
    [
        dbc.Label("Public", html_for="example-public"),
        dbc.Input(type="Public", id="example-public", placeholder="Enter Public"),
        dbc.FormText(
            "Enter Public",
            color="secondary",
        ),
    ],
)

otherusers_input = html.Div(
    [
        dbc.Label("Other Users", html_for="example-otherusers"),
        dbc.Input(type="Other Users", id="example-otherusers", placeholder="Enter Other Users"),
        dbc.FormText(
            "Enter Other Users",
            color="secondary",
        ),
    ],
)


#############################################
## LOGIN
#############################################

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

save_button =  html.Div(dbc.Button("Save", color="primary"), className = "FORM_SAVE_BUTN")

submit_button =  html.Div(dbc.Button("Submit", color="primary"), className = "FORM_SUBMIT_BUTN")

cancel_button =  html.Div(dbc.Button("Cancel", color="secondary"), className = "FORM_CANCEL_BUTN")

#cancel_button =  dbc.Col(dbc.Button("Cancel", color="secondary"), width="auto")

login_form = html.Div(
    #[newplot_title,newplot_input3],
    [emailform_title, enter_emailandpassword, submit_button, cancel_button],
    className = "NOPADDING_CONTENT CENTRE_FORM"
)


###############

newplotform_container = dbc.Container(
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
    #style={"height": "600px","width": "700px","background-color": "green","padding":"0px", "margin":"auto"},
    #style={"height": "600px","width": "700px", "margin": "0px",\
    #       "position": "absolute","top": "50%", "left": "50%", \
    #       "transform": "translate(-50%, -50%)"},
    className = "CENTRE_FORM_CONTAINER",
)

'''

"margin": "0px", "position": "absolute","top": "50%", "left": "50%", "transform": "translate(-50%, -50%)"


page_header_0 =  dbc.Row(
            [
                dbc.Col(
                    html.P("DM Tools Plotter", className="HEADER_TEXT"),
                    width=12,
                    className = "HEADER_COLUMN",
                ),
            ] , ##className="PAGE_HEADER_0",
                justify="center",
        )

'''
page_header_0 = dbc.Row(
            [
                dbc.Col(html.Div("One of three columns"), width=4),
                dbc.Col(
                    html.Div("DM Tools Plotter", className="HEADER_TEXT"), width=4
                        ),
                dbc.Col(html.Div("One of three columns"), width=4),
            ],
    className="PAGE_HEADER_0",
        )



page_header_1 =  dbc.Row(
            [
                dbc.Col(
                    html.P("Need Help", className="HEADER_TEXT"),
                    width=3,
                    className = "HEADER_COLUMN",
                ),
                dbc.Col(
                    html.P("FAQ",className="HEADER_TEXT"),
                    width=3,
                    className = "HEADER_COLUMN",
                ),
                dbc.Col(
                    html.P("Found A Bug", className="HEADER_TEXT"),
                    width=3,
                    className = "HEADER_COLUMN",
                ),
                dbc.Col(
                    html.P("What's New", className="HEADER_TEXT"),
                    width=3,
                    className = "HEADER_COLUMN",
                ),
            ],
            className="PAGE_HEADER_1",
        )

##header1 = html.Div(
page_header_1 =  dbc.Row(
            [
                dbc.Col(
                    html.P("Need Help", className="HEADER_TEXT"),
                    width=3,
                    className = "HEADER_COLUMN",
                ),
                dbc.Col(
                    html.P("FAQ",className="HEADER_TEXT"),
                    width=3,
                    className = "HEADER_COLUMN",
                ),
                dbc.Col(
                    html.P("Found A Bug", className="HEADER_TEXT"),
                    width=3,
                    className = "HEADER_COLUMN",
                ),
                dbc.Col(
                    html.P("What's New", className="HEADER_TEXT"),
                    width=3,
                    className = "HEADER_COLUMN",
                ),
            ],
            className="PAGE_HEADER_1",
        )

#header2 = html.Div(
page_header_2 = dbc.Row(
            [
                dbc.Col(
                    html.P("Plots", className="HEADER_TEXT"),
                    width=3,
                    className = "HEADER_COLUMN",
                ),
                dbc.Col(
                    html.P("Data",  className="HEADER_TEXT"),
                    width=3,
                    className = "HEADER_COLUMN",
                ),
                 dbc.Col(
                    html.P("Logged in as pauser (log out)", className="HEADER_TEXT"),
                    width=6,
                    className = "HEADER_COLUMN",
                 ),
            ],
            className="PAGE_HEADER_2",
        )
##, style=HEADER_STYLE,)

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