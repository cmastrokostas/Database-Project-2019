import sys
import pymysql
conn = pymysql.connect(host='150.140.186.217',user='db19_up1053708',
                       passwd='up1053708' ,db='project_up1053708',charset='utf8')## connection object
cur=conn.cursor()   

#_______________GENERAL_______________#
def more(cur):
     print('''
        ΕΠΙΛΕΞΤΕ ΕΝΕΡΓΕΙΑ :
        1.ΠΡΟΒΟΛΗ ΧΩΡΩΝ ΜΕ ΧΩΡΗΤΙΚΟΤΗΤΑ ΠΟΥ ΕΠΙΛΕΓΕΙ Ο ΧΡΗΣΤΗΣ
        2.ΠΡΟΒΟΛΗ ΠΕΛΑΤΩΝ ΜΕ ΒΑΣΗ ΤΗΝ ΗΛΙΚΙΑ
        3.ΔΙΑΓΡΑΦΗ ΕΚΔΗΛΩΣΕΩΝ ΠΟΥ ΓΙΝΟΝΤΑΙ ΠΡΙΝ ΑΠΟ ΕΠΙΛΕΓΜΕΝΗ ΗΜΕΡΟΜΗΝΙΑ''')
     inp1=int(input())
     if inp1==1:
          print("ΕΠΙΛΕΞΤΕ ΧΩΡΗΤΙΚΟΤΗΤΑ:")
          inp=input()
          print("ΟΝΟΜΑ ΧΩΡΟΥ,ΚΩΔΙΚΟΣ ΧΩΡΟΥ, ΧΩΡΗΤΙΚΟΤΗΤΑ")
          cur.execute("SELECT `ΟΝΟΜΑ_ΧΩΡΟΥ`,`ID_ΧΩΡΟΥ`,`ΘΕΣΕΙΣ` FROM `ΧΩΡΟΣ` WHERE `ΘΕΣΕΙΣ` > %s",inp)
          names = cur.description
          attr_names(cur)
          data = cur.fetchall()
          for i in data:
               print(i)
     elif inp1==2:
          print("ΕΠΙΛΕΞΤΕ ΚΑΤΩΤΑΤΟ ΟΡΙΟ ΗΛΙΚΙΑΣ:")
          inp2=input()
          print("ΕΠΙΛΕΞΤΕ ΑΝΩΤΑΤΟ ΟΡΙΟ ΗΛΙΚΙΑΣ:")
          inp3=input()
          cur.execute("SELECT`ΟΝΟΜΑ`,`ΕΠΩΝΥΜΟ`,`ID_ΠΕΛΑΤΗ` FROM `ΠΕΛΑΤΗΣ` WHERE `ΗΛΙΚΙΑ` >= %s AND `ΗΛΙΚΙΑ` <= %s",(inp2,inp3))
          names = cur.description
          attr_names(cur)
          data = cur.fetchall()
          for i in data:
               print(i)
     elif inp1==3:
          print("ΕΠΙΛΕΞΤΕ ΗΜΕΡΟΜΗΝΙΑ:")
          inp1=input()
          sql='''DELETE FROM `ΕΚΔΗΛΩΣΗ` WHERE `ΗΜΕΡΟΜΗΝΙΑ_ΔΙΕΞΑΓΩΓΗΣ`< %s;'''
          res = cur.execute(sql,inp1)
          print("deleted")
          conn.commit()
          view_table(cur,'ΕΚΔΗΛΩΣΗ'
                     )
          
def print_tables():
     print('''
        ΕΠΙΛΕΞΤΕ ΠΙΝΑΚΑ :
        1.ΣΧΕΣΗ ΕΚΔΗΛΩΣΗΣ ΜΕ ΚΑΤΗΓΟΡΙΑ
        2.ΔΙΟΡΓΑΝΩΣΗ ΕΚΔΗΛΩΣΗΣ
        3.ΔΙΟΡΓΑΝΩΤΕΣ
        4.ΕΙΣΗΤΗΡΙΑ
        5.ΕΚΔΗΛΩΣΕΙΣ
        6.ΠΕΛΑΤΗΣ ΠΑΙΡΝΕΙ ΕΙΣΗΤΗΡΙΟ/Α
        7.ΚΑΛΛΙΤΕΧΝΕΣ
        8.ΚΑΤΗΓΟΡΙΕΣ
        9.ΠΕΛΑΤΕΣ
        10.ΣΥΜΜΕΤΟΧΗ ΚΑΛΛΙΤΕΧΝΗ ΣΕ ΕΚΔΗΛΩΣΗ
        11.ΧΩΡΟI
        
        ''')
def attr_names(cur):
    names = cur.description
    x=int(len(names))
    for i in range(x):
        print(names[i][0]+" ", end =  '')
    print (end='\n')
