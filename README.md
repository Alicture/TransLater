## TransLater

一个网页翻译工具，可以在开源书籍翻译工作中提高效率。

* 使用腾讯云机器翻译API（限量免费）,[sdk](https://github.com/QcloudApi/qcloudapi-sdk-python)
* 使用开源markdown在线编辑器[editor.md](https://pandao.github.io/editor.md/)
* 使用Flask框架

## To-do list

- [x] 接入机器翻译API
- [x] 网页正文内容翻译
- [x] html转MD
- [x] 保存MD文件到本地
- [x] Flask具体实现
## Tip
* 使用前，先在config.json中设置SecretKEY和SecretID，如何获取腾讯云APIkey看[这里](https://www.cloudbility.com/help/qcloud/access-key.html)
* 使用到的module: flask-markdown,html2text，请先安装。
* `python3 run.py`运行程序