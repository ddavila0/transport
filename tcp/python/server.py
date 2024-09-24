#!/usr/bin/env python3
import socket
import sys 
import signal
import datetime
import logging
import argparse

HOST = "169.228.130.130" 
PORT = 1094

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    fd.close()
    conn.close()
    sys.exit(0)

def receive_data(file_name, receive_size):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        x = datetime.datetime.now()
        file_suffix = str(datetime.datetime.now().minute)+str(datetime.datetime.now().second)
        filename="recv_file_"+file_suffix
        fd = open(filename,'wb')
        conn, addr = s.accept()
        received_bytes = 0 
        received_packets = 0 
        with conn:
            print(f"Connected by {addr}")
            timer_start = datetime.datetime.now()
            data = conn.recv(receive_size)
            while data:
                received_bytes += len(data)
                received_packets +=1 
                #print(f"Received {len(data)} bytes")
                #print(f"Received {(data)}")
                fd.write(data)
                data = conn.recv(receive_size)
            timer_end = datetime.datetime.now()
            fd.close()
        conn.close()
    
    time_diff = timer_end - timer_start
    print("received: "+str(received_bytes)+" bytes")
    print("received: "+str(received_packets)+" packets")
    print("avg packet size: "+str(received_bytes/received_packets))
    print("took: "+str(time_diff))
    bits = received_bytes*8
    bps = bits/time_diff.total_seconds()
    if bps > (1024*1024*1024):
        t = bps/(1024*1024*1204)
        tag = " Gbps"
    elif bps > (1024*1024):
        t = bps/(1024*1024)
        tag = " Mbps"
    elif bps > (1024):
        t = bps/(1024)
        tag = " Kbps"
    else:
        tag = " bps"
    print("throughput: "+str(round(t,2))+tag)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", default="100M")
    parser.add_argument("--receive_size", type=int, default=4096)
    return parser.parse_args()

def main():
    args = parse_args()
    filename    = args.filename
    receive_size   = args.receive_size
    
    receive_data(filename, receive_size)

log = logging.getLogger()
signal.signal(signal.SIGINT, signal_handler)
if __name__ == "__main__":
    main()
