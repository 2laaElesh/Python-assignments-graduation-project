# This program is used to unpack an ethernet packet/frame so it can be called as ethernet sniffer tool

#The socket libraty is used only in Linux !! so make sure to used this program on linux machine !!
import socket
import struct
import textwrap



Tab_1= "\t\t\t - "

#defining main function to listen for data coming from the socket connection 
def main():
	
	# Starting a connection to get ethernet packet/frame
	conn= socket.socket(socket.AF_PACKET, socket.SOCK_RAW,socket.ntohs(3))
	
	# Running the program infinitely
	while True:
	
		# Receiving data from connection in two variables (Raw data and Address) after setting the port value
		Raw_Data, Address = conn.recvfrom(65536)
		
		# Calling Ethernet function to unpack the first part of ethernet frame
		Destination_MAC,Source_MAC,Proto,data = Ethernet_Frame(Raw_Data)
		
		#Printing the values returned from Ethernet_Frame function
		print('\nEthernet frame:')
		print('\t - Destination: {}, Source: {}, Protocol: {}'.format(Destination_MAC,Source_MAC,Proto))
		
		# if Ethernet protocol = 8 it means that IPv4 (IP Address version 4) is used 
		if Proto == 8:
		
			# Calling IPv4_Packet function to unpack the IPv4 frame
			(Version,Header_Length,TimeToLive,Protocol,Source,Target,data)= IPv4_Packet(data)
			
			#Printing the values returned from Ethernet_Frame function
			print("\t - IPv4 Packet:")
			print("\t\t - Version: {}, Header_Length: {}, TTL: {}".format(Version,Header_Length,TimeToLive))
			print("\t\t - Protocol: {}, Source: {}, Target: {}".format(Protocol,Source,Target))
			
			# Checking the protocol inside the IPv4 frame
			# If protocol value =1 then ICMP protocol is used 
			if Protocol == 1:
				
				# Calling ICMP_Packet function to unpack the ICMP frame
				ICMP_Type,Code,Checksum, data=ICMP_Packet(data)
				
				#Printing the values returned from ICMP_Packet function
				print("\t - ICMP Packet:")
				print("\t\t - Type: {}, Code: {}, Checksum: {}".format(ICMP_Type,Code,Checksum))
				print("\t\t - Data:")
				# Printing the value of data using Format_Multiline function
				print(Format_Multiline(Tab_1, data))
				
			# If protocol value =6 then TCP protocol is used 
			elif Protocol == 6:
			
				# Calling TCP_Packet function to unpack the TCP frame
				(Source_Port, Destination_Port,Sequence,Acknowledgment,Flag_Urg, Flag_Ack, Flag_Psh,Flag_Rst,Flag_Syn,Flag_Fin,data)= TCP_Packet(data)
				
				#Printing the values returned from TCP_Packet function
				print("\t - TCP Packet:")
				print("\t\t - Source Port: {}, Destination Port: {}".format(Source_Port, Destination_Port))
				print("\t\t - Sequence: {}, Acknowledgment: {}".format(Sequence,Acknowledgment))
				print("\t\t - Flags:")
				print("\t\t\t - URG: {}, Ack: {}, Psh: {}, Rst: {}, Syn: {}, Fin: {}".format(Flag_Urg, Flag_Ack, Flag_Psh,Flag_Rst,Flag_Syn,Flag_Fin))
				print("\t\t - Data:")
				# Printing the value of data using Format_Multiline function
				print(Format_Multiline(Tab_1, data))
				
			# If protocol value =17 then UDP protocol is used 
			elif Protocol == 17:
			
				# Calling UDP_Packet function to unpack the UDP frame
				Source_Port,Destination_Port,Size,data = UDP_Packet(data)
				
				#Printing the values returned from UDP_Packet function
				print("\t - UDP Packet:")
				print("\t\t - Source Port: {}, Destination Port: {}, Length: {}".format(Source_Port,Destination_Port,Size))
				print("\t\t - Data:")
				# Printing the value of data using Format_Multiline function
				print(Format_Multiline(Tab_1, data))
			
			# In case if any other protocol was used print the data only	
			else:
				print("\t - Data:")
				# Printing the value of data using Format_Multiline function
				print(Format_Multiline(Tab_1, data))
			
			
