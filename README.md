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

## Useful Sample Codes for arcpy
1. Print a list of feature datasets and feature classes
-----------------
    import arcpy
        arcpy.env.workspace="C:/gis03/ex01/ex01.gdb"  
        dataset=arcpy.ListDatasets("*","Feature")
        for data in dataset:
            print("Feature datasets: "+data)
            fcList=arcpy.ListFeatureClasses("*","",data)
            for fc in fcList:
                print(fc)
-----------------------

2. Print a list of field names of a feature class
--------------------
    fc="watergate"
    field_names=[f.name for f in arcpy.ListFields(fc)]
    print("field names is {0}".format(field_names))
--------------------

