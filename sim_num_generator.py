'''

'''
import random
import mysql.connector
import smtplib
mydb=mysql.connector.connect(
host="localhost",
user="root",
password="ashikraina",
database="sim_number_generator"

)

mycursor=mydb.cursor()
def airtel_provider():
    #airtel_sim=[]
    name=input("Enter your name : ")
    age=int(input("Enter your age : "))
    email_id=input("Enter your Mail id : ")
    address=input("Enter your address")
    country_code="+91"
    prefixes="9"
    number=random.randint(100000000,999999999)
    phone_number=print(f"{country_code}  {prefixes} {number}")
    #airtel_sim.append(phone_number)
    #print(airtel_sim)
    sql="insert into airtel(name,age,email_id,address) values (%s,%s,%s,%s,%s)"
    val=(name,age,email_id,address)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Information has been stored successfully ---------")
    print(f"Hi {name} you will receive your sim_number through the Mail ----")
    sender_mail="mohammedashik10012003@gmail.com"
    s=smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login(sender_mail,"gwwg nvbk cfze pooi")
    message=print(f" Hi {name} Thank you for choosing Airtel services \n your sim_number is {phone_number}")
    s.sendmail(sender_mail,email_id,message)
    s.quit()
    print("Mail has been sended ---")
def jio_provider():
    #jio_sim=[]
    name=input("Enter your name : ")
    age=int(input("Enter your age : "))
    email_id=input("Enter your Mail id : ")
    
    address=input("Enter your address")
    country_code="+91"
    prefixes="7"
    number=random.randint(100000000,999999999)
    phone_number=print(f"{country_code}  {prefixes} {number} ")
    #jio_sim.append(phone_number)
    #print(jio_sim)
    sql="insert into jio(name,age,email_id,address) values (%s,%s,%s,%s)"
    val=(name,age,email_id,address)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Information has been stored successfully ---------")
    print(f"Hi {name} you will receive your sim_number through the Mail ----")
    sender_mail="mohammedashik10012003@gmail.com"
    s=smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login(sender_mail,"gwwg nvbk cfze pooi")
    message=print(f" Hi {name} Thank you for choosing JIO services \n your sim_number is {phone_number}")
    s.sendmail(sender_mail,email_id,message)
    s.quit()
    print("Mail has been sended ---")
def generate_sim_number():
    print("--------------- WELCOME TO SIM SERVICE PROVIDERS -----------------")
    print("Select your service provider ----- ")
    user=input("select service provider - ")
    if user == "airtel":
        airtel_provider()
    elif user == "jio":
        jio_provider()
    else:
        print("please select avalid service provider")
        return generate_sim_number()
    
generate_sim_number()