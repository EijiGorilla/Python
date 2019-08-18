# -*- coding: utf-8 -*-
"""
Created on Thu May 30 10:16:16 2019

@author: oc3512
"""

import arcpy
import os
from arcpy.sa import *

arcpy.env.OverwriteOutput=True

#if arcpy.CheckExtension("Spatial") == "Available":
#    arcpy.CheckOutExtension("Spatial")
#else:
#    raise LicenseError
    
# Set Parameters
workSpace=arcpy.GetParameterAsText(0) # Workspace
lineFeature=arcpy.GetParameterAsText(1) # Feature Set
elvInterval=arcpy.GetParameterAsText(2) # Linear Unit
dem=arcpy.GetParameterAsText(3) # Raster Layer
#output=arcpy.GetParameterAsText(3) # Table geodatabase

# Generate points along the lineFeature
outFC="distance_interval"
Points=arcpy.GeneratePointsAlongLines_management(lineFeature,outFC,'DISTANCE',elvInterval)

# Extract DEM values from the Points
elevPoints=ExtractMultiValuesToPoints(Points,dem,"BILINEAR") # need bilinear?
#elevPoints=ExtractMultiValuesToPoints(Points,dem,"NONE") # need bilinear?

# Add X, Y coordinates
arcpy.AddXY_management(elevPoints)

# Copy and add Field
#outFiles="temp"
#elevPointsCopy=arcpy.CopyFeatures_management(elevPoints,outFiles)
#arcpy.AddField_management(elevPointsCopy,field_name="Distance",field_type="long")
fieldName="Distance"
arcpy.AddField_management(elevPoints,field_name=fieldName,field_type="long")

#fieldNames=[f.name for f in arcpy.ListFields(inputTable)]

# Get total records
nRow=int(arcpy.GetCount_management(elevPoints).getOutput(0)) 

# Obtain integer values of points interval along the line
interVal=[int(s) for s in elvInterval.split() if s.isdigit()][0]

# update field
n=0
with arcpy.da.UpdateCursor(elevPoints,[fieldName,]) as cursor:
    for row in cursor:
        row[0]=n
        n=n+interVal
        cursor.updateRow(row)
#
elevPoints1=ExtractMultiValuesToPoints(elevPoints,dem,"BILINEAR")

# Copy
outFile=os.path.join(workSpace,"ElevationProfileTable")
arcpy.CopyFeatures_management(elevPoints1,outFile)

        
del Points
del elevPoints
del outFile

#arcpy.CheckInExtension("Spatial")
