# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 11:41:24 2018

@author: oc3512
"""

import arcpy

# Assignment: make a shapefile for each amenity within El Salvador

try:
    arcpy.env.overwriteOutput=True
    arcpy.env.workspace="C:/Users/oc3512/Documents/ArcGIS/Projects/Python_practice/Project3"
    
    # Define names
    country="El Salvador"
    amenities=["school","hospital","place_of_worship"]
    newValue="OpenStreetMap"
    
    # check feature classes in the workspace folder
    featureList=arcpy.ListFeatureClasses()
    for feature in featureList:
        print("{0}".format(feature))   
    
    # shape file
    CentralAmerica="CentralAmerica.shp"
    OSMpoints="OSMpoints.shp"
    hospital="hospital.shp"
    school="school.shp"
    place_of_worship="place_of_worship.shp"
    newShapeFiles=(hospital,school,place_of_worship)
    
    # check field names for each shapefile
    fieldList=[f.name for f in arcpy.ListFields(CentralAmerica)]
    for field in fieldList:
        print("{0}".format(field))
    
    fieldList=[f.name for f in arcpy.ListFields(OSMpoints)]
    for field in fieldList:
        print("{0}".format(field))
    
    # Get country names from CentralAmerica
    with arcpy.da.SearchCursor(CentralAmerica,("NAME",)) as cursor:
        for row in cursor:
            print("{0}".format(row))
    
    with arcpy.da.SearchCursor(OSMpoints,("amenity",)) as cursor:
        for row in cursor:
            print("{0}".format(row))
    
    # Make a feature layer for a country El Salvador
    arcpy.MakeFeatureLayer_management(CentralAmerica,"El_SalvadorLayer",'"NAME"='+"'"+country+"'")
    arcpy.MakeFeatureLayer_management(OSMpoints,"amenitiesLayer")
    
    for amenity in amenities:        
        # Make a feature layer for each amenity selected
        arcpy.MakeFeatureLayer_management("amenitiesLayer","selectedAmenity",'"amenity"='+"'"+amenity+"'")
        
        # Select each amenity only within a El Salvador
        arcpy.SelectLayerByLocation_management("selectedAmenity","CONTAINED_BY","El_SalvadorLayer")
        
        # Copy
        arcpy.CopyFeatures_management("selectedAmenity",amenity)
        
    # Note that you cannot add field on a Layer! i.e. CopyFeature first then add field on a new feature class

    # Add a new field: "source"
    for shapes in newShapeFiles:
        arcpy.AddField_management(shapes,"source","TEXT")
        with arcpy.da.UpdateCursor(shapes,("source",)) as cursor:
            for row in cursor:
                row[0]=newValue
                cursor.updateRow(row)

    # Delete 
    arcpy.Delete_management("selectedAmenity")

except:
    arcpy.GetMessage()

arcpy.Delete_management("El_SalvadorLayer")
arcpy.Delete_management("amenitiesLayer")
arcpy.Delete_management("selectedAmenity")
    

    
    
