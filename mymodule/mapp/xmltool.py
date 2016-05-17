import os
from drozer import android
from drozer.modules import common, Module
from output import Output

class rexml(Module, common.Filters, common.IntentFilter, common.PackageManager):
    
    name = "Gets information about exported activities."
    description = "Gets information about exported activities."
    examples = """List activities exported by the Browser:

    dz> run app.activity.info --package com.android.browser
    Package: com.android.browser
      com.android.browser.BrowserActivity
      com.android.browser.ShortcutActivity
      com.android.browser.BrowserPreferencesPage
      com.android.browser.BookmarkSearch
      com.android.browser.AddBookmarkPage
      com.android.browser.widget.BookmarkWidgetConfigure"""
    author = "MWR InfoSecurity (@mwrlabs)"
    date = "2012-11-06"
    license = "BSD (3 clause)"
    path = ["mapp", "xmltool"]
    permissions = ["com.mwr.dz.permissions.GET_CONTEXT"]

    def add_arguments(self, parser):
        parser.add_argument("-a", "--package", default=None, help="specify the package to inspect")
        parser.add_argument("-f", "--filter", default=None, help="specify a filter term for the activity name")
        parser.add_argument("-i", "--show-intent-filters", action="store_true", default=False, help="specify whether to include intent filters")
        parser.add_argument("-u", "--unexported", action="store_true", default=False, help="include activities that are not exported")
        parser.add_argument("-v", "--verbose", action="store_true", default=False, help="be verbose")

    def execute(self, arguments):
        try:
            package = self.packageManager().getPackageInfo(arguments.package, common.PackageManager.GET_ACTIVITIES | common.PackageManager.GET_RECEIVERS | common.PackageManager.GET_PROVIDERS | common.PackageManager.GET_SERVICES)
            application = package.applicationInfo
            appname = str(application.packageName)
            filename = appname.replace(".", "_") + ".xml"
            self.__modify(filename)
        except:
            print "modify xml...something wrong!!!!!!"

    def __modify(self, filename):
        filepath = "report/" + filename
        orifile = open(filepath, "r")
        lines = []
        count = 1
        for l in orifile.readlines():
            if count == 2:
                lastLine = l
            if l[:1] == "<" and count > 4:
                pass
            else:
                rl = l.replace("\n","")
                rl = rl.replace("\t","")
                lines.append(rl)
            count = count + 1
        orifile.close()
        refile = open(filepath, "w")
        for l in lines:
            refile.write(l)

        refile.write(lastLine.replace("<", "</"))
        refile.close()
        print "\n>>>> reportion write to " + filepath + " <<<<\n"
