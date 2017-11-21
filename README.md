# TaoBao Crawler
![lucky-ing](https://github.com/lucky-ing/TaoBaoCrawler/raw/master/cache/haimianbaobao.jpg  "lucky-ing")
星期一, 20. 十一月 2017 07:10下午 
做图像处理和做物体识别检测的很多朋友都会有这样一个感受。没有数据集！！！！博主一直苦于没有数据集。而作为最大的，最集中的图片库--淘宝网（百度出来的图片的离散度太高）却无法使用简单的爬虫方式获取图片。（妹子图的爬虫+cook处理也没有用。。。）为此，博主使用了selenium仿真爬虫，这种爬虫的兼容性比较高，只是速度一般，5000张图片需要大约30min，如果爬一夜的话，估计就够我们用的了。有兴趣交流的请发邮件到博主邮箱：
>lucky_lsq@163.com


博主致力于深度学习领域研究。欢迎互相学习，互相交流。

# 2017-10-20更新！突破&终结淘宝全线封锁！
---
本次**TaoBaoCrawler**版本，我们主要是更新了淘宝爬虫的整体架构。主要功能有：

- 支持任意检索词检索，支持中文词汇检索。
- 支持更改保存路径以及保存名字。
- 支持更改最大下载量数目。
- 显示页面批次下载数目条。

**依赖项**
---
>firefox browser
>python 3.0+
>selenium
>BeautifulSoup
>tqdm

### Tutorial

```python
#this program uses firefox browser, we should have firefox browser in computer first.\n
#if we just use the base function of this program
#-s specific the key word of searching.you can input any word you want to scraper. this parameter is requested!
python3 main.py -s 电脑
 #-f specific the path where Image storage location
python3 main.py -s 电脑 -f ./image
#-n specific the max num of the downloads
python3 main.py -s 电脑 -n 5000
```
---
![tb](https://github.com/lucky-ing/TaoBaoCrawler/raw/master/cache/tb.png  "tb")

---
### about the selenium

selenium is a Automated testing tool, it can run browser automatly. Taobao have anti-reptile strategy that if we use this tool, taobao website will send the context. 

### 淘宝爬虫效果
![xia](https://github.com/lucky-ing/TaoBaoCrawler/raw/master/cache/tuoxiascraper.png  "xia")

### ANTI TAOBAO!!!
淘宝有最全的图片库，虽然离散度也比较高，但是经过简单标注之后可以应用到图片分类的深度学习算法中。我们通过这个程序，可以简单的爬取淘宝的图片。希望大家一起讨论，通过简单的图片分类算法对原始数据集处理操作。
### Contact
Any question owned you can contact me with the wechat:liu806353105, or e-mail:lucky_lsq@163.com
### Copyright
(c) 2017 Lucky-ing LICENSE Apache 2.0