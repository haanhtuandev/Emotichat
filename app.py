import streamlit as st
import cv2
import numpy as np

def main():
    st.title("Emotion Detection App")
    
    col1, col2 = st.columns(2)
    
    with col1:

        if 'camera_on' not in st.session_state:
            st.session_state.camera_on = True

        # Create a button to toggle camera
        if st.button('Toggle camera'):
            st.session_state.camera_on = not st.session_state.camera_on

        # Display current camera state
        st.write(f"Camera is {'ON' if st.session_state.camera_on else 'OFF'}")

        # Only show camera feed if camera is on
        if st.session_state.camera_on:
            camera = st.camera_input("Camera Feed")
            
            if camera:
                img = cv2.imdecode(np.frombuffer(camera.getvalue(), np.uint8), cv2.IMREAD_COLOR)
                # Add ML model predictions here
                age = "25"
                gender = "Female"
                emotion = "Happy"
                
                # Display predictions
                st.write(f"Age: {age}")
                st.write(f"Gender: {gender}")
                st.write(f"Emotion: {emotion}")
        
    with col2:
        st.header("Chat Interface")
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        if prompt := st.chat_input("What's on your mind?"):
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            response = f"I see you're feeling happy! How can I help?"
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()