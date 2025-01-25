#!/bin/python3

# Functions For Blockchain Development

import hashlib
import sqlite3
import random
from colorama import Fore
from os import system

Menu = '''
        TYPE OF DATA
    Text [1]
    Photos, Videos or Files [2]
    Show your private data [3]
    Change Password [4]
    Exit [0]
'''
system("clear")
print(Fore.GREEN, Menu, Fore.WHITE)

# Generet Data To Hash
def HashGeneretor(data):
    EncryptedData = hashlib.sha256(data.encode())
    return EncryptedData.hexdigest()

# Save Data In BLockchain Database

def BlockchainDatabase(SetNumber, CorrentDateTime, Data, Hash, PreviousHash):
    Connection = sqlite3.connect("database/blockchain.db")
    Connect = Connection.cursor()
 
    # Connect.execute('''CREATE TABLE BlockchainTextDatabase(
        # CorrentTime text,
        # Data text,
        # Hash text,
        # PrivusHash text
    # )''')
 
    if SetNumber == 1:
        Connect.execute(f"INSERT INTO BlockchainTextDatabase(CorrentTime, Data, Hash, PrivusHash) VALUES(?,?,?,?);", (CorrentDateTime, Data, Hash, PreviousHash))
    elif SetNumber == 2:
        Connect.execute(f"INSERT INTO BlockchainImageDatabase(CorrentTime, Data, Hash, PrivusHash) VALUES(?,?,?,?);", (CorrentDateTime, Data, Hash, PreviousHash))

    Connection.commit()
    Connection.close()

# Show Data Into Database

def ReadDatabase(DatabaseNumber, Key):
    Connection = sqlite3.connect("database/blockchain.db")
    Connect = Connection.cursor()
    
    if DatabaseNumber == 1:
        Connect.execute(f"SELECT * FROM BlockchainTextDatabase WHERE Hash = '{Key}'")
        return Connect.fetchall()
    elif DatabaseNumber == 2:
        Connect.execute(f"SELECT * FROM BlockchainImageDatabase WHERE Hash = '{Key}'")
        return Connect.fetchall() 
    # Connect.execute('''CREATE TABLE BlockchainTextDatabase(
        # CorrentTime text,
        # Data text,
        # Hash text,
        # PrivusHash text
    # )''')
 

    Connection.commit()
    Connection.close()

# Private Key Save In File

def SaveKey(PrivateKey):
    Alphabate = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Number = "1234567890"
    Sigh = "@#$%&!"
    all = Alphabate + Number + Sigh
    lenght = 5
    FileName = ''.join(random.sample(all, lenght))

    with open(f"key/{FileName}.key", 'w') as File:
        File.write(PrivateKey)
        File.close()

