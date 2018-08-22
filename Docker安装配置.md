# Docker安装配置

更新ubuntu的apt源索引

```
sudo apt-get update
```

安装包允许apt通过HTTPS使用仓库

```
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
```

添加Docker官方GPG key,需要网络状况良好

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

设置Docker稳定版仓库

```
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

添加仓库后，更新apt源索引

```
sudo apt-get update
```

安装最新版Docker CE（社区版）

```
sudo apt-get install docker-ce
```

检查Docker CE是否安装正确

```
sudo docker run hello-world
```

为了避免每次命令都输入sudo，可以设置用户权限，**注意执行后须注销重新登录**

```
sudo usermod -a -G docker $USER
```

## 启动与停止

安装完成Docker后，默认已经启动了docker服务，如需手动控制docker服务的启停，可执行如下命令

```
# 启动docker
sudo service docker start

# 停止docker
sudo service docker stop

# 重启docker
sudo service docker restart
```

#### 列出镜像

```
docker image ls
```

#### 拉取镜像

Docker维护了镜像仓库，分为共有和私有两种，共有的官方仓库[Docker Hub(https://hub.docker.com/)](https://hub.docker.com/)是最重要最常用的镜像仓库。私有仓库（Private Registry）是开发者或者企业自建的镜像存储库，通常用来保存企业 内部的 Docker 镜像，用于内部开发流程和产品的发布、版本控制。

要想获取某个镜像，我们可以使用pull命令，从仓库中拉取镜像到本地，如

```
docker image pull library/hello-world
```

#### 删除镜像

```
docker image rm 镜像名或镜像id
```

### 创建容器

```
docker run [option] 镜像名 [向启动容器中传入的命令]
```

#### 交互式容器

例如，创建一个交互式容器，并命名为myubuntu

```
docker run -it --name=myubuntu ubuntu /bin/bash
```

#### 守护式容器

创建一个守护式容器:如果对于一个需要长期运行的容器来说，我们可以创建一个守护式容器。在容器内部exit退出时，容器也不会停止。

```
docker run -dit --name=myubuntu2 ubuntu
```

#### 进入已运行的容器

```
docker exec -it 容器名或容器id 进入后执行的第一个命令
```

#### 查看容器

```
# 列出本机正在运行的容器
docker container ls

# 列出本机所有容器，包括已经终止运行的
docker container ls --all
```

#### 停止与启动容器

```
# 停止一个已经在运行的容器
docker container stop 容器名或容器id

# 启动一个已经停止的容器
docker container start 容器名或容器id

# kill掉一个已经在运行的容器
docker container kill 容器名或容器id
```

#### 删除容器

```
docker container rm 容器名或容器id
```

## 将容器保存为镜像

我们可以通过如下命令将容器保存为镜像

```
docker commit 容器名 镜像名
```

## 镜像备份与迁移

我们可以通过save命令将镜像打包成文件，拷贝给别人使用

```
docker save -o 保存的文件名 镜像名
```

在拿到镜像文件后，可以通过load方法，将镜像加载到本地

```
docker load -i ./ubuntu.tar
```

获取镜像可以通过下载

```
docker image pull delron/fastdfs
```

## 运行tracker

执行如下命令开启tracker 服务

```
docker run -dti --network=host --name tracker -v /var/fdfs/tracker:/var/fdfs delron/fastdfs tracker
```

执行如下命令查看tracker是否运行起来

```
docker container ls
```

如果想停止tracker服务，可以执行如下命令

```
docker container stop tracker
```

停止后，重新运行tracker，可以执行如下命令

```
docker container start tracker
```

## 运行storage

执行如下命令开启storage服务

```
docker run -dti --network=host --name storage -e TRACKER_SERVER=10.211.55.5:22122 -v /var/fdfs/storage:/var/fdfs delron/fastdfs storage
```

执行如下命令查看storage是否运行起来

```
docker container ls
```

如果想停止storage服务，可以执行如下命令

```
docker container stop storage
```

停止后，重新运行storage，可以执行如下命令

```
docker container start storage
```

**注意：如果无法重新运行，可以删除/var/fdfs/storage/data目录下的fdfs_storaged.pid 文件，然后重新运行storage。**