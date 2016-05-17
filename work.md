---
title: drozer
tags:
---
## 1. Introduction
---
drozer is the leading security assessment framework for the Android platform.
drozer came about because we were tired of having to create dozens of custom, one-use applications to test for vulnerabilities during the security assessment of an Android app or device. The process was laborious and wasted a lot of time.
The need for a proper tool for dynamic analysis on Android was clear, and drozer was born.
This guide explains how to get started with drozer, and how to use it to perform a security assessment. It assumes some familiarity with the Android platform, in particular its IPC mechanism. We recommend that you read the Android Developers’ Guide (http://developer.android.com) before this guide.
Another resource which makes extensive use of drozer in its Android chapters is “The Mobile Application Hacker’s Handbook” (ISBN: 978-1-118-95850-6) which was written by one of drozer’s developers. This publication
explains Android security concepts and is comprehensive in its use of drozer.

drozer是为Android平台的领先的安全评估框架。
drozer的出现，因为我们厌倦了手动创建几十自定义，一是使用的应用程序的Andr​​oid应用程序或设备的安全评估过程中来测试漏洞。这个过程是艰苦的，浪费了很多时间。
我们需要一个 android 平台的动态分析的工具，因此drozer诞生了。
本指南介绍如何开始使用drozer，以及如何使用它来进行安全评估。它假定一些熟悉Android平台，特别是其IPC机制。我们建议您在本指南之前阅读Android开发者指南（http://developer.android.com）。
另一个资源是“移动应用黑客手册”（ISBN：978-1-118-95850-6）,在其Android章节,介绍了Android的安全概念,大量全面的使用了 drozer。

## 2. What is drozer
---
drozer allows you to assume the role of an Android app and interact with other apps. It can do anything that an installed application can do, such as make use of Android’s Inter-Process Communication (IPC) mechanism and interact with the underlying operating system.
drozer also helps to you to remotely exploit Android devices, by building malicious files or web pages that exploit known vulnerabilities. 
The payload that is used in these exploits is a rogue drozer agent that is essentially a remote administration tool. 
Depending on the permissions granted to the vulnerable app, drozer can install a full agent, inject a limited agent into the process using a novel technique or spawn a reverse shell.
drozer is open source software, released under a BSD license and maintained by MWR InfoSecurity. To get in touch with the project see Section 6.

drozer允许你设定一个Android应用程序和其他应用程序的交互作用。它可以做任何安装的应用程序可以做事情，比如利用Android的进程间通信（IPC）机制与底层操作系统交互。
利用 drozer 也可以通过建立恶意文件或利用网页漏洞，来远程检测 Android 设备。drozer 是一个漏洞检测管理工具。
根据授予的脆弱的应用程序的权限，可以安装一个全drozer代理，将有限的代理的过程中使用了一种新的技术或产生反向的外壳。
drozer是开放源代码的软件，发布了BSD许可下由MWR InfoSecurity保持。去接触的项目见6节。

## 3. How drozer Works
---
Agent— A lightweight Android application that runs on the device or emulator being used for testing. There are two versions of the agent, one that provides a user interface and embedded server and another that does not contain a graphical interface and can be used as a Remote Administration Tool on a compromised device. Since version 2.0, drozer supports “Infrastructure mode,” in which the agent establishes a connection outward to traverse firewalls and NAT. This allows more realistic attack scenarios to be created and requires a drozer server.
Console—A command-line interface running on your computer that allows you to interact with the device through the agent.
Server—Provides a central point where consoles and agents can rendezvous, and routes sessions between them.
These components use a custom protocol named drozerp (drozer protocol) to exchange data. The agent is somewhat of an empty shell that knows only how to run commands it receives from the console and provide the result. A very technically brilliant method of using the Java Reflection API facilitates the execution of code from Python in the console to Java on the agent. This means that from Python code it is possible to instantiate and interact with Java objects on the connected device.

## 4. Modules
---
```
dz> list
app.activity.forintent                   Find activities that can handle the given intent
app.activity.info                        Gets information about exported activities.
app.activity.start                       Start an Activity
app.broadcast.info                       Get information about broadcast receivers
app.broadcast.send                       Send broadcast using an intent
app.broadcast.sniff                      Register a broadcast receiver that can sniff particular intents
app.package.attacksurface                Get attack surface of package
app.package.backup                       Lists packages that use the backup API (returns true on FLAG_ALLOW_BACKUP)
app.package.debuggable                   Find debuggable packages
app.package.info                         Get information about installed packages
app.package.launchintent                 Get launch intent of package
app.package.list                         List Packages
app.package.manifest                     Get AndroidManifest.xml of package
app.package.native                       Find Native libraries embedded in the application.
app.package.shareduid                    Look for packages with shared UIDs
app.provider.columns                     List columns in content provider
app.provider.delete                      Delete from a content provider
app.provider.download                    Download a file from a content provider that supports files
app.provider.finduri                     Find referenced content URIs in a package
app.provider.info                        Get information about exported content providers
app.provider.insert                      Insert into a Content Provider
app.provider.query                       Query a content provider
app.provider.read                        Read from a content provider that supports files
app.provider.update                      Update a record in a content provider
app.service.info                         Get information about exported services
app.service.send                         Send a Message to a service, and display the reply
app.service.start                        Start Service
app.service.stop                         Stop Service
auxiliary.webcontentresolver             Start a web service interface to content providers.
exploit.jdwp.check                       Open @jdwp-control and see which apps connect
exploit.pilfer.general.apnprovider       Reads APN content provider
exploit.pilfer.general.settingsprovider  Reads Settings content provider
information.datetime                     Print Date/Time
information.deviceinfo                   Get verbose device information
information.permissions                  Get a list of all permissions used by packages on the device
scanner.activity.browsable               Get all BROWSABLE activities that can be invoked from the web browser
scanner.misc.native                      Find native components included in packages
scanner.misc.readablefiles               Find world-readable files in the given folder
scanner.misc.secretcodes                 Search for secret codes that can be used from the dialer
scanner.misc.sflagbinaries               Find suid/sgid binaries in the given folder (default is /system).
scanner.misc.writablefiles               Find world-writable files in the given folder
scanner.provider.finduris                Search for content providers that can be queried from our context.
scanner.provider.injection               Test content providers for SQL injection vulnerabilities.
scanner.provider.sqltables               Find tables accessible through SQL injection vulnerabilities.
scanner.provider.traversal               Test content providers for basic directory traversal vulnerabilities.
shell.exec                               Execute a single Linux command.
shell.send                               Send an ASH shell to a remote listener.
shell.start                              Enter into an interactive Linux shell.
tools.file.download                      Download a File
tools.file.md5sum                        Get md5 Checksum of file
tools.file.size                          Get size of file
tools.file.upload                        Upload a File
tools.setup.busybox                      Install Busybox.
tools.setup.minimalsu                    Prepare 'minimal-su' binary installation on the device. 
```

## 5. Exploitation Features in drozer
---
drozer offers features to help deploy a drozer agent onto a remote device, through means of exploiting applications on the device or performing attacks that involve a degree of social engineering.
drozer provides a framework for sharing of exploits and reuse of high quality payloads. It provides modules that allow the generation of shell code for use in exploits in order to help gain access to sensitive data on the remotely compromised device.

drozer提供的功能来帮助部署drozer代理到远程设备，通过利用设备上的应用程序或执行涉及一定程度的社会工程的攻击手段。
drozer提供了攻击的共享和重复使用的高品质的有效载荷的框架。它提供了多个模块，允许以帮助访问敏感数据的远程损害设备上的用于攻击使用壳代码的生成。

## 6. 编写自己的 module
---

### 创建 module repository
运行命令，创建自己的 module repository：

```
dz> module repository create repository
```
会在当前目录（随便什么地方）下创建名为 repository 的文件夹及 __init__.py 文件。

### 编写 module
首先准备好 module 文件，如 test.py ，内容如下：

```
from drozer.modules import Module

class GetInteger(Module):

    name = ""
    description = ""
    examples = ""
    author = "Joe Bloggs (@jbloggs)"
    date = "2012-12-21"
    license = "BSD (3-clause)"
    path = ["ex", "random"]

    def execute(self, arguments):
        random = self.new("java.util.Random")
        integer = random.nextInt()

        self.stdout.write("int: %d\n" % integer)
```

在 repository 下新建文件夹 exp，此处应与 test.py 文件中的 path 声明保持一致（path = ["exp", "test"]）。
将自己写好的 module 文件 test.py 放在 repository/exp 下，
并在 repository/exp 下新建空白文件 __init__.py

### 激活

接着运行命令：

```
dz> module repository enable repository
```

就完成了。

### 使用运行

运行命令：

```
dz> run exp.test.getinteger
```

使用自定的 module，输出结果如下：

```
int: -1962468164
```

> **Tips**
drozer 安装目录：
```
/usr/local/lib/python2.7/dist-packages
```

## 7. 模块的reload及动态加载问题
---
编写drozer module难免会涉及到调试的问题,drozer console提供了debug选项,会在console中
打印异常信息,但是比较麻烦的是,修改module源码后必须要重启drozer console才能生效。
查看drozer源码,发现drozer在debug模式下提供了reload命令,但是测试了下,在mac下并没有
用,还是要重启console才能生效。仔细研究drozer loader.py的相关源码:

```
def  all(self, base):
     """
     Loads all modules from the specified module repositories, 
and returns a  collection of module identifiers.
     """
 
     if (len(self.__modules)  ==  0):
        self.__load(base)
 
     return  sorted(self.__modules.keys())
 
def  get(self, base, key):
    """
    Gets a module implementation, given its identifier.
    """
 
     if (len(self.__modules)  ==  0):
        self.__load(base)
 
     return  self.__modules[key]
 
def  reload(self):
    self.__modules  =  {}
```

reload命令将 self.__modules 置为空,在get中按理说就会重新加载所有的drozer模块。但是在
mac下始终无法实现该功能,其他平台未做测试。这里就涉及到python模块的import及reload机制
问题,在网上查找到python的reload机制一些解释:

>reload会重新加载已加载的模块,但原来已经使用的实例还是会使用旧的模块, 而新生产的实例会使用新的模块, reload后还是用原来的内存地址;不能支持from。。import。。格式的模块进行重新加载。[http://blog.csdn.net/five3/article/details/7762870](http://blog.csdn.net/five3/article/details/7762870)

猜测可能就是这个问题,虽然用python的reload机制可以重新加载模块,但是以前使用的模块可能
还是在使用中,导致修改的源码没有生效。
为什么不在执行时动态加载模块呢?这样可以保证加载的模块源码是最新的。
分析了drozer相关的所有源码,终于在session.py中找到实例化模块类的代码:

``` python
def __module(self, key):
        """
        Gets a module instance, by identifier, and initialises it with the
        required session parameters.
        """

        module = None

        try:
            module = self.modules.get(self.__module_name(key))
        except KeyError:
            pass

        if module == None:
            try:
                module = self.modules.get(key)
            except KeyError:
                pass

        if module == None:
            raise KeyError(key)
        else:
            return module(self)

```

该函数的功能就是根据模块类的key实例化该模块,从而运行该模块。因此,我们可以在这里实现
动态加载要运行的模块类,放弃已经加载的模块:

```
def  __module(self, key):
 
   """
   Gets a module instance, by identifier, and initialises it 
with the
   required session parameters.
   """
 
   module  =  None
 
    try :
       module  =  self.modules.get(self.__module_name(key))
    except  KeyError:
        pass
 
    if  module  ==  None:
        try :
           module  =  self.modules.get(key)
        except  KeyError:
            pass
 
    if  module  ==  None:
        raise  KeyError(key)
    else :
 
       #reload module
       mod  =  reload(sys.modules[module.__module__])
 
       module_class_name  =  module.__name__
       module_class  =  getattr(mod,module_class_name)  #get module class object
        return  module_class(self)
```

关键的代码如下:

```
#reload module   
mod  =  reload(sys.modules[module.__module__])
 
module_class_name  =  module.__name__
module_class  =  getattr(mod,module_class_name)  #get module class 
object
return  module_class(self)
```

首先使用python的reload函数重新加载指定的模块,然后再在重新加载的模块中查找到drozer模块
关联的类,最后实例化并返回。只需添加几行代码便可实现动态加载模块类,这样调试的时候就
不用每次重启drozer console了。这里只是提供了一种简单的实现动态加载模块的方法,主要是方
便模块的编写及测试。

## 8. 用java代码编写dex插件
---
### *待解决。。。*
首先我们将该java文件编译为class文件:

```
javac ­cp lib/android.jar dextest.java
```

然后用android sdk提供的dx工具将class文件转换为dex文件:

```
dx --dex --output=dextest.apk dextest*.class
```

这里编译遇到了问题：

```
UNEXPECTED TOP-LEVEL EXCEPTION:
java.lang.RuntimeException: Exception parsing classes
	at com.android.dx.command.dexer.Main.processClasds(Main.java:752)
	at com.android.dx.command.dexer.Main.processFileBytes(Main.java:718)
	at com.android.dx.command.dexer.Main.access$1200(Main.java:85)
	at com.android.dx.command.dexer.Main$FileBytesConsumer.processFileBytes(Main.java:1645)
	at com.android.dx.cf.direct.ClassPathOpener.processOne(ClassPathOpener.java:170)
	at com.android.dx.cf.direct.ClassPathOpener.process(ClassPathOpener.java:144)
	at com.android.dx.command.dexer.Main.processOne(Main.java:672)
	at com.android.dx.command.dexer.Main.processAllFiles(Main.java:574)
	at com.android.dx.command.dexer.Main.runMonoDex(Main.java:311)
	at com.android.dx.command.dexer.Main.run(Main.java:277)
	at com.android.dx.command.dexer.Main.main(Main.java:245)
	at com.android.dx.command.Main.main(Main.java:106)
Caused by: com.android.dx.cf.iface.ParseException: bad class file magic (cafebabe) or version (0034.0000)
	at com.android.dx.cf.direct.DirectClassFile.parse0(DirectClassFile.java:472)
	at com.android.dx.cf.direct.DirectClassFile.parse(DirectClassFile.java:406)
	at com.android.dx.cf.direct.DirectClassFile.parseToInterfacesIfNecessary(DirectClassFile.java:388)
	at com.android.dx.cf.direct.DirectClassFile.getMagic(DirectClassFile.java:251)
	at com.android.dx.command.dexer.Main.parseClass(Main.java:764)
	at com.android.dx.command.dexer.Main.access$1500(Main.java:85)
	at com.android.dx.command.dexer.Main$ClassParserTask.call(Main.java:1684)
	at com.android.dx.command.dexer.Main.processClass(Main.java:749)
	... 11 more
1 error; aborting
```

## 9. module install mwrlabs.develop
---
This module provides an interactive shell to test the instantiation of objects, retrieval of constant values, and execution of methods. For example, suppose you want to create a module that returns the package’s name when provided with an application’s UID. You could test it first using the auxiliary.develop .interactive module that was installed previously.
### 安装
```
dz> module install mwrlabs.develop
```

### 示例

```
dz> run auxiliary.develop.interactive 
Entering an interactive Python shell. Type 'c' to end. 
 
>/home/tyrone/dz-repo/mwrlabs/develop.py(24)execute() 
-> self.pop_completer() 
(Pdb) context = self.getContext() 
(Pdb) pm = context.getPackageManager() 
(Pdb) name = pm.getNameForUid(10059) 
(Pdb) print name 
com.mwr.dz
```

## 10. Application Components
---
Android applications and their underlying frameworks were designed in a way that keeps them modular and able to communicate with each other. The communication between applications is performed in a well-defined manner that is strictly facilitated by a kernel module named binder, which is an Inter-Process Communication (IPC) system that started as the OpenBinder project and was completely rewritten in 2008 for use on Android. It is implemented as a character device located at /dev/binder, which applications interact with through multiple layers of abstraction.

Android applications can make use of four standard components that can be invoked via calls to binder.

* Activities
Activities represent visual screens of an application with which users interact. For example, when you launch an application, you see its main activity. Figure 6.4 shows the main activity of the clock application.
* Services
Services are components that do not provide a graphical interface. They provide the facility to perform tasks that are long running in the background and continue to work even when the user has opened another application or has closed all activities of the application that contains the service. To view running services on your device go to the Running tab in the Application Manager, as shown in Figure 6.5.
Two different modes of operation exist for services. They can be started or bound to. A service that is started is typically one that does not require the ability to communicate back to the application that started it. A bound service provides an interface to communicate back results to the calling application. A started service continues to function even if the calling application has been terminated. A bound service only stays alive for the time that an application is bound to it.

* Broadcast receivers
Broadcast receivers are non-graphical components that allow an application to register for certain system or application events. For instance, an application that requires a notification when receiving an SMS would register for this event using a broadcast receiver. This allows a piece of code from an application to be executed only when a certain event takes place. This avoids a situation where any polling needs to take place and provides a powerful event-driven model for applications. In contrast to other application components, a broadcast receiver can be created at runtime.
* Content providers
These are the data storehouses of an application that provide a standard way to retrieve, modify, and delete data. The terminology used to define and interact with a content provider is similar to SQL: query, insert, update, and delete. This component is responsible for delivering an application’s data to another in a structured and secure manner. The developer defines the back-end database that supports a content provider, but a common choice is SQLite (see http://www.sqlite.org/), because Android makes the implementation of SQLite so easy due to their similar structures. Defining a content provider that can retrieve files and serve them is also possible. This may provide a preferable approach for applications that implement access control on the retrieval of their files from other applications.

## 10. attacksurface
---

```
dz> run app.package.attacksurface com.android.browser
dz> run app.broadcast.info -a com.android.browser
dz> run app.activity.info -a com.mwr.example.sieve -u
```

To find components that are not exported by an application, you can examine the manifest or use the -u flag on any of the drozer app.<component> .info modules.

The app.package.attacksurface module shows only application components that have been exported in their manifest. This means that application components that have not been exported and can be attacked from a privileged user context are not shown in this module’s output.

## now, using drozer
---

### interacting with components using drozer
eg.

```
dz>run app.activity.start --action android.intent.action.VIEW --data-uri http://www.baidu.com --component com.android.browser
```

### collect the app's info

```
dz> run app.package.info -a com.android.browser
```

> **PROTECTION LEVEL**
PROTECTION LEVEL	
INTEGER VALUE
DESCRIPTION
normal	
0x0
The default value for a permission. Any application may request a permission with this protection level.
dangerous	
0x1
Indicates that this permission has the ability to access some potentially sensitive information or perform actions on the device. Any application may request a permission with this protection level.
signature	
0x2
Indicates that this permission can only be granted to another application that was signed with the same certificate as the application that defined the permission.
signatureOrSystem	
0x3
This is the same as the signature protection level, except that the permission can also be granted to an application that came with the Android system image or any other application that is installed on the /system partition.
system	
0x10
This permission can only be granted to an application that came with the Android system image or any other application that is installed in particular folders on the /system partition.
development	
0x20
This permission can be granted from a privileged context to an application at runtime. This scarcely documented feature was discussed at https://code.google.com/p/android/issues/detail?id=34785.

### 


