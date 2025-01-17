from io import StringIO
import pandas as pd

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


class DMTool():
    def __init__(self):
        self.mstring = StringIO("""x,y
          70,50
          90,100
          90,0
          70,0
          70,50
          60,25
          50,0
          30,50
          30,0
          10,0
          10,100
          30,100
          60,25
        """)
        
        self.mdf = pd.read_csv(self.mstring, sep=",")
        
        self.ostring = StringIO("""x,y
          50,0
          65,5
          80,15
          87,30
          90,50
          87,70
          80,90
          65,97
          50,100
          60,85
          65,70
          67,65
          70,50
          67,35
          65,25
          60,12
          50,0
          """)
       
        self.ReadLetterO()
    
        self.tstring = StringIO("""x,y
          10,80
          10,100
          90,100
          90,80
          60,80
          60,0
          40,0
          40,80
          10,80
          """)
    
        self.tdf = pd.read_csv(self.tstring, sep=",")
    
        self.lstring = StringIO("""x,y
          10,0
          100,0
          100,20
          30,20
          30,100
          10,100
          10,0
          """)
    
        self.ldf = pd.read_csv(self.lstring, sep=",")
    
        self.dstring = StringIO("""x,y
          30,0
          65,5
          90,25
          100,50
          90,75
          65,95
          30,100
          60,85
          75,75
          80,50
          75,35
          60,15
          30,0
          10,0
          10,100
          30,100
          30,0
          """)
    
        self.ddf = pd.read_csv(self.dstring, sep=",")
    
        self.MakeDMTool()
    
    #################################
    def ReadLetterO(self):
        
        odf_stage = pd.read_csv(self.ostring, sep=",")
        
        odf_out = odf_stage.copy()
        
        def reflectx(x_in):
            return 50 - (x_in-50)

        odf_out['x'] = odf_out['x'].apply(reflectx)
        
        #odf_out['x'] = 50 - (odf_out['x']-50)
        
        #odf_out = odf_out.assign(x=50)
        
        odf_out = pd.concat([odf_out, odf_stage])
        self.odf = odf_out
   
    def MakeDMTool(self):
        
        def add100(x_in):
            return (x_in + 100)
        
        dmtool_out = self.ddf.copy()
        
        dmtool_out['letter'] = 'd'
        
        #"M"
        df_working = self.mdf.copy()
        df_working['letter'] = 'm'
        
      

        df_working['x'] = df_working['x'].apply(add100)
        
        dmtool_out = pd.concat([dmtool_out, df_working])
        
        #"T"
        
        df_working = self.tdf.copy()
        df_working['letter'] = 't'

        df_working['x'] = df_working['x'].apply(add100)
        df_working['x'] = df_working['x'].apply(add100)
        
        dmtool_out = pd.concat([dmtool_out, df_working])
        
        #"O1 & O2"
        
        df_working = self.odf.copy()
        df_working['letter'] = 'o1'

        df_working['x'] = df_working['x'].apply(add100)
        df_working['x'] = df_working['x'].apply(add100)
        df_working['x'] = df_working['x'].apply(add100)
        
        dmtool_out = pd.concat([dmtool_out, df_working])
        
        df_working['letter'] = 'o2'
        df_working['x'] = df_working['x'].apply(add100)
        
        dmtool_out = pd.concat([dmtool_out, df_working])
        
        #"L"
        
        df_working = self.ldf.copy()
        df_working['letter'] = 'l'

        df_working['x'] = df_working['x'].apply(add100)
        df_working['x'] = df_working['x'].apply(add100)
        df_working['x'] = df_working['x'].apply(add100)
        df_working['x'] = df_working['x'].apply(add100)
        df_working['x'] = df_working['x'].apply(add100)
        
        dmtool_out = pd.concat([dmtool_out, df_working])
        
        ## out
        
        self.dmtdf = dmtool_out
        