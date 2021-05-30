from Bio.Seq import Seq

"""
The actual biological transcription process works from the template strand, doing a reverse complement (TCAG → CUGA) to give the mRNA. However, in Biopython and bioinformatics in general, we typically work directly with the coding strand because this means we can get the mRNA sequence just by switching T → U.
"""

coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

print("Coding DNA : {}\n".format(coding_dna))

template_dna = coding_dna.reverse_complement()
print("Template DNA : {}\n".format(template_dna))

messenger_rna = coding_dna.transcribe()
print("Messenger RNA: {}\n".format(messenger_rna))

