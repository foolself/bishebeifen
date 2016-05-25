import re, os
from drozer import android
from drozer.modules import common, Module
from output import Output

class check(Module, common.Assets, common.Filters, common.PackageManager):

    name = "Get attack surface of package"
    description = "Examine the attack surface of an installed package."
    examples = """Finding the attack surface of the built-in browser

    dz> run app.package.attacksurface com.android.browser

    6 activities exported
    4 broadcast receivers exported
    1 content providers exported
    0 services exported"""
    author = "MWR InfoSecurity (@mwrlabs)"
    date = "2012-11-06"
    license = "BSD (3 clause)"
    path = ["mapp", "backup"]
    permissions = ["com.mwr.dz.permissions.GET_CONTEXT"]

    def add_arguments(self, parser):
        parser.add_argument("package", help="the identifier of the package to inspect")

    def execute(self, arguments):
        package = self.packageManager().getPackageInfo(arguments.package, common.PackageManager.GET_ACTIVITIES | common.PackageManager.GET_RECEIVERS | common.PackageManager.GET_PROVIDERS | common.PackageManager.GET_SERVICES)
        application = package.applicationInfo
        appname = str(application.packageName)
        opHlr = Output(appname)
        node_backup = opHlr.insert("Backup")
        if self.__write_manifest(package.packageName):
            print "ok"
            opHlr.insert("AllowBackup", "False", node_backup)
        else:
            opHlr.insert("AllowBackup", "True", node_backup)
            print "allowBackup"
        opHlr.write()
    def __write_manifest(self, package):
        lines = self.getAndroidManifest(package)
        r = re.compile(r'allowBackup="false"')
        isAllowBackup = re.search(r, lines)
        return isAllowBackup