# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:49:48 2019

@author: oc3512
"""

# import system modules
import arcpy

# Set environment settings
arcpy.env.overwriteOutput=True

# Set local variables
in_features=arcpy.GetParameterAsText(0) # in_features: feature layer (parameter), choose point feature

#in_features="C:/Users/oc3512/Documents/ArcGIS/Projects/MMSP/MMSP_utm.gdb/MMSP_Stations_utm"

properties="POINT_X_Y_Z_M" # properties: string (parameter), choose "POINT_X_Y_Z_M"
length_unit = ""
area_unit = ""

# CHoose coordinate of your interest
## To generate UTM: choose "UTM" coordinates
## TO generate lat, long: choose "GCS_WGS_1984"

#coordinate=arcpy.Describe(in_features).spatialReference.Name
coordinate1=arcpy.SpatialReference(32651)
coordinate2=arcpy.SpatialReference(4326)

# Generate UTM coordinates
output=arcpy.AddGeometryAttributes_management(in_features, properties, length_unit, area_unit, coordinate1)

# Rename the field
## As field names are overwriten every time different coordinates are added, we need to 
## change the field names:

fieldNames = [f.name for f in arcpy.ListFields(output)]

if "X" in fieldNames:
    print("")
else:
    output=arcpy.AlterField_management(output, 'POINT_X', 'X', '')
    output=arcpy.AlterField_management(output, 'POINT_Y', 'Y', '')

# Generate lat and long
output1=arcpy.AddGeometryAttributes_management(output, properties, length_unit, area_unit, coordinate2)

#arcpy.CopyFeatures_management(output1, in_features+"_TEST")

# Add different coordinate format from the above table
x_field="POINT_X"
y_field="POINT_Y"
input_coordinate="DD_2"
output_coordinate="DD_1"
#out_pts = "C:/Users/oc3512/Documents/ArcGIS/Projects/MMSP/MMSP_utm.gdb/MMSP_Stations_utm333"
out_pts=arcpy.GetParameterAsText(1) # output: feature class
arcpy.ConvertCoordinateNotation_management(output1, out_pts, x_field, y_field, input_coordinate, output_coordinate)