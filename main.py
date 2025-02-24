import os
import json
from pathlib import Path
import csv

from PIL.Image import new

IMG_WIDTH = 1280
IMG_HEIGHT = 720

image_train_path = r"./bdd100k_images_100k/images/100k/train/"
label_path = r"./bdd100k_det_20_labels_trainval/labels/det_20/det_train.json"
img_list = []
newfolder = r"./train_new_labels/"

here1 = r"./here1/"
here2 = r"./here2/"

nfolder = r"./val_new_labels/"
image_val_path = r"./bdd100k_images_100k/images/100k/val/"
label_val_path = r"./bdd100k_det_20_labels_trainval/labels/det_20/det_val.json"

t_lab = r"./train_llabels/"
v_lab = r"./val_llabels/"

# if not os.path.exists(newfolder):
#     os.makedirs(newfolder)

DEEPDRIVE_CLASSES = [
    "pedestrian",
    "rider",
    "car",
    "truck",
    "bus",
    "train",
    "motorcycle",
    "bicycle",
    "traffic light",
    "traffic sign"
]

with open(label_path) as f:
    data = json.load(f)

for idx in range(len(data)):
    img_list.append(data[idx]["name"])

loop_2 = os.listdir(newfolder)

loop_2.sort()
img_list.sort()

# print("loop_2 length: ", len(loop_2))
# print("img_list length: ", len(img_list))
# print(loop_2[0])
# print(img_list[0])
#l = os.listdir(v_lab)
#l.sort()

# create new .txt file inside folder
# for f in img_list:
#     f = Path(f).stem + ".txt"
#     file_path = Path(nfolder + f)
#     file_path.touch()

# print(img_list[0])
# print(l[0])
# write csv
# for i in range(len(img_list)):
#     print(i)
#     with open('new_val.csv', 'a') as csvfile:
#         filewriter = csv.writer(csvfile)
#         filewriter.writerow([img_list[i], l[i]])

# convert to yolo format


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x, y, w, h)


def convert2(xmin, ymin, xmax, ymax, img_w, img_h):
    dw = 1./(img_w)
    dh = 1./(img_h)
    x = (xmin + xmax)/2.0 - 1
    y = (ymin + ymax)/2.0 - 1
    w = xmax - xmin
    h = ymax - ymin
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x, y, w, h)


def convert3(width, height, xmin, ymin, xmax, ymax):  # use this
    x = xmin / width
    y = ymin / height
    w = (xmax - xmin) / width
    h = (ymax - ymin) / height
    return (x, y, w, h)

def box2d_to_yolo(xmin, ymin, xmax, ymax):
    x1 = xmin / IMG_WIDTH
    x2 = xmax / IMG_WIDTH
    y1 = ymin / IMG_HEIGHT
    y2 = ymax / IMG_HEIGHT

    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    width = abs(x2 - x1)
    height = abs(y2 - y1)

    return cx, cy, width, height

b = [
    data[0]['labels'][1]['box2d']['x1'],
    data[0]['labels'][1]['box2d']['x2'],
    data[0]['labels'][1]['box2d']['y1'],
    data[0]['labels'][1]['box2d']['y2']
]
xmin = data[0]['labels'][1]['box2d']['x1']
ymin = data[0]['labels'][1]['box2d']['y1']
xmax = data[0]['labels'][1]['box2d']['x2']
ymax = data[0]['labels'][1]['box2d']['y2']
# x, y, w, h = convert3(1280,720, xmin, ymin, xmax, ymax)
# xx, yy, ww, hh =  convert((1280, 720), b)

# print(data[0]["name"])
# print(data[0]["labels"][1]["category"])
# print(xmin)
# print(ymin)
# print(xmax)
# print(ymax)

# print(xx)
# print(yy)
# print(ww)
# print(hh)

# print("%f and %d", xx, xx)

# print(json.dumps(data[19705], indent=2))
# train_llabels
for i in loop_2:
    if i == 'b1c81faa-3df17267.txt':
        print(i)
# for i in range(len(loop_2)):
#     if i in [6879, 15376, 15763, 19525, 19705, 28516, 28852, 31942, 34556, 39770]:
#         continue
#     #print(i)
#     with open(t_lab+loop_2[i], 'a') as f:
#         temp = Path(loop_2[i]).stem + ".jpg"
#         for k in range(len(img_list)):
#             if (temp == img_list[k]):
#                 for j in range(len(data[i]["labels"])):
#                     for n in range(len(DEEPDRIVE_CLASSES)):
#                         if data[i]["labels"][j]["category"] == DEEPDRIVE_CLASSES[n]:
#                             xmin = data[i]["labels"][j]["box2d"]["x1"]
#                             ymin = data[i]["labels"][j]["box2d"]["y1"]
#                             xmax = data[i]["labels"][j]["box2d"]["x2"]
#                             ymax = data[i]["labels"][j]["box2d"]["y2"]
#                             x, y, w, h = convert2(xmin, ymin, xmax, ymax, 1280, 720)
#                             if x < 0 or y < 0 or w < 0 or h < 0:
#                                 print(data[i]['name'])
                            # if j != len(data[k]["labels"])-1:
                            #     f.write('%d' % n)
                            #     f.write(' %f' % x)
                            #     f.write(' %f' % y)
                            #     f.write(' %f' % w)
                            #     f.write(' %f' % h)
                            #     f.write('\n')
                            # else:
                            #     f.write('%d' % n)
                            #     f.write(' %f' % x)
                            #     f.write(' %f' % y)
                            #     f.write(' %f' % w)
                            #     f.write(' %f' % h)

