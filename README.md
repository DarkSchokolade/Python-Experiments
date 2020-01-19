# PasswordCollector
##Collects wifi passwords the device was previously connected to

### **run the exe file in your pc to gather wifi password**
### **Works only on windows**
###### **uses commands:**
	netsh wlan show profile
	netsh wlan show profile [profile_name] key=clear

*Saves the network name and password in a text file passdata.txt*

This helps in retrieving forgotten passwords of previously connected wifi

*you can implement a smtp server to send the output to your email,*
*when the script is ran on an other machine*
