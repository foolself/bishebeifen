---
title: my doc for drozer
---

# 研究背景
---
简述课题研究内容，必要性，Android 安全现状

# Android 安全理论
---
简述 Android 安全相关的理论知识

## Android 应用程序安全 
* 分类
* Android 安全机制
* 漏洞，攻击方法
* 防御策略

# 检测标准 standard
---
提出自己的 Android App 安全检测标准

## 检测 App 安全标准

* 思路来源（权威性）
* 几个方面
* 如何实施
* 检测难度

# 检测工具 tool
---
列举目前大家常用的检测工具，及着重的介绍本课题所使用的检测工具 drozer


# 检测 detection
---

## connect device

open the drozer agent on you mobile device, and turn on the button of "Embedded Server".

```
$ adb kill-server
$ adb start-server
$ adb forward tcp:31415 tcp:31415
$ drozer console connect
```

## install application

```
adb install packagename.apk
```

## get app's information
---

list the application summary information and output to a file

* Get the application package name.
```
dz> run app.package.list -f estro
com.estrongs.android.pop (ES File Explorer)
```

* Now, use the package name to get information.
This step will also output the information to a file.
```
dz> run mapp.package.info -a com.estrongs.android.pop
...
dz> run mapp.package.attacksurface com.estrongs.android.pop
...
dz> run mapp.activity.info -a com.estrongs.android.pop
...
dz> run mapp.broadcast.info -a com.estrongs.android.pop
...
dz> run mapp.provider.info -a com.estrongs.android.pop
...
dz> run mapp.service.info -a com.estrongs.android.pop
...
```

To find the activities that are not exported by an application, you can examine the manifest or use the -u flag on the app.activity.info module.

e.g.

```
dz> run mapp.activity.info -a com.estrongs.android.pop -u
```

## Exploiting Insecure Content Providers

### Unprotected Content Providers

> A common root cause of content provider problems is the fact that they are not explicitly marked as exported="false" in their manifest declarations because the assumption is that they follow the same default export behavior as other components.

gather information about exported content providers

```
dz> run app.provider.info -a com.mwr.example.sieve
```

All content providers whether they are exported or not can be queried from a privileged context. To find content providers inside the default Android Clock package that have not been exported, you can use the -u flag on app.provider .info:

```
dz> run app.provider.info -a com.android.deskclock -u
```

Scan content URIs with follow command

```
dz> run app.provider.finduri com.mwr.example.sieve 
Scanning com.mwr.example.sieve... 
content://com.mwr.example.sieve.DBContentProvider/ 
content://com.mwr.example.sieve.FileBackupProvider/ 
content://com.mwr.example.sieve.DBContentProvider 
content://com.mwr.example.sieve.DBContentProvider/Passwords/ 
content://com.mwr.example.sieve.DBContentProvider/Keys/ 
content://com.mwr.example.sieve.FileBackupProvider 
content://com.mwr.example.sieve.DBContentProvider/Passwords 
content://com.mwr.example.sieve.DBContentProvider/Keys
```

Now, we get some path that we can access and have any protect permissions. and we may found something can exploit like: `content://com.mwr.example.sieve.DBContentProvider/Passwords`

Query this content URI by follow command: 

```
dz> run app.provider.query content://com.mwr.example.sieve.DBContentProvider/Passwords
```

Further more, we can insert a itme to this database and so on.

## Attacking Insecure Services

### Unprotected Started Services

> If a service is exported, either explicitly or implicitly, other applications on the device can interact with it. Started services are ones that implement the onStartCommand() method inside its class. This method receives intents destined for this service from applications and may be a source of vulnerabilities for an attacker. This is completely dependent on what the code does inside this function. The code may perform an unsafe task even just by being started or may use parameters that are sent and when certain conditions take place, perform an unexpected action.

## Abusing Broadcast Receivers

## scanner

```
scanner.activity.browsable   scanner.misc.writablefiles 
scanner.misc.native               scanner.provider.finduris 
scanner.misc.readablefiles   scanner.provider.injection 
scanner.misc.secretcodes     scanner.provider.sqltables 
scanner.misc.sflagbinaries   scanner.provider.traversal
```



# 检测报告 report
---
检测结果分析，如何呈现，量化

## 

# 存在问题，不足
---



# 批量处理

给定一个文件夹，安装该文件下的apk文件，并检测行对应的 application，

* 启动环境，device, adb, drozer

* 安装 apk 文件
adb install ***.apk

* 获得所安装 apk 文件的包名，检测及卸载时用
aapt d badging design/apps/xbrowser-release.apk | grep 'package:'

* 检测
drozer, go xxx.xxx.xxx

* 卸载
adb uninstall xxx.xxx.xxx
