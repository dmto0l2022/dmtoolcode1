import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc


######################### fields ######################


# Plot Name - Text

plotname_input_row = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Label('Enter Plot Name :',className='FORM_COLUMN_LABEL'),
                    className='FORM_LABEL_COLUMN',
                    width=2
                ),
                dbc.Col(
                    dcc.Input(id='plotnameinputid', type='text',maxLength=10,
                                  className='FORM_COLUMN_TEXTINPUT'),
                    className='FORM_TEXTINPUT_COLUMN',
                    width=1
                ),
                dbc.Col(dcc.Input(id='example_textinput', type='text', value='example', readOnly=True,
                                  className='FORM_COLUMN_EXAMPLE'),
                    className='FORM_EXAMPLE_COLUMN',
                    width=1),
                dbc.Popover(
                    dbc.PopoverBody('enter plot unique name'),
                    target="textinput",trigger="hover"),
                dbc.Popover(dbc.PopoverBody('Plot of Experiment M'),
                    target="example_textinput",trigger="click"), 
                
            ],
        className='g-0'),
    ]
)


# X Range: Lower Bound - Text

xrangelower_input_row = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Label('Enter X Range Lower :',className='FORM_COLUMN_LABEL'),
                    className='FORM_LABEL_COLUMN',
                    width=2
                ),
                dbc.Col(
                    dcc.Input(id='xrangelowerid', type='text',maxLength=10,
                                  className='FORM_COLUMN_TEXTINPUT'),
                    className='FORM_TEXTINPUT_COLUMN',
                    width=1
                ),
                dbc.Col(dcc.Input(id='example_textinput', type='text', value='example', readOnly=True,
                                  className='FORM_COLUMN_EXAMPLE'),
                    className='FORM_EXAMPLE_COLUMN',
                    width=1),
                dbc.Popover(
                    dbc.PopoverBody('enter lower bound X'),
                    target="textinput",trigger="hover"),
                dbc.Popover(dbc.PopoverBody('12345'),
                    target="example_textinput",trigger="click"), 
                
            ],
        className='g-0'),
    ]
)


# Upper Bound - Text

xrangeupper_input_row = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Label('Enter X Range Upper :',className='FORM_COLUMN_LABEL'),
                    className='FORM_LABEL_COLUMN',
                    width=2
                ),
                dbc.Col(
                    dcc.Input(id='xrangeupperid', type='text',maxLength=10,
                                  className='FORM_COLUMN_TEXTINPUT'),
                    className='FORM_TEXTINPUT_COLUMN',
                    width=1
                ),
                dbc.Col(dcc.Input(id='example_textinput', type='text', value='example', readOnly=True,
                                  className='FORM_COLUMN_EXAMPLE'),
                    className='FORM_EXAMPLE_COLUMN',
                    width=1),
                dbc.Popover(
                    dbc.PopoverBody('enter upper bound X'),
                    target="textinput",trigger="hover"),
                dbc.Popover(dbc.PopoverBody('12345'),
                    target="example_textinput",trigger="click"), 
                
            ],
        className='g-0'),
    ]
)


# Scale - Dropdown

scale_input_row = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Label('Scale :',className='FORM_COLUMN_LABEL'),
                    className='FORM_LABEL_COLUMN',
                    width=2
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id='scaleid',
                        options=[{'label': k, 'value': v} for k, v in scaleDict.items()],
                        className='FORM_COLUMN_SCALE'
                        ),
                    className='FORM_SCALE_COLUMN',
                    width=1
                ),
                dbc.Col(dcc.Input(id='example_scale', type='text', value='example', readOnly=True,
                                  className='FORM_COLUMN_EXAMPLE'),
                    className='FORM_EXAMPLE_COLUMN',
                    width=1),
                dbc.Popover(
                    dbc.PopoverBody('enter scale'),
                    target="scaleid",trigger="hover"),
                dbc.Popover(dbc.PopoverBody('4'),
                    target="example_scale",trigger="click"), 
                
            ],
        className='g-0'),
    ]
)

# Trace Trace ID - Integer

traceid_input_row = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Label('Enter Number :',className='FORM_COLUMN_LABEL'),
                    className='FORM_LABEL_COLUMN',
                    width=2
                ),
                dbc.Col(
                    dcc.Input(id='traceidinput', type='number',
                                  className='FORM_COLUMN_TRACEID'),
                    className='FORM_TRACEID_COLUMN',
                    width=1
                ),
                dbc.Col(dcc.Input(id='example_traceid', type='text', value='example', readOnly=True,
                                  className='FORM_COLUMN_EXAMPLE'),
                    className='FORM_EXAMPLE_COLUMN',
                    width=1),
                dbc.Popover(
                    dbc.PopoverBody('enter traceid'),
                    target="traceidinput",trigger="hover"),
                dbc.Popover(dbc.PopoverBody('4'),
                    target="example_traceid",trigger="click"), 
                
            ],
        className='g-0'),
    ]
)

# Trace Name - Text

tracename_input_row = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Label('Enter Trace Name :',className='FORM_COLUMN_LABEL'),
                    className='FORM_LABEL_COLUMN',
                    width=2
                ),
                dbc.Col(
                    dcc.Input(id='tracenameinputid', type='text',maxLength=10,
                                  className='FORM_COLUMN_TEXTINPUT'),
                    className='FORM_TEXTINPUT_COLUMN',
                    width=1
                ),
                dbc.Col(dcc.Input(id='example_tracename', type='text', value='example', readOnly=True,
                                  className='FORM_COLUMN_EXAMPLE'),
                    className='FORM_EXAMPLE_COLUMN',
                    width=1),
                dbc.Popover(
                    dbc.PopoverBody('enter trace name'),
                    target="textinput",trigger="hover"),
                dbc.Popover(dbc.PopoverBody('Plot of Experiment M'),
                    target="example_tracename",trigger="click"), 
                
            ],
        className='g-0'),
    ]
)


# Trace Color - Dropdown Trace

tracecolor_input_row = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Label('Select Color :',className='FORM_COLUMN_LABEL'),
                    className='FORM_LABEL_COLUMN',
                    width=2
                ),
                dbc.Col(
                     dbc.Input(
                        type="color",
                        id="colorpicker",
                        value="#000000",
                     className='FORM_COLUMN_COLOR'
                    ),
                    className='FORM_COLOR_COLUMN',
                    width=1
                ),
                dbc.Col(dcc.Input(id='example_tracecolor', type='text', value='example', readOnly=True,
                                  className='FORM_COLUMN_EXAMPLE'),
                    className='FORM_EXAMPLE_COLUMN',
                    width=1),
                dbc.Popover(
                    dbc.PopoverBody('enter color'),
                    target="radioitemid",trigger="hover"),
                dbc.Popover(dbc.PopoverBody('red'),
                    target="example_tracecolor",trigger="click"), 
                
            ],
        className='g-0'),
    ]
)


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

# Measurement Type - Dropdown

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