def add(cur):
    print_tables()
    dic = {1: 'ΑΝΗΚΕΙ', 2: 'ΔΙΟΡΓΑΝΩΝΕΙ', 3: 'ΔΙΟΡΓΑΝΩΤΗΣ', 4: 'ΕΙΣΗΤΗΡΙΟ', 5: 'ΕΚΔΗΛΩΣΗ', 6: 'ΕΧΕΙ', 7: 'ΚΑΛΛΙΤΕΧΝΗΣ', 8: 'ΚΑΤΗΓΟΡΙΑ', 9: 'ΠΕΛΑΤΗΣ', 10: 'ΣΥΜΜΕΤΕΧΕΙ', 11: 'ΧΩΡΟΣ'}     
    inp = int(input())
    if inp == 1:
        add_item1(cur)
    elif inp==2:
        add_item2(cur)
    elif inp==3:
        add_item3(cur)
    elif inp==4:
        add_item4(cur)
    elif inp==5:
        add_item5(cur)
    elif inp==6:
        add_item6(cur)
    elif inp==7:
        add_item7(cur)
    elif inp==8:
        add_item8(cur)
    elif inp==9:
        add_item9(cur)
    elif inp==10:
        add_item10(cur)
    elif inp==11:
        add_item11(cur)
def remove(cur):
    print_tables()
    dic = {1: 'ΑΝΗΚΕΙ', 2: 'ΔΙΟΡΓΑΝΩΝΕΙ', 3: 'ΔΙΟΡΓΑΝΩΤΗΣ', 4: 'ΕΙΣΗΤΗΡΙΟ', 5: 'ΕΚΔΗΛΩΣΗ', 6: 'ΕΧΕΙ', 7: 'ΚΑΛΛΙΤΕΧΝΗΣ', 8: 'ΚΑΤΗΓΟΡΙΑ', 9: 'ΠΕΛΑΤΗΣ', 10: 'ΣΥΜΜΕΤΕΧΕΙ', 11: 'ΧΩΡΟΣ'}     
    inp = int(input())
    if inp==1:
        remove_item1(cur)
    elif inp==2:
        remove_item2(cur)
    elif inp==3:
        remove_item3(cur)
    elif inp==4:
        remove_item4(cur)
    elif inp==5:
        remove_item5(cur)
    elif inp==6:
        remove_item6(cur)
    elif inp==7:
        remove_item7(cur)
    elif inp==8:
        remove_item8(cur)
    elif inp==9:
        remove_item9(cur)
    elif inp==10:
        remove_item10(cur)
    elif inp==11:
        remove_item11(cur)

def view(cur):
    print_tables()
    dic = {1: 'ΑΝΗΚΕΙ', 2: 'ΔΙΟΡΓΑΝΩΝΕΙ', 3: 'ΔΙΟΡΓΑΝΩΤΗΣ', 4: 'ΕΙΣΗΤΗΡΙΟ', 5: 'ΕΚΔΗΛΩΣΗ', 6: 'ΕΧΕΙ', 7: 'ΚΑΛΛΙΤΕΧΝΗΣ', 8: 'ΚΑΤΗΓΟΡΙΑ', 9: 'ΠΕΛΑΤΗΣ', 10: 'ΣΥΜΜΕΤΕΧΕΙ', 11: 'ΧΩΡΟΣ'}     
    inp = int(input())
    view_table(cur, dic[inp])

def view_table(cur, value):
    
    cur.execute("SELECT * FROM " +value)
    names = cur.description
    attr_names(cur)
    data = cur.fetchall()
    for i in data:
        print(i)
    
    
#__________________________________________________________________________________________#
    
#___________________________________ADD FUNCTIONS__________________________________________#
#_____ΑΝΗΚΕΙ_____#
def add_item1(cur):
    print("ΟΝΟΜΑ ΚΑΤΗΓΟΡΙΑΣ, ΚΩΔΙΚΟΣ ΚΑΤΗΓΟΡΙΑΣ:")
    cur.execute('''SELECT`ΟΝΟΜΑ_ΚΑΤΗΓΟΡΙΑΣ`,`ID_ΚΑΤΗΓΟΡΙΑΣ` FROM `ΚΑΤΗΓΟΡΙΑ`''')
    data = cur.fetchall()
    for i in data:
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΚΑΤΗΓΟΡΙΑΣ:")
    inp1=input()
    print("ΟΝΟΜΑ ΕΚΔΗΛΩΣΗΣ, ΚΩΔΙΚΟΣ ΕΚΔΗΛΩΣΗΣ\n")
    cur.execute('''SELECT `ΟΝΟΜΑ_ΕΚΔΗΛΩΣΗΣ`,`ID_ΕΚΔΗΛΩΣΗΣ` FROM `ΕΚΔΗΛΩΣΗ`''')
    data = cur.fetchall()
    for i in data:
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΕΚΔΗΛΩΣΗΣ:")
    inp2=input()
    insertStatement='''INSERT INTO `ΑΝΗΚΕΙ` (`ΚΩΔΙΚΟΣ_ΚΑΤΗΓΟΡΙΑΣ`, `ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ`) VALUES (%s, %s);'''
    cur.execute(insertStatement,(inp1,inp2))
    print('ADDED')
    conn.commit()
