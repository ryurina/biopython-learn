from Bio.Seq import Seq
from Bio import SeqIO

"""
parsing and make something fun with SARS-COV2 genome
"""

# parsing the fasta file

for seq_record in SeqIO.parse("sarscov2.fasta", "fasta"):
    covid_seq_id = seq_record.id
    covid_seq = repr(seq_record.seq)
    covid_seq_len = len(seq_record)


print("SARS-COV2 Info:\nID: {}\nGenes Sequences: {}\nLength: {}\n".format(covid_seq_id, covid_seq, covid_seq_len))


# Translation / Transcription 

covid_seq = covid_seq.replace("Seq('","")
covid_seq = covid_seq.replace("')", "")
covid_seq = Seq(covid_seq)

template_covid = covid_seq.reverse_complement()
messenger_rna = covid_seq.transcribe()
print("Complement: {}\nRNA: {}\n".format(template_covid, messenger_rna))


