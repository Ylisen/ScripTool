# 分发脚本
### 1. scp（secure copy）安全拷贝
scp可以实现服务器与服务器之间的数据拷贝。（from server1 to server2）  
* 基本语法
```
scp  -r   $pdir/$fname  $user@slave$host:$pdir/$fname
命令   递归  要拷贝的文件路径/名称   目的用户@主机:目的路径/名称
``` 
* 案例
1. 在slave01上，将slave01中/opt/module目录下的软件拷贝到slave02上。
```bash
[myuser@slave01 /]$ scp -r /opt/module  root@slave02:/opt/module
```
2. 在slave03上，将slave01服务器上的/opt/module目录下的软件拷贝到slave03上。
```bash
[myuser@slave03 opt]$sudo scp -r myuser@slave01:/opt/module root@slave03:/opt/module
```
3. 在slave03上操作将slave01中/opt/module目录下的软件拷贝到slave04上。
```bash
[myuser@slave03 opt]$ scp -r myuser@slave01:/opt/module root@slave04:/opt/module
```
注意：拷贝过来的/opt/module目录，别忘了在hadoop102、hadoop103、hadoop104上修改所有文件的，所有者和所有者组。sudo 
```bash
chown myuser:myuser -R /opt/module
```

### 2. rsync 远程同步工具
rsync主要用于备份和镜像。具有速度快、避免复制相同内容和支持符号链接的优点。
rsync和scp区别：用rsync做文件的复制要比scp的速度快，rsync只对差异文件做更新。scp是把所有文件都复制过去。   
* 基本语法
```bash
rsync    -rvl       $pdir/$fname        $user@slave$host:$pdir/$fname
命令   选项参数   要拷贝的文件路径/名称    目的用户@主机:目的路径/名称
```
选项参数说明

| 选项 | 功能  |
| ------------ | ------------ |
|  -r | 递归  |
| -v  | 显示复制过程  |
| -l  | 拷贝符号连接  |

* 案例
1. 把slave01机器上的/opt/software目录同步到slave02服务器的root用户下的/opt/目录
```bash
[myuser@slave01 opt]$ rsync -rvl /opt/software/ root@slave02:/opt/software
```

### 3. xsync集群分发脚本
* 需求：循环复制文件到所有节点的相同目录下
* 说明：在/home/myuser/bin这个目录下存放的脚本，myuser用户可以在系统任何地方直接执行。
* 脚本实现
1. 在/home/myuser目录下创建bin目录，并在bin目录下xsync创建文件，文件内容如下：
```bash
[myuser@slave02 ~]$ mkdir bin
[myuser@slave02 ~]$ cd bin/
[myuser@slave02 bin]$ touch xsync
[myuser@slave02 bin]$ vi xsync
```
在该文件中编写如下代码
```shell
#!/bin/bash
#1 获取输入参数个数，如果没有参数，直接退出
pcount=$#
if((pcount==0)); then
echo no args;
exit;
fi
#2 获取文件名称
p1=$1
fname=`basename $p1`
echo fname=$fname
#3 获取上级目录到绝对路径
pdir=`cd -P $(dirname $p1); pwd`
echo pdir=$pdir
#4 获取当前用户名称
user=`whoami`
#5 循环
for((host=103; host<105; host++)); do
        echo ------------------- slave$host --------------
        rsync -rvl $pdir/$fname $user@slave$host:$pdir   # 此为rsync的语句
done
```

* 修改脚本 xsync 具有执行权限
```bash
[myuser@slave02 bin]$ chmod 777 xsync
```
* 调用脚本形式：xsync 文件名称
```shell
[myuser@slave02 bin]$ xsync /home/myuser/bin
```

注意：如果将xsync放到/home/myuser/bin目录下仍然不能实现全局使用，可以将xsync移动到/usr/local/bin目录下。








