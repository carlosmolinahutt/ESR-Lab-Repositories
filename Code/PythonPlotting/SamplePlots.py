"""
Created on Tue Dec  3 19:12:31 2019

@author: Christian
"""
import numpy as np
import PaperPlotFunctions as PF




# Sample Input Variables
ExperimentX = np.array([1,2,3,4,5])
ExperimentY = np.array([1,2,3,4,5])**2    
InputX = np.array([1,2,3,4,5])
InputY = np.array([1,2,3,4,5])**2 + np.sin(ExperimentX)
limits = 1.1*np.array([np.min(ExperimentX),np.max(ExperimentX),
                      np.min(ExperimentY),np.max(ExperimentY)])

PlotTitle = "My Test Plot"
AnalysisLabel = "OpenSees"
ExperimentLabel = "Experiment"
AxisLabel = ["BaseShear KN" , "Drift (m)"]

OutputSize = [8.25, 5.5]
dpi = 300
grid = 'n'
legend = 'y'

SaveFile = 'y'
OutputName = 'FileOutput.jpeg'


PF.PlotVaribleData(InputX, InputY, AnalysisLabel, ExperimentX, ExperimentY, 
                ExperimentLabel, AxisLabel, PlotTitle, legend, grid, limits,
                OutputSize, SaveFile, dpi, OutputName)



# %%


InputXName = 'GM5_Reaction_W1.out'
InputYName = 'GM5_Reaction_W1.out'
ExperimentXName = 'GM5_Experiment_Shear.csv'
ExperimentYName = 'GM5_Experiment_Shear.csv'

limits = [10,30,-100000,100000]

PositionData = np.array([0,1,0,1])

PF.PlotFileData(InputXName, InputYName, AnalysisLabel,PositionData, 
                ExperimentXName, ExperimentYName, ExperimentLabel, AxisLabel, 
                PlotTitle, legend, grid, limits, 
                OutputSize, SaveFile, dpi, OutputName)