#_____ΔΙΟΡΓΑΝΩΝΕΙ_____#
def add_item2(cur):
    print("ΔΙΟΡΓΑΝΩΤΡΙΑ ΕΤΑΙΡΕΙΑ, ΚΩΔΙΚΟΣ ΔΙΟΡΓΑΝΩΤΗ:")
    cur.execute('''SELECT `ΔΙΟΡΓΑΝΩΤΡΙΑ_ΕΤΑΙΡΕΙΑ`,`ID_ΔΙΟΡΓΑΝΩΤΗ` FROM `ΔΙΟΡΓΑΝΩΤΗΣ`''')
    data = cur.fetchall()
    for i in data:
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΔΙΟΡΓΑΝΩΤΗ:")
    inp1=input()
    print("ΟΝΟΜΑ ΕΚΔΗΛΩΣΗΣ, ΚΩΔΙΚΟΣ ΕΚΔΗΛΩΣΗΣ\n")
    cur.execute('''SELECT `ΟΝΟΜΑ_ΕΚΔΗΛΩΣΗΣ`,`ID_ΕΚΔΗΛΩΣΗΣ` FROM `ΕΚΔΗΛΩΣΗ` WHERE 1''')
    data = cur.fetchall()
    for i in data:
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΕΚΔΗΛΩΣΗΣ:")
    inp2=input()
    insertStatement='''INSERT INTO `ΔΙΟΡΓΑΝΩΝΕΙ` (`ΚΩΔΙΚΟΣ_ΔΙΟΡΓΑΝΩΤΗ`, `ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ`) VALUES (%s, %s);'''
    cur.execute(insertStatement,(inp1,inp2))
    print('ADDED')
    conn.commit()
    

#_____ΔΙΟΡΓΑΝΩΤΗΣ_____#
def add_item3(cur):
    print("ΤΗΛΕΦΩΝΟ:")
    inp1=input()
    print("EMAIL:")
    inp2=input()
    print("ONOMA:")
    inp3=input()
    print("ΕΠΩΝΥΜΟ:")
    inp4=input()
    print("ID_ΔΙΟΡΓΑΝΩΤΗ:")
    inp5=input()
    print("ΔΙΟΡΓΑΝΩΤΡΙΑ_ΕΤΑΙΡΕΙΑ:")
    inp6=input()
    insertStatement =  '''INSERT INTO `ΔΙΟΡΓΑΝΩΤΗΣ` (`ΤΗΛΕΦΩΝΟ`, `EMAIL`, `ΟΝΟΜΑ`, `ΕΠΩΝΥΜΟ`, `ID_ΔΙΟΡΓΑΝΩΤΗ`, `ΔΙΟΡΓΑΝΩΤΡΙΑ_ΕΤΑΙΡΕΙΑ`) VALUES("%s", "%s","%s","%s","%s","%s")'''
    cur.execute(insertStatement,(inp1,inp2,inp3,inp4,inp5,inp6))
#_____ΕΙΣΗΤΗΡΙΟ_____#  
def add_item4(cur):
    print("ΚΟΣΤΟΣ:")
    inp1=input()
    print("ΚΩΔΙΚΟΣ ΚΡΑΤΗΣΗΣ ΕΙΣΗΤΗΡΙΟΥ:")
    inp2=input()
    print("ΗΜΕΡΟΜΗΝΙΑ ΚΡΑΤΗΣΗΣ: YYYY-MM-DD")
    inp3=input()
    print("ΟΝΟΜΑ ΠΕΛΑΤΗ, ΕΠΩΝΥΜΟ ΠΕΛΑΤΗ, ΚΩΔΙΚΟΣ ΠΕΛΑΤΗ")
    cur.execute('''SELECT `ΟΝΟΜΑ`,`ΕΠΩΝΥΜΟ`,`ID_ΠΕΛΑΤΗ` FROM `ΠΕΛΑΤΗΣ`''')
    data = cur.fetchall()
    for i in data:
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΠΕΛΑΤΗ:")
    inp4=input()
    print("ΤΥΠΟΣ ΕΙΣΗΤΗΡΙΟΥ:")
    inp5=input()
    insertStatement =''' INSERT INTO `ΕΙΣΗΤΗΡΙΟ` (`ΚΟΣΤΟΣ`, `ΚΩΔΙΚΟΣ_ΚΡΑΤΗΣΗΣ`, `ΗΜΕΡΟΜΗΝΙΑ_ΚΡΑΤΗΣΗΣ`, `ΚΩΔΙΚΟΣ_ΠΕΛΑΤΗ`, `ΤΥΠΟΣ_ΕΙΣΗΤΗΡΙΟΥ`) VALUES (%s, %s,%s,%s,%s);'''
    cur.execute(insertStatement,(int(inp1),inp2,inp3,inp4,inp5))
    print('ADDED')
    conn.commit()
