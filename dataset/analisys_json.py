import json
import os
import numpy as np
import matplotlib.pyplot as plt

# Path to the annotations
coco_annotations_path = 'coco10/annotations/instances_train2017_subset.json'

# Load annotations
with open(coco_annotations_path, 'r') as f:
    coco = json.load(f)

#Print the categories
print(coco['categories'])

#Create a dictionary of categories with the category ID as the key
categories = {category['id']: category['name'] for category in coco['categories']}
print(categories)

# Count the number of images per category
category_images = {16: 10806, 17: 4768, 18: 5508, 19: 6587, 20: 9509, 21: 8147, 22: 5513, 23: 1294, 24: 5303, 25: 5131}

#Change the category IDs to category names
category_images = {categories[category_id]: count for category_id, count in category_images.items()}

#convert to csv

# Save the dictionary to a CSV file
with open('category_images.csv', 'w') as f:
    f.write('category,count\n')
    for category, count in category_images.items():
        f.write(f'{category},{count}\n')

#Count the of images
image_ids = [image['id'] for image in coco['images']]
print("Number of images:",len(image_ids))

#Count the number of annotations
annotation_ids = [annotation['id'] for annotation in coco['annotations']]
print("Number of annotations",len(annotation_ids))

