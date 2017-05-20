# Wifi AP Scanner
Simple python script to scan Wi-Fi APs' SSID, BSSID and Signal Strength. 

## Note

I only tested this code on Ubuntu 16.04, x86_64. If you guys make it work on other platforms, pls let me know.

## Dependencies

```
sudo apt install python-dbus
```

## Usage

```
./wifi_ap_scanner.py
```

## Example

```
$ ./wifi_ap_scanner.py 
ssid:           dlink-B5C0		bssid: C4:A8:1D:85:B5:C0		strength: 57
ssid:     dlink-media-B5C2		bssid: C4:A8:1D:85:B5:C2		strength: 30
ssid:         Easecox ASUS		bssid: 1C:B7:2C:D6:60:D4		strength: 39
ssid:         SINGTEL-519D		bssid: E0:8E:3C:14:51:9E		strength: 40
ssid:             sehchang		bssid: 20:25:64:47:F6:2E		strength: 34
ssid:           Mohd Tahir		bssid: F8:32:E4:EC:C0:D8		strength: 22
ssid:         SINGTEL-2DB8		bssid: 50:C7:BF:58:99:E6		strength: 22
ssid:      Kimberly (2.4G)		bssid: E4:3E:D7:FD:7F:20		strength: 35
ssid:       DR650GW-805DE3		bssid: 00:25:42:80:5D:E3		strength: 35
ssid:  Fernandez (Printer)		bssid: 30:B5:C2:41:A0:2E		strength: 29
```
