# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 09:27:36 2019

@author: oc3512
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:48:19 2019

@author: oc3512
"""

import arcpy
import os
import fnmatch
import glob

arcpy.env.overwriteOutput=True

# Set parameters
#workSpace="C:/Users/oc3512/Documents/ArcGIS/Projects/MMSP/001-CIVIL.gdb"
#dataDir="C:/Users/oc3512/Documents/ArcGIS/Projects/MMSP/001-CIVIL/04-Tunneling/CP101/TBM"
#TBM="C:/Users/oc3512/Documents/ArcGIS/Projects/MMSP/001-CIVIL.gdb/TBM_Drawing_1"

workSpace=arcpy.GetParameterAsText(0) # Workspace
dataDir=arcpy.GetParameterAsText(1)
#TBM=arcpy.GetParameterAsText(2)

dirPath=os.path.join(dataDir,"*.csv")
out_path=workSpace

# Choose only files of interest:
tables=glob.glob(dirPath)
patterns=['*excavation*','*backfill*','*face*','*subside*','*tolera*']

for pattern in patterns:
    for name in fnmatch.filter(tables, pattern):
        #name=fnmatch.filter(tables,pattern)[0]
        out_name=os.path.splitext(os.path.basename(name))[0] # remove.csv
        # Delete file deodatabase table
        arcpy.Delete_management(out_name)
        
        # Run table to table conversion (convert csv to gdb table)
        desti=arcpy.TableToTable_conversion(name,workSpace,out_name)
        
        # Generate relationship class with TBM drawings for each table
        #originTBM=os.path.splitext(os.path.basename(TBM))[0]
        #out_reclass=os.path.join(workSpace,originTBM+"_"+out_name)
        #forLabel=out_name
        #backLabel=originTBM
        #primaryKey="TYPE"
        #foreignKey="TYPE"
        #arcpy.CreateRelationshipClass_management(TBM,desti,out_reclass,"COMPOSITE",forLabel,backLabel,"NONE","ONE_TO_MANY","NONE",primaryKey,foreignKey)
        
#del arcpy
#del os
del desti
