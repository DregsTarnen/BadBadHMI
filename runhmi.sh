#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
export DISPLAY=:0
CLIENTPATH="/home/hmi/.ignition/clientlauncher-data/vision-client-launcher.json"
WINDOWMODE=`cat $CLIENTPATH | grep window.mode | tr -d "[:punct:]"`
PROJECT=`sed 's/[^[:alnum:]]\+$//' $CLIENTPATH | grep name | grep -v gateway | cut -b 16-
echo $PROJECT
ETHUP=`/sbin/ifconfig enp1s0 | grep 'inet'`
CHECKJAVA=`pgrep java`
CHECKVINO=`pgrep vino`
CHECKDOCK=`pgrep plank`
if [[ "$WINDOWMODE" == *"windowmode null"* ]]
       then
           sed -i 's/"window.mode": null/"window.mode": "fullscreen"/' $CLIENTPATH
fi
if [ -z "$CHECKDOCK" ]
       then
           /usr/bin/plank &
fi
if [ -z "$CHECKVINO" ]
       then
           /usr/libexec/vino-server &
fi
if [ -n "$ETHUP" ]
       then
           if  [ -z "$CHECKJAVA" ]
                   then
                       /home/rfphmi/clearignitecache.sh
                       sh -c "/home/hmi/visionclientlauncher/app/visionclientlauncher.sh -Dapplication=$PROJECT &"
           fi
fi
