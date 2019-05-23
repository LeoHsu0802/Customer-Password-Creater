# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 10:54:11 2018

@author: user1
"""
#from reportlab.pdfgen import canvas
import PyPDF2
from fpdf import FPDF
import os
import secrets
import string

#生成密碼
for i in range (4):
    i += 1
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(8)) #密碼長度
        if (any(c.islower() for c in password)
                and sum(c.isupper() for c in password) == 2  #英文大寫個數
                and sum(c.isdigit() for c in password) > 2): #數字個數
            break


b = input("請輸入客戶帳號:")

#讀取TXT

with open(b+'.txt') as f:
    QQ = f.read()


pdf = FPDF()
pdf.add_page()
pdf.image('JihSun.png', x=2, y=2, w=30)  #圖片
pdf.add_font('fireflysung', '', 'fireflysung.ttf', uni=True)
pdf.set_font('fireflysung', '', 12)
pdf.set_xy(8,8)   #放置位置
pdf.ln(8) #字體下移


pdf.multi_cell(0,5,QQ) 
pdf.output('666.pdf', 'F')



with open("666.pdf", "rb") as pdffile:
    pdfReader = PyPDF2.PdfFileReader(pdffile)
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))

#PDF加密
    pdfWriter.encrypt(password)
    with open(b+'_'+password+".pdf", "wb") as resultPDF:
        pdfWriter.write(resultPDF)
    
os.remove("666.pdf")
os.remove(b+".txt")



