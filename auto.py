import commands
from subprocess import call

directory = raw_input("please input apps directory: ")

apps_list = commands.getoutput("ls %s | grep '.apk'" % directory)
apps_list = apps_list.split('\n')

if not call(['adb', 'start-server']):
	for app in apps_list:
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

			print ">>>> uninstall... <<<<"
			if not call(['adb', 'uninstall', packageName]):
				print ">>>> uninstall success <<<<"
				print "Done.\n"
		else:
			print "ERROR"
