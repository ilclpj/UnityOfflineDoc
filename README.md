# Unity离线文档的安装与加速
# 总览

平时在使用Unity时, 经常会查询一些Api或者用法示例, 但是Unity官网经常出问题, 而且有时访问速度不够理想, 我们可以将文件下载下来在本地查看, Unity提供了这个功能, 我在这里给大家介绍下如何操作, 并且给出一些小的建议和技巧. 

# 离线文档的下载和安装

Unity的离线文档是以Html形式的文件, 每次只要打开本地的index.html即可访问.

首先我们打开Unity的[文档首页](https://docs.unity.cn/cn/current/Manual/index.html), 选择好想要的版本后, 点击[用户手册](https://docs.unity.cn/cn/current/Manual/UnityManual.html), 然后点击[离线文档](https://docs.unity.cn/cn/current/Manual/OfflineDocumentation.html), 最后点击右侧面板的**下载离线文档**即可**.** 操作过程如图所示:
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308155250833.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dvb2Rlbmdt,size_16,color_FFFFFF,t_70)
下载完成后直接解压, 文件结构如图所示:
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308155320689.png)



图中的两个文件夹分别对应了**手册**和**脚本API**. 两个文件夹中都存在一份index.html. 点击后可跳转对应的首页.

# 访问加速

访问加速? 我们下载的不是本地的离线文档么? 为什么还需要加速呢?

虽然大家安装我上面介绍的方法**安装**好了离线文档, 但是如果你现在尝试去打开, 会发现依然要加载半天才能看到内容, 这是怎么回事呢?

我们从官网下载的离线文档只是以html文件存在的网页文件, 在每个文件中存在着访问google的内容, 可能是一些样式, 可能是一些字体, 这些对于我们本地访问来说是不需要的, 但是因为国内无法访问google, 所以每次需要加载超时后才能看到内容.

我们需要将这些内容移除, 才能达到比较完美的结果.

我们的办法很简单, 就是将所有的html文件中访问google的Tag移除即可. 如图所示:
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210308155407631.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dvb2Rlbmdt,size_16,color_FFFFFF,t_70)


## 脚本

具体的过程我已经帮大家写好啦, 大家可以基于我的脚本自己定制想要的功能和调整.

脚本需要用到两个库: **bs4**和**lxml**, 可以通过以下的命令下载:
```Bash
pip install bs4
pip install lxml
```

注意脚本需要在python3下运行哦!

好的, 今天的分享就到这里, 祝大家开心😄.