# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 13:31:45 2019

@author: oc3512
"""

import arcpy

arcpy.env.workspace="C:/Users/oc3512/Documents/ArcGIS/Projects/MMSP/001-CIVIL.gdb"
arcpy.env.overwriteOutput=True

datasets=arcpy.ListDatasets(feature_type="feature")
datasets = [''] + datasets if datasets is not None else []

FeatureClass=arcpy.ListFeatureClasses(feature_dataset=datasets[3])
fNames=[f.name for f in arcpy.ListFields(FeatureClass[0])]



# Set local variables
in_table = FeatureClass[0]
name = "calculateRuleLabel"
script_expression = 'if ($feature.OperationType == 1) {return 1} else {return 2}'
triggering_events = "INSERT;UPDATE"
description = "Populate label text"
subtype = "OperationType"
field = "test"

arcpy.AddAttributeRule_management(in_table, name, "CONSTRAINT", script_expression, "EDITABLE", triggering_events, "", "", description, subtype, field)