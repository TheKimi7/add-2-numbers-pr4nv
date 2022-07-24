from tkinter import Y
from numpy import float_
import streamlit as st
import streamlit as st

st.title("Welcome to my Streamlit Application!")
st.subheader("This is an application that adds the given 2 numbers and displays the sum. I have done this as a part of my Graded Assignment 8")

num1 = st.number_input(label="Enter the first number: ", min_value=0, value=0, step=1, format='%d')
num2 = st.number_input(label="Enter the second number: ", min_value=0, value=0, step=1, format='%d')

def addn(x,y):
    s = x+y
    return s
s = addn(num1,num2)
if st.button("Add"):
    st.write(f"The sum of the two numbers is: {s}")
