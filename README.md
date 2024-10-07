# Trees-of-Boston
Project Overview

This project visualizes the locations of over 200,000 trees within the city limits of Boston using geospatial data. The goal is to plot the position of each tree on a 1000x1000 grid using data from a JSON file, mapping GPS coordinates to x, y coordinates.

Features

Geo-Spatial Mapping: Converts GPS coordinates of trees into a 2D numpy array grid.
Visualization: A 1000x1000 scatter plot image where each tree's location is represented by a pixel.
Efficient Plotting: Uses numpy arrays for efficient plotting, avoiding the performance issues of matplotlib's scatter plots for large datasets.
Project Files

treemap.py: The main Python file containing code to read the JSON tree data, map the coordinates, and generate the tree map.
treemap.png: The output image file representing the plotted tree locations within Boston.
How It Works

The code reads the JSON file, which contains GPS coordinates for each tree in Boston.
These coordinates are mapped to a 1000x1000 grid representing the Boston city limits.
The trees' locations are marked on the grid with 1s in a numpy array, which are then converted into a PNG image using a provided plotting function.
