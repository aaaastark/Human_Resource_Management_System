from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages


#------------------------------===========================================================================================================-----------------------------------#


## Create your views here.
import mysql.connector

#                                               XAMPP SERVER DATABASE MYSQL 
# conn = mysql.connector.connect(host="localhost", user='root')
# print('Successfully Created Database')
# cur = conn.cursor(buffered=False)
# #cur.execute("DROP DATABASE allah_rakha")
# cur.execute("CREATE DATABASE IF NOT EXISTS allah_rakha")
# conn = mysql.connector.connect(host="localhost", user='root', database="allah_rakha")
# print('Successfully Created Database')
# cur = conn.cursor(buffered=False)

conn = mysql.connector.connect(host="sql11.freesqldatabase.com", user='sql11455348', password='BwFwAHbX33', port="3306", database = "sql11455348")
print('Successfully Connected Database')
cur = conn.cursor(buffered=False)

    
def Operation_DataBase():
    Table_General = """
                    CREATE TABLE IF NOT EXISTS tb_cateory_3(
                        id int not null auto_increment primary key,
                        your_name varchar(50) not null,
                        father_name varchar(50) not null,
                        gender varchar(20) not null,
                        age varchar(20) not null,
                        height_weight varchar(50) not null,
                        date_of_birth varchar(30) not null,
                        marital_status varchar(30) not null,
                        languages_known varchar(70) not null,
                        country varchar(30) not null,
                        present_address varchar(70) not null,
                        permanent_address varchar(70) not null,
                        email varchar(30) not null,
                        phone varchar(30) not null
                    );
                    """
    cur.execute(Table_General)


    Table_Job = """
                    CREATE TABLE IF NOT EXISTS tb_cateory_4(
                        id int not null auto_increment primary key,
                        title varchar(50) not null,
                        employee_id varchar(50) not null,
                        date_of_appointment varchar(30) not null,
                        date_of_confirmation varchar(30) not null,
                        date_of_joining varchar(30) not null,
                        department_posted varchar(50) not null,
                        monthly_contribution varchar(50) not null,
                        education_qualification varchar(70) not null,
                        professional_qualification varchar(70) not null
                    );
                    """
    cur.execute(Table_Job)

    Holiday_Information = """
                    CREATE TABLE IF NOT EXISTS tb_holiday(
                        id int not null auto_increment primary key,
                        holiday_name varchar(30) not null,
                        holiday_country varchar(20) not null,
                        holiday_day varchar(20) not null,
                        holiday_date date not null
                    );
                    """
    cur.execute(Holiday_Information)

    Department_Information = """
                    CREATE TABLE IF NOT EXISTS tb_department(
                        id int not null auto_increment,
                        department_code varchar(4) not null,
                        department_name varchar(40) not null,
                        primary key(id,department_code)
                    );
                    """    
    cur.execute(Department_Information)

    Designation_Information = """
                    CREATE TABLE IF NOT EXISTS tb_designation(
                        id int not null auto_increment,
                        designation_code varchar(10) not null,
                        designation_name varchar(40) not null,
                        designation_status varchar(40) not null,
                        primary key(id,designation_code)
                    );
                    """    
    cur.execute(Designation_Information)

    Timesheet_Information = """
                    CREATE TABLE IF NOT EXISTS tb_timesheet(
                        id int not null auto_increment,
                        timesheet_employee_name varchar(30) not null,
                        timesheet_designation_status varchar(30) not null,
                        timesheet_project varchar(40) not null,
                        timesheet_dataissue date not null,
                        timesheet_datedeadline date not null,
                        timesheet_total_hours int(6) not null,
                        timesheet_remaining_hours int(6) not null,
                        timesheet_description varchar(100) not null,
                        primary key(id,timesheet_employee_name)
                    );
                    """    
    cur.execute(Timesheet_Information)

    Leave_Information = """
                    CREATE TABLE IF NOT EXISTS tb_leave(
                        id int not null auto_increment,
                        leave_employee_name varchar(30) not null,
                        leave_designation_status varchar(30) not null,
                        leave_type varchar(40) not null,
                        leave_from date not null,
                        leave_to date not null,
                        leave_days int(6) not null,
                        leave_reason varchar(50) not null,
                        leave_status varchar(30) not null,
                        primary key(id,leave_employee_name)
                    );
                    """    
    cur.execute(Leave_Information)

