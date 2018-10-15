from Bio import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

dan=open("chapter19/hemoglobin-gene.txt").read().strip()
dan=Seq.Seq(dan,IUPAC.unambiguous_dna)

mrna=dan.transcribe()
protein=mrna.translate()
protein_record = SeqRecord(protein, id='sp|P69905.2|HBA_HUMAN',description="Hemoglobin subunit alpha, Homo sapiens")
outfile=open("chapter19/HBA_HUMAN.fasta","w")
SeqIO.write(protein_record,outfile,"fasta")
outfile.close()
