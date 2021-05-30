from Bio.Seq import Seq

"""
Sticking with the same example discussed in the transcription section above, now let’s translate this mRNA into the corresponding protein sequence - again taking advantage of one of the Seq object’s biological methods:
"""

coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

print("Coding DNA : {}\n".format(coding_dna))

template_dna = coding_dna.reverse_complement()
print("Template DNA : {}\n".format(template_dna))

messenger_rna = coding_dna.transcribe()
print("Messenger RNA: {}\n".format(messenger_rna))

# Translation

proteins = messenger_rna.translate()
print("Proteins seq : {} \n".format(proteins))