# val_llabels
# for i in range(len(loop_2)):
#     print(i)
#     with open(nfolder+loop_2[i], 'a') as f:
#         temp = Path(loop_2[i]).stem + ".jpg"
#         for k in range(len(img_list)):
#             if (temp == img_list[k]):
#                 for j in range(len(data[i]["labels"])):
#                     for n in range(len(DEEPDRIVE_CLASSES)):
#                         if data[i]["labels"][j]["category"] == DEEPDRIVE_CLASSES[n]:
#                             xmin = data[i]["labels"][j]["box2d"]["x1"]
#                             ymin = data[i]["labels"][j]["box2d"]["y1"]
#                             xmax = data[i]["labels"][j]["box2d"]["x2"]
#                             ymax = data[i]["labels"][j]["box2d"]["y2"]
#                             x, y, w, h = convert2(xmin, ymin, xmax, ymax, 1280, 720)
#                             if j != len(data[k]["labels"])-1:
#                                 f.write('%d' % n)
#                                 f.write(' %f' % x)
#                                 f.write(' %f' % y)
#                                 f.write(' %f' % w)
#                                 f.write(' %f' % h)
#                                 f.write('\n')
#                             else:
#                                 f.write('%d' % n)
#                                 f.write(' %f' % x)
#                                 f.write(' %f' % y)
#                                 f.write(' %f' % w)
#                                 f.write(' %f' % h)

# train_new_labels
# for i in range(len(loop_2)):
#     print(i)
#     with open(nfolder+loop_2[i], 'a') as f:
#         temp = Path(loop_2[i]).stem + ".jpg"
#         for k in range(len(img_list)):
#             if (temp == img_list[k]):
#                 for j in range(len(data[i]["labels"])):
#                     for n in range(len(DEEPDRIVE_CLASSES)):
#                         if data[i]["labels"][j]["category"] == DEEPDRIVE_CLASSES[n]:
#                             if j != len(data[k]["labels"])-1:
#                                 f.write('%d' % n)
#                                 f.write(' %f' % data[i]["labels"][j]["box2d"]["x1"])
#                                 f.write(' %f' % data[i]["labels"][j]["box2d"]["y1"])
#                                 f.write(' %f' % data[i]["labels"][j]["box2d"]["x2"])
#                                 f.write(' %f' % data[i]["labels"][j]["box2d"]["y2"])
#                                 f.write('\n')
#                             else:
#                                 f.write('%d' % n)
#                                 f.write(' %f' % data[i]["labels"][j]["box2d"]["x1"])
#                                 f.write(' %f' % data[i]["labels"][j]["box2d"]["y1"])
#                                 f.write(' %f' % data[i]["labels"][j]["box2d"]["x2"])
#                                 f.write(' %f' % data[i]["labels"][j]["box2d"]["y2"])


# for i in range(len(loop_2)):
#     print(loop_2[i])
#     print(newfolder+loop_2[i])
#     with open(newfolder+loop_2[i], 'a') as f:
#         temp = Path(loop_2[i]).stem + ".jpg"
#         print(temp)
#         for k in range(len(img_list)):
#             if temp == img_list[k]:
#                 print(data[k]['name'])
#                 for j in range(len(data[k]["labels"])):
#                     print("j: ",j)
#                     for n in range(len(DEEPDRIVE_CLASSES)):
#                         if data[k]["labels"][j]["category"] == DEEPDRIVE_CLASSES[n]:
#                             print("Category: ",data[k]["labels"][j]["category"])
#                             if j != len(data[k]["labels"])-1:
#                                 f.write('%d' % n)
#                                 f.write(' %f' % data[k]["labels"][j]["box2d"]["x1"])
#                                 f.write(' %f' % data[k]["labels"][j]["box2d"]["y1"])
#                                 f.write(' %f' % data[k]["labels"][j]["box2d"]["x2"])
#                                 f.write(' %f' % data[k]["labels"][j]["box2d"]["y2"])
#                                 f.write('\n')
#                             else:
#                                 f.write('%d' % n)
#                                 f.write(' %f' % data[k]["labels"][j]["box2d"]["x1"])
#                                 f.write(' %f' % data[k]["labels"][j]["box2d"]["y1"])
#                                 f.write(' %f' % data[k]["labels"][j]["box2d"]["x2"])
#                                 f.write(' %f' % data[k]["labels"][j]["box2d"]["y2"])
