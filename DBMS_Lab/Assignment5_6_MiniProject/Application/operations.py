import pandas as pd
import streamlit as st
from database import *

#-------------------------------ADD operations-------------------------------------------------

def cu_create():
    col1, col2, col3 = st.columns(3)
    with col1:
        c_id = st.number_input("Customer ID: ",min_value = 2000, max_value = 2999)
        cf_name = st.text_input("First Name: ")
        cl_name = st.text_input("Last Name: ")
        c_qual = st.text_input("Qualification: ")
        c_phone = st.text_input("Phone: ")
        b_bank = st.text_input("Bank: ")

    with col2:
        c_address = st.text_input("Address: ")
        c_locate = st.text_input("Locality: ")
        c_city = st.text_input("City: ")
        c_email = st.text_input("Email: ")
        c.execute("SELECT E_ID FROM Employee")
        emp_data = c.fetchall()
        e_data = []
        for i in emp_data:
            for j in i:
                e_data.append(int(j))
        c_emp = st.selectbox("Serving Employee", e_data)
        b_tid = st.text_input("Transaction ID: ")
        b_id = c_id + 7000
    
    with col3:
        c.execute("SELECT Item_ID FROM Items")
        data = c.fetchall()
        item_data = []
        for i in data:
            for j in i:
                item_data.append(int(j))
        c_item_id = st.selectbox("Item", item_data)
        c.execute("SELECT Item_Name,Brand,Size FROM Item_Category WHERE Item_ID ={}".format(c_item_id))
        it_n = c.fetchall()
        in_data = []
        for i in it_n:
            for j in i:
                in_data.append((j))
        in_data = in_data[0] + " :: "+in_data[1] + " :: " + in_data[2]
        st.write("Item Name :: Item Brand :: Item Size")
        st.markdown('`{}`'.format(in_data))

        c_qty = st.number_input("Quantity: ",min_value=1, max_value=50)
        c.execute("SELECT Price FROM Items WHERE Item_ID = {}".format(c_item_id))
        it_da = c.fetchall()
        price_data = []
        for i in it_da:
            for j in i:
                price_data.append(float(j))
        c_price = price_data[0]
        st.markdown("Price: ")
        st.write(c_price)
        c_dop = st.date_input("Purchase Date:")
        st.write("Total item order value")
        c_total = st.write(c_price * c_qty)
        c_total = c_price * c_qty
    
    c.execute("SELECT sum(O.O_Amount) AS Total_Bill FROM ORDERS AS O WHERE O.C_ID = {} ORDER BY sum(O.O_Amount) DESC".format(c_id))
    b_amt = c.fetchall()
    price_data = []
    for i in b_amt:
            for j in i:
                price_data.append((j))
    b_amount = price_data[0]
    with col3:
        st.markdown("Total Bill Amount: ")
        st.write(b_amount)

    with col1:
        if st.button("Add CUSTOMER"):
                cu_add_data(c_id,cf_name,cl_name,c_qual,c_address,c_locate,c_city,c_email,c_phone,c_dop,c_emp)
                st.success("Successfully added CUSTOMER: {}".format(cf_name))
    with col2:
        if st.button("Add ORDERS"):
                cu_orders_add_data(c_id,c_item_id,c_price,c_qty,c_dop,c_total)
                st.success("Successfully added ORDERS: {}".format(c_item_id))
    
    if st.button("GENERATE BILL"):
        cu_bill(b_id,b_bank,c_dop,b_tid,b_amount,c_id)
        st.success("Successfully generated BILL :: {}".format(b_id))
        view_bill(c_id)
        st.success("Successfully printed BILL :: {}".format(b_id))

def em_create():
    col1, col2 = st.columns(2)
    with col1:
        e_id = st.number_input("Employee ID: ",min_value = 1000,max_value = 1999)
        e_fn = st.text_input("First Name: ")
        e_ln = st.text_input("Last Name: ")
        e_address = st.text_input("Address: ")
        e_phone = st.text_input("Phone: ")
    with col2:
        c.execute("SELECT DISTINCT MGR_ID FROM EMPLOYEE WHERE MGR_ID <> 0")
        data = c.fetchall()
        mgr_data = []
        for i in data:
            for j in i:
                mgr_data.append(int(j))
        emgr_id = st.selectbox("Manager", mgr_data)
        e_gender = st.radio("Gender",('M', 'F'))
        e_salary = st.number_input("Salary: ")
        e_dob = st.date_input("Date of Birth:")
    
    if st.button("Add Employee"):
        em_add_data(e_id,e_fn,e_ln,emgr_id,e_gender,e_salary,e_dob,e_address,e_phone)
        st.success("Successfully added EMPLOYEE: {}".format(e_fn))

def it_create():
    col1, col2, col3 = st.columns(3)
    with col1:
        i_id = st.number_input("ITEM ID: ",min_value = 4000,max_value = 4999)
        i_name = st.text_input("Name: ")
        i_price = st.number_input("Price: ")
        
    with col2:
        i_brand = st.text_input("Brand: ")
        i_colour = st.text_input("Colour: ")
        i_size = st.selectbox("Size", ["NA","28","30","32","34","36","38","40","42","44","46","48","50","52","54","56","58","60","M","L","XL","XXL","XXXL"])
    with col3:
        i_gender = st.radio("Gender",('M', 'F'))
        i_quantity = st.number_input("Quantity: ",min_value = 1, max_value = 50)
        c.execute("SELECT STORE_ID FROM STORE")
        data = c.fetchall()
        store_data = []
        for i in data:
            for j in i:
                store_data.append(int(j))
        st_id = st.selectbox("STORE-ID",store_data)

    
    if st.button("Add ITEM-STOCK"):
        it_add_data(i_id,i_name,i_price,i_gender,i_brand,i_colour,i_size,i_quantity,st_id)
        st.success("Successfully added ITEM TO STORE: {}".format(i_id))

def su_create():
    col1, col2 = st.columns(2)
    with col1:
        su_id = st.number_input("Supplier ID: ",min_value = 7000,max_value = 7999)
        su_name = st.text_input("Name: ")
        su_address = st.text_input("Address: ")
        c.execute("SELECT STORE_ID FROM STORE")
        data = c.fetchall()
        store_data = []
        for i in data:
            for j in i:
                store_data.append(int(j))

        su_st_id = st.selectbox("STORE-ID",store_data)
    with col2:
        sh_id = st.number_input("Ship ID: ",min_value = 8000,max_value = 8999)
        sh_cost = st.number_input("Shipping Cost: ")
        sh_date = st.date_input("Date of Shipment: ")
        sh_mode = st.selectbox("Mode of Travel", ["Roadways","Railways","Airways","Waterways"])

        
    
    if st.button("Add SUPPLIER - SHIP"):
        su_add_data(su_id,su_name,su_address,sh_id,sh_cost,sh_mode,sh_date,su_st_id)
        st.success("Successfully added SUPPLIER-SHIP: {}".format(su_name))

#-------------------------------------READ----------------------------------------------------

def cu_read():
    result = cu_view_cust_data()
    df = pd.DataFrame(result, columns = ['C_ID', 'First_Name','Last Name','Qualification','Address','Locality','City','Email','Phone_NO'])
    st.dataframe(df)

def em_read():
    result = em_view_all_data()
    df = pd.DataFrame(result, columns = ['E_ID', 'First_Name','Last_Name','MGR_ID','GENDER','SALARY','DOB','ADDRESS','Phone_NO'])
    st.dataframe(df)

def it_read():
    result = it_view_all_data()
    df = pd.DataFrame(result, columns = ['Item_ID', 'Item_Name','Gender','Brand','Colour','Size','Quantity','Store_ID','Store_Name'])
    st.dataframe(df)

def su_read():
    result = su_view_all_data()
    df = pd.DataFrame(result, columns = ['Supp_ID','Name','Address','Ship_ID','Cost_of_shipping','Mode_of_Travelling','Date_Of_Shipment','Store_ID'])
    st.dataframe(df)


#--------------------------------------------UPDATE----------------------------------------------------

def cu_update():
    list_of_customers = [i[0] for i in cu_view_only()]
    selected_cus = st.selectbox("Customer to Edit", list_of_customers)
    selected_result = cu_get(selected_cus)

    if selected_result:
        c_id = selected_result[0][0]
        c_fn = selected_result[0][1]
        c_ln = selected_result[0][2]
        c_qual = selected_result[0][3]
        c_address = selected_result[0][4]
        c_locate = selected_result[0][5]
        c_city = selected_result[0][6]
        c_email = selected_result[0][7]
        c_phone = selected_result[0][8]


    # Layout of Create

    col1, col2 = st.columns(2)
    with col1:
        new_c_id = st.number_input("Customer ID: ",max_value = 2999,value = c_id)
        new_c_fn = st.text_input("First Name: ",value = c_fn)
        new_c_ln = st.text_input("Last Name: ",value = c_ln)
        new_c_qual = st.text_input("Qualification: ",value = c_qual)
        new_c_phone = st.text_input("Phone: ",value = c_phone)

    with col2:
        new_c_address = st.text_input("Address: ",value = c_address)
        new_c_locate = st.text_input("Locality: ",value = c_locate)
        new_c_city = st.text_input("City: ",value = c_city)
        new_c_email = st.text_input("Email: ",value = c_email)
        st.markdown("\n")
        st.markdown("\n")
        
        if st.button("Update Customer Details"):
            cu_edit(new_c_id,new_c_fn,new_c_ln,new_c_qual, new_c_address, new_c_locate, new_c_city, new_c_email,new_c_phone,c_id,c_fn,c_ln, c_qual, c_address, c_locate, c_city, c_email,c_phone)
            st.success("Successfully updated:: {} to :: {} and other details".format(c_fn, new_c_fn))


def em_update():
    list_of_trains = [i[0] for i in em_view_only()]
    selected_train = st.selectbox("Employee name to Edit", list_of_trains)
    selected_result = em_get(selected_train)

    if selected_result:
        e_id = selected_result[0][0]
        e_fn = selected_result[0][1]
        e_ln = selected_result[0][2]
        emgr_id = selected_result[0][3]
        e_gender = selected_result[0][4]
        e_salary = selected_result[0][5]
        e_dob = selected_result[0][6]
        e_address = selected_result[0][7]
        e_phone = selected_result[0][8]

        # Layout of Create

        col1, col2 = st.columns(2)
    with col1:
        new_e_id = st.number_input("Employee ID: ",min_value = 1000, max_value = 1999,value = e_id)
        new_e_fn = st.text_input("First Name: ",value = e_fn)
        new_e_ln = st.text_input("Last Name: ",value = e_ln)
        new_e_address = st.text_input("Address: ",value = e_address)
        new_e_phone = st.text_input("Phone: ",value = e_phone)
    with col2:
        c.execute("SELECT DISTINCT MGR_ID FROM EMPLOYEE WHERE MGR_ID <> 0")
        data = c.fetchall()
        mgr_data = []
        for i in data:
            for j in i:
                mgr_data.append(int(j))
        new_emgr_id = st.selectbox("Manager", mgr_data)
        new_e_gender = st.radio("Gender",('M', 'F'))
        new_e_salary = st.number_input("Salary: ",value = e_salary)
        new_e_dob = st.date_input("Date of Birth:",value = e_dob)
        st.markdown("\n")

        if st.button("Update Employee"):
            em_edit(new_e_id,new_e_fn,new_e_ln,new_emgr_id,new_e_gender,new_e_salary,new_e_dob,new_e_address,new_e_phone,e_id,e_fn,e_ln,emgr_id,e_gender,e_salary,e_dob,e_address,e_phone)
            st.success("Successfully updated :: {} to :: {} and other details".format(e_fn, new_e_fn))


def it_update():
    list_of_trains = [i[0] for i in it_view_only()]
    selected_train = st.selectbox("Items in Store to Edit", list_of_trains)
    selected_result = it_get(selected_train)

    if selected_result:
        i_id = selected_result[0][0]
        i_name = selected_result[0][1]
        i_price = selected_result[0][2]
        i_gender = selected_result[0][3]
        i_brand = selected_result[0][4]
        i_colour = selected_result[0][5]
        i_size = selected_result[0][6]
        i_quantity = selected_result[0][7]
        st_id = selected_result[0][8]


        # Layout of Create

        col1, col2, col3 = st.columns(3)
    with col1:
        new_i_id = st.number_input("ITEM ID: ",min_value = 4000,max_value = 4999,value = i_id)
        new_i_name = st.text_input("Name: ",value = i_name)
        new_i_price = st.number_input("Price: ",value = i_price)
        
    with col2:
        new_i_brand = st.text_input("Brand: ",value = i_brand)
        new_i_colour = st.text_input("Colour: ",value = i_colour)
        new_i_size = st.selectbox("Size", ["NA","28","30","32","34","36","38","40","42","44","46","48","50","52","54","56","58","60","M","L","XL","XXL","XXXL"])
    
    with col3:
        new_i_gender = st.radio("Gender",('M', 'F'))
        new_i_quantity = st.number_input("Quantity: ",min_value = 1, max_value = 50,value = i_quantity)
        new_st_id = st.selectbox("STORE-ID",[6001,6002,6003,6004])

    with col1:
        if st.button("Update Item in Store"):
            it_edit(new_i_id,new_i_name,new_i_price,new_i_brand,new_i_colour,new_i_size,new_i_gender,new_i_quantity,new_st_id,i_id,i_name,i_price,i_brand,i_colour,i_size,i_gender,i_quantity,st_id)
            st.success("Successfully updated :: {} to :: {} and other details".format(i_name, new_i_name))


