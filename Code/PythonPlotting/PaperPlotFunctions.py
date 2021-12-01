"""
Created on Tue Dec  3 17:12:46 2019

@author: Christian
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd



# Style Variables
ExperimentStyle = {'linewidth':2, 'linestyle':'-','color':'C1'}
AnalysisStyle = {'linewidth':1, 'linestyle':'--','color':'C0'}


def PlotValue(AnalysisName, RecorderName, Position):
    
    DisplacementFileName = AnalysisName + RecorderName
    
    
    
    BaseDirectory=os.getcwd()
    DisplacementDirectory = "%s\%s" %(BaseDirectory, DisplacementFileName)
    DisplacementData = np.loadtxt(DisplacementDirectory,delimiter=' ')
    XData = DisplacementData[:,0]
    YData = DisplacementData[:,Position]
    fig, ax = plt.subplots()
    line1, = ax.plot(XData,YData, Label=RecorderName)
    plt.title( AnalysisName + RecorderName)
    
    
    
    


    
def PlotVaribleData(InputX, InputY, AnalysisLabel, 
                    ExperimentX=0, ExperimentY=0, ExperimentLabel=0, 
                    AxisLabel = 0, PlotTitle=0, legend=0, grid=0, limits=0,
                    OutputSize=0, SaveFile=0, dpi=300, OutputName=0):
    """
    Parameters
    ----------
    InputX : array
        The X data to be plotted.
        
    InputY : array
        The Y data to be plotted.   
        
    AnalysisLabel : string
        The name of the analysis data. Used to Label analysis data.
        
    ExperimentX : array
        The Experimental x data to be plotted (optional.)   
                
    ExperimentY : array
        The Experimental y data to be plotted (optional.)   
                
    ExperimentLabel : string
        The name of the Experiment data. Used to Label analysis data. 
        (optional.) 
                
    AxisLabel : list of strings
        The name of each axis (optional.) 
                
    legend : string
        This turns the chart legend on or off. 'y' =  on (optional.) 
                        
    grid : string
        This turns the chart grid on or off. 'y' =  on (optional.) 

    limits : array [xmin,xmax,ymin,ymax]
        The limits on the plot.
                        
    OutputSize : list [x,y]
        This specifies the output char size in inches (optional.) 
                        
    SaveFile : string
        This specifies if the file will be saved or not. 'y' =  saved 
        (optional.)         
    
    dpi : int
        This specifies the numper of pixels per inch of the output figure
        (optional.)       
        
    OutputName : int   
        This specifies the name of the output file (optional.)      
    
    """  
    
    
    # Create base Plot
    fig, ax = plt.subplots()
    
    # Plot experiment Data
    if hasattr(ExperimentX, "__len__"):
        line2, = ax.plot(ExperimentX,ExperimentY, label=ExperimentLabel, 
                         **ExperimentStyle) 
    
    #Plot Analysis Data
    line1, = ax.plot(InputX,InputY, label=AnalysisLabel, **AnalysisStyle)   
    
    #Plot Label    
    if AxisLabel != 0:
        plt.ylabel(AxisLabel[0])
        plt.xlabel(AxisLabel[1])
            
    if PlotTitle != 0:
        plt.title(PlotTitle)
        
    if legend == 'y':
        ax.legend(loc='lower right')

    if grid == 'y':
        ax.grid(True)
    
    if hasattr(limits, "__len__"):
        ax.set_xlim(limits[0],limits[1])
        ax.set_ylim(limits[2],limits[3])
        
    if OutputSize != 0:
        fig.set_size_inches(OutputSize[0], OutputSize[1])        
    
    if SaveFile == 'y':
        if dpi==0 or OutputName == 0:
            raise Exception('There has been an error in the system')
        plt.savefig(OutputName, dpi=dpi)
    
    plt.show()    




def PlotFileData(InputXName, InputYName, AnalysisLabel, PositionData,
                 ExperimentXName=0, ExperimentYName=0, ExperimentLabel=0, 
                 AxisLabel = 0, PlotTitle=0, legend=0, grid=0, limits=0,
                 OutputSize=0, SaveFile=0, dpi=300, OutputName=0):
    """

    Parameters
    ----------
    InputXName : string
        The file name for the analysis X data to be plotted.
        
    InputYName : string
        The file name for the analysis Y data to be plotted.
        
    AnalysisLabel : string
        The name of the analysis data. Used to Label analysis data.

    PositionData : list, ints [x,y,experimetnx,experimenty]
        The column location of the desired analysis and experiment data.
        
    ExperimentX : string
        The file name for the xperimental x data to be plotted (optional.)   
                
    ExperimentY : string
        The file name for the xperimental y data to be plotted (optional.)   
                
    ExperimentLabel : string
        The name of the Experiment data. Used to Label analysis data. 
        (optional.) 
                
    AxisLabel : list of strings
        The name of each axis (optional.) 
                
    legend : string
        This turns the chart legend on or off. 'y' =  on (optional.) 
                        
    grid : string
        This turns the chart grid on or off. 'y' =  on (optional.) 

    limits : array [xmin,xmax,ymin,ymax]
        The limits on the plot.
                        
    OutputSize : list [x,y]
        This specifies the output char size in inches (optional.) 
                        
    SaveFile : string
        This specifies if the file will be saved or not. 'y' =  saved 
        (optional.)         
    
    dpi : int
        This specifies the numper of pixels per inch of the output figure
        (optional.)       
        
    OutputName : int   
        This specifies the name of the output file (optional.)      
    
    """  
    
    
    
    # Get base directory    
    BaseDirectory=os.getcwd()
    
    # Read Input data
    XDirectory = "%s\%s" %(BaseDirectory, InputXName)
    YDirectory = "%s\%s" %(BaseDirectory, InputYName)
    
    XData = np.loadtxt(XDirectory,delimiter=' ')  
    YData = np.loadtxt(YDirectory,delimiter=' ') 
    
    InputX = XData[:,PositionData[0]]
    InputY = YData[:,PositionData[1]]
    
    # Get Experiment Data    
    if ExperimentXName != 0:
        EXDirectory = "%s\%s" %(BaseDirectory, ExperimentXName)
        EYDirectory = "%s\%s" %(BaseDirectory, ExperimentYName)
        
        EXData = np.loadtxt(EXDirectory,delimiter=',')  
        EYData = np.loadtxt(EYDirectory,delimiter=',') 

        ExperimentX = EXData[:,PositionData[2]]
        ExperimentY = -EYData[:,PositionData[3]]/4
    
    # Create base Plot
    fig, ax = plt.subplots()
    
    # Plot experiment Data
    if ExperimentXName != 0:
        line2, = ax.plot(ExperimentX,ExperimentY, label=ExperimentLabel, 
                         **ExperimentStyle) 
    
    #Plot Analysis Data
    line1, = ax.plot(InputX,InputY, label=AnalysisLabel, **AnalysisStyle)   
    
    #Plot Label    
    if AxisLabel != 0:
        plt.ylabel(AxisLabel[0])
        plt.xlabel(AxisLabel[1])
            
    if PlotTitle != 0:
        plt.title(PlotTitle)
        
    if legend == 'y':
        ax.legend(loc='lower right')

    if grid == 'y':
        ax.grid(True)
    
    if hasattr(limits, "__len__"):
        ax.set_xlim(limits[0],limits[1])
        ax.set_ylim(limits[2],limits[3])
        
    if OutputSize != 0:
        fig.set_size_inches(OutputSize[0], OutputSize[1])        
    
    if SaveFile == 'y':
        if dpi==0 or OutputName == 0:
            raise Exception('There has been an error in the system')
        plt.savefig(OutputName, dpi=dpi)
    
    plt.show()  


