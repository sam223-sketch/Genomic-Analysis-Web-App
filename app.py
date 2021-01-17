import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
from Bio.Seq import Seq
from Bio import SeqIO
from collections import Counter
import neatbio.sequtils as utils
import numpy as np
from PIL import Image

from DNAtoolkit import *
st.set_option('deprecation.showPyplotGlobalUse', False)
# def delta(x,y):
#     return 0 if x == y else 1


# def M(seq1,seq2,i,j,k):
#     return sum(delta(x,y) for x,y in zip(seq1[i:i+k],seq2[j:j+k]))


# def makeMatrix(seq1,seq2,k):
#     n = len(seq1)
#     m = len(seq2)
#     return [[M(seq1,seq2,i,j,k) for j in range(m-k+1)] for i in range(n-k+1)]


# def plotMatrix(M,t, seq1, seq2, nonblank = chr(0x25A0), blank = ' '):
#     print(' |' + seq2)
#     print('-'*(2 + len(seq2)))
#     for label,row in zip(seq1,M):
#         line = ''.join(nonblank if s < t else blank for s in row)
#         print(label + '|' + line)


# def dotplot(seq1,seq2,k = 1,t = 1):
#     M = makeMatrix(seq1,seq2,k)
#     plotMatrix(M, t, seq1,seq2) #experiment with character choice


# # Convert to Fxn
# def dotplotx(seq1,seq2):
#     plt.imshow(np.array(makeMatrix(seq1,seq2,1)))
#     # on x-axis list all sequences of seq 2
#     xt=plt.xticks(np.arange(len(list(seq2))),list(seq2))
#     # on y-axis list all sequences of seq 1
#     yt=plt.yticks(np.arange(len(list(seq1))),list(seq1))
#     plt.show()


# def gc_content(seq):
#     result = float(str(seq).count('G') + str(seq).count('C'))/len(seq) * 100
#     return result

# def at_content(seq):
#     result = float(str(seq).count('A') + str(seq).count('T'))/len(seq) * 100
#     return result



def main():
    """A Simple Streamlit App """
    st.title("BioInformatics App")

    activity = ['Intro','DNA','DotPlot',"About"]
    choice = st.sidebar.selectbox("Select Activity",activity)
    if choice == 'Intro':
	       st.subheader("Intro")
    elif choice == "DNA Sequence":
	       st.subheader("DNA Sequence Analysis")

    seq_input = st.text_input('Input Sequence')
    st.write(validateSeq(seq_input))

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

