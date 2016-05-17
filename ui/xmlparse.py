from bs4 import BeautifulSoup as bs

class Parser(object):
	"""docstring for Pa"""
	def __init__(self, filepath):
		self.soup = bs(open(filepath), 'xml')
		self.package = self.soup.package
		self.iss_permissions = []

	def get_iss_permissions(self, who = None):
		result = ""
		try:
			file = open("permission.txt", 'r')
			for i in file.readlines():
				self.iss_permissions.append(i.replace("\n",""))
			file.close()
		except:
			result = "can not found the permissions.txt file"
		permissions = self.get_Permissions(1)
		for i in permissions:
			if i in self.iss_permissions:
				result = result + i + "\n"
		result = "Null" if result =="" else result
		return result if who==None else result[:800]

	def get_package_info(self):
		result = "package_info: \n\n"

		package_info = self.package.package_info
		for x in package_info.children:
			try:
				item = x.name + ": " + x.contents[0] + "\n\n"
				result = result + item
			except:
				pass
		return result

	def get_Permissions(self, who = None):
		list_up = []
		list_dp = []
		Uses_Permissions = self.package.package_info.Uses_Permissions
		Defines_Permissions = self.package.package_info.Defines_Permissions
		for u in Uses_Permissions.children:
			list_up.append(u.contents[0])
		for d in Defines_Permissions.children:
			list_dp.append(d.contents[0])
		result_up = "Uses_Permissions: \n\n"
		for i in list_up:
			result_up = result_up + i + "\n\n"
		result_dp = "Defines_Permissions: \n\n"
		for i in list_dp:
			result_dp = result_dp + i + "\n\n"

		result = result_up + "\n" + result_dp
		if who == None:
			return result
		else:
			return list_up

	def get_Attack_Surface(self):
		list_Attack_Surface = []
		result = "Attack_Surface: \n\n"
		Attack_Surface = self.package.Attack_Surface
		for i in Attack_Surface.children:
			list_Attack_Surface.append([i.name, i.contents[0]])
		for i in list_Attack_Surface:
			result = result + i[0] + ": " + i[1] + "\n\n"
			
		return result
	def get_Activities(self):
		list_Activities = []
		result = "Exported_Activity: \n\n"
		try:
			Exported_Activity = self.package.Activity.Exported_Activity
			for i in Exported_Activity.children:
				list_Activities.append([i.Activity_Name.contents[0], i.Activity_Permission.contents[0]])
			for i in list_Activities:
				result = result + "Activity_Name: " + i[0] + "\n" + "Activity_Permission: " + i[1] + "\n\n" 
		except:
			result = result + "Null"
		return result
	def get_Broadcast(self):
		list_Broadcast = []
		result = "Exported_Broadcast_Receivers: \n\n"
		try:
			Broadcast = self.package.Broadcast.Exported_Receivers
			for i in Broadcast.children:
				list_Broadcast.append([i.Receiver_Name.contents[0], i.Receiver_Permission.contents[0]])
			for i in list_Broadcast:
				result = result + "Receiver_Name: " + i[0] + "\n" + "Receiver_Permission: " + i[1] + "\n\n"
		except:
			result = result + "Null"
		return result
	def get_Provider(self):
		list_Provider = []
		result = "Exported_Providers: \n\n"
		try:
			Provider = self.package.Provider.Exported_Providers
			for i in Provider.children:
				list_Provider.append([i.Authority.contents[0], i.Read_Permission.contents[0], 
								i.Write_Permission.contents[0], i.Content_Provider.contents[0], 
								i.Multiprocess_Allowed.contents[0], i.Grant_Uri_Permissions.contents[0]])
			for i in list_Provider:
				result = result + "Authority: " + i[0] + "\n" + "Read_Permission: " + i[1] + "\n" \
						+ "Write_Permission: " + i[2] + "\n" + "Content_Provider: " + i[3] + "\n" \
						+ "Multiprocess_Allowed: " + i[4] + "\n" + "Grant_Uri_Permissions: " + i[5] + "\n\n"
		except:
			result = result + "Null"
		return result
	def get_Service(self):
		list_Service = []
		result = "Exported_Services: \n\n"
		try:
			Service = self.package.Service.Exported_Services
			for i in Service.children:
				list_Service.append([i.Service_Name.contents[0], i.Service_Permission.contents[0]])
			for i in list_Service:
				result = result + "Service_Name: " + i[0] + "\n" + "Service_Permission: " + i[1] + "\n\n"
		except:
			result = result + "Null"
		return result
	def get_Uri(self):
		list_Uri = []
		result = "Content URIs: \n\n"
		FindUri = self.package.FindUri
		for i in FindUri.children:
			list_Uri.append(i.contents[0])
		for i in list_Uri:
			result = result + i + "\n\n"

		return result
	def get_Browsable(self, who=None):
		Browsable = self.package.Browsable
		Invocable_URIs = Browsable.Invocable_URIs
		Classes = Browsable.Classes

		result = "Browsable: \n\n"
		try:
			result = result + "Invocable_URIs: \n\n"
			for i in Invocable_URIs.children:
				result = result + i.contents[0] + "\n"
			result = result + "\nClasses: \n\n"
			for i in Classes.children:
				result = result + i.contents[0] + "\n"
		except:
			result = "Browsable: \n\nNull."

		return result if who == None else result[:800]
	def get_Injection(self):
		list_Not_Vulnerable = []
		list_Injection_Projection = []
		list_Injection_Selection = []

		Injection = self.package.Injection
		Not_Vulnerable = Injection.Not_Vulnerable
		Injection_Projection = Injection.Injection_Projection
		Injection_Selection = Injection.Injection_Selection

		result = "Injection: \n\n"

		result = result + "Not_Vulnerable: \n\n"
		for i in Not_Vulnerable.children:
			result = result + i.contents[0] + "\n\n"
			list_Not_Vulnerable.append(i.contents[0])

		result = result + "Injection_in_Projection: \n\n"
		for i in Injection_Projection.children:
			result = result + i.contents[0] + "\n\n"
			list_Injection_Projection.append(i.contents[0])

		result = result + "Injection_in_Selection: \n\n"
		for i in Injection_Selection.children:
			result = result + i.contents[0] + "\n\n"
			list_Injection_Selection.append(i.contents[0])

		return result

	def get_SqlTables(self, who = None):
		SqlTables = self.package.SqlTables
		result = "Access SqlTables: \n\n"
		try:
			if list(SqlTables.children):
				for i in SqlTables.children:
					result = result + "Table Uri: " + i.Uri.contents[0] + "\n"
					result = result + "Table Content: " + i.Table_List.contents[0] + "\n\n"
			else:
				result = result + "Null."
		except:
			result = result + "Null."
		return result if who == None else result[:800]
if __name__ == '__main__':
	# parser = Parser("../report/com_mwr_example_sieve.xml")
	parser = Parser("../report/com_baidu_input.xml")
	print parser.get_iss_permissions()