Operation_DataBase()


#------------------------------===========================================================================================================-----------------------------------#



# --------------------------------------------------------------------------------------------------------------------------------------------------------- #

def employee_index_view(request):
	return render(request,'employee_index.html')


def holiday_index_view(request):
	return render(request,'holiday/holidays_index.html') 

def department_index_view(request):
	return render(request,'department/departments_index.html') 

def designation_index_view(request):
	return render(request,'designation/designations_index.html') 

def timesheet_index_view(request):
	return render(request,'timesheet/timesheets_index.html') 

def leave_index_view(request):
	return render(request,'leave/leaves_index.html') 


# --------------------------------------------------------------------------------------------------------------------------------------------------------- #




# ============================================  HOLIDAY PYTHON START ================================================= #
def holiday_form(request):
    if request.method == 'POST':
        holiday_name = request.POST['holiday_name']
        holiday_country = request.POST['country']
        holiday_day = request.POST['holiday_day']
        holiday_date = request.POST['holiday_date']
        # Gernal Table Information (tb_holiday)
        table_form_values_1 = """INSERT INTO tb_holiday (holiday_name,holiday_country,holiday_day,holiday_date) VALUES (%s,%s,%s,%s)"""

        record_1 =(holiday_name,holiday_country,holiday_day,holiday_date)
        
        cur.execute(table_form_values_1, record_1)
        conn.commit()
        return redirect("/employees/holiday_table/")

    return render(request,'holiday/holidays_form.html')


def holiday_table(request):
    # Table tb_holiday
    cur.execute("SELECT * FROM `tb_holiday`")
    data = cur.fetchall()
    
    return render(request,"holiday/holidays_tableview.html",{'tb_cateory_3_data': data})

def holiday_edit(request,id):
     # Table tb_holiday
    cur.execute("SELECT * FROM `tb_holiday` WHERE `id` = {}".format(id))
    data = cur.fetchall()
    
    return render(request,"holiday/holidays_edit.html",{'tb_cateory_3_data': data})

def holiday_update(request):
    if request.method == 'POST':
        id_index_3 = request.POST['id_index_3']
        holiday_name = request.POST['holiday_name']
        holiday_country = request.POST['country']
        holiday_day = request.POST['holiday_day']
        holiday_date = request.POST['holiday_date']

        # Gernal Table Information (tb_holiday)
        table_form_values_1 = """UPDATE tb_holiday SET holiday_name=%s, holiday_country=%s, holiday_day=%s, holiday_date=%s WHERE id=%s"""

        record_1 =(holiday_name,holiday_country,holiday_day,holiday_date,id_index_3)

        cur.execute(table_form_values_1, record_1)
        
        conn.commit()
    return redirect("/employees/holiday_table/")

def holiday_delete(request,id):
    # Table tb_holiday
    data = "DELETE FROM `tb_holiday` WHERE `id` = {}".format(id)
    cur.execute(data)

    conn.commit()
    return redirect("/employees/holiday_table/")

# ============================================  HOLIDAY PYTHON END ================================================= #




# ============================================  DEPARTMENT PYTHON START ================================================= #
def department_form(request):
    if request.method == 'POST':
        department_code = request.POST['department_code']
        department_name = request.POST['department_name']
        # Gernal Table Information (tb_department)
        table_form_values_1 = """INSERT INTO tb_department (department_code,department_name) VALUES (%s,%s)"""

        record_1 =(department_code,department_name)
        
        cur.execute(table_form_values_1, record_1)
        conn.commit()
        return redirect("/employees/department_table/")

    return render(request,'department/departments_form.html')


def department_table(request):
    # Table tb_holiday
    cur.execute("SELECT * FROM `tb_department`")
    data = cur.fetchall()
    
    return render(request,"department/departments_tableview.html",{'tb_cateory_3_data': data})

