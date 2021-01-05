import streamlit as st
from Bio.Seq import Seq
from Bio import SeqIO
from collections import Counter

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
        seq_file = st.file_uplaoder("Upload FASTA file", type=["fasta","fa","txt"])
        if seq_file is not None:
            dna_record = SeqIO.read(seq_file,"fasta","txt")
            st.write(dna_record)

    elif choice == "Information":
        st.subheader("Information")



if __name__ == '__main__':
    main()