#_____ΕΚΔΗΛΩΣΗ_____#
def add_item5(cur):
    print("TARGET GROUP:")
    inp1=input()
    print("ΗΜΕΡΟΜΗΝΙΑ ΔΙΕΞΑΓΩΓΗΣ: YYYY-MM-DD")
    inp2=input()
    print("ID ΕΚΔΗΛΩΣΗΣ:")
    inp3=input()
    print("ΩΡΑ ΕΝΑΡΞΗΣ: HH:MM:SS")
    inp4=input()
    print("ΟΝΟΜΑ ΧΩΡΟΥ, ΚΩΔΙΚΟΣ ΧΩΡΟΥ")
    cur.execute('''SELECT `ΟΝΟΜΑ_ΧΩΡΟΥ`,`ID_ΧΩΡΟΥ` FROM `ΧΩΡΟΣ`''')
    data = cur.fetchall()
    for i in data:
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΧΩΡΟΥ:")
    inp5=input()
    print("ΟΝΟΜΑ ΕΚΔΗΛΩΣΗΣ:")
    inp6=input()
    print("ΔΙΑΘΕΣΙΜΑ ΕΙΣΗΤΗΡΙΑ:")
    inp7=input()
    insertStatement = '''INSERT INTO `ΕΚΔΗΛΩΣΗ` (`TARGET_GROUP`, `ΗΜΕΡΟΜΗΝΙΑ_ΔΙΕΞΑΓΩΓΗΣ`, `ID_ΕΚΔΗΛΩΣΗΣ`, `ΩΡΑ_ΕΝΑΡΞΗΣ`, `ΚΩΔΙΚΟΣ_ΧΩΡΟΥ`, `ΟΝΟΜΑ_ΕΚΔΗΛΩΣΗΣ`, `ΔΙΑΘΕΣΙΜΑ_ΕΙΣΗΤΗΡΙΑ`) VALUES (%s, %s, %s, %s, %s, %s, %s);'''
    cur.execute(insertStatement,(inp1,inp2,inp3,inp4,inp5,inp6,int(inp7)))
    print('ADDED')
    conn.commit()
#_____ΕΧΕΙ_____#
def add_item6(cur):
    print("ONOMA ΠΕΛΑΤΗ, ΕΠΩΝΥΜΟ ΠΕΛΑΤΗ, ΚΩΔΙΚΟΣ ΠΕΛΑΤΗ, ΚΩΔΙΚΟΣ ΚΡΑΤΗΣΗΣ:")
    cur.execute('''SELECT `ΟΝΟΜΑ`,`ΕΠΩΝΥΜΟ`,`ID_ΠΕΛΑΤΗ`, `ΚΩΔΙΚΟΣ_ΚΡΑΤΗΣΗΣ` FROM `ΠΕΛΑΤΗΣ` JOIN `ΕΙΣΗΤΗΡΙΟ` ON (`ID_ΠΕΛΑΤΗ` = `ΚΩΔΙΚΟΣ_ΠΕΛΑΤΗ`) ''')
    data = cur.fetchall()
    for i in data:
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΚΡΑΤΗΣΗΣ:")
    inp1=input()
    print("ΕΚΔΗΛΩΣΕΙΣ \n")
    cur.execute('''SELECT `ΟΝΟΜΑ_ΕΚΔΗΛΩΣΗΣ`,`ID_ΕΚΔΗΛΩΣΗΣ` FROM `ΕΚΔΗΛΩΣΗ` ''')
    data = cur.fetchall()
    for i in data:
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΕΚΔΗΛΩΣΗΣ:")
    inp2=input()
    insertStatement='''INSERT INTO `ΕΧΕΙ` (`ΚΩΔΙΚΟΣ_ΚΡΑΤΗΣΗΣ_ΕΙΣΗΤΗΡΙΟΥ`, `ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ`) VALUES (%s, %s);'''
    
    cur.execute(insertStatement,(inp1,inp2))
    print('ADDED')
    conn.commit()
#_____ΚΑΛΛΙΤΕΧΝΗΣ_____#
def add_item7(cur):
    print("ΟΝΟΜΑ:")
    inp1=input()
    print("ΕΠΩΝΥΜΟ:")
    inp2=input()
    print("ΚΑΛΛΙΤΕΧΝΙΚΟ ΟΝΟΜΑ:")
    inp3=input()
    print("ΕΙΔΟΣ:")
    inp4=input()
    print("ID ΚΑΛΛΙΤΕΧΝΗ:")
    inp5=input()
    print("ΣΥΓΚΡΟΤΗΜΑ/ΟΜΑΔΑ:")
    inp6=input()
    insertStatement = '''INSERT INTO `ΚΑΛΛΙΤΕΧΝΗΣ` (`ΟΝΟΜΑ`, `ΕΠΩΝΥΜΟ`, `ΚΑΛΛΙΤΕΧΝΙΚΟ_ΟΝΟΜΑ`, `ΕΙΔΟΣ`, `ID_ΚΑΛΛΙΤΕΧΝΗ`, `ΣΥΓΚΡΟΤΗΜΑ/ΟΜΑΔΑ`) VALUES (%s, %s,%s,%s,%s,%s);'''
    cur.execute(insertStatement,(inp1,inp2,inp3,inp4,inp5,inp6))
    print('ADDED')
    conn.commit()
#_____ΚΑΤΗΓΟΡΙΑ_____#
def add_item8(cur):
    print("ID ΚΑΤΗΓΟΡΙΑΣ:")
    inp1=input()
    print("ΕΙΔΟΣ:")
    inp2=input()
    print("ΟΝΟΜΑ ΚΑΤΗΓΟΡΙΑΣ:")
    inp3=input()
    insertStatement = '''INSERT INTO `ΚΑΤΗΓΟΡΙΑ` (`ID_ΚΑΤΗΓΟΡΙΑΣ`, `ΕΙΔΟΣ`, `ΟΝΟΜΑ_ΚΑΤΗΓΟΡΙΑΣ`) VALUES ("%s", "%s","%s");'''
    cur.execute(insertStatement,(inp1,inp2,inp3))
    print('ADDED')
    conn.commit()
