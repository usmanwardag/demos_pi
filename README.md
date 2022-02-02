# Setting Up Raspberry Pi
### Install the Raspberry Pi OS & enable remote access

- Download Raspberry Pi Imager for your OS [here](https://www.raspberrypi.org/software).
- Connect an SD card reader with the SD card inside.
- Open Raspberry Pi Imager and choose the required OS (Raspberry Pi OS recommended).
<img width="671" alt="Screen Shot 2022-02-02 at 12 07 10 PM" src="https://user-images.githubusercontent.com/8848723/152202162-446ddca0-38fd-40d0-8323-8c7b51a2e28c.png">

- Flash the image onto your SD card.
- Create an empty file called `.ssh` and put it in the root SD card folder. This is important to allow ssh access later.

### Connect the Pi to a WiFi network

- Create a file named wpa_supplicant.conf with the desired access points to connect to. Follow the template [here](https://github.com/usmanwardag/demos_pi/blob/main/wpa_supplicant.conf).
<img width="463" alt="Screen Shot 2022-02-02 at 12 09 14 PM" src="https://user-images.githubusercontent.com/8848723/152202528-509db9bc-8ed8-4f4f-9daa-3992230b24f3.png">

- Place this file in the root folder of the SD card.
- Whenever Pi boots, it will connect to the first available access point.

### Access the Pi remotely through SSH

- Insert SD card into its slot, and plug in power supply.
- Determine the IP address of Pi.

##### Finding IP address

- Install [nmap](https://nmap.org/download.html).
- Discover host machine’s IP address. Let's say it is `192.168.2.5`. This means that the other devices connected to the same access point will have IP address like `192.168.2.1`, `192.168.2.2`, `192.168.2.3` etc. The notation of this range is `192.168.2.0/24` (covers `192.168.2.0` to `192.168.2.255`).
- Run this nmap command on the host machine: `sudo nmap –sn 192.168.2.0/24`
<img width="486" alt="Screen Shot 2022-02-02 at 12 16 07 PM" src="https://user-images.githubusercontent.com/8848723/152203712-ff22d06a-29a8-4fdd-9816-2d4e3d45e09e.png">
- Run `ssh pi@192.168.182.81`
- The default password is `raspberry`. Run `sudo raspi-config` to set your own password.



