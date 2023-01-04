from dash import html
from dash import dcc
import dash
import dash_bootstrap_components as dbc



'''
class MyClass():
    def __init__(self, filename):
        self.filename = filename 

        self.stat1 = None
        self.stat2 = None
        self.stat3 = None
        self.stat4 = None
        self.stat5 = None
        self.parse_file()

    def parse_file(self):
        #do some parsing
        self.stat1 = result_from_parse1
        self.stat2 = result_from_parse2
        self.stat3 = result_from_parse3
        self.stat4 = result_from_parse4
        self.stat5 = result_from_parse5



import dash
from dash import html
import dash_bootstrap_components as dbc


def sidebar():
    return html.Div(
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
                if page["path"].startswith("/topic")
            ],
            vertical=True,
            pills=True,
            className="bg-light",
        )
    )

'''

class PageFrame():
    
    def __init__(self):
        self.data = []
        self.l_sidebar_text = 'L Var',
        self.r_sidebar_text = 'R Var'
        self.headertext = "Dark Matter Tool"
        self.footertext = "ACG"
        self.page_l_sidebar = html.Div(children="L",className="PAGE_NOPADDING PAGE_SIDEBAR",)
        self.page_l_sidebar_component = html.Div(children="L",className="PAGE_NOPADDING PAGE_SIDEBAR",)
        self.page_r_sidebar = html.Div(children="R",className="PAGE_NOPADDING PAGE_SIDEBAR",)
        self.page_header =  html.Div(children="Header",className = "PAGE_HEADER PAGE_NOPADDING",)
        self.page_footer =  html.Div(children="Footer",className = "PAGE_FOOTER PAGE_NOPADDING",)
        self.content_frame = []
        self.GetSideBars()
        self.GetHeaderAndFooter()
        self.PopulateFrame()
        
    def SetSideBarComponents(self, SideBarComponent_in):
        self.page_l_sidebar_component = SideBarComponent_in
        self.page_l_sidebar = html.Div(self.page_l_sidebar_component, className="PAGE_NOPADDING PAGE_SIDE_LEFT",)
   
    def GetSideBars(self):

        self.page_l_sidebar =  html.Div(children=self.l_sidebar_text,
                                      className="PAGE_NOPADDING PAGE_SIDE_LEFT",)
        #self.page_l_sidebar = self.page_l_sidebar_component
        self.page_r_sidebar =  html.Div(children=self.r_sidebar_text,
                                      className="PAGE_NOPADDING PAGE_SIDE_RIGHT",)
        
    
    def GetHeaderAndFooter(self):

        hdivs = html.P(self.headertext)
        header1 = html.Div([hdivs], className = "FULL_DIV PAGE_NOPADDING",)

        fdivs = [html.P(self.footertext)]

        footer1 = html.Div(fdivs, className = "FULL_DIV PAGE_NOPADDING",)

        self.page_header =  html.Div(children=[header1],className = "PAGE_HEADER PAGE_NOPADDING",)

        self.page_footer =  html.Div(children=[footer1],className = "PAGE_FOOTER PAGE_NOPADDING",)
        
    def PopulateFrame(self):
        self.content_frame = [self.page_header,self.page_l_sidebar,self.page_r_sidebar,self.page_footer]
        

    
    
