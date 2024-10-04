"""
Created on Wed Apr 10 23:16:52 2024

@author: Chigozirim Ike
NUID: 002217920
DS2000 Programming with Data
File: tree.py
Descriprtion:
"""
import json
import numpy as np
import matplotlib.pyplot as plt


def read_trees(filename):
    """ Read the tree data into a dictionary """
    with open(filename, 'r') as file:
        tree_data = json.load(file)
    return tree_data
    

def gps_to_xy(gps_lon, gps_lat, boundary, size=(1000,1000)):
    """ Map gps latitude and longitude coordinates to
    array coordinates based on the boundaries given as 
    (min_longitude, max_longitude, min_latitude, max_latitude) 
    and the size (width, height) of the array. 
    Return (x,y) grid coordinates - two INTEGERS. 
    
    HINT:   (min_longitude, max_latitude) => (0,0)
            (max_longitude, min_latitude) => (1000, 1000)
            
    When plotting images:
        - the (0,0) is in the UPPER LEFT
        - x is DOWN:   Increasing x is decreasing LATITUDE
        - y is ACROSS: Increasing y is increasing LONGITUDE
    """
    min_long, max_long, min_lat, max_lat = boundary
    x = int((gps_lon - min_long) / (max_long - min_long) * size[0])
    y = int((max_lat - gps_lat) / (max_lat - min_lat) * size[1])
    return x, y


def plot_trees(grid, title=""):
    """ Plot the map of trees """
    plt.figure(figsize=(10,10))
    plt.title(title)
    plt.grid()
    plt.imshow(grid, cmap='viridis')
    plt.savefig("treemap.png")
    

def main():
    
    # 1. Set up map boundaries
    # (minlon, maxlon, minlat, maxlat)    
    boston = (-71.2, -70.9, 42.2, 42.4 )
    northeastern = (-71.12, -71.05, 42.32, 42.36)

    # 2. Set up a positionary grid covering your boundary
    # We're using a special 2D array using numpy
    # (This is faster than lists of lists!)
    # To update the grid we can say: grid[x,y] = 1  (0 = No Tree, 1 = Tree)
    # or grid[x][y] = 1
    
    grid_size = (1000,1000)   
    grid = np.zeros(shape=grid_size)   # Our grid is 1000 x 1000
    
    # 3. Read the geojson data into a dictionary
    #    Note: 'geojson is json!'
    tree_data = read_trees("trees.geojson")

    # 4. For each tree in the dataset ....
    for tree in tree_data['features']:
        #    a. Extract the tree's gps location 
        gps_lon = tree['geometry']['coordinates'][0]
        gps_lat = tree['geometry']['coordinates'][1]

        #    b. Convert to (x,y) grid coordinates using
        #       the function gps_to_xy that you will implement
        x, y = gps_to_xy(gps_lon, gps_lat, boston)
    
        #    c. IF the tree is in bounds, i.e, if 
        #       0 <= x < 1000 and 0 <= y < 1000, 
        #       then set a point in your array like so:
        #       grid[x,y] = 1
        #       OTHERWISE, ignore that tree
        if 0 <= x < 1000 and 0 <= y < 1000:
            grid[x, y] = 1

    # 4. Visualize your map - the plotting function is provided for you!
    # Depending on your "color map", cmap, different colors will appear 
    # depending on the density of your trees in any given area of the city
    # Experiment with different color maps, listed here:
    # https://matplotlib.org/stable/users/explain/colors/colormaps.html
    plot_trees(grid, "Boston Tree Map")
    
if __name__ == '__main__':
    main()