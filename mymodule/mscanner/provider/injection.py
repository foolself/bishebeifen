from pydiesel.reflection import ReflectionException

from drozer.modules import common, Module
from output import Output

class Injection(Module, common.FileSystem, common.PackageManager, common.Provider, common.Strings, common.ZipFile):

    name = "Test content providers for SQL injection vulnerabilities."
    description = "Search for content providers with SQL Injection vulnerabilities."
    examples = ""
    author = "Rob (@mwrlabs)"
    date = "2012-11-06"
    license = "BSD (3 clause)"
    path = ["mscanner", "provider"]
    permissions = ["com.mwr.dz.permissions.GET_CONTEXT"]

    def add_arguments(self, parser):
        parser.add_argument("-a", "--package", "--uri", dest="package_or_uri", help="specify a package, or content uri to search", metavar="<package or uri>")
        
    def execute(self, arguments):
        # print arguments.package_or_uri
        # package = self.packageManager().getPackageInfo(arguments.package, common.PackageManager.GET_ACTIVITIES | common.PackageManager.GET_RECEIVERS | common.PackageManager.GET_PROVIDERS | common.PackageManager.GET_SERVICES)
        appname = arguments.package_or_uri
        # application = package.applicationInfo
        # appname = str(application.packageName)
        opHlr = Output(appname)

        node_injection = opHlr.insert("Injection")

        vulnerable = { 'projection': set([]), 'selection': set([]), 'uris': set([]) }
    
        if arguments.package_or_uri != None and arguments.package_or_uri.startswith("content://"):
            self.__test_uri(arguments.package_or_uri, vulnerable)
        else:
            for uri in self.findAllContentUris(arguments.package_or_uri):
                self.__test_uri(uri, vulnerable)

        # remove the collection of vulnerable URIs from the set of all URIs
        vulnerable['uris'] = vulnerable['uris'] - vulnerable['projection'] - vulnerable['selection']
                        
        # print out a report
        self.stdout.write("Not Vulnerable:\n")
        node_Not_Vulnerable = opHlr.insert("Not_Vulnerable", None, node_injection)
        if len(vulnerable['uris']) > 0:
            for uri in vulnerable['uris']:
                self.stdout.write("  %s\n" % uri)
                opHlr.insert("item", uri, node_Not_Vulnerable)
        else:
            self.stdout.write("  No non-vulnerable URIs found.\n")
            opHlr.insert("item", "No non-vulnerable URIs found", node_Not_Vulnerable)

        self.stdout.write("\nInjection in Projection:\n")
        node_Injection_Projection = opHlr.insert("Injection_Projection", None, node_injection)
        if len(vulnerable['projection']) > 0:
            for uri in vulnerable['projection']:
                self.stdout.write("  %s\n" % uri)
                opHlr.insert("item", uri, node_Injection_Projection)
        else:
            self.stdout.write("  No vulnerabilities found.\n")
            opHlr.insert("item", "No vulnerabilities found", node_Injection_Projection)

        self.stdout.write("\nInjection in Selection:\n")
        node_Injection_Selection = opHlr.insert("Injection_Selection", None, node_injection)
        if len(vulnerable['selection']) > 0:
            for uri in vulnerable['selection']:
                self.stdout.write("  %s\n" % uri)
                opHlr.insert("item", uri, node_Injection_Selection)
        else:
            self.stdout.write("  No vulnerabilities found.\n")
            opHlr.insert("item", "No vulnerabilities found", node_Injection_Selection)

        opHlr.write()
    def __test_uri(self, uri, vulnerable):
        vulnerable['uris'].add(uri)

        try:
            self.contentResolver().query(uri, projection=["'"])
        except ReflectionException as e:
            if e.message.find("unrecognized token") >= 0:
                vulnerable['projection'].add(uri)

        try:
            self.contentResolver().query(uri, selection="'")
        except ReflectionException as e:
            if e.message.find("unrecognized token") >= 0:
                vulnerable['selection'].add(uri)
            
