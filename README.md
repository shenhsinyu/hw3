# hw3 - Instance Segmentation

## environment
- ubuntu 18.04
- pytorch

## data
- tiny PASCAL VOC dataset
- contains only 1,349 training images, 100 test images with 20 common object classes

## train on custom dataset
- first modify the `data/config.py`. Create a definition for your dataset. if you don't have validation data, use the same path to training_inages for path_to_validation_images. 

  In `train.py` `--parser.add_argument('--validation_size', default=200, type=int, help='The number of images to use for validation.')` will use the first 200 images for validation.
  
```
my_custom_dataset = dataset_base.copy({
    'name': 'My Dataset',

    'train_images': 'path_to_training_images',
    'train_info':   'path_to_training_annotation',

    'valid_images': 'path_to_validation_images',
    'valid_info':   'path_to_validation_annotation',

    'has_gt': True,
    'class_names': ('my_class_id_1', 'my_class_id_2', 'my_class_id_3', ...)
})
```
- then turn `yolact_base_config = 'dataset'` to  `yolact_base_config = 'my_custom_dataset'`

## training
- add `--parser.add_argument('--config', defalut=yolact_base_config)`
- you can choose learning rate for SGD, batchsize, epoch...
- run `python3 train.py` to train your model.

## eval
- run `python3 eval.py` to get image with mask and bounding box on detected item.
- you can choose weight, score_threshold, number of item.
- add the test images to `data/test_images` and output will in `data/output`
- example:

  ![image](https://github.com/shenhsinyu/hw3/blob/main/2007_002823.png)
