# Python
1. General Instructions and codes to use Python in RStudio
2. Information on other education materials to learn Python in GIS

* Use "Spyder" embedded in "Anaconda", Python use-interface, if prefer to RStudio

## Python in General
### Python manager for ArcGIS
Use Spyder in Anaconda when coding for ArcGIS so you can code arcpy in Spyder
Read the followings for environmental settings
* Go to Python setting in ArcGIS Pro
* Create new environment (the new environment will be linked to e.g., C:\Users..\AppData\Local\ESRI\conda\envs\new-environment)

### DataCamp
https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-1-python-basics?ex=5

## Python in ArcGIS
https://www.e-education.psu.edu/geog485/node/17
* Lesson3 Project datasets are stored in "Project3" folder. My script for the Project is saved "project3.py".
## Useful Sample Codes for arcpy
1. Print a list of feature datasets and feature classes
-----------------
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
    import arcpy
    fieldNames=[f.name for f in arcpy.ListFields(table)]
    return fieldNames
-----------------------

## Map Documents for ArcGIS Pro
* Tutorial
http://pro.arcgis.com/en/pro-app/arcpy/mapping/tutorial-getting-started-with-arcpy-mp.htm
