#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import dbus
import sys
import glib
from dbus.mainloop.glib import DBusGMainLoop


class WiFiList():
    def __init__(self):
        self.bus = dbus.SystemBus()
        self.NM = 'org.freedesktop.NetworkManager'
        self.bus.add_signal_receiver(
            None, None, self.NM + '.AccessPoint', None, None)
        nm = self.bus.get_object(self.NM, '/org/freedesktop/NetworkManager')
        self.devlist = nm.GetDevices(dbus_interface=self.NM)
        self.rssid = {}

    def dbus_get_property(self, prop, member, proxy):
        return proxy.Get(
            self.NM + '.' + member,
            prop,
            dbus_interface='org.freedesktop.DBus.Properties')

    def repopulate_ap_list(self):
        apl = []
        res = []
        for i in self.devlist:
            tmp = self.bus.get_object(self.NM, i)
            if self.dbus_get_property('DeviceType', 'Device', tmp) == 2:
                apl.append(
                    self.bus.get_object(self.NM, i) .GetAccessPoints(
                        dbus_interface=self.NM + '.Device.Wireless'))
        for i in apl:
            for j in i:
                res.append(self.bus.get_object(self.NM, j))
        return res

    def form_rssi_dic(self):
        for i in self.repopulate_ap_list():
            ssid = self.dbus_get_property('Ssid', 'AccessPoint', i)
            bssid = self.dbus_get_property('HwAddress', 'AccessPoint', i)
            strength = self.dbus_get_property('Strength', 'AccessPoint', i)
            ssid_str = "".join("%s" % k for k in ssid)
            print "ssid: %20s\t\tbssid: %s\t\tstrength: %d" % (ssid_str, bssid, strength)

if __name__ == '__main__':
    DBusGMainLoop(set_as_default=True)
    wfl = WiFiList()
    wfl.form_rssi_dic()