# This function is used to unpack The first packet of ethernet frame to get Destination MAC address, Source Mac Address, and Protocol
def Ethernet_Frame(data):
	#Unpacking the fisrt 14 bits of the frame to get Destination+Source Mac Addresses and protcol
	Destination_MAC_Address, Source_MAC_Address, Protocol = struct.unpack('! 6s 6s H',data[:14])
	#Get_MAC_Address is used to write a readable MAC Address. socket.htons is used to make the protocol bytes readable and finally returning data
	return Get_MAC_Address(Destination_MAC_Address), Get_MAC_Address(Source_MAC_Address), socket.htons(Protocol), data[14:]
	
	
# This function is used to write a readable MAC Address (ex: 11:AA:22:BB:33:CC)
def Get_MAC_Address(Address_in_Bytes):
	# Map function is used put the address in bytes in the form of {:2x}
	Bytes_Str= map('{:2x}'.format, Address_in_Bytes)
	# returning the Address in Upper case letters and joined with ':' together
	return ':'.join(Bytes_Str).upper()
	
	
	

# This function is used to unpack IPv4 packet of ethernet frame to get version, header length, time to live, protocol, source IP, target IP, and data
def IPv4_Packet(data):
	# Finding the version after shifting the first bit of IPv4 packet by 4
	Version_Header_Length= data[0]
	Version= Version_Header_Length >> 4
	# Finding header length to determine where the data starts
	Header_Length = (Version_Header_Length &15)*4 
	# Unpacking the rest of the frame to get time to live, protocol, source IP, target IP, and data
	TimeToLive,Protocol,Source,Target= struct.unpack('! 8x B B 2x 4s 4s',data[:20])
	# Returning the version, header length, time to live, protocol, source IP, target IP, and data of IPv4 packet
	return Version,Header_Length,TimeToLive,Protocol,Get_IP_Address(Source),Get_IP_Address(Target),data[Header_Length:]


# This function is used to write a readable IP Address (ex: 127.0.1.1)
def Get_IP_Address(Address):
	# Writing the IP Address in readable format using join+map functions
	IP_Address= '.'.join(map(str,Address))
	# Returning the IP Address after writing it in a readable format
	return IP_Address
	
	
# This function Unpacks ICMP Protocol Packet to get ICMP_Type,Code,Checksum after IPv4 packet
def ICMP_Packet(data):
	# Unpacking the first 4 bits of the frame to get ICMP_Type,Code,Checksum
	ICMP_Type,Code,Checksum= struct.unpack('! B B H',data[:4])
	# Returning the ICMP_Type,Code,Checksum, and data of ICMP packet 
	return ICMP_Type,Code,Checksum, data[4:]
	
	
# This function unpacks TCP Protocol Packet after IPv4 packet
def TCP_Packet(data):
	# Unpacking the first 14 bits of the frame to get Source_Port, Destination_Port,Sequence,Acknowledgment, and Offset_Reserved_Flags of TCP packet
	(Source_Port, Destination_Port,Sequence,Acknowledgment,Offset_Reserved_Flags)= struct.unpack('! H H L L H ',data[:14])
	# Defining each flag from Offset_Reserved_Flags in TCP packet 
	Offset= (Offset_Reserved_Flags  >> 12)*4
	Flag_Urg= (Offset_Reserved_Flags & 32) >> 5
	Flag_Ack= (Offset_Reserved_Flags & 16) >> 4
	Flag_Psh= (Offset_Reserved_Flags &  8) >> 3
	Flag_Rst= (Offset_Reserved_Flags &  4) >> 2
	Flag_Syn= (Offset_Reserved_Flags &  2) >> 1
	Flag_Fin= Offset_Reserved_Flags  &  1 
	# Returning Source_Port, Destination_Port,Sequence,Acknowledgment, and Offset_Reserved_Flags of TCP packet
	return Source_Port, Destination_Port,Sequence,Acknowledgment,Flag_Urg, Flag_Ack, Flag_Psh,Flag_Rst,Flag_Syn,Flag_Fin, data[Offset:]
	
	
# This function Unpacks UDP Protocol Packet to get Source_Port,Destination_Port,Size after IPv4 packet
def UDP_Packet(data):
	# Unpacking the first 8 bits of the frame to get Source_Port, Destination_Port,and size of UDP packet
	Source_Port,Destination_Port,Size=struct.unpack('! H H 2x H',data[:8])
	# Returning the Source_Port,Destination_Port,Size, and data of UDP packet 
	return Source_Port,Destination_Port,Size,data[8:]
	
	
# This function is used to format multiline data
def Format_Multiline(prefix,string,size=80):
	size-=len(prefix)
	if isinstance(string, bytes):
		string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
		if size % 2:
			size-=1
	# Returning data in a wrapped text
	return '\n'.join([prefix + line for line in textwrap.wrap(string,size)])


# Calling main function to start the program
main()

