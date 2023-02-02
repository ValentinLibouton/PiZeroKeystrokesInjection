# PiZeroKeystrokesInjection
This project allows to inject keystrokes such as a keyboard in an automated way like the Rubber Ducky from Hak5.org does

![image of a duck with a raspberry](https://github.com/ValentinLibouton/PiZeroKeystrokesInjection/blob/bd96f7e9aaae284f0932438f2e56a36b56301500/images/raspduck.png?raw=true)

## Contents
- [Usage](#big-title)
- [Examples](#big-title)
- [Prerequisites](#big-title)
- [Pi Zero setup](#big-title)

## Usage
List of commands that can be used in command_file.txt:

- `STRING`  The string following this command will be typed on the keyboard
- `SLEEP`   The number after this command is the pause delay in second
- `WRITE`   The filename following this command will be read and typed entirely on the keyboard. Here no need to put a "STRING" command.
- `#`       This entire line will be ignored at runtime. Lines beginning with # are intended for your comments. Can also be used as a log via SSH.
- `REPLAY` The first number following the REPLAY command is the number of repeats and the second number is the number of rows to repeat
- you can also use other keystrokes such as `CTRL_LEFT ALT_LEFT DELETE` you just need to leave a space between each command.

List of all specific commands:
`CTRL_LEFT` `SHIFT_LEFT` `ALT_LEFT` `WIN` `CTRL_RIGHT` `SHIFT_RIGHT` `ALT_RIGHT` `ENTER` `ESCAPE` `BACK` `TAB` `SPACE` `CAPS_LOCK` `F1` `F2` `F3` `F4` `F5` `F6` `F7` `F8` `F9` `F10` `F11` `F12` `PRINT_SCREEN` `SCROLL_LOCK` `PAUSE` `INSERT` `HOME` `PAGE_UP` `DELETE` `END` `PAGE_DOWN` `RIGHT_ARROW` `LEFT_ARROW` `DOWN_ARROW` `UP_ARROW` `NUM_LOCK` `MENU`

## Examples
- ´STRING Hello World! @#123_°(`
```bash
Hello World! @#123_°(
```
- `SLEEP 3`
- `WRITE example_file.txt` This example is available in the root
```bash
for i in range(10):
    print("Hello World", i)
rtfm = True

```
- `# This is a comment`
- `REPLAY 2 6` replay the last 6 lines twice
- `CTRL_LEFT s`
- `CTRL_LEFT ALT_LEFT t`
- `CTRL_LEFT ALT_LEFT DELETE`
- `ALT_LEFT TAB`

## Prerequisites
### Hardware
Raspberry Pi Zero with WiFi for file transfer via SSH
### Software
1. Configure WiFi and keyboard via:
```bash
sudo raspi-config
```
2. Setup Pi Zero

- See **Pi Zero setup** chapter below

3. Copy files projetc on Pi via SSH:

- conversion.py
- run_keystrokes.py

5. Write you scrypt and copy on Pi via SSH:

- command_file.txt


## Pi Zero setup

### Sources
https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/

### Installation according to the original source
#### 1 - Enabling Modules and Drivers
These next steps to prepare the Pi Zero board are based on the instructions from iSticktoit. First, you need to run these three commands to enable the necessary modules and drivers:
```bash
echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
echo "dwc2" | sudo tee -a /etc/modules
sudo echo "libcomposite" | sudo tee -a /etc/modules
```
#### 2 - Configuring the Gadget
Now, you have to define your Pi Zero (HID gadget) as a USB keyboard. The configuration is done via ConfigFS, a virtual file system located in /sys/.
##### 2.1 - Creating the config script
The configuration is volatile, so it must run on each startup. Create a new file called isticktoit_usb in /usr/bin/ and make it executable:
```bash
sudo touch /usr/bin/isticktoit_usb
sudo chmod +x /usr/bin/isticktoit_usb
```
Then, you need to run this script automatically at startup. Open /etc/rc.local with this command:
```bash
sudo nano /etc/rc.local
```
Add the following before the line containing exit 0:
```bash
/usr/bin/isticktoit_usb # libcomposite configuration
```
#### 3 - Creating the gadget
For this project, we will turn the Raspberry Pi into a USB keyboard, but you could make it work as a Serial adapter, Ethernet adapter, and Mass Storage. Open the file with:
```bash
sudo nano /usr/bin/isticktoit_usb
```
Leave the default values, but you could even change the serial number, manufacturer and product name to fit your specific needs.
```bash
#!/bin/bash
cd /sys/kernel/config/usb_gadget/
mkdir -p isticktoit
cd isticktoit
echo 0x1d6b > idVendor # Linux Foundation
echo 0x0104 > idProduct # Multifunction Composite Gadget
echo 0x0100 > bcdDevice # v1.0.0
echo 0x0200 > bcdUSB # USB2
mkdir -p strings/0x409
echo "fedcba9876543210" > strings/0x409/serialnumber
echo "Tobias Girstmair" > strings/0x409/manufacturer
echo "iSticktoit.net USB Device" > strings/0x409/product
mkdir -p configs/c.1/strings/0x409
echo "Config 1: ECM network" > configs/c.1/strings/0x409/configuration
echo 250 > configs/c.1/MaxPower

# Add functions here
mkdir -p functions/hid.usb0
echo 1 > functions/hid.usb0/protocol
echo 1 > functions/hid.usb0/subclass
echo 8 > functions/hid.usb0/report_length
echo -ne \\x05\\x01\\x09\\x06\\xa1\\x01\\x05\\x07\\x19\\xe0\\x29\\xe7\\x15\\x00\\x25\\x01\\x75\\x01\\x95\\x08\\x81\\x02\\x95\\x01\\x75\\x08\\x81\\x03\\x95\\x05\\x75\\x01\\x05\\x08\\x19\\x01\\x29\\x05\\x91\\x02\\x95\\x01\\x75\\x03\\x91\\x03\\x95\\x06\\x75\\x08\\x15\\x00\\x25\\x65\\x05\\x07\\x19\\x00\\x29\\x65\\x81\\x00\\xc0 > functions/hid.usb0/report_desc
ln -s functions/hid.usb0 configs/c.1/
# End functions

ls /sys/class/udc > UDC
```
#### 4 - Python Script (Change according to personal use)
* After preparing your Raspberry Pi Zero, connect it to a laptop or desktop computer through the micro USB port that is used for data and peripherals. That micro USB will both power the Pi Zero and act as a keyboard to the connected computer.
* Establish an SSH connection with your Pi and use the next command to create a new Python script:
  ```bash
  nano RPi_Keyboard_Example.py
  ```
* Copy and paste the next Python script to your Raspberry Pi.
  ```bash
  #!/usr/bin/env python3
  NULL_CHAR = chr(0)

  def write_report(report):
      with open('/dev/hidg0', 'rb+') as fd:
          fd.write(report.encode())

  # Press a
  write_report(NULL_CHAR*2+chr(4)+NULL_CHAR*5)
  # Release keys
  write_report(NULL_CHAR*8)
  # Press SHIFT + a = A
  write_report(chr(32)+NULL_CHAR+chr(4)+NULL_CHAR*5)

  # Press b
  write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
  # Release keys
  write_report(NULL_CHAR*8)
  # Press SHIFT + b = B
  write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)

  # Press SPACE key
  write_report(NULL_CHAR*2+chr(44)+NULL_CHAR*5)

  # Press c key
  write_report(NULL_CHAR*2+chr(6)+NULL_CHAR*5)
  # Press d key
  write_report(NULL_CHAR*2+chr(7)+NULL_CHAR*5)

  # Press RETURN/ENTER key
  write_report(NULL_CHAR*2+chr(40)+NULL_CHAR*5)

  # Press e key
  write_report(NULL_CHAR*2+chr(8)+NULL_CHAR*5)
  # Press f key
  write_report(NULL_CHAR*2+chr(9)+NULL_CHAR*5)

  # Release all keys
  write_report(NULL_CHAR*8)
  ```
#### 5 - Test
Let’s test it, if you plug the Pi Zero to Computer #1, after a few seconds you’ll see an alert message or sound that indicates that a keyboard was connected successfully.

Sometimes you might see this warning message saying “USB device not recognized”. Throughout my tests, I found that you can ignore this warning message and your Pi Zero works as a keyboard without any additional configuration or drivers installation. So, you can continue and it will work just fine.
* Computer N°1: Open any text editor program and leave your cursor in the new file:
* Computer N°2: Establish an SSH connection with your Pi Zero and run the Python script created earlier:
  ```bash
  sudo python3 RPi_Keyboard_Example.py
  ```
* Computer N°1: The text editor has been filled