def department_edit(request,id):
     # Table tb_holiday
    cur.execute("SELECT * FROM `tb_department` WHERE `id` = {}".format(id))
    data = cur.fetchall()
    
    return render(request,"department/departments_edit.html",{'tb_cateory_3_data': data})

def department_update(request):
    if request.method == 'POST':
        id_index_3 = request.POST['id_index_3']
        department_code = request.POST['department_code']
        department_name = request.POST['department_name']

        # Gernal Table Information (tb_holiday)
        table_form_values_1 = """UPDATE tb_department SET department_code=%s, department_name=%s WHERE id=%s"""

        record_1 =(department_code,department_name,id_index_3)

        cur.execute(table_form_values_1, record_1)
        
        conn.commit()
    return redirect("/employees/department_table/")

def department_delete(request,id):
    # Table tb_holiday
    data = "DELETE FROM `tb_department` WHERE `id` = {}".format(id)
    cur.execute(data)

    conn.commit()
    return redirect("/employees/department_table/")

# ============================================  DEPARTMENT PYTHON END ================================================= #





# ============================================  DESIGNATION PYTHON START ================================================= #
def designation_form(request):
    if request.method == 'POST':
        designation_code = request.POST['designation_code']
        designation_name = request.POST['designation_name']
        designation_status = request.POST['designation_status']
        # Gernal Table Information (tb_department)
        table_form_values_1 = """INSERT INTO tb_designation (designation_code,designation_name,designation_status) VALUES (%s,%s,%s)"""

        record_1 =(designation_code,designation_name,designation_status)
        
        cur.execute(table_form_values_1, record_1)
        conn.commit()
        return redirect("/employees/designation_table/")

    return render(request,'designation/designations_form.html')


def designation_table(request):
    # Table tb_holiday
    cur.execute("SELECT * FROM `tb_designation`")
    data = cur.fetchall()
    
    return render(request,"designation/designations_tableview.html",{'tb_cateory_3_data': data})

def designation_edit(request,id):
     # Table tb_holiday
    cur.execute("SELECT * FROM `tb_designation` WHERE `id` = {}".format(id))
    data = cur.fetchall()
    
    return render(request,"designation/designations_edit.html",{'tb_cateory_3_data': data})

def designation_update(request):
    if request.method == 'POST':
        id_index_3 = request.POST['id_index_3']
        designation_code = request.POST['designation_code']
        designation_name = request.POST['designation_name']
        designation_status = request.POST['designation_status']
        # Gernal Table Information (tb_holiday)
        table_form_values_1 = """UPDATE tb_designation SET designation_code=%s, designation_name=%s, designation_status=%s  WHERE id=%s"""

        record_1 =(designation_code,designation_name,designation_status,id_index_3)

        cur.execute(table_form_values_1, record_1)
        
        conn.commit()
    return redirect("/employees/designation_table/")

def designation_delete(request,id):
    # Table tb_holiday
    data = "DELETE FROM `tb_designation` WHERE `id` = {}".format(id)
    cur.execute(data)

    conn.commit()
    return redirect("/employees/designation_table/")

# ============================================  DESIGNATION PYTHON END ================================================= #




