import os
from shutil import copyfile
import random

train_directory = 'dataset/train/'
val_directory = 'dataset/val/'

new_dataset = 'new_dataset/'
new_train = 'new_dataset/train/'
new_val = 'new_dataset/val/'
new_test = 'new_dataset/test/'

os.mkdir(new_dataset)
os.mkdir(new_train)
os.mkdir(new_val)
os.mkdir(new_test)

classes = [line.rstrip('\n') for line in open('dataset/wnids.txt', 'r')]
val_classes = [line.rstrip('\n') for line in open(
    'dataset/val/val_annotations.txt', 'r')]

for i_class in classes:

    print('\n\nClass: ' + i_class)
    os.mkdir(new_train + i_class)
    os.mkdir(new_val + i_class)
    os.mkdir(new_test + i_class)

    class_images = []

    for image in os.listdir(train_directory + i_class + '/images/'):
        class_images.append(train_directory + i_class + '/images/' + image)

    print('Train done: ' + i_class)

    val_list = os.listdir(val_directory + 'images/')

    val_list.sort()

    i = 0
    for image in val_list:
        if(i_class in val_classes[i]):
            val_img = val_classes[i].split()
            class_images.append(val_directory + 'images/' + val_img[0])
        i += 1

    print('Val done: ' + i_class)

    print('Size: ' + str(len(class_images)))

    random.shuffle(class_images)

    train_split = class_images[:450]
    val_split = class_images[450:500]
    test_split = class_images[500:550]

    i = 0

    for image in train_split:
        copyfile(image, new_train + i_class + '/' + str(i) + ".JPEG")
        i += 1

    i = 0

    for image in val_split:
        copyfile(image, new_val + i_class + '/' + str(i) + ".JPEG")
        i += 1

    i = 0

    for image in test_split:
        copyfile(image, new_test + i_class + '/' + str(i) + ".JPEG")
        i += 1

    print('Copy done: ' + i_class)
