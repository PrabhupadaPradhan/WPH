import streamlit as st
import os
import pyperclip as pc
os.system('cmd /c netsh wlan show profile | clip')
a = pc.paste()
b = a[(int(a.index("User profiles")) + 28):]
list_1 = b[29:-5].split('\r\n    All User Profile     : ')
list_2 = []
for i in list_1:
    os.system('cmd /c netsh wlan show profile name=' + i + ' key=clear | clip')
    c = pc.paste()
    try:
        s = c[(int(c.index("Key Content")) + 25):int(c.index("\r\n\r\nCost"))]
    except:
    	s = "N.A."
    list_2.append(s)
    st.write(i, "   ::   ", s)
list_3 = list(zip(list_1, list_2))