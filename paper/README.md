# tensorflow-MTCNN
## 模型理解
[MTCNN](https://kpzhang93.github.io/MTCNN_face_detection_alignment/index.html)是目前比较流行的人脸检测方法，通过人脸检测可以进行更精准的人脸识别。模型主要通过PNet，RNet，ONet三个网络级联，一步一步精调来对人脸进行更准确的检测。论文中的模型图如下：<br>
![](https://github.com/LeslieZhoa/tensorflow-MTCNN/blob/master/output/model1.png)<br>
![](https://github.com/LeslieZhoa/tensorflow-MTCNN/blob/master/output/model2.png)<br>

三个模型要按顺序训练，首先是PNet,然后RNet,最后ONet。
PNet:
PNet是全卷积网络，主要为了应对不同输入尺度，层数很浅，主要作用是尽可能多的把人脸框都选进来，宁愿错误拿来好多个，也不丢掉一个。训练数据由四部分组成：pos,part,neg,landmark，比例为1：1：3：1。

数据是怎么来的呢？pos,part,neg是随机和人脸的数据裁剪得到的，裁剪图片与人脸框最大的iou值大于0.65的为pos图像，大于0.4的为part图像，小于0.3的为neg图像，landmark截取的是带有关键点的图像。其中pos,part的label含有它们的类别1,-1还有人脸框相对于图像左上角的偏移量，偏移量除以图像大小做了归一化;neg的label只含有类别0;landmark的label含有类别-2和5个关键点的坐标偏移也是进行了归一化的。
这四种图像都resize成12x12作为PNet的输入，通过PNet得到了是否有人脸的概率[batch,2]，人脸框的偏移量[batch,4]，关键点的偏移量[batch,10]。

四种不同的数据该怎么训练呢？
对于是否存在人脸的类别损失只通过neg和pos数据来对参数进行更新，具体办法是通过label中的类别值做了一个遮罩来划分数据，只计算neg和pos的损失，不计算其他数据的损失;人脸框的损失只计算pos和part数据的;关键点的损失只计算landmark的。论文中有个小技巧就是只通过前70%的数据进行更新参数，说是模型准确率会有提升，在代码中也都有体现，具体实现可以参考代码。<br>
RNet,ONet:
RNet和ONet都差不多都是精修人脸框，放在一起解释。RNet的landmark数据和PNet一样，是对带有关键点的图像截取得到，但要resize成24x24的作为输入。
pos,part,neg的数据是通过PNet得到的。这里就可以理解为什么PNet的输入要是四种数据大小是12了，为了速度，也为了RNet的输入。一张图片输入到PNet中会得到[1,h,w,2],[1,h,w,4],[1,h,w,10]的label预测值，这有点像yolo的思想.(https://github.com/LeslieZhoa/tensorflow-YOLO1)。
把一张图片像网格一样划分，每一个网格都预测它的人脸框，划分的图片包含的人脸有多有少，所以划分了neg，pos，part三种数据，landmark只是起辅助作用。图片还要以一定值来缩小尺度做成图像金字塔目的是获取更多可能的人脸框，人脸框中有人的概率大于一定阈值才保留，还要进行一定阈值的非极大值抑制，将太过重合的人脸框除掉，将PNet预测的人脸框于原图上截取，与真实人脸框的最大iou值来划分neg，pos,part数据，并resize成24作为RNet的输入。

RNet，ONet的损失函数和PNet相同，不同的是三种损失所占的比例不同。ONet的输入是图片通过PNet金字塔得到的裁剪框再经过RNet的裁剪框裁剪的图片划分neg,pos,part三种数据resize成48作为输入，landmark与RNet相同只不过resize成48大小的了。
