FasterRCNN如何使用：

1.VOC数据集：链接:https://pan.baidu.com/s/12Qgndt1TWUYBeIcL0Th20g  密码:dzi8

放入FasterRCNN\data文件夹中

2.vgg预训练权重：链接:https://pan.baidu.com/s/1GdxNN7MwRS_tyItklpRyzg  密码:fmi7

放入FasterRCNN\data文件夹中

3.训练好的FasterRCNN网络权重：链接:https://pan.baidu.com/s/19MIZmKAq0BoWmj8UhljmNg  密码:qmi4

放入FasterRCNN\models\vgg16\pascal_voc中

训练：

python trainval_net.py

gpu:

python trainval_net.py --cuda
