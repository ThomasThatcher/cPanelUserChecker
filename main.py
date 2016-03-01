#!/usr/bin/python

# Import required libraries
import sys, os, requests

class cPanel:

    class Util:
        
        class Logs:
            
            def __init__(self):
                self.smtp = '/var/log/exim_mainlog' 
                self.dovecot = '/var/log/maillog'
                self.apache = '/usr/local/apache/logs/error_log'
                self.cpanel_access = '/usr/local/cpanel/logs/access_log'
                self.accounting  = '/var/cpanel/accounting.log'
                self.horde = '/var/cpanel/horde/log/'
                self.squirrelmail = '/var/cpanel/roundcube/log/'
                self.squirrelmail = '/var/cpanel/squirrelmail/'
                self.myself_slow_queries = '/var/log/slowqueries'

        class Colour:
    
            def __init__(self):
                self.CLEAR        = '\033[0m'
                self.RED          = '\033[0;31m'
                self.GREEN        = '\033[0;32m'
                self.ORANGE       = '\033[0;33m'
                self.BLUE         = '\033[0;34m'
                self.PURPLE       = '\033[0;35m'
                self.CYAN         = '\033[0;36m'
                self.LIGHT_GREY   = '\033[0;37m'
                self.DARK_GREY    = '\033[1;30m'
                self.LIGHT_RED    = '\033[1;31m'
                self.LIGHT_GREEN  = '\033[1;32m'
                self.YELLOW       = '\033[1;33m'
                self.LIGHT_BLUE   = '\033[1;34m'
                self.LIGHT_PURPLE = '\033[1;35m'
                self.LIGHT_CYAN   = '\033[1;36m'
                self.WHITE        = '\033[1;37m'
        
            def println(self, text, colour):
                print colour + text + self.CLEAR

    class Server:
        
        def __init__(self):
            self.logs = cPanel.Util.Logs
            
        class Mail:
            
            def __init__(self):
                self.queue = os.system('exim -bpc')
                
        class Web:
            
            def __init__(self):
                pass

    class User:
        
        def __init__(self, domain_name):
            self.domain = domain_name
            self.http = requests.get(self.domain)
            self.username = os.system('/scripts/whoowns' + self.domain)
            self.path = '/home/' + self.username
            self.php_version = os.system('selectorctl --user-current --user=' + self.username)
            self.inodes = os.system('ls -i ' + self.path).split(' ')[0]
            self.registrant, self.registrar, self.domain_status = self.get_whois_data()
            self.a_record, self.mx_record, self.txt__record, self.ns__record = self.get_dns_info()
            self.size = os.system('du -sh ' + self.path).split(' ')[0]
            self.plan, self.local_assigned_ip, self.backup_enabled = self.get_user_data()
           
        def detect_quarantined_files(self):
            if os.path.isdir('/home/quarantined/cxsuser/' + self.username):
                return True
            else:
                return False  
           
        def detect_htaccess(self):
            for file in os.listdir(dir):
                if file.search('.htaccess'):
                    return True 
            return False
            
        def detect_wordpress(self, dir):
            for file in os.listdir(dir):
                if file.search('wp-'):
                    return True
            return False  
        
        def detect_wp_version(self, dir):
            if os.path.isfile(dir + '/wp-includes/version.php'):
                file = open(dir + '/wp-includes/version.php', 'r')
                for line in file.readlines():
                    if line.search('$wp_version'):
                        return ''.join(line.split('=').split("'")[1::2])
                file.close()
            return False
                
        def get_user_data(self):
            plan, ip, backup_enabled, owner = '', '', False, ''
            file = open('/var/cpanel/userdata/' + self.username, 'r')
            for line in file.readlines():
                if line.search('PLAN'):
                    plan = line.split('=')[1]
                if line.search('IP'):
                    ip = line.split('=')[1]
                if line.search('BACKUP'):
                    if line.split('=')[1] == '1':
                        backup_enabled = True
                if line.search('OWNER'):
                    owner = line.split('=')[1]
            file.close()
            return plan, ip, backup_enabled, owner
                
        def find_large_files(self, size):
            return os.system('find ' + self.user_path + '/* -size +' + size + 'MB') # Print all files above the size of 
        
        def check_user_permissions(self):
            return os.system('find ' + self.user_path + '/ -type d -not -perm 755 -o -type f -not -perm 655') # Print files/folders that match 644/755 permissions
            
        def get_whois_data(self):
            registrant_email = os.system('whois ' + self.domain + ' | grep Registrant Email:')
            registrar = os.system('whois ' + self.domain + ' | grep Registrar:')
            status = os.system('whois ' + self.domain + ' | grep Domain Status:')
            return registrant_email.split(':')[1], registrar.split(':')[1], status.split(':')[1]
        
        def get_dns_info(self):
            a   = os.system('dig a ' + self.domain + ' +short')
            mx  = os.system('dig mx ' + self.domain + ' +short')
            txt = os.system('dig txt ' + self.domain + ' +short')
            ns  = os.system('dig ns ' + self.domain + ' +short')
            return a, mx, txt, ns
        
        
if __name__ == "__main__":
    pass
    
