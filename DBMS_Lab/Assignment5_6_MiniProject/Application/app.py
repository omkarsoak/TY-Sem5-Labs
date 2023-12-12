# Importing pakages
import streamlit as st
from streamlit_option_menu import option_menu
from database import *
from operations import *


def main():
    st.set_page_config(
        page_title = "Apparel Store Management System",
        layout = "wide",
        initial_sidebar_state = "collapsed",
    )

    # Centered title using HTML and CSS
    st.markdown("""
        <h1 style='text-align: center;'>Apparel Store Management System</h1>
    """, unsafe_allow_html=True)

    selected = option_menu(
                menu_title=None,  # required
                options=["HOME", "CUSTOMER","EMPLOYEE","ITEMS","SUPPLIER"],  # required
                icons=["house","person-circle","people","box","truck"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
                orientation="horizontal",
            )
            
    if selected == "HOME":
        # Centered title using HTML and CSS
        st.markdown("""
            <h2 style='text-align: center;'>Welcome to the Home Page!</h2>
        """, unsafe_allow_html=True)
        st.image('Header.jpg', caption='Centered Image', use_column_width=True)
        st.write("Welcome to the Store Management System! Use the navigation menu to explore different functionalities.")

    if selected == "CUSTOMER":
        option = option_menu(
            menu_title=None,  # required
            options=["ADD", "VIEW", "EDIT", "REMOVE"],  # required
            icons=["plus-circle","eye","pencil","trash"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )

        cu_create_table()
        if option == "ADD":
            st.subheader("Enter CUSTOMER Details :")
            cu_create()

        elif option == "VIEW":
            st.subheader("View added CUSTOMER :")
            cu_read()

        elif option == "EDIT":
            st.subheader("Update CUSTOMER Details :")
            cu_update()

        elif option == "REMOVE":
            st.subheader("Delete CUSTOMER Details :")
            cu_delete()

        else:
            st.subheader("About tasks")

    if selected == "EMPLOYEE":
        option = option_menu(
            menu_title=None,  # required
            options=["ADD", "VIEW", "EDIT", "REMOVE"],  # required
            icons=["plus-circle","eye","pencil","trash"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        em_create_table()
        if option == "ADD":
            st.subheader("Enter EMPLOYEE Details :")
            em_create()

        elif option == "VIEW":
            st.subheader("View added EMPLOYEE :")
            em_read()

        elif option == "EDIT":
            st.subheader("Update EMPLOYEE Details :")
            em_update()

        elif option == "REMOVE":
            st.subheader("Delete EMPLOYEE Details :")
            em_delete()

        else:
            st.subheader("About tasks")

    if selected == "ITEMS":
        option = option_menu(
            menu_title=None,  # required
            options=["ADD", "VIEW", "EDIT", "REMOVE"],  # required
            icons=["plus-circle","eye","pencil","trash"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        it_create_table()
        if option == "ADD":
            st.subheader("Enter ITEM Details :")
            it_create()

        elif option == "VIEW":
            st.subheader("View added ITEMS :")
            it_read()

        elif option == "EDIT":
            st.subheader("Update ITEM Details :")
            it_update()

        elif option == "REMOVE":
            st.subheader("Delete ITEM Details :")
            it_delete()

        else:
            st.subheader("About tasks")

    if selected == "SUPPLIER":
        option = option_menu(
            menu_title=None,  # required
            options=["ADD", "VIEW", "EDIT", "REMOVE"],  # required
            icons=["plus-circle","eye","pencil","trash"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        su_create_table()
        if option == "ADD":
            st.subheader("Enter SUPPLIER AND SHIPPING Details :")
            su_create()

        elif option == "VIEW":
            st.subheader("View added SUPPLIER :")
            su_read()

        elif option == "EDIT":
            st.subheader("Update SUPPLIER AND SHIPPING Details :")
            su_update()

        elif option == "REMOVE":
            st.subheader("Delete SUPPLIER Details :")
            su_delete()

        else:
            st.subheader("About tasks")


if __name__ == '__main__':
    main()