#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:40:09 2019

@author: antoinechesnais
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm
from sklearn.cluster import KMeans
from IPython.display import display

def kmeans_analysis(k, original_data, scaled_data, palette):
    '''Perform Kmeans on the scaled data and return the Kmeans model.
       Display features importance, population and revenue contribution for each segment.
    
    Parameters
    ----------
    k : Number of clusters to use (integer)
    original_data : Data without transformation, will be use to interpret segment (dataframe)
    scaled_data : Data after tansformation, will be use to determine segment with Kmeans (dataframe)
    palette : palette name to use for the 2 donuts graph (string)
        
    Returns
    -------
    kmeans : Kmeans model calculated with k clusters.
    
    '''
    
    # Computing Kmeans with k clusters on scaled data
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(scaled_data)
    
    # Assign segment to each customer in original dataset
    data_kmeans = original_data.assign(segment=kmeans.labels_)
    
    # Compute average for each feature by segment
    kmeans_averages = data_kmeans.groupby(['segment']).mean().round(2)
    print('Moyennes par segment : ')
    display(kmeans_averages)
    print("\n")
    
    # Compute relative importance for each feature by segment
    relative_imp = kmeans_averages / original_data.mean() - 1
    relative_imp.round(2)
    
    # Compute % of population in each segment
    pop_perc = data_kmeans['segment'].value_counts() / data_kmeans.shape[0] * 100
    pop_perc.sort_index(inplace=True)
    
    # Compute revenue for each segment
    segment_value = data_kmeans.groupby('segment')['order_value'].sum()
    
    # Create figure with 3 subplots
    fig, axs = plt.subplots(1,3, figsize=(12,4))
    col = cm.get_cmap(palette, k)
    
    # Creation of graph displaying features importance for each segment
    sns.heatmap(data=relative_imp, annot=True, fmt='.2f', cmap='RdBu_r', ax=axs[0])
    axs[0].set_title('Importance relative des features', pad=20)
    axs[0].set_ylabel(ylabel='Segment', labelpad = 20)
    
    # Creation of graph displaying relative population for each segment
    axs[1].pie(pop_perc, autopct='%1.0f%%', pctdistance=0.82, colors=col.colors, textprops=dict(color="w"))
    axs[1].set_title('Proportion des segments', pad=20)
    f_circle=plt.Circle( (0,0), 0.65, color='white')
    axs[1].add_patch(f_circle)
    
    # Creation of graph displaying relative revenue for each segment
    axs[2].pie(segment_value, autopct='%1.0f%%', pctdistance=0.82, colors=col.colors, textprops=dict(color="w"))
    axs[2].legend(labels=segment_value.index, loc='center right', bbox_to_anchor=(1.25, 0.5))
    axs[2].set_title('Contribution de chaque segment au CA', pad=20)
    s_circle=plt.Circle( (0,0), 0.65, color='white')
    axs[2].add_patch(s_circle)
    
    return(kmeans)