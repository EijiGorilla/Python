# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:07:16 2019

@author: oc3512
"""
datasets = arcpy.ListDatasets(feature_type='feature')  
datasets = [''] + datasets if datasets is not None else []   
fc=arcpy.ListFeatureClasses(feature_dataset=datasets[2])
