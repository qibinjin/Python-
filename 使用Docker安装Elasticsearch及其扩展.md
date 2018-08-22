### 使用Docker安装Elasticsearch及其扩展

获取镜像，可以通过网络pull

```
docker image pull delron/elasticsearch-ik:2.4.6-1.0
```

或者加载提供给大家的镜像文件

```
docker load -i elasticsearch-ik-2.4.6_docker.tar
```

修改elasticsearch的配置文件 elasticsearc-2.4.6/config/elasticsearch.yml第54行，更改ip地址为本机ip地址

```
network.host: 10.211.55.5
```

创建docker容器运行

```
docker run -dti --network=host --name=elasticsearch -v /home/python/elasticsearch-2.4.6/config:/usr/share/elasticsearch/config delron/elasticsearch-ik:2.4.6-1.0
```

### 5. 使用haystack对接Elasticsearch

Haystack为Django提供了模块化的搜索。它的特点是统一的，熟悉的API，可以让你在不修改代码的情况下使用不同的搜索后端（比如 Solr, Elasticsearch, Whoosh, Xapian 等等）。

我们在django中可以通过使用haystack来调用Elasticsearch搜索引擎。

1）安装

```
pip install drf-haystack
pip install elasticsearch==2.4.1
```

drf-haystack是为了在REST framework中使用haystack而进行的封装（如果在Django中使用haystack，则安装django-haystack即可）。

2）注册应用

```
INSTALLED_APPS = [
    ...
    'haystack',
    ...
]
```

3）配置

在配置文件中配置haystack使用的搜索引擎后端

```
# Haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://10.211.55.5:9200/',  # 此处为elasticsearch运行的服务器ip地址，端口号固定为9200
        'INDEX_NAME': 'meiduo',  # 指定elasticsearch建立的索引库的名称
    },
}

# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
```

**注意：**

**HAYSTACK_SIGNAL_PROCESSOR 的配置保证了在Django运行起来后，有新的数据产生时，haystack仍然可以让Elasticsearch实时生成新数据的索引**

4）创建索引类

通过创建索引类，来指明让搜索引擎对哪些字段建立索引，也就是可以通过哪些字段的关键字来检索数据。

在goods应用中新建search_indexes.py文件，用于存放索引类

```
from haystack import indexes

from .models import SKU


class SKUIndex(indexes.SearchIndex, indexes.Indexable):
    """
    SKU索引数据模型类
    """
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        """返回建立索引的模型类"""
        return SKU

    def index_queryset(self, using=None):
        """返回要建立索引的数据查询集"""
        return self.get_model().objects.filter(is_launched=True)
```

在SKUIndex建立的字段，都可以借助haystack由elasticsearch搜索引擎查询。

其中text字段我们声明为document=True，表名该字段是主要进行关键字查询的字段， 该字段的索引值可以由多个数据库模型类字段组成，具体由哪些模型类字段组成，我们用use_template=True表示后续通过模板来指明。

在REST framework中，索引类的字段会作为查询结果返回数据的来源。