# Copyright 2021 Allah
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views

app_name = 'employee'

urlpatterns = [
    path('employee/',views.employee_index_view,name='employee_index_view'),
    path('employee_form_add/',views.employee_form_add,name='form'),
    path('employee_table_views/',views.employee_table_views,name='table'),
    path('employee_table_delete/',views.employee_table_delete,name='delete'),
    path('employee_table_delete_view/<int:id>',views.employee_table_delete_view,name='employee_table_delete_view'),
    path('employee_table_edit_update/',views.employee_table_edit_update,name='edit_delete'),
    path('employee_table_edit/<int:id>',views.employee_table_edit,name='edit'),
    path('employee_table_update/',views.employee_table_update,name='update'),

    path('holiday/',views.holiday_index_view,name="holiday_index_view"),
    path('holiday_form/',views.holiday_form,name="holiday_form"),
    path('holiday_table/',views.holiday_table,name="holiday_table"),
    path('holiday_edit/<int:id>',views.holiday_edit,name="holiday_edit"),
    path('holiday_update/',views.holiday_update,name='holiday_update'),
    path('holiday_delete/<int:id>',views.holiday_delete,name="holiday_delete"),
    
    
    path('department/',views.department_index_view,name="department_index_view"),
    path('department_form/',views.department_form,name="department_form"),
    path('department_table/',views.department_table,name="department_table"),
    path('department_edit/<int:id>',views.department_edit,name="department_edit"),
    path('department_update/',views.department_update,name='department_update'),
    path('department_delete/<int:id>',views.department_delete,name="department_delete"),

    path('designation/',views.designation_index_view,name="designation_index_view"),
    path('designation_form/',views.designation_form,name="designation_form"),
    path('designation_table/',views.designation_table,name="designation_table"),
    path('designation_edit/<int:id>',views.designation_edit,name="designation_edit"),
    path('designation_update/',views.designation_update,name='designation_update'),
    path('designation_delete/<int:id>',views.designation_delete,name="designation_delete"),


    path('timesheet/',views.timesheet_index_view,name="timesheet_index_view"),
    path('timesheet_form/',views.timesheet_form,name="timesheet_form"),
    path('timesheet_table/',views.timesheet_table,name="timesheet_table"),
    path('timesheet_edit/<int:id>',views.timesheet_edit,name="timesheet_edit"),
    path('timesheet_update/',views.timesheet_update,name='timesheet_update'),
    path('timesheet_delete/<int:id>',views.timesheet_delete,name="timesheet_delete"),


    path('leave/',views.leave_index_view,name="leave_index_view"),
    path('leave_form/',views.leave_form,name="leave_form"),
    path('leave_table/',views.leave_table,name="leave_table"),
    path('leave_edit/<int:id>',views.leave_edit,name="leave_edit"),
    path('leave_update/',views.leave_update,name='leave_update'),
    path('leave_delete/<int:id>',views.leave_delete,name="leave_delete"),


]
