#!/bin/python3

# Blockchain Beast Project Application

import datetime 
from colorama import Fore
import Blockchain
import Lock

class BlockchainWithDatabase:
    Key = input("Enter Your Acess Code --> ")
    Lock.PasswordCheck(Key)
    
    Loop = True
    while(Loop):
        try:
            MenuNumber = int(input("{Silect Number} --> "))
        except(Exception):
            print(Fore.RED, "Enter Valid Integer Value", Fore.WHITE)

        CorrentDateTime = str(datetime.date.today())
        PreviousHash = "No PreviousHash"

        if MenuNumber == 1:
            TextData = input("Input Text Data --> ")
            EncryptedText = Blockchain.HashGeneretor(TextData)

            try:
                with open("LocalOne.txt", 'r') as File:
                    PreviousHash = File.read()
            except(Exception):
                pass
        
            Blockchain.BlockchainDatabase(MenuNumber, CorrentDateTime, TextData, EncryptedText, PreviousHash)

            try:
                with open("LocalOne.txt", 'w') as File:
                    File.write(EncryptedText)
            except(Exception):
                pass

            Blockchain.SaveKey(EncryptedText)

        elif MenuNumber == 2:
            ImagePath = str(input("Input File Path --> "))
        
            try:
                with open(f"{ImagePath}", "rb") as File:
                    ReadImageData = File.read()
                EncryptedImage = Blockchain.HashGeneretor(str(ReadImageData))
        
                try:
                    with open("LocalTwo.txt", 'r') as File:
                        PreviousHash = File.read()
                except(Exception):
                    pass
                
                Blockchain.BlockchainDatabase(MenuNumber, CorrentDateTime, ReadImageData, EncryptedImage, PreviousHash)
        
                try:
                    with open("LocalTwo.txt", 'w') as File:
                        File.write(EncryptedImage)
                except(Exception):
                    pass
                
            except(Exception):
                pass

            Blockchain.SaveKey(EncryptedImage)

        elif MenuNumber == 3:
            try:
                DatabaseNumber = int(input("Enter Database Number : ")) 
                PrivatKey = input("Enter you data private hash : ")
                ReadingDatabase = Blockchain.ReadDatabase(DatabaseNumber, PrivatKey)
                print(ReadingDatabase)
            except(Exception) as e:
                print(Fore.RED, "Enter Valid Integer Value", Fore.WHITE)
                print(e)

        elif MenuNumber == 4:
            NewPassword = input("Enter Your New Password ----> ")
            Lock.ChangePasswd(NewPassword)

        elif MenuNumber == 0:
            Loop = False

        else:
            print("Out Of Range")


if __name__=="__main__":
    try:
        BCD = BlockchainWithDatabase()
    except(Exception):
        pass
    
