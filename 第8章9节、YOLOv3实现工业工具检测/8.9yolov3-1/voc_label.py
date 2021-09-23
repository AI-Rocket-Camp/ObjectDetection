"""
create by cv调包侠
公众号：DeepAI 视界
用以转换xml为yolo支持的格式，并归一化坐标。
"""
import xml.etree.ElementTree as ET
import os
import random
classes = ["0", "1", "2", "3"]  # 输入类别名称，必须与xml标注名称一致


# 用以归一化坐标
def convert(size, box):
    print(size, box)
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


# 转换xml为labels
def convert_annotation(image_id):
    in_file = open(r'./data/Annotations/%s' % (image_id), 'rb')  # 读取xml文件路径
    if not os.path.exists('./data/labels'):
        os.makedirs('./data/labels')
    out_file = open('./data/labels/%s.txt' % (image_id.split('.')[0]), 'w')  # 需要保存的txt格式文件路径
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


image_ids_train = os.listdir('./data/Annotations')  # 读取xml文件名索引

for image_id in image_ids_train:
    print(image_id)
    convert_annotation(image_id)

# 用以生成训练集和验证集，并写入到data/train.txt,data/test.txt
trainval_percent = 0.1  # 验证集比例
train_percent = 1
xmlfilepath = './data/images'
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)
ftest = open('./data/test.txt', 'w')
ftrain = open('./data/train.txt', 'w')

for i in list:
    name = total_xml[i] + '\n'
    if i in trainval:
        if i in train:
            ftest.write('data/images/' + name)
    else:
        ftrain.write('data/images/' + name)
ftrain.close()
ftest.close()
