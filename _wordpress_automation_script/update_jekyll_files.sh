#!/bin/bash
#set -x #echo on


#Put this in your ~/.netrc and it won't ask for your username/password (at least on Linux and Mac):
#machine github.com
#       login <user>
#       password <password>


echo copying files...
cp /home/mfoadmin/apps/wordpress/htdocs/wp-content/plugins/mfo-wordpress-plugin/jekyll-build/*.md /home/mfoadmin/mfo-static-website/_exhibits/
OUTPUT=$(ls /home/mfoadmin/mfo-static-website/_exhibits/ -1 | wc -l)
echo -n ${OUTPUT}
echo " exhibits now in directory"

cd /home/mfoadmin/mfo-static-website/_exhibits
git add *
git commit -m "updating exhibits from wordpress"
git push

