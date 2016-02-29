import os
import sys
import requests

class cPanel

	def __init__(self):
		pass
	
	class User
	
		def __init__(self, domain_name):
			self.domain_name = domain_name
			self.http = requests.get(domain_name)
			self.username = os.system('/scripts/whoowns' domain_name)
			self.user_path = '/home/' + username
			self.http_status = http.status_code
			self.http_headers = http.headers
			self.a_record = os.system('dig a +short ' + domain_name)
			self.mx_record = os.system('dig mx +short ' + domain_name)
			self.ns_record = os.system('dig ns +short ' + domain_name)
			self.php_version = os.system('selectorctl --user-current --user=' + username)
			self.owned_domains = (lambda path: path.find(domain_name))(os.listdir('/var/cpanel/userdata/' + username))
			self.inodes = os.system('ls -i ' + user_path)
			self.domain_registrar = os.system('grep Registrar: ' + domain_name)
			self.domain_registrant_email = os.system('grep Registrant Email: ' + domain_name)
		
		def search_for_large_files(self, size):
			return os.system('find ' + self.user_path + '/* -size +' + size + 'MB')
		
		def check_users_permissions(self):
			return os.system('find ' + self.user_path + '/ -type d -not -perm 755 -o -type f -not -perm 655')
		
		def detect_htaccess(self):
			files = []
			if os.path.isfile(self.user_path + '/.htaccess'):
				files.append(self.user_path + '/.htaccess')
			for f in os.listdir(self.user_path + '/public_html'):
				if os.file.isfile(f) and sf.find('.htaccess'):
					files.append(f)
				for sf in os.listdir(f):
					if os.file.isfile(sf) and sf.find('.htaccess'):
						files.append(sf)
			return (lambda f: f == '.htaccess')(files)	
				
		def detect_wordpress(self):
			for f in os.listdir(self.user_path):
				if f.find('wp-'):
					return True
					
		def detect_joomla(self):
			if os.path.isdir(self.user_path + '/libraries'):
				for f in os.listdir(self.user_path + '/libraries'):
					if f.find('joomla'):
						return True
			else:
				return False
			
			
			
		
		