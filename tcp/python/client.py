#!/usr/bin/env python3
import socket
import logging
import argparse

HOST = "169.228.130.130"
PORT = 1094
send_size=4096

def send_data(filename, send_size):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        with open(filename, "rb") as f:
            byte = f.read(send_size)
            while byte != b"":
                s.sendall(byte)
                byte = f.read(send_size)
            print("Done Sending")
            s.shutdown(socket.SHUT_WR)
            s.close()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", default="100M")
    parser.add_argument("--send_size", type=int, default=4096)
    return parser.parse_args()

def main():
    args = parse_args()
    filename    = args.filename
    send_size   = args.send_size

    send_data(filename, send_size)

log = logging.getLogger()
if __name__ == "__main__":
    main()
