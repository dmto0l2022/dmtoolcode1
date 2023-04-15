
# New Plot


Row 10
    Header
    Need Help
    FAQ
    Found A Bug
    What's New
Row 2
    Plots
    Data
  
All Plots

New Plot
    Name : Enter Plot Name
Code

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

# Edit Plot

Plot Name : Testing

x range (WIMP mass)  lower bound: 1  to upper bound : 1000 GeV/c^2
y range (cross-section) smallest c-s: 10^ : -46 [text entry] to largest c-s: 10^ : -31 [text entry] cm^2 dropdown

remember: a larger negative exponent results in a smaller limit! (and vice versa)

[X] Check to remove site address/names from plot

[Save] [Save & Render]

Table - multiple results allowed
[Remove] Result Reference PlotAppearance Color

Search for limits : Text box

5 Column Dropdown

Type Spin Experiment Year GreatestHits

Result Page Navigation <<Previous>> <<Next>>

Table

[Add] Result Reference

Fields

  Edit Limit

  Upload xml file [browse] No File selected

  Load Limit from File

  XML upload examples and info on XML file uploads can be found here

  Data Label : DAMA...

  show example
  Data labels must be less than 60 characters long

  Data Reference : <a ref....

  Data Comment : 

  show reference example
  show comment example

  Experiment: Dropdown of Experiments

  Date of Announcement : Date input

  Year : 2009

  Y rescale 1e-36
  show example

  X rescale 1
  show example
  
  Data Values : big text field
  show example

  More Data Formatting Help

  Result Type Experiment Drop Down
  Spin Dependency :
  Measurement Type :
  [why]

  By checking the box below, you make this limit viewable by any user
  Public [X]

  The Following Users will be able to view and edit this limit.
  Enter logins separated by commas
  To remove a login put a dash before the login.
  Other users : big text field

  [Save Button]

# List All Limits

6 Columns with Drop Down
Official Type Spin Experiment Year Greatest Hits

Table
Result Reference [Show] [Edit] [Copy] [Destroy]

# Listing Plots

  Table
  PlotName [Show] [Edit] [Copy] [Destroy] FullTimeStamp

[All Limits]

# New Limit

Upload xml file [Browse] No File Selected
[Load Limit from File]

XML upload examples and info on XML file uploads can be found [here]

Data Label: large text field
show example
Data labels must be less than 60 characters long

Data reference : big text field
show reference example

Data comment: big text field
show comment example

Experiment: Dropown

Date of Announcement : Select Date
Year : Year Field

Y rescale : 1
show example
X rescale : 1
show example

Data Values : Large Text Field
show example

[More Data Formatting Help]

Result Type [DropDown]
Spin Dependency [DropDown]
Measurement Type [Dropdown]

By checking the box below, you make this limit viewable by any user.
Public [X]

The following users will be able to view and edit this limit.
Enter logins separated by commas.
To remove a user put a dash before the login.

Other users: Large Text Box

[Save]

# Show Existing

Data Label : 
Data Reference :
Data Comment :

Result Type :
Spin Dependency :

[Nominate for Greatest Hits] [Recant Nomination]

Download in [XML] Format
                      
# Form Help & References                      

https://dash-bootstrap-components.opensource.faculty.ai/docs/components/form/

https://github.com/facultyai/dash-bootstrap-components/issues/286

