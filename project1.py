import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline=' ')as csv_files:
        writer=csv.writer(csv_files)

    if csv_file.tell()==0:
        writer.writerow(["Name","Age","Contact_number","E-mail_id"])

    writer.writerow(info_list)

if __name__=='__main__':
    condition = True
    student_num=1

    while(condition):
         student_info= input('enter student information for student a{} in the following format(Name Age Contact_number E-mail_id):'.format(student_num))

         #split
         student_info_list= student_info.split(' ')
    
         print("\n the entered information is \nName:{}\nAge:{}\nContact_number:{}\nE-mail_id:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

         choice_check=input("is the information entered correct? [yes/no]:")

         if choice_check=="yes":
            write_into_csv(student_info_list)

            conditio_check=input("Enter (yes/no) if you want to enter information for another student:")
            if condition_check =="yes":
               condition=True
               student_num= student_num +1
            elif condition_check=="no":
               condition=False
         elif choice_check=="no":
            print("\n please re enter the information:")
