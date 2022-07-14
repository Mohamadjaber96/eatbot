#Auteur: Mohamad Jaber
choix=" "
p_dict={}
reponse=""
nbr=0
from random import*
import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy
import tflearn
import tensorflow
from tensorflow.python.ops.variable_scope import*
import random
import json
from tkinter import *
from PIL import ImageTk,Image
import requests
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_file_path = "Holy-Quran-in-Arabic-Language.pdf"
file_base_name = pdf_file_path.replace('.pdf', '')
output_folder_path = os.path.join(os.getcwd(), 'Output')

pdf = PdfFileReader(pdf_file_path)

class Quraanbot3(object):
    
    
    
    def OnlineQuraanbot(p_dict:dict)->dict:
        p_dict={}
        choix=" "
        reponse = input("Bienvenue, l'assistant virtuel est la pour vouz aider:")
        while reponse!="au revoir":
            nbr=int(input("saisir la page"))
            page1=pdf.getPage(nbr)
            pdfdata=page1.extractText()
            for key, value in dict.items():
                for page_num in range(pdf.numPages):
                    pdfWriter = PdfFileWriter()
                    pdfWriter.addPage(pdf.getPage(page_num))

                    with open(os.path.join(output_folder_path, '{0}_Page{1}.pdf'.format(file_base_name, page_num+1)), 'wb') as f:
                        pdfWriter.write(f)
                        f.close()

        
                for elem in reponse.split():
                    if elem in pdfdata :
                        p_dict[key]=reponse
                        reponse= input( value)
                        for elem_reponse in reponse.split():
                            print(p_dict, elem_reponse, elem)
                            if elem_reponse=="Menu":
                                print(eatbot3.menu())
                                reponse= input( value)
                            elif elem_reponse=="ID":
                                print(selection_ID.Id(p_ID))
                                reponse= input( value)
                    if "لا إكراه في الدين" == elem or (elem in value):
                       aya="""
                        هل الإيمان يؤدي إلى
                        الصلاة أم الصلاة تؤدي إلى الإيمان
                        ولكن الصلاة معروف و يجب أن نأمر بالمعروف
                        وننهي عن المنكر                         
                           لا إكراه في الدين يعني النهي
                        عن الإكره في الدين
                        """
                       p_dict[key]=aya
                       if (aya in page_num) or (reponse in dict):
                           return (True , pdf.numPages[page_num].split())

       
                       
            return aya

"""
    def decrypt(input_file, password): 
        pdf_file_path = "Holy-Quran-in-Arabic-Language.pdf"
        pdf = PdfFileReader(pdf_file_path)
        file_base_name = pdf_file_path.replace('.pdf', '')
        output_folder_path = os.path.join(os.getcwd(), 'Output')

       
        writer= PdfFileWriter()
        pdf.decrypt(password)
        for i in range(pdf.getNumPages()):
            page= pdf.getPage(i)
            writer.addPage(page)

        with open('decrypted_' + input_file, 'wb') as output_file:
            writer.write(output_file)
"""    
"""    
    def menu()->str:



class selection_ID(object):
    
    
    def Id(p_ID:list)->list:
        if True:"""
 


#Main function

dict = {"لا إكراه في الدين": """
                        هل الإيمان يؤدي إلى
                        الصلاة أم الصلاة تؤدي إلى الإيمان
                        ولكن الصلاة معروف و يجب أن نأمر بالمعروف
                        وننهي عن المنكر                         
                           لا إكراه في الدين يعني النهي
                        عن الإكره في الدين
                        """}
while True:
    aya=Quraanbot3.OnlineQuraanbot(dict)
    Quraanbot3.decrypt('encrypted_pygame.pdf','password')
    if aya == ("لا إكراه في الدين"):
         aya=Quraanbot3.decrypt('encrypted_pygame.pdf','password') and """
                        هل الإيمان يؤدي إلى
                        الصلاة أم الصلاة تؤدي إلى الإيمان
                        ولكن الصلاة معروف و يجب أن نأمر بالمعروف
                        وننهي عن المنكر                         
                           لا إكراه في الدين يعني النهي
                        عن الإكره في الدين
                        """
    for page_num in range(pdf.numPages):
        pdfWriter = PdfFileWriter()
        pdfWriter.addPage(pdf.getPage(page_num))

        with open(os.path.join(output_folder_path, '{0}_Page{1}.pdf'.format(file_base_name, page_num+1)), 'wb') as f:
            pdfWriter.write(f)
            f.close()

        if (aya in page_num) or (reponse in dict):
            print("True" , pdf.numPages[page_num].split())
            
    else:
        print(pdf.numPages[page_num].split())
        break
        
print("Merci Au revoir.")


