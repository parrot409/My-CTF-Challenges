#!/bin/sh
npm install

userdel app 2> /dev/null
rm -r /home/app 2> /dev/null

useradd -ms /bin/bash -d /home/app app
su --preserve-environment app -c "NODE_ENV=production node ./index.js"