# ============================================  TIMESHEET PYTHON START ================================================= #
def timesheet_form(request):
    if request.method == 'POST':
        timesheet_employee_name = request.POST['timesheet_employee_name']
        timesheet_designation_status = request.POST['timesheet_designation_status']
        timesheet_project = request.POST['timesheet_project']
        timesheet_dataissue = request.POST['timesheet_dataissue']
        timesheet_datedeadline = request.POST['timesheet_datedeadline']
        timesheet_total_hours = request.POST['timesheet_total_hours']
        timesheet_remaining_hours = request.POST['timesheet_remaining_hours']
        timesheet_description = request.POST['timesheet_description']

        # Gernal Table Information (tb_timesheet)
        table_form_values_1 = """INSERT INTO tb_timesheet (timesheet_employee_name,timesheet_designation_status,timesheet_project,timesheet_dataissue,timesheet_datedeadline,timesheet_total_hours,timesheet_remaining_hours,timesheet_description) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

        record_1 =(timesheet_employee_name,timesheet_designation_status,timesheet_project,timesheet_dataissue,timesheet_datedeadline,timesheet_total_hours,timesheet_remaining_hours,timesheet_description)
        
        cur.execute(table_form_values_1, record_1)
        conn.commit()
        return redirect("/employees/timesheet_table/")

    return render(request,'timesheet/timesheets_form.html')


def timesheet_table(request):
    # Table tb_timesheet
    cur.execute("SELECT * FROM `tb_timesheet`")
    data = cur.fetchall()
    
    return render(request,"timesheet/timesheets_tableview.html",{'tb_cateory_3_data': data})

def timesheet_edit(request,id):
     # Table tb_timesheet
    cur.execute("SELECT * FROM `tb_timesheet` WHERE `id` = {}".format(id))
    data = cur.fetchall()
    
    return render(request,"timesheet/timesheets_edit.html",{'tb_cateory_3_data': data})

def timesheet_update(request):
    if request.method == 'POST':
        id_index_3 = request.POST['id_index_3']
        timesheet_employee_name = request.POST['timesheet_employee_name']
        timesheet_designation_status = request.POST['timesheet_designation_status']
        timesheet_project = request.POST['timesheet_project']
        timesheet_dataissue = request.POST['timesheet_dataissue']
        timesheet_datedeadline = request.POST['timesheet_datedeadline']
        timesheet_total_hours = request.POST['timesheet_total_hours']
        timesheet_remaining_hours = request.POST['timesheet_remaining_hours']
        timesheet_description = request.POST['timesheet_description']
        # Gernal Table Information (tb_timesheet)
        table_form_values_1 = """UPDATE tb_timesheet SET timesheet_employee_name=%s, timesheet_designation_status=%s, timesheet_project=%s, timesheet_dataissue=%s, timesheet_datedeadline=%s, timesheet_total_hours=%s, timesheet_remaining_hours=%s, timesheet_description=%s   WHERE id=%s"""

        record_1 =(timesheet_employee_name,timesheet_designation_status,timesheet_project,timesheet_dataissue,timesheet_datedeadline,timesheet_total_hours,timesheet_remaining_hours,timesheet_description,id_index_3)

        cur.execute(table_form_values_1, record_1)
        
        conn.commit()
    return redirect("/employees/timesheet_table/")

def timesheet_delete(request,id):
    # Table tb_timesheet
    data = "DELETE FROM `tb_timesheet` WHERE `id` = {}".format(id)
    cur.execute(data)

    conn.commit()
    return redirect("/employees/timesheet_table/")

# ============================================  TIMESHEET PYTHON END ================================================= #




# ============================================  LEAVE PYTHON START ================================================= #
def leave_form(request):
    if request.method == 'POST':
        leave_employee_name = request.POST['leave_employee_name']
        leave_designation_status = request.POST['leave_designation_status']
        leave_type = request.POST['leave_type']
        leave_from = request.POST['leave_from']
        leave_to = request.POST['leave_to']
        leave_days = request.POST['leave_days']
        leave_reason = request.POST['leave_reason']
        leave_status = request.POST['leave_status']

        # Gernal Table Information (tb_leave)
        table_form_values_1 = """INSERT INTO tb_leave (leave_employee_name,leave_designation_status,leave_type,leave_from,leave_to,leave_days,leave_reason,leave_status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

        record_1 =(leave_employee_name,leave_designation_status,leave_type,leave_from,leave_to,leave_days,leave_reason,leave_status)
        
        cur.execute(table_form_values_1, record_1)
        conn.commit()
        return redirect("/employees/leave_table/")

    return render(request,'leave/leaves_form.html')


def leave_table(request):
    # Table tb_leave
    cur.execute("SELECT * FROM `tb_leave`")
    data = cur.fetchall()
    
    return render(request,"leave/leaves_tableview.html",{'tb_cateory_3_data': data})

def leave_edit(request,id):
     # Table tb_leave
    cur.execute("SELECT * FROM `tb_leave` WHERE `id` = {}".format(id))
    data = cur.fetchall()
    
    return render(request,"leave/leaves_edit.html",{'tb_cateory_3_data': data})

def leave_update(request):
    if request.method == 'POST':
        id_index_3 = request.POST['id_index_3']
        leave_employee_name = request.POST['leave_employee_name']
        leave_designation_status = request.POST['leave_designation_status']
        leave_type = request.POST['leave_type']
        leave_from = request.POST['leave_from']
        leave_to = request.POST['leave_to']
        leave_days = request.POST['leave_days']
        leave_reason = request.POST['leave_reason']
        leave_status = request.POST['leave_status']
        # Gernal Table Information (tb_leave)
        table_form_values_1 = """UPDATE tb_leave SET leave_employee_name=%s, leave_designation_status=%s, leave_type=%s, leave_from=%s, leave_to=%s, leave_days=%s, leave_reason=%s, leave_status=%s WHERE id=%s"""

        record_1 =(leave_employee_name,leave_designation_status,leave_type,leave_from,leave_to,leave_days,leave_reason,leave_status,id_index_3)

        cur.execute(table_form_values_1, record_1)
        
        conn.commit()
    return redirect("/employees/leave_table/")

def leave_delete(request,id):
    # Table tb_leave
    data = "DELETE FROM `tb_leave` WHERE `id` = {}".format(id)
    cur.execute(data)

    conn.commit()
    return redirect("/employees/leave_table/")

# ============================================  LEAVE PYTHON END ================================================= #






# ============================================  EMPLOYEE PYTHON START ================================================= #


def employee_form_add(request):        
    if request.method == 'POST':
        your_name = request.POST['your_name']
        father_name = request.POST['father_name']
        gender = request.POST['gender']
        age = request.POST['age']
        height_weight = request.POST['height_weight']
        date_of_birth = request.POST['date_of_birth']
        marital_status = request.POST['marital_status']
        languages_known = request.POST['languages_known']
        country = request.POST['country']
        present_address = request.POST['present_address']
        permanent_address = request.POST['permanent_address']
        email = request.POST['email']
        phone = request.POST['phone']
        title = request.POST['title']
        employee_id = request.POST['employee_id']
        date_of_appointment = request.POST['date_of_appointment']
        date_of_confirmation = request.POST['date_of_confirmation']
        date_of_joining = request.POST['date_of_joining']
        department_posted = request.POST['department_posted']
        monthly_contribution = request.POST['monthly_contribution']
        education_qualification = request.POST['education_qualification']
        professional_qualification = request.POST['professional_qualification']
        
        # Gernal Table Information (tb_cateory_3)
        table_form_values_1 = """INSERT INTO tb_cateory_3 (your_name,father_name,gender,age,height_weight,date_of_birth,marital_status,languages_known,country,present_address,permanent_address,email,phone) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        record_1 =(your_name,father_name,gender,age,height_weight,date_of_birth,marital_status,languages_known,country,present_address,permanent_address,email,phone)
        
        cur.execute(table_form_values_1, record_1)
        
        
        # Job Table Information (tb_cateory_4)
        table_form_values_2 = """INSERT INTO tb_cateory_4 (title,employee_id,date_of_appointment,date_of_confirmation,date_of_joining,department_posted,monthly_contribution,education_qualification,professional_qualification) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        record_2 =(title,employee_id,date_of_appointment,date_of_confirmation,date_of_joining,department_posted,monthly_contribution,education_qualification,professional_qualification)
        
        cur.execute(table_form_values_2, record_2)

        conn.commit()
        return redirect("/employees/employee_table_views/")
    
    return render(request,'employee_form.html')



def employee_table_views(request):
    # Table tb_cateory_3
    cur.execute("SELECT * FROM `tb_cateory_3`")
    data_3 = cur.fetchall()

    # Table tb_cateory_4
    cur.execute("SELECT * FROM `tb_cateory_4`")
    data_4 = cur.fetchall()
    
    return render(request,"employee_tableview.html",{'tb_cateory_3_data': data_3,'tb_cateory_4_data': data_4})



def employee_table_delete(request):
    if request.method == 'POST':
        employee_id_delete = request.POST['id']
    
        # Table tb_cateory_3
        table_form_values_3 = "DELETE FROM `tb_cateory_3` WHERE `id` = {}".format(employee_id_delete)
        cur.execute(table_form_values_3)
        
        # Table tb_cateory_4
        table_form_values_4 = "DELETE FROM `tb_cateory_4` WHERE `id` = {}".format(employee_id_delete)
        cur.execute(table_form_values_4)

        conn.commit()
        return redirect("/employees/employee_table_views/")
    
    return render(request,'employee_delete.html')

def employee_table_delete_view(request,id):
    # Table tb_cateory_3
    table_form_values_3 = "DELETE FROM `tb_cateory_3` WHERE `id` = {}".format(id)
    cur.execute(table_form_values_3)
    
    # Table tb_cateory_4
    table_form_values_4 = "DELETE FROM `tb_cateory_4` WHERE `id` = {}".format(id)
    cur.execute(table_form_values_4)

    conn.commit()
    return redirect("/employees/employee_table_views/")


def employee_table_edit_update(request):
    return render(request,"employee_update.html")


def employee_table_edit(request,id):
     # Table tb_cateory_3
#    id = 2
    cur.execute("SELECT * FROM `tb_cateory_3` WHERE `id` = {}".format(id))
    data_3 = cur.fetchall()

    # Table tb_cateory_4
    cur.execute("SELECT * FROM `tb_cateory_4` WHERE `id` = {}".format(id))
    data_4 = cur.fetchall()
    
    return render(request,"employee_edit.html",{'tb_cateory_3_data': data_3,'tb_cateory_4_data': data_4})


def employee_table_update(request):
    if request.method == 'POST':
        id_index_3 = request.POST['id_index_3']
        id_index_4 = request.POST['id_index_4']
        your_name = request.POST['your_name']
        father_name = request.POST['father_name']
        gender = request.POST['gender']
        age = request.POST['age']
        height_weight = request.POST['height_weight']
        date_of_birth = request.POST['date_of_birth']
        marital_status = request.POST['marital_status']
        languages_known = request.POST['languages_known']
        country = request.POST['country']
        present_address = request.POST['present_address']
        permanent_address = request.POST['permanent_address']
        email = request.POST['email']
        phone = request.POST['phone']
        title = request.POST['title']
        employee_id = request.POST['employee_id']
        date_of_appointment = request.POST['date_of_appointment']
        date_of_confirmation = request.POST['date_of_confirmation']
        date_of_joining = request.POST['date_of_joining']
        department_posted = request.POST['department_posted']
        monthly_contribution = request.POST['monthly_contribution']
        education_qualification = request.POST['education_qualification']
        professional_qualification = request.POST['professional_qualification']

        # Gernal Table Information (tb_cateory_3)
        table_form_values_1 = """UPDATE tb_cateory_3 SET your_name=%s, father_name=%s, gender=%s, age=%s, height_weight=%s, date_of_birth=%s, marital_status=%s, languages_known=%s, country=%s, present_address=%s, permanent_address=%s, email=%s, phone=%s WHERE id=%s"""

        record_1 =(your_name,father_name,gender,age,height_weight,date_of_birth,marital_status,languages_known,country,present_address,permanent_address,email,phone,id_index_3)

        cur.execute(table_form_values_1, record_1)


        # Job Table Information (tb_cateory_4)                
        table_form_values_2 = """UPDATE tb_cateory_4  SET title=%s,employee_id=%s,date_of_appointment=%s,date_of_confirmation=%s,date_of_joining=%s,department_posted=%s,monthly_contribution=%s,education_qualification=%s,professional_qualification=%s WHERE id=%s"""

        record_2 =(title,employee_id,date_of_appointment,date_of_confirmation,date_of_joining,department_posted,monthly_contribution,education_qualification,professional_qualification,id_index_4)

        cur.execute(table_form_values_2, record_2)
        
        conn.commit()
    return redirect("/employees/employee_table_views/")



# ============================================  EMPLOYEE PYTHON END ================================================= #
