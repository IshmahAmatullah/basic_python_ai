#Reference 1 = github samlopezf "send_email.py"
#Reference 2 = blog.mailtrap.io "how to send an email in Python"
#Reference 3 = stack overflow https://stackoverflow.com/questions/30823683/python-sending-email-to-multiple-recipients

#import necessary packages
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#definisi fungsi penerima
def getreceiver(receiver_list):
  receiver = []
  a = open("D:\\File Ishmah\\[Course]\\basic_python_ai\\Final_Project\\receiver_list.txt", "r")
  for line in a:
    receiver.append(line)
  return receiver

#set up the parameters of the message
#1 pengirim email dan passwordnya
pengirim = input("Pengirim email : ")
pwd = input("Password : ")
#2 penerima email
penerima = getreceiver("receiver_list.txt")
#3 subjek email
subjek = "Reminder Pengumpulan Final Project Basic Python AI Batch #5"

#create message object instance
msg = MIMEMultipart()
#add relevant header
msg["From"] = pengirim
msg["To"] = penerima
msg["Subject"] = subjek

#add text 
# write the plain text part
txt = """\
Halo Sobat AI Batch #5!
Mengingatkan untuk jangan lupa mengumpulkan final-project AI Basic Python Batch #5
Pengumpulan tugas akan dipresentasikan pada akhir pertemuan, Minggu, 4 April 2021."""
# write the HTML text part 
html = """\
<html>
 <body>
   <p>Join google classroom : </p>
   <p><a href="https://meet.google.com/xyb-nnuo-wuf?authuser=1">Google Classroom: Basic Python Batch #5</p>
   <p>Jika punya pertanyaan, jangan lupa hubungi <strong>Mentor</strong> lewat <strong>Telegram</strong> yaa</p>
   <img src="cid:MailIconImage">
 </body>
</html>
"""
#convert both parts to MIMEText objects and add them to the MIMEMultipart message
part1 = MIMEText(txt,"plain")
part2 = MIMEText(html, "html")
msg.attach(part1)
msg.attach(part2)

#attach image to message body
imgname = "D:\\File Ishmah\\[Course]\\basic_python_ai\\Final_Project\\Image.jpg"
#open IMG file in binary mode
img_attachment = open(imgname, "rb")
image = MIMEImage((img_attachment).read())
img_attachment.close()
#specify the ID according to the img source in the HTML part
image.add_header("Content-ID", "<MailIconImage>")
msg.attach(image)

# msg.attach(MIMEImage(open().read()))

#attachment document to message body
filename = "D:\\File Ishmah\\[Course]\\basic_python_ai\\Final_Project\\Final Project - Basic Python.pdf"
#open PDF file in binary mode
pdf_attachment = open(filename, "rb")
#the content type "application/octet-stream" means that a MIME attachment is a binary
part3 = MIMEBase("application", "octet-stream")
part3.set_payload((pdf_attachment).read())
#encode to base64
encoders.encode_base64(part3)
#add header
part3.add_header("Content-Disposition", "pdf_attachment; filename= "+filename)
#add attachment to your message and convert it to string
msg.attach(part3)
text = msg.as_string()

for indeks in range(len(penerima)):
  msg()
  server = smtplib.SMTP('smtp.gmail.com',587) #membuat objek SMTP : Server 
  server.starttls() #server = smtplib.SMTP(host="host_adress",port=your_port)
  server.login(pengirim, pwd) #log in credentials for sending the mail
  server.sendmail(pengirim, penerima[indeks], text) #send the message via the server
  server.quit() #terminate the SMTP session and close the connection
  print("successfully sent email to %s:" %penerima[indeks]) #notification