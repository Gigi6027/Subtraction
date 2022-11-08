import streamlit as st

st.title('Railway Reservation System PES1UG20CS252')
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
        except ValueError:
            st.error("Enter numbers only !!!")
    else:
        st.error('Please enter numbers')
