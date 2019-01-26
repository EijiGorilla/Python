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

## Useful Python Code
---------------------------------------------------------
import arcpy
import ListNamesFeatureClass

try:
    arcpy.env.workspace="C:/Users/oc3512/Documents/ArcGIS/Projects/Python_practice/output"
    arcpy.env.overwright=True
    
    # open gdb
    inFiles="C:/Users/oc3512/Documents/ArcGIS/Projects/Python_practice/USA.gdb"
    
    # check what feature class in the gdb file
    featureClass=ListNamesFeatureClass.listFeatureClassNames(inFiles)
    boundaries="Boundaries"
    
    # Make a feature layer
    arcpy.MakeFeatureLayer_management(boundaries,"testBoundary")
    
    # Copy (i.e., generate and save) as a new feature class (you cannot manipulate field with a feature layer)
    arcpy.CopyFeatures_management("testBoundary","NewBoundary")
    
    # Add Field
    arcpy.AddField_management("allBoundary", "ref_ID", "TEXT", "", "", "", "refID", "NULLABLE", "REQUIRED")
    
    # Set Local variables
    inTable="newBoundary"
    fieldName="ref_ID"
    expression="reclass(!Shape_Area!,!ref_ID!)"
    
    codeblock="""
    def reclass(Area,ID):
        if Area > 250:
            c="A"
        else:
            c="B"
        return c"""
    
    # Execute CalculateField
    arcpy.CalculateField_management(inTable,fieldName,expression,"PYTHON3",codeblock)

except:
    arcpy.GetMessage()
    
arcpy.Delete_management("allBoundary")
---------------------------------------------------------

## Map Documents for ArcGIS Pro
* Tutorial
http://pro.arcgis.com/en/pro-app/arcpy/mapping/tutorial-getting-started-with-arcpy-mp.htm
