# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 09:35:37 2019
This module create a user-defined script that gives a list of feature datasets,
feature class and/or list of fields.

@author: oc3512
"""
# 1. List of Feature class datasets and feature classes
## Note that featureclass datasets are only available for geodatabase
def listFeatureClassDatasetNames(gdb):
    import arcpy
    arcpy.env.workspace=gdb
    datasets=arcpy.ListDatasets("*","Feature")
    
    for data in datasets:
        return data
        fcList=arcpy.ListFeatureClasses(data)
        for fc in fcList:
            return fc

# List of feature class 
## note location can be a folder or geodatabase (.gdb) 
def listFeatureClassNames(location):
    import arcpy
    arcpy.env.workspace=location
    fcList=arcpy.ListFeatureClasses()
    for fc in fcList:
        return fc
        
# 2. List of field names of a feature class
def listFieldNames(table):
    fieldNames=[f.name for f in arcpy.ListFields(table)]
    return fieldNames