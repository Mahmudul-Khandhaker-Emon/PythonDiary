import streamlit as st



#The Section of Title
st.title("Welcome to You ,I Love You Baby")

#The Section of SubHeader
st.subheader("Hello Mr. Welcome our homepage")
st.subheader("Write Your Information Here:")

#Input the Name text here

st.text_input("Write Your Name:",key="Name")

# Show the User Input text
if st.session_state.Name:
     st.write("Your Name is:",st.session_state.Name)


#Input Your Age here
 
age_input=st.text_input("Write Your Age:",key="Age_text")

#Show the User Input Age
if age_input:
     
    if age_input.isdigit():
        st.session_state.Age=int(age_input)
        st.write("Your Age is :",st.session_state.Age)
    else:
        st.warning("Please to write a write number Baby")
    


#Input the User Profession

profession_input=st.radio("Select Your Profession:",["Student","Engineer","Doctor","Scientists","Researcher","Developer","Poet"])

st.write(" ")


#Submit Button Section

if st.button("Generate My Profile 😊"):
   st.balloons()

   st.success("Generated My Profile Successfully   😊 Baby")

#To Create Profile Summery Box 
#Show the Name:
   st.markdown("----")
   st.markdown("Your Generated Profile:")

   if st.session_state.Name:
       st.write(f"**Name:** {st.session_state.Name}")
   else:
       st.write("Not Provided!")

#Show the Age
   if age_input and age_input.isdigit():
       st.write(f"**Age:** {age_input}")
   else:
       st.write("**Age:** Not Provided " )

#Show the Profession 
   st.write(f"**Profession:** {profession_input}")