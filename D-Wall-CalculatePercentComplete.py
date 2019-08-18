# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:00:31 2019

@author: oc3512
"""

import arcpy
from collections import Counter
import ListNamesFeatureClass

arcpy.env.overwriteOutput = True

# Choose parameters
structureT=arcpy.GetParameterAsText(0)
panelT=arcpy.GetParameterAsText(1)

structureT="C:/Users/oc3512/Documents/ArcGIS/Projects/MMSP/001-CIVIL.gdb/D_Wall/DWallArea"

arcpy.env.workspace = "C:/Users/oc3512/Documents/ArcGIS/Projects/MMSP/001-CIVIL.gdb"

# Print to the Interactive window all the feature datasets in the
#   workspace that start with the letter C.
datasets = arcpy.ListDatasets("*", "Feature")

for dataset in datasets:
    print(dataset)

##
import arcpy  
import os  
  
arcpy.env.workspace = r"C:/Users/oc3512/Documents/ArcGIS/Projects/MMSP/001-CIVIL.gdb" 

#  
datasets = arcpy.ListDatasets(feature_type='feature')  
datasets = [''] + datasets if datasets is not None else []   
fc=arcpy.ListFeatureClasses(feature_dataset=datasets[2])

structureT=fc[0]

def listFieldNames(table):
    import arcpy
    fieldNames=[f.name for f in arcpy.ListFields(table)]
    return fieldNames

listFieldNames(structureT)


##



# For each structure_ID, calculate % progress

with arcpy.da.UpdateCursor(structureT, "Completion") as cursor:
    for row in cursor:
        for n in # of structure ID:
        tempT=filter(structureT, "structure_ID"==n) 
        percValue=
        row[0] = percValue
        cursor.updateRow(row)

# Update "Completion" field
        
del tempT
del percValue

words = [1,2,3,4,1]
unique_words = set(words)             # == set(['a', 'b', 'c'])
unique_word_count = len(unique_words) # == 3