def su_update():
    list_of_sup = [i[0] for i in su_view_only()]
    selected_sup = st.selectbox("Supplier/Ship to Edit", list_of_sup)
    selected_result = su_get(selected_sup)

    if selected_result:
        su_id = selected_result[0][0]
        su_name = selected_result[0][1]
        su_address = selected_result[0][2]
        sh_id = selected_result[0][3]
        sh_cost = selected_result[0][4]
        sh_mode = selected_result[0][5]
        sh_date = selected_result[0][6]
        su_st_id = selected_result[0][7]

        # Layout of Create

        col1, col2 = st.columns(2)
    with col1:
        new_su_id = st.number_input("Supplier ID: ",min_value = 7000,max_value = 7999,value = su_id)
        new_su_name = st.text_input("Name: ",value = su_name)
        new_su_address = st.text_input("Address: ",value = su_address)
        c.execute("SELECT STORE_ID FROM STORE")
        data = c.fetchall()
        store_data = []
        for i in data:
            for j in i:
                #j = j.replace(",","")
                store_data.append(int(j))

        new_su_st_id = st.selectbox("STORE-ID",store_data)

    with col2:
        new_sh_id = st.number_input("Ship ID: ",min_value = 8000,max_value = 8999,value = sh_id)
        new_sh_cost = st.number_input("Shipping Cost: ",value = sh_cost)
        new_sh_date = st.date_input("Date of Shipment: ",value = sh_date)
        new_sh_mode = st.selectbox("Mode of Travel", ["Roadways","Railways","Airways","Waterways"])

    with col1:
        if st.button("Update SUPPLIER - SHIP"):
            su_edit(new_su_id,new_su_name,new_su_address,new_sh_id,new_sh_cost,new_sh_mode,new_sh_date,new_su_st_id,su_id,su_name,su_address,sh_id,sh_cost,sh_mode,sh_date,su_st_id)
            st.success("Successfully updated :: {} to :: {} and other details".format(su_name, new_su_name))    


#--------------------------------------DELETE------------------------------------
def cu_delete():
    list_of_customers = [i[0] for i in cu_view_only()]
    selected_customers = st.selectbox("Customer to Delete", list_of_customers)
    st.warning("Do you want to delete :: {}".format(selected_customers))
    if st.button("Delete Customer"):
        cu_delete_data(selected_customers)
        st.success("Customer has been deleted successfully")

def em_delete():
    list_of_emp = [i[0] for i in em_view_only()]
    selected_emp = st.selectbox("Employee to Delete", list_of_emp)
    st.warning("Do you want to delete :: {}".format(selected_emp))
    if st.button("Delete Employee"):
        em_delete_data(selected_emp)
        st.success("Employee has been deleted successfully")

def it_delete():
    list_of_items = [i[0] for i in it_view_only()]
    selected_items = st.selectbox("Item to Delete", list_of_items)
    st.warning("Do you want to delete :: {}".format(selected_items))
    if st.button("Delete Item from Store"):
        it_delete_data(selected_items)
        st.success("Item in store has been deleted successfully")

def su_delete():
    list_of_sup = [i[0] for i in su_view_only()]
    selected_sup = st.selectbox("Supplier to Delete", list_of_sup)
    st.warning("Do you want to delete :: {}".format(selected_sup))
    if st.button("Delete Supplier"):
        su_delete_data(selected_sup)
        st.success("Supplier has been deleted successfully")