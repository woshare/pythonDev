1，找到selenium的版本和本地chrome的版本一致
https://googlechromelabs.github.io/chrome-for-testing/#stable
https://chromedriver.storage.googleapis.com/index.html

2，在下载目录，解压，存入/usr/local/bin

3，执行chromedriver -v会报错

4，在/usr/local/bin执行这个，就不会有问题了
xattr -d com.apple.quarantine chromedriver

5，执行
python3 lottery_happy.py

6，数据简要统计
cat lottery.csv|awk -F ',' '{print $7}'|sort|uniq -c
