#!/usr/bin/python
#-*- coding:utf-8 -*-
import subprocess
import sys

sys.path.append("/opt/profile_server/build_profile")



sgn = 'ps -ef | grep ./profile_onoff_processor.sh | grep -v grep | wc -l'
sc = 'screen -ls|grep profile_onoff_processor_bak|wc -l'
t_sc = 'screen -dmS profile_onoff_processor_bak'
wk = 'cd /opt/profile_server/build_profile'
se = 'screen -x profile_onoff_processor_bak -p 0 -X stuff "cd /opt/profile_server/build_profile && ./profile_onoff_processor.sh\n"'

jg = subprocess.Popen(sgn,shell=True,stdout=subprocess.PIPE)
js = subprocess.Popen(sc,shell=True,stdout=subprocess.PIPE)

def auto_restart(g,s):
	if g >= 2:
		pass
	else:
		if s == 0:
			subprocess.call(t_sc,shell=True)
		else:
			pass
		try:
			subprocess.call(se,shell=True)
		except:
			pass

g = int(jg.stdout.read().strip())
s = int(js.stdout.read().strip())
auto_restart(g,s)
	     
