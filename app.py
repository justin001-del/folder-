import streamlit as st 
import os
import shutil


with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.title("Folder")
st.set_page_config(page_title="Folder Organiser", page_icon="📂")


fol=st.text_input("Required Folder to Organise",placeholder="Defaulted to downloads")

if fol:
    
    paths=os.path.expanduser(f"~/{fol}")    
else:
    paths=os.path.expanduser("~/Downloads")


try:
    s=os.listdir(paths)
    with st.expander("Content"):
        st.write(s)
except Exception as e :    
    st.warning(f"{e}")
    st.stop()
  
files=[]
for things in s:
    path_file=os.path.join(paths,things)
    result= os.path.isfile(path_file)
    folder=["jpeg","jpg","png"]
    folder_1=["txt","csv"]
    
    if result:
        
        split=things.split('.')
        c=split[0],split[-1]
        files.append(c)
       
        
        
        if split[-1] in folder_1:
            pathtxt=os.path.join(paths,"all_txt")
            os.makedirs(pathtxt,exist_ok=True)
            src=path_file
            dst=pathtxt
            try:
                shutil.move(src,dst)
            except Exception as e:
                with st.expander("ERROR"):
                    st.warning(f"{e}")
                    st.write("if the error appears to be destination error then theres a clone of a file ")
        if split[-1]=="py":
            pathpy=os.path.join(paths,"all_py")
            os.makedirs(pathpy,exist_ok=True)
            src=path_file
            dst=pathpy
            try:
                shutil.move(src,dst)
            except Exception as e:
                with st.expander("ERROR"):
                    st.warning(f"{e}")
                    st.write("if the error appears to be destination error then theres a clone of a file ")

        if split[-1] in folder:
            pathpic=os.path.join(paths,"all_pic")
            os.makedirs(pathpic,exist_ok=True)
            src=path_file
            dst=pathpic
            try:
                shutil.move(src,dst)
            except Exception as e:
                with st.expander("ERROR"):
                    st.warning(f"{e}")
                    st.write("if the error appears to be destination error then theres a clone of a file ")
                


        if split[-1]=="exe":
            pathexe=os.path.join(paths,"all_exetensions")
            os.makedirs(pathexe,exist_ok=True)
            src=path_file
            dst=pathexe
            try:
                shutil.move(src,dst)
            except Exception as e:
                with st.expander("ERROR"):
                    st.warning(f"{e}")
                    st.write("if the error appears to be destination error then theres a clone of a file ")

        
with st.expander("Files & Types"):
    st.write(files)
   

st.markdown('<div class="wrapper"><div class="sun"><div class="sunny">📂</div></div></div>',unsafe_allow_html=True)