# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 09:44:49 2019

@author: oc3512
"""

import arcpy

aprx=arcpy.mp.ArcGISProject("C:/Users/oc3512/Documents/ArcGIS/Projects/MMSP/MMSP.aprx")
#mapC=arcpy.GetParameterAsText(1) # choose map


# List maps and associated tables
#for m in aprx.listMaps():
#    print("Map: " + m.name)
#    for lyr in m.listLayers():
#        print("   " + lyr.name)

# List layouts
#for lyt in aprx.listLayouts():
#    print(lyt.name)

#
aprx=arcpy.mp.ArcGISProject("C:/Users/oc3512/Documents/ArcGIS/Projects/MMSP/MMSP.aprx")
map=aprx.listMaps()[4] # MMSP_CORE map
chartLayer=map.listLayers("TBM_Segment")[0]
c=arcpy.Chart("MyChart")

c.type="line"
c.title="Status"
c.description=" "
c.xAxis.field="Segment_No"
c.yAxis.field="Status"
c.xAxis.title="X"
c.yAxis.title="Y"
c.addToLayer(chartLayer)



