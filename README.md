# Django-loonflow学习记录

##### 搭建loonflow时，我首先使用的是window10来搭建，后来仔细看了一下代码以后我就选择了使用阿里云服务器来搭建后端，并且使用centos7作为操作系统。

##### 首先遇到的第一个问题就是在搭建loonflow时数据库的问题，在使用virtualenv新建的python3虚拟环境里面安装mysql时安装mysqlclient库失败，在多次尝试以后我直接在系统环境中安装所有的依赖库来解决了此问题，（可能是因为虚拟环境里面我没有配置默认启动python3），解决了loonflow依赖库后很轻松的运行了loonflow后端，并且测试成功。

##### 在安装好后端loonfloww后我就开始搭建shutongFlow前端，在搭建时，数据库的创建、导入用户数据都很顺利，也成功启动vue来监听6061端口，但是在进行前后端数据库的同步工作时，安装python3-ldap时也报错了，后来了解到是因为openldap版本不兼容，于是我使用yum命令安装openldap，解决了安装后端依赖库后完成了前端的部署，成功使用python3 manage.py runserver 0.0.0.0:6062以及npm run dev发布了shutongFlow前端，

##### 在搭建前端数据库时建错了数据库，导致进入6062前端数据库后台时无法登录进去，后面重新建立了shutongflow数据库解决了此问题。


![1.png](https://i.loli.net/2020/11/18/t25LkdMWjsTQI8e.png)


##### 但是在登录前端6061端口时，报错但是在登录前端6061端口时，报错

> HTTP 405 Method Not Allowed， Allow: POST, OPTIONS， "detail": "方法 “GET” 不被允许。

##### 前端登录的时候他被后端给405了，直接登录失败。

![2.png](https://i.loli.net/2020/11/18/jl3tpcbzxJESa9B.png)


##### 查看后端信息显示为系统使用的是get请求，但是前端需要使用post请求才可以获取到数据。查看后端信息显示为系统使用的是get请求，但是前端需要使用post请求才可以获取到数据。

![3.png](https://i.loli.net/2020/11/18/Bb6vrZukyoqDf9c.png)



##### 在尝试修改GET、post请求后也没有解决，后来我以为是ip的问题，修改为39.100.110.139、0.0.0.0、127.0.0.1、loclhost等都没有解决，本想修改前端网页的代码，后来发现一个按钮用的都是js监听，想修改也无从下手，然后我就更换了前端框架，更换为workflow框架。在尝试修改GET、post请求后也没有解决，后来我以为是ip的问题，修改为39.100.110.139、0.0.0.0、127.0.0.1、loclhost等都没有解决，本想修改前端网页的代码，后来发现一个按钮用的都是js监听，想修改也无从下手，然后我就更换了前端框架，更换为workflow框架。

![4.png](https://i.loli.net/2020/11/18/3foe4nNdwYFHvrs.png)

##### Workflow框架的搭建跟shutongflow框架大同小异，根据搭建shutongflow框架的经验，在搭建workflow时并没有遇到棘手的问题，轻松使用命令启动了workflow前端。Workflow框架的搭建跟shutongflow框架大同小异，根据搭建shutongflow框架的经验，在搭建workflow时并没有遇到棘手的问题，轻松使用命令启动了workflow前端。

![5.png](https://i.loli.net/2020/11/18/tGMmLuUEOTqDxWs.png)

##### 至此前后端的搭建完成，我开始尝试实现请假功能，至此前后端的搭建完成，我开始尝试实现请假功能

##### 新建了laoshi、xuesheng两个用户并且赋予了对应的权限，我使用xuesheng用户成功发起请假工单，但是使用laoshi用户审批时，点击同意/拒绝按钮没有反应，但是前端已经向后端发送了数据，但是后端并没有解析成功，所以导致点击同意/拒绝按钮无响应。也可以是shutongflow框架并没有开发完，我看见github上也只是到达登录界面的一步，于是本次基于django框架的工单引擎搭建请假系统便到了目前这一步。新建了laoshi、xuesheng两个用户并且赋予了对应的权限，我使用xuesheng用户成功发起请假工单，但是使用laoshi用户审批时，点击同意/拒绝按钮没有反应，但是前端已经向后端发送了数据，但是后端并没有解析成功，所以导致点击同意/拒绝按钮无响应。本次基于django框架的工单引擎搭建请假系统便到了目前这一步。

![6.png](https://i.loli.net/2020/11/18/7IQzxbnOSUgt1M9.png)
