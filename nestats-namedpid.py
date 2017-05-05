import subprocess

# Tasklist command
cmd_tasklist = ["tasklist"]
process = subprocess.Popen(cmd_tasklist, stdout=subprocess.PIPE)

pid_col = 1
name_col = 0
name_list = {}

# Invoking tasklist command
print "=> invoking tasklist command"
for line in process.stdout.readlines():
	list = line.split(" ")
	filtered = filter(None,list)
	if len(filtered) > 2:
		name_list[filtered[pid_col]] = filtered[name_col]

# Invoking Netstat command
print "==> invoking netstat command"
cmd_netstat = ["netstat", "-ano"]
process = subprocess.Popen(cmd_netstat, stdout=subprocess.PIPE)

network_list = []
netstat_loc_addr_col = 1
netstat_for_addr_col = 2
netstat_state_col = 3
netstat_pid_col = 4
output_file_name = "netstat_output.txt"

# merging Image Name for PID and Netstat output
print "===> processing output"
start_recording = False
for line in process.stdout.readlines():
	list = line.split(" ")
	filtered = filter(None,list)
	
#	if start_recording:
#		network_list.append(filtered)
	
	if "TCP" in filtered[0]:
#		start_recording = True
		network_list.append(filtered)
		
print "====> printing output to file named ==> " + output_file_name		
output_f = open(output_file_name, "w")
output_f.write("Proto   \"Local Address\"   \" Foreign Address\"    \" PID\"    \"Image Name\" \n" +
               "==============================================================================\n")	
		
for line in network_list:
	if "TCP" in line[0]:
		pid = line[netstat_pid_col]
		pid_cleansed = pid.replace("\r\n","")
		line[netstat_pid_col] = pid_cleansed
		try:
			name = name_list[pid_cleansed]
			line.append(name)
		except:
			line.append("unknown")

	as_string = "   ".join(line)
	output_f.write(as_string)
	output_f.write("\n")

print "======> finished! <====="

