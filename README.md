# Image-classification-with-front-end-interface
Image classification with front-end interface,Examples of categorical use: Chinese herbal medicine;Included Networks:mobilenetv2、resnet、vgg、swin_transformer.etc
## Classification：分类模型在Pytorch当中的实现
---

## 文件下载
训练所需的预训练权重，数据集和训练好的权重都可以在百度云下载。     
链接：https://pan.baidu.com/s/10lAJLDWlCI7RX3PblKRxYQ 
提取码：ifl0


## 训练步骤
1. datasets文件夹下存放的图片分为两部分，train里面是训练图片，test里面是测试图片。  
2. 在训练之前需要首先准备好数据集，在train或者test文件里里面创建不同的文件夹，每个文件夹的名称为对应的类别名称，文件夹下面的图片为这个类的图片。文件格式可参考如下：
```
|-datasets
    |-train
        |-Anxixiang
            |-123.jpg
            |-234.jpg
        |-Baibiandou
            |-345.jpg
            |-456.jpg
        |-...
    |-test
        |-Anxixiang
            |-567.jpg
            |-678.jpg
        |-Baibiandou
            |-789.jpg
            |-890.jpg
        |-...
```
3. 在准备好数据集后，需要在根目录运行txt_annotation.py生成训练所需的cls_train.txt，运行前需要修改其中的classes，将其修改成自己需要分的类。   
4. 之后修改model_data文件夹下的cls_classes.txt，使其也对应自己需要分的类。  
5. 在train.py里面调整自己要选择的网络和权重后，就可以开始训练了！  


## 评估步骤
1. datasets文件夹下存放的图片分为两部分，train里面是训练图片，test里面是测试图片，在评估的时候，我们使用的是test文件夹里面的图片。  
2. 在评估之前需要首先准备好数据集，在train或者test文件里里面创建不同的文件夹，每个文件夹的名称为对应的类别名称，文件夹下面的图片为这个类的图片。

## 开始
前端界面只用运行login.py这个文件，包括注册和用户登录，管理员登录用户为:user,密码为：123456


