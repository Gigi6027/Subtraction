import streamlit as st

st.title('Subtraction of two numbers')
st.subheader('Gigi')


num1 = st.text_input('Enter first number : ')
num2 = st.text_input('Enter second number : ')

btn = st.button('Calculate')



if btn:
    if num1 and num2:
        try:
            num1 = int(num1)
            num2 = int(num2)
            st.markdown(f"## {num1} - {num2} = {float(num1) - float(num2)}")
        except ZeroDivisionError:
            st.error("Do not divide by zero !!!")
        except ValueError:
            st.error("Enter numbers only !!!")
    else:
        st.error('Please enter numbers')
