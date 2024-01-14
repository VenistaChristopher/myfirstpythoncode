# ============== BRMM Bankside Rakaia Motorkhana Mavens ADMIN DATA ==============
# Student Name: Nadar Venista Christopher
# Student ID : 1159129
# ===============================================================================
 
import datetime

col_customers = {'ID':int,'Name':str,'Telephone':str,'e-mail':str}
db_customers = {563:{'details':['Simon Smith','0244881901','simon@smith.nz'],'jobs':{datetime.date(2022,2,11):[(45,),(),45.78,True]}},241:{'details':['Jasmine Holiday','0274823801','jaz@onholiday.co.nz'],'jobs':{datetime.date(2022,9,15):[(57,56),(5,6),631.88,False],datetime.date(2022,11,5):[(),(6,),78.09,False]}}}
col_services = {'ID':int,'Name':str,'Cost':float}
db_services = {45:['Sandblast',45.78],56:['Small Dent Repair',55.32],57:['Large Dent Repair',150.67]}
col_parts = {'ID':int,'Name':str,'Cost':float}
db_parts = {5:['Front Wing',347.80],6:['Headlight',78.09]}
col_bills = {'Customer':str,'Telephone':str,'Date':datetime.date,'Amount':float}


