# Migrate-Image
用来迁移镜像到可下载的地方。

## 使用方法

首先fork该仓库，然后修改dest.txt文件，填写自己的仓库地址，然后再点击Settings，选择Secrets and variables，选择 Actions，在右侧添加DOCKERPASS和DOCKERUSER两个密钥（ps.这个用户名和密码就是dest.txt文件中填写的仓库地址对应的用户名密码）。

![QQ_1720676934865](https://github.com/s1eke/Migrate-Image/assets/10690839/d17c2f18-8d9d-4522-b6ef-d5e69864914c)


最后点击右上方的 Actions，选择 Migrate Docker Image，点击右侧的run workflow，填写你需要迁移的镜像即可，譬如debian:10，等运行完即迁移成功。

![QQ_1720676679095](https://github.com/s1eke/Migrate-Image/assets/10690839/78a8a051-d549-43d3-8387-c85925439a96)

![image](https://github.com/s1eke/Migrate-Image/assets/10690839/935dd508-9a83-446d-900c-bf8b084186a0)


## TODO

1. dest.txt支持多个目标，但是还没想好是在一个job里传好所有目标合适，还是每个job传一个地址合适。
2. 添加一个 web ui，通过 [nicegui](https://github.com/zauberzeug/nicegui) 实现。