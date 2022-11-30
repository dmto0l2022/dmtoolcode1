from dash import html

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



'''

class PageFrame():
    
    def __init__(self):
        self.data = []
        self.l_sidebar_text = 'L Var'
        self.r_sidebar_text = 'R Var'
        self.l_sidebar = html.Div(children="L",className="col col-lg-1 PAGE_NOPADDING PAGE_SIDEBAR",)
        self.r_sidebar = html.Div(children="R",className="col col-lg-1 PAGE_NOPADDING PAGE_SIDEBAR",)
        self.GetSideBars()
   
    def GetSideBars(self):

        self.l_sidebar =  html.Div(children=self.l_sidebar_text,
                                      className="col col-lg-1 PAGE_NOPADDING PAGE_SIDEBAR",)
        self.r_sidebar =  html.Div(children=self.r_sidebar_text,
                                      className="col col-lg-1 PAGE_NOPADDING PAGE_SIDEBAR",)
    
    
