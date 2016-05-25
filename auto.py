import commands
from subprocess import call

directory = raw_input("please input apps directory: ")

apps_list = commands.getoutput("ls %s | grep '.apk'" % directory)
apps_list = apps_list.split('\n')

list_success = []
list_failt = []


if not call(['adb', 'start-server']) and not call(['adb', 'forward', 'tcp:31415', 'tcp:31415']):
	for app in apps_list:
		isOK = False
		appPath = directory + app
		print ">>>> install %s... <<<<" % app
		if not call(['adb', 'install', appPath]):
			packageInfo = commands.getoutput("aapt dump badging %s | grep 'package'" % appPath)
			packageName = packageInfo.split('\'')[1]
			print ">>>> install success. <<<<"
			print ">>>> package name: %s <<<<" % packageName

			print ">>>> begin examine... <<<<"
			if call(['drozer', 'console', 'connect', packageName]):
				print ">>>> examine done <<<<"
				isOK = True
			print ">>>> uninstall... <<<<"
			if not call(['adb', 'uninstall', packageName]):
				print ">>>> uninstall success <<<<"
				print "Done.\n"
		else:
			print "ERROR"
		if isOK:
			list_success.append(app)
		else:
			list_failt.append(app)

print "-*-*-*"
print ">>>> %d success <<<<" % len(list_success)
print str(list_success)
print ">>>> %d failt <<<<" % len(list_failt)
print str(list_failt)
print "-*-*-*"
