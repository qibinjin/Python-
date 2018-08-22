#安装

```python
pip install py3Fdfs
pip install mutagen
pip isntall requests
```

### 使用

```python
base_path=FastDFS客户端存放日志文件的目录
tracker_server=运行tracker服务的机器ip:22122
```

上传文件需要先创建fdfs_client.client.Fdfs_client的对象，并指明配置文件，如

```
from fdfs_client.client import Fdfs_client
client = Fdfs_client('配置文件路径')
```

```
ret = client.upload_by_filename('/Users/delron/Desktop/1.png')
```

## 自定义Django文件存储系统

需要继承自`django.core.files.storage.Storage`，如

```
from django.core.files.storage import Storage

class FastDFSStorage(Storage):
    ...
```

支持Django不带任何参数来实例化存储类，也就是说任何设置都应该从django.conf.settings中获取

```
from django.conf import settings
from django.core.files.storage import Storage

class FastDFSStorage(Storage):
    def __init__(self, base_url=None, client_conf=None):
        if base_url is None:
            base_url = settings.FDFS_URL
        self.base_url = base_url
        if client_conf is None:
            client_conf = settings.FDFS_CLIENT_CONF
        self.client_conf = client_conf
```

存储类中必须实现`_open()`和`_save()`方法，以及任何后续使用中可能用到的其他方法。

- `_open(name, mode='rb')`

  被Storage.open()调用，在打开文件时被使用。

- `_save(name, content)`

  被Storage.save()调用，name是传入的文件名，content是Django接收到的文件内容，该方法需要将content文件内容保存。

  Django会将该方法的返回值保存到数据库中对应的文件字段，也就是说该方法应该返回要保存在数据库中的文件名称信息。

- `exists(name)`

  如果名为name的文件在文件系统中存在，则返回True，否则返回False。

- `url(name)`

  返回文件的完整访问URL

- `delete(name)`

  删除name的文件

- `listdir(path)`

  列出指定路径的内容

- `size(name)`

  返回name文件的总大小

  注意，并不是这些方法全部都要实现，可以省略用不到的方法。

- FstDfs存储类

- ```
  from django.conf import settings
  from django.core.files.storage import Storage
  from django.utils.deconstruct import deconstructible
  from fdfs_client.client import Fdfs_client
  
  
  @deconstructible
  class FastDFSStorage(Storage):
      def __init__(self, base_url=None, client_conf=None):
          """
          初始化
          :param base_url: 用于构造图片完整路径使用，图片服务器的域名
          :param client_conf: FastDFS客户端配置文件的路径
          """
          if base_url is None:
              base_url = settings.FDFS_URL
          self.base_url = base_url
          if client_conf is None:
              client_conf = settings.FDFS_CLIENT_CONF
          self.client_conf = client_conf
  
      def _open(self, name, mode='rb'):
          """
          用不到打开文件，所以省略
          """
          pass
  
      def _save(self, name, content):
          """
          在FastDFS中保存文件
          :param name: 传入的文件名
          :param content: 文件内容
          :return: 保存到数据库中的FastDFS的文件名
          """
          client = Fdfs_client(self.client_conf)
          ret = client.upload_by_buffer(content.read())
          if ret.get("Status") != "Upload successed.":
              raise Exception("upload file failed")
          file_name = ret.get("Remote file_id")
          return file_name
  
      def url(self, name):
          """
          返回文件的完整URL路径
          :param name: 数据库中保存的文件名
          :return: 完整的URL
          """
          return self.base_url + name
  
      def exists(self, name):
          """
          判断文件是否存在，FastDFS可以自行解决文件的重名问题
          所以此处返回False，告诉Django上传的都是新文件
          :param name:  文件名
          :return: False
          """
          return False
  ```

## 在Django配置中设置自定义文件存储类

在settings/dev.py文件中添加设置

```python
# django文件存储
DEFAULT_FILE_STORAGE = '上文中提到的存储类文件路径'

# FastDFS
FDFS_URL = 'http://FastDFS服务器路径:8888/'  
FDFS_CLIENT_CONF = os.path.join(BASE_DIR, '配置文件路径')
```

