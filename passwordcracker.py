import PyPDF2
import zipfile36 as zipfile
import rarfile
import string
import msoffcrypto
from pptx import Presentation

class Crackpassword:
    #####
    def pdfcrack(self):
        pdf = str(input("Enter the path of the PDF file: "))
        passwords = str(input("Enter the path of the password file: "))
        with open(passwords, "r") as f:
            passwords = [line.strip() for line in f]
        for password in passwords:
            try:
                with open(pdf, "rb") as file:
                    reader = PyPDF2.PdfReader(file)
                    reader.decrypt(password)
                    print(f"Password found: {password}")
                    break
            except:
                continue
        else:
            print("Password was not in this txt")

    ######
    def zipcrack(self):
        zip_file = str(input("ENTER THE PATH FOR THE ZIP FILE : "))
        zip_pass = str(input("ENTER THE PATH FOR THE PASSWORD TEXT FILE : "))
        with zipfile.ZipFile(zip_file, 'r') as zip1:
            with open(zip_pass,'r') as f:
                for password in f:
                    password = password.strip()
                    try:
                        zip1.extractall(pwd=bytes(password, 'utf-8'))
                        print("Password Found : ", password)
                        exit()
                    except RuntimeError:
                        pass
        print("Password not found")

    ######
    def rarcrack(self):
        rar_file = str(input("ENTER THE PATH FOR RAR FILE :"))
        rar_passfile = str(input("ENTER THE PATH FOR RAR PASSWORD FILE TXT : "))
        rar_file1 = rarfile.RarFile(rar_file)
        with open(rar_passfile, 'r') as f:
            for password in f:
                password = password.strip()
                try:
                    rar_file1.extractall(pwd=password.encode())
                    print("Password Found: ", password)
                    break
                except rarfile.BadRarFile:
                    continue
                else:
                    print("Password not Found")
    #####
    def docxcrack(self):
        file_docx = str(input("Enter the path for the DOCX file: "))
        passwords_file = str(input("Enter the path for the text file containing passwords: "))
        with open(passwords_file, "r") as f:
            passwords = [line.strip() for line in f]
        
        for password in passwords:
            password = password.strip() 
            try:
                file = msoffcrypto.OfficeFile(open(file_docx, "rb"))
                file.load_key(password=password)
                file.decrypt(open("decrypted.docx", "wb"))
                print(f"Password found: {password}")
                break
            except:
                continue
        else:
            print("Password not found")
    #####
    def pptcrack(self):
        pptx_file = str(input("Enter the path for the PPTX file: "))
        passwords_file = str(input("Enter the path for the text file containing passwords: "))
        with open(passwords_file, "r") as f:
            passwords = [line.strip() for line in f]
        for password in passwords:
            try:
                file = msoffcrypto.OfficeFile(open(pptx_file, "rb"))
                file.load_key(password=password)
                file.decrypt(open("temp.pptx", "wb"))
                prs = Presentation("temp.pptx")
                print("Password found: ",password)
                break
            except:
                continue
        else:
            print("Password not Found!!")
    #####
    def xlscrack(self):
        file_docx = str(input("Enter the path for the XL_file: "))
        passwords_file = str(input("Enter the path for the text file containing passwords: "))
        with open(passwords_file, "r") as f:
            passwords = [line.strip() for line in f]
        
        for password in passwords:
            password = password.strip() 
            try:
                file = msoffcrypto.OfficeFile(open(file_docx, "rb"))
                file.load_key(password=password)
                file.decrypt(open("decrypted.xlsx", "wb"))
                print(f"Password found: {password}")
                break
            except:
                continue
        else:
            print("Password not found")
            ####
if __name__ == '__main__':
    p = Crackpassword()
    print("\n")
    print("<<< WELCOME TO PASSWORD CRACK >>> \n 1 - > for pdf cracking \n 2 - > for zip cracking \n 3 - > for rar cracking \n 4 - > for docx cracking \n 5 - > for ppt cracking \n 6 - > for XL cracking")
    n = int(input("\n>>>"))
    if n == 1:
        p.pdfcrack()
    elif n == 2:
        p.zipcrack()
    elif n == 3:
        p.rarcrack()
    elif n == 4:
        p.docxcrack()
    elif n == 5:
        p.pptcrack()
    elif n == 6:
        p.xlscrack()
    else:
        print("THANKS FOR USING")
        exit()
