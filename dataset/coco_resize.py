import json
import os
from pycocotools.coco import COCO
from shutil import copy2

# Paths to the sources annotations
coco_annotations_path = 'annotations/instances_train2017.json'
coco_images_dir = 'train2017'

# Paths to the output annotations and images
output_annotations_path = 'coco10/annotations/instances_train2017_subset.json'
output_images_dir = 'coco10/train2017_subset/'

# Ten classes to keep
target_classes = ['cat', 'dog', 'horse', 'bird' , 'sheep','cow','elephant','bear','zebra','giraffe']

# Create output directories
os.makedirs(output_images_dir, exist_ok=True)

# Define COCO object
coco = COCO(coco_annotations_path)

# Find IDs of the target classes
target_category_ids = [animal['id'] for animal in coco.loadCats(coco.getCatIds()) if animal['name'] in target_classes]

# Find annotations of the target classes
target_annotation_ids = coco.getAnnIds(animalIds=target_category_ids)
target_annotations = coco.loadAnns(target_annotation_ids)

# Find images containing the target annotations
target_image_ids = list(set([ann['image_id'] for ann in target_annotations]))
target_images = coco.loadImgs(target_image_ids)

# Copy images to the output directory
for img in target_images:
    source_path = os.path.join(coco_images_dir, img['file_name'])
    dest_path = os.path.join(output_images_dir, img['file_name'])
    copy2(source_path, dest_path)

# Create a new JSON file
filtered_annotations = {
    'info': coco.dataset['info'],
    'licenses': coco.dataset['licenses'],
    'images': target_images,
    'annotations': target_annotations,
    'categories': [animal for animal in coco.loadCats(coco.getCatIds()) if animal['id'] in target_category_ids]
}

# Save new JSON file
with open(output_annotations_path, 'w') as f:
    json.dump(filtered_annotations, f)


