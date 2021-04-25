#!/bin/sh
npm install

userdel app 2> /dev/null
rm -r /home/app 2> /dev/null
chmod 777 ./notes -R
useradd -ms /bin/bash -d /home/app app
su --preserve-environment app -c "NODE_ENV=production node ./main.js & 1>&1;NODE_ENV=production node ./sandbox.js"