#_____ΠΕΛΑΤΗΣ_____#
def add_item9(cur):
    print("EMAIL:")
    inp1=input()
    print("ΤΗΛΕΦΩNΟ:")
    inp2=input()
    print("ΑΡΙΘΜΟΣ:")
    inp3=int(input())
    print("ΤΑΧΥΔΡΟΜΙΚΟΣ ΚΩΔΙΚΑΣ:")
    inp4=int(input())
    print("ΟΔΟΣ:")
    inp5=input()
    print("ΟΝΟΜΑ:")
    inp6=input()
    print("ΕΠΩΝΥΜΟ:")
    inp7=input()
    print("ID_ΠΕΛΑΤΗ:")
    inp8=input()
    print("ΦΥΛΟ:")
    inp9=input()
    print("ΗΛΙΚΙΑ:")
    inp10=int(input())
    insertStatement = '''INSERT INTO `ΠΕΛΑΤΗΣ` (`EMAIL`, `ΤΗΛΕΦΩΝΟ`, `ΑΡΙΘΜΟΣ`, `ΤΚ`, `ΟΔΟΣ`, `ΟΝΟΜΑ`, `ΕΠΩΝΥΜΟ`, `ID_ΠΕΛΑΤΗ`, `ΦΥΛΟ`, `ΗΛΙΚΙΑ`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
    cur.execute(insertStatement,(inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8,inp9,inp10))
    print('ADDED')
    conn.commit() 
#_____ΣΥΜΜΕΤΕΧΕΙ_____#      
def add_item10(cur):
    print("ΚΑΛΛΙΤΕΧΝHΣ, ΚΩΔΙΚΟΣ ΚΑΛΛΙΤΕΧΝΗ:")
    cur.execute('''SELECT `ΚΑΛΛΙΤΕΧΝΙΚΟ_ΟΝΟΜΑ`,`ID_ΚΑΛΛΙΤΕΧΝΗ` FROM `ΚΑΛΛΙΤΕΧΝΗΣ` ''')
    data = cur.fetchall()
    for i in data:
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΚΑΛΛΙΤΕΧΝΗ:")
    inp1=input()
    print("ΕΚΔΗΛΩΣΕΙΣ \n")
    cur.execute('''SELECT `ΟΝΟΜΑ_ΕΚΔΗΛΩΣΗΣ`,`ID_ΕΚΔΗΛΩΣΗΣ` FROM `ΕΚΔΗΛΩΣΗ` ''')
    data = cur.fetchall()
    for i in data:
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΕΚΔΗΛΩΣΗΣ:")
    inp2=input()
    insertStatement='''INSERT INTO `ΣΥΜΜΕΤΕΧΕΙ` (`ΚΩΔΙΚΟΣ_ΚΑΛΛΙΤΕΧΝΗ`, `ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ`) VALUES (%s,%s);'''
    cur.execute(insertStatement,(inp1,inp2))
    print('ADDED')
    conn.commit()
#_____ΧΩΡΟΣ_____#
def add_item11(cur):
    print("ΟΝΟΜΑ ΧΩΡΟΥ:")
    inp1=input()
    print(" ID_ΧΩΡΟΥ:")
    inp2=input()
    print("ΤΗΛΕΦΩΝΟ:")
    inp3=input()
    print("ONOMA ΥΠΕΥΘΥΝΟΥ ΧΩΡΟΥ:")
    inp4=input()
    print("ΕΠΩΝΥΜΟ ΥΠΕΥΘΥΝΟΥ ΧΩΡΟΥ:")
    inp5=input()
    print("ΑΡΙΘΜΟΣ ΘΕΣΕΩΝ:")
    inp6=int(input())
    print("ΠΡΟΣΒΑΣΗ_ΑΜΕΑ:")
    inp7=input()
    print("ΑΡΙΘΜΟΣ ΟΔΟΥ:")
    inp8=int(input())
    print("ΝΟΜΟΣ:")
    inp9=input()
    print("ΠΟΛΗ:")
    inp10=input()
    print("ΟΔΟΣ:")
    inp11=int(input())
    insertStatement =''' INSERT INTO `ΧΩΡΟΣ` (`ΟΝΟΜΑ_ΧΩΡΟΥ`, `ID_ΧΩΡΟΥ`, `ΤΗΛΕΦΩΝΟ`, `ΟΝΟΜΑ`, `ΕΠΩΝΥΜΟ`, `ΘΕΣΕΙΣ`, `ΠΡΟΣΒΑΣΗ_ΑΜΕΑ`, `ΑΡΙΘΜΟΣ`, `ΝΟΜΟΣ`, `ΠΟΛΗ`, `ΟΔΟΣ`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
    cur.execute(insertStatement,(inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8,inp9,inp10,inp11))
    print('ADDED')
    conn.commit() 
#_______________________________________________________________________________________________#



#__________________________________________DELETE FUNCTIONS_____________________________________#
#_____ΑΝΗΚΕΙ_____#
def remove_item1(cur):
    print("ΚΑΤΗΓΟΡΙΑ , ΚΩΔΙΚΟΣ ΚΑΤΗΓΟΡΙΑΣ,ΕΚΔΗΛΩΣΗ,ΚΩΔΙΚΟΣ,ΕΚΔΗΛΩΣΗΣ")
    cur.execute('''SELECT `ΟΝΟΜΑ_ΚΑΤΗΓΟΡΙΑΣ`,`ΕΙΔΟΣ`,`ΚΩΔΙΚΟΣ_ΚΑΤΗΓΟΡΙΑΣ`,`ΟΝΟΜΑ_ΕΚΔΗΛΩΣΗΣ`,`ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ` FROM `ΚΑΤΗΓΟΡΙΑ` JOIN `ΑΝΗΚΕΙ`ON (`ID_ΚΑΤΗΓΟΡΙΑΣ`= `ΚΩΔΙΚΟΣ_ΚΑΤΗΓΟΡΙΑΣ`) JOIN `ΕΚΔΗΛΩΣΗ` ON (`ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ`=`ID_ΕΚΔΗΛΩΣΗΣ`)''')
    data = cur.fetchall()
    for i in data:
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΚΑΤΗΓΟΡΙΑΣ :")
    inp1=input()
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΕΚΔΗΛΩΣΗΣ :")
    inp2=input()
    sql='''DELETE FROM `ΔΙΟΡΓΑΝΩΝΕΙ` WHERE `ΚΩΔΙΚΟΣ_ΔΙΟΡΓΑΝΩΤΗ` = %s AND `ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ` = %s ;'''
    res = cur.execute(sql,(inp1,inp2))
    print("deleted")
    conn.commit()
#_____ΔΙΟΡΓΑΝΩΝΕΙ_____#
def remove_item2(cur):
    print("ΔΙΟΡΓΑΝΩΤΡΙΑ ΕΤΑΙΡΙΑ ,ΚΩΔΙΚΟΣ ΔΙΟΡΓΑΝΩΤΗ,ΟΝΟΜΑ ΕΚΔΗΛΩΣΗΣ,ΚΩΔΙΚΟΣ ΕΚΔΗΛΩΣΗΣ ")
    cur.execute('''SELECT `ΔΙΟΡΓΑΝΩΤΡΙΑ_ΕΤΑΙΡΕΙΑ`,`ΚΩΔΙΚΟΣ_ΔΙΟΡΓΑΝΩΤΗ`,`ΟΝΟΜΑ_ΕΚΔΗΛΩΣΗΣ`,`ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ` FROM `ΔΙΟΡΓΑΝΩΝΕΙ` JOIN `ΔΙΟΡΓΑΝΩΤΗΣ` ON (`ΚΩΔΙΚΟΣ_ΔΙΟΡΓΑΝΩΤΗ`=`ID_ΔΙΟΡΓΑΝΩΤΗ`) JOIN `ΕΚΔΗΛΩΣΗ` ON (`ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ` =`ID_ΕΚΔΗΛΩΣΗΣ`)''')
    data = cur.fetchall()
    for i in data:
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΚΡΑΤΗΣΗΣ ΔΙΟΡΓΑΝΩΤΗ ΣΕ ΣΥΝΔΥΑΣΜΟ ΜΕ ΚΩΔΙΚΟ ΕΚΔΗΛΩΣΗΣ ΓΙΑ ΔΙΑΓΡΑΦΗ:")
    inp1=input()
    inp2=input()
    sql='''DELETE FROM `ΔΙΟΡΓΑΝΩΝΕΙ` WHERE `ΚΩΔΙΚΟΣ_ΔΙΟΡΓΑΝΩΤΗ` = %s AND `ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ` = %s ;'''
    res = cur.execute(sql,(inp1,inp2))
    print("deleted")
    
    conn.commit()
#_____ΔΙΟΡΓΑΝΩΤΗΣ_____#
def remove_item3(cur):
    print("ΔΙΟΡΓΑΝΩΤΡΙΑ ΕΤΑΙΡΙΑ ,ΚΩΔΙΚΟΣ ΔΙΟΡΓΑΝΩΤΗ ")
    cur.execute('''SELECT `ΔΙΟΡΓΑΝΩΤΡΙΑ_ΕΤΑΙΡΕΙΑ`, `ID_ΔΙΟΡΓΑΝΩΤΗ` FROM `ΔΙΟΡΓΑΝΩΤΗΣ` ''')
    data = cur.fetchall()
    for i in data:
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΔΙΟΡΓΑΝΩΤΗ ΓΙΑ ΔΙΑΓΡΑΦΗ:")
    inp1=input()
    sql='''DELETE FROM `ΔΙΟΡΓΑΝΩΤΗΣ` WHERE `ID_ΔΙΟΡΓΑΝΩΤΗ` =%s;'''
    res = cur.execute(sql,inp1)
    print("deleted")
    conn.commit()
#_____ΕΙΣΗΤΗΡΙΟ_____#  
def remove_item4(cur):
    print("ΟΝΟΜΑ ΕΚΔΗΛΩΣΗΣ , ΗΜΕΡΟΜΗΝΙΑ ΔΙΕΞΑΓΩΓΗΣ, ΚΩΔΙΚΟΣ ΕΚΔΗΛΩΣΗΣ ")
    cur.execute('''SELECT `ΟΝΟΜΑ`,`ΕΠΩΝΥΜΟ`,`ΚΩΔΙΚΟΣ_ΚΡΑΤΗΣΗΣ`,`ΤΥΠΟΣ_ΕΙΣΗΤΗΡΙΟΥ` FROM `ΠΕΛΑΤΗΣ` JOIN `ΕΙΣΗΤΗΡΙΟ` ON (`ID_ΠΕΛΑΤΗ` = `ΚΩΔΙΚΟΣ_ΠΕΛΑΤΗ`)''')
    data = cur.fetchall()
    for i in data:
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΕΙΣΗΤΗΡΙΟΥ ΓΙΑ ΔΙΑΓΡΑΦΗ:")
    inp1=input()
    sql='''DELETE FROM `ΕΙΣΗΤΗΡΙΟ` WHERE `ΚΩΔΙΚΟΣ_ΚΡΑΤΗΣΗΣ` = %s;'''
    res = cur.execute(sql,inp1)
    print("deleted")
    conn.commit()
    
#_____ΕΚΔΗΛΩΣΗ_____
def remove_item5(cur):
     
    print("ΟΝΟΜΑ ΕΚΔΗΛΩΣΗΣ , ΗΜΕΡΟΜΗΝΙΑ ΔΙΕΞΑΓΩΓΗΣ, ΚΩΔΙΚΟΣ ΕΚΔΗΛΩΣΗΣ ")
    cur.execute('''SELECT `ΟΝΟΜΑ_ΕΚΔΗΛΩΣΗΣ`,`ΗΜΕΡΟΜΗΝΙΑ_ΔΙΕΞΑΓΩΓΗΣ`,`ID_ΕΚΔΗΛΩΣΗΣ` FROM `ΕΚΔΗΛΩΣΗ`''')
    data = cur.fetchall()
    for i in data:
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΚΑΤΗΓΟΡΙΑΣ ΓΙΑ ΔΙΑΓΡΑΦΗ:")
    inp1=input()
    sql='''DELETE FROM `ΚΑΤΗΓΟΡΙΑ` WHERE `ID_ΚΑΤΗΓΟΡΙΑΣ` = %s;'''
    res = cur.execute(sql,inp1)
    print("deleted")
    conn.commit()
#_____ΕΧΕΙ_____#
def remove_item6(cur):
    print("ONOMA ΠΕΛΑΤΗ, ΕΠΩΝΥΜΟ ΠΕΛΑΤΗ, ΚΩΔΙΚΟΣ ΠΕΛΑΤΗ, ΚΩΔΙΚΟΣ ΚΡΑΤΗΣΗΣ:")
    cur.execute('''SELECT `ΟΝΟΜΑ`,`ΕΠΩΝΥΜΟ`,`ID_ΠΕΛΑΤΗ`, `ΚΩΔΙΚΟΣ_ΚΡΑΤΗΣΗΣ` FROM `ΠΕΛΑΤΗΣ` JOIN `ΕΙΣΗΤΗΡΙΟ` ON (`ID_ΠΕΛΑΤΗ` = `ΚΩΔΙΚΟΣ_ΠΕΛΑΤΗ`) ''')
    data = cur.fetchall()
    for i in data:
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΚΡΑΤΗΣΗΣ ΕΙΣΗΤΗΡΙΟΥ ΣΕ ΣΥΝΔΥΑΣΜΟ ΜΕ ΚΩΔΙΚΟ ΕΚΔΗΛΩΣΗΣ ΓΙΑ ΔΙΑΓΡΑΦΗ:")
    inp1=input()
    inp2=input()
    sql=''' DELETE FROM `ΕΧΕΙ` WHERE `ΚΩΔΙΚΟΣ_ΚΡΑΤΗΣΗΣ_ΕΙΣΗΤΗΡΙΟΥ` = %s AND `ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ` = %s ' '''
    res = cur.execute(sql,(inp1,inp2))
    print("deleted")
    conn.commit()
#_____ΚΑΛΛΙΤΕΧΝΗΣ_____#
def remove_item7(cur):
    print("ONOMA MANAGER ,ΕΠΙΘΕΤΟ MANAGER , ΚΑΛΛΙΤΕΧΝΙΚΟ ΟΝΟΜΑ , ΕΙΔΟΣ ,ΚΩΔΙΚΟΣ ΚΑΛΛΙΤΕΧΝΗ ,ΣΥΓΚΡΟΤΗΜΑ/ΟΜΑΔΑ")
    cur.execute('''SELECT * FROM `ΚΑΛΛΙΤΕΧΝΗΣ`  ''')
    data = cur.fetchall()
    for i in data:
         
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΚΑΛΛΙΤΕΧΝΗ ΓΙΑ ΔΙΑΓΡΑΦΗ:")
    inp1=input()
    sql='''DELETE FROM `ΚΑΛΛΙΤΕΧΝΗΣ` WHERE `ID_ΚΑΛΛΙΤΕΧΝΗ` = %s;'''
    res = cur.execute(sql,inp1)
    print("deleted")
    conn.commit()
#_____ΚΑΤΗΓΟΡΙΑ_____#
def remove_item8(cur):
    print("ΚΩΔΙΚΟΣ ΚΑΤΗΓΟΡΙΑΣ , ΕΙΔΟΣ , ΟΝΟΜΑ ΚΑΤΗΓΟΡΙΑΣ")
    cur.execute('''SELECT * FROM `ΚΑΤΗΓΟΡΙΑ`  ''')
    data = cur.fetchall()
    for i in data:
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΚΑΤΗΓΟΡΙΑΣ ΓΙΑ ΔΙΑΓΡΑΦΗ:")
    inp1=input()
    sql='''DELETE FROM `ΚΑΤΗΓΟΡΙΑ` WHERE `ID_ΚΑΤΗΓΟΡΙΑΣ` = %s;'''
    res = cur.execute(sql,inp1)
    print("deleted")
    conn.commit()
#_____ΠΕΛΑΤΗΣ_____#
def remove_item9(cur):
    print("ΠΕΛΑΤΕΣ(EMAIL,THΛΕΦΩΝΟ,ΑΡΙΘΜΟΣ ΟΔΟΥ,ΟΔΟΣ,ΟΝΟΜΑ,ΕΠΩΝΥΜΟ,KΩΔΙΚΟΣ ΠΕΛΑΤΗ,ΦΥΛΟ,ΗΛΙΚΙΑ)")
    cur.execute('''SELECT * FROM `ΠΕΛΑΤΗΣ`  ''')
    data = cur.fetchall()
    for i in data:
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΠΕΛΑΤΗ ΓΙΑ ΔΙΑΓΡΑΦΗ:")
    inp1=input()
    sql='''  DELETE FROM `ΠΕΛΑΤΗΣ` WHERE `ID_ΠΕΛΑΤΗ`= %s '''
    res = cur.execute(sql,inp1)
    print("deleted")
    conn.commit()
    
#_____ΣΥΜΜΕΤΕΧΕΙ_____# 
def remove_item10(cur):
    print("ΣΥΜΜΕΤΟΧΗ ΚΑΛΛΙΤΕΧΝΗ ΣΕ ΕΚΔΗΛΩΣΗ")
    cur.execute('''SELECT `ΚΑΛΛΙΤΕΧΝΙΚΟ_ΟΝΟΜΑ`,`ΚΩΔΙΚΟΣ_ΚΑΛΛΙΤΕΧΝΗ`,`ΟΝΟΜΑ_ΕΚΔΗΛΩΣΗΣ`,`ID_ΕΚΔΗΛΩΣΗΣ` FROM `ΣΥΜΜΕΤΕΧΕΙ` JOIN `ΚΑΛΛΙΤΕΧΝΗΣ`ON (ID_ΚΑΛΛΙΤΕΧΝΗ=ΚΩΔΙΚΟΣ_ΚΑΛΛΙΤΕΧΝΗ) JOIN `ΕΚΔΗΛΩΣΗ` ON (ID_ΕΚΔΗΛΩΣΗΣ=ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ)''')
    data = cur.fetchall()
    for i in data:
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΚΑΛΛΙΤΕΧΝΗ ΣΕ ΣΥΝΔΥΑΣΜΟ ΜΕ ΚΩΔΙΚΟ ΕΚΔΗΛΩΣΗΣ ΓΙΑ ΔΙΑΓΡΑΦΗ:")
    inp1=input()
    inp2=input()
    sql='''DELETE FROM `ΣΥΜΜΕΤΕΧΕΙ` WHERE `ΚΩΔΙΚΟΣ_ΚΑΛΛΙΤΕΧΝΗ` = %s AND `ΚΩΔΙΚΟΣ_ΕΚΔΗΛΩΣΗΣ` = %s ;'''
    res = cur.execute(sql,(inp1,inp2))
    print("deleted")
    conn.commit()
#_____ΧΩΡΟΣ_____#
def remove_item11(cur):

    print("ΧΩΡΟΙ (ΟΝΟΜΑ ΧΩΡΟΥ,ΚΩΔΙΚΟΣ ΧΩΡΟΥ,ΤΗΛΕΦΩΝΟ,ΟΝΟΜΑ ΥΠΕΥΘΥΝΟΥ,ΕΠΩΝΥΜΟ ΥΠΕΥΘΥΝΟΥ,ΑΡΙΘΜΟΣ ΟΔΟΥ,ΘΕΣΕΩΝ,ΑΡΙΘΜΟΣ,ΝΟΜΟΣ,ΠΟΛΗ,ΟΔΟΣ):")
    cur.execute('''SELECT * FROM `ΧΩΡΟΣ`''')
    data = cur.fetchall()
    for i in data:
        print(i)
    print("ΕΠΙΛΕΞΤΕ ΚΩΔΙΚΟ ΧΩΡΟΥ ΓΙΑ ΔΙΑΓΡΑΦΗ:")
    inp1=input()
    sql='''  DELETE FROM `ΧΩΡΟΣ` WHERE `ID_ΧΩΡΟΥ`= %s '''
    res = cur.execute(sql,inp1)
    print("deleted")
    conn.commit()
#_______________________________________________________________________________________________#
def main_menu(cur):
     
    print('''
        ΕΠΙΛΕΞΤΕ ΕΝΕΡΓΕΙΑ:
        1.ΠΡΟΣΘΗΚΗ
        2.ΑΦΑΙΡΕΣΗ
        3.ΠΡΟΒΟΛΗ
        4.ΠΕΡΙΣΣΟΤΕΡΕΣ ΕΠΙΛΟΓΕΣ
        5.ΕΞΟΔΟΣ
    ''')
    inp = int(input())
    if inp==1:
        add(cur)
    if inp==2:
        remove(cur)
    if inp==3:
        view(cur)
    if inp==4:
        more(cur)
    if inp==5:
       sys.exit()
while True:
     main_menu(cur)
cur.close()
conn.close()

