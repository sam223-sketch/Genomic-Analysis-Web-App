import streamlit as st
from Bio.Seq import Seq
from Bio import SeqIO
from collections import Counter
import gzip

# Data Visualization
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")




def main():
    """Genomic Analysis Web App"""

    st.title("Genomic Analysis Web App")

    menu = ["Introduction", "DNA Sequence", "Information"]
    choice = st.sidebar.selectbox("Select Activity", menu)

    if choice == "Introduction":
        st.subheader("Introduction to Genommic Analysis")
    elif choice == "DNA Sequence":
        st.subheader("DNA Sequence Analysis")

        """Upload file"""
        seq_file = st.file_uploader("Upload FASTA File",type=["fasta","fa"])

        if seq_file is not None:
            dna_record = SeqIO.read(seq_file,"fasta")
            # st.write(dna_record)
            dna_seq = dna_record.seq
            
            details = st.radio("Details",("Description","Sequence"))
            if details == "Description":
                st.write(dna_record.description)
            elif details == "Sequence":
                st.write(dna_record.seq)

    elif choice == "Information":
        st.subheader("Information")



if __name__ == '__main__':
    main()
