import streamlit as st
from matplotlib.backends.backend_agg import RendererAgg
_lock = RendererAgg.lock
import matplotlib.pyplot as plt


from collections import Counter


from DNAtoolkit import *
st.set_option('deprecation.showPyplotGlobalUse', False)



def main():
    """A Simple Streamlit App """
    st.title("BioInformatics Web App")

    #activity = ['Intro','DNA','DotPlot',"About"]
    # choice = st.sidebar.selectbox("Select Activity",activity)
    # if choice == 'Intro':
	#        st.subheader("Intro")
    # elif choice == "DNA Sequence":
	#        st.subheader("DNA Sequence Analysis")

    #input sequence
    seq_input = st.text_input('Input Sequence')

    #check validity of sequence entered
    validateSeq(seq_input)

    details = st.radio("Functions",("Sequence Length",
                        "Frequency of each Nucleotide",
                        "Transcription of DNA", 
                        "Reverse Transcription", 
                        "Find Complementory Strand",
                        "GC Content Percentage"))
    if details == "Sequence Length":
        st.write(len(seq_input))

    elif details == "Frequency of each Nucleotide":
        st.subheader("Nucleotide Frequency")
        seq_input = Counter(seq_input)
        st.write(seq_input)
        adenine_color = st.color_picker("Adenine Color")
        thymine_color = st.color_picker("thymine Color")
        guanine_color = st.color_picker("Guanine Color")
        cytosil_color = st.color_picker("cytosil Color")

        if st.button("Plot Freq"):
            barlist = plt.bar(seq_input.keys(),seq_input.values())
            barlist[2].set_color(adenine_color)
            barlist[3].set_color(thymine_color)
            barlist[1].set_color(guanine_color)
            barlist[0].set_color(cytosil_color)

            st.pyplot()
    
    elif details == "Transcription of DNA":
        st.write(transcription(seq_input))

    elif details == "Reverse Transcription":
        st.write(reversetranscription(seq_input))

    elif details == "Find Complementory Strand":
        st.text(f" DNA String + Complement + Reverse Complement: \n 5'{seq_input} 3'  \n   {''.join(['|' for c in range(len(seq_input))])} \n 3'{reverse_complement(seq_input)[::-1]} 5'[Complement] \n 5'{reverse_complement(seq_input)} 3'[Reverse Complement]")

    elif details == "GC Content Percentage":
        st.write(f" {gc_content(seq_input)}%")



if __name__ == '__main__':
    main()

