# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 10:48:47 2019

This script is used to publish a feature layer to ArcGIS Online (share as or overwrite web layer)


@author: oc3512
"""

import arcpy
import os, sys
from arcgis.gis import GIS

### Start setting variables
# Set the path to the project

prjDir=arcpy.GetParameterAsText(0) # parameter: Workspace,'C:/Users/oc3512/Documents/ArcGIS/Projects/MMSP'
prjPath=arcpy.GetParameterAsText(1) #"C:/Users/oc3512/Documents/ArcGIS/Projects/MMSP/MMSP.aprx"
inMap=arcpy.GetParameterAsText(2) # parameter: Map
shareLayer=arcpy.GetParameterAsText(3) # parameter: layer feature, table view?

# Update the following variables to match:
# Feature service/SD name in arcgis.com, user/password of the owner account
portal = "http://www.arcgis.com" # Can also reference a local portal
user = "eijimatsuzaki1"
password = "timberland12345"

# Local paths to create temporary content
sd_fs_name=os.path.splitext(os.path.basename(shareLayer))[0]
sddraft=os.path.join(prjDir,sd_fs_name + ".sddraft")
sd=os.path.join(prjDir,sd_fs_name + ".sd")

# Create a new SDDraft and stage to SD
print("Creating SD file")
arcpy.env.overwriteOutput = True
prj = arcpy.mp.ArcGISProject(prjPath)
mp = prj.listMaps(inMap)[0]
lyr=mp.listLayers(sd_fs_name)[0]

arcpy.mp.CreateWebLayerSDDraft(lyr, sddraft, sd_fs_name, 'MY_HOSTED_SERVICES', 'FEATURE_ACCESS',"", True, True)
arcpy.StageService_server(sddraft, sd)
arcpy.UploadServiceDefinition_server(sd, 'My Hosted Services',"","",'','Land Acquisition & Resettlement')

del prj
del mp
del lyr
