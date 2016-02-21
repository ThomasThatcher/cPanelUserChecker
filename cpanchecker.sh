#!/bin/bash

# Heading
echo -e "Normal \e[4mPRINT USER DATA\n\n";

# Set the URL variable to the first arg passed to the script
url = $1;

#Find the user associated with the domain name
usur = "$(/scripts/whoowns url)";

echo -e "\e[7mHTTP Status Code\n";
curl -o /dev/null --silent --head --connect-timeout 3 --write-out '%{http_code}\n' ${url};

# Show user's PHP Version
echo -e "\e[7mUser's PHP Version ";
selectorctl --user-current --user=${user};

echo -e "\e[7mCurrent Wordpress Version(s)\n";
find /home/${user}/ -name wp_version.php -exec grep wp_version /home/${user}/wp-includes/version.php {}\;

# Find files in the user's home dir that do not have the correct permissions set.
echo -e "\e[7mFiles that may have the correct permissions";
find /home/${user}/ -type d -not -perm 755 -o -type f -not -perm 655;

# Determine whether or not there are .htaccess files in the account
echo -e "\e[7m.htaccess file(s)\n";
find /home/${user}/ -name htaccess;

echo -e "\e[7mDNS Info\n";
echo -e "A:  "; dig a ${url} +short;
echo -e "MX: "; dig mx ${url} +short;
echo -e "NS: "; dig ns ${url} +short;

echo -e "\e[7mWHOIS DATA\n";
whois ${url} | grep Registrar;
whois ${url} | grep Domain\ Status:;
whois ${url} | grep Registrant\ Email:;
whois ${url} | grep Name\ Server:;

echo -e "\e[7mCalculating INodes...\n";
echo "Detailed Inode usage for: $(pwd)" ;  find /home/${user}/ -printf "%h\n" | cut -d/ -f-2 | sort | uniq -c | sort -rn ; printf "Total: \t\t$(find $(pwd) | wc -l)\n"

echo -e "\e[7mFinding files larger than 100MBs\n";
find /home/${user}/* -size +100MB