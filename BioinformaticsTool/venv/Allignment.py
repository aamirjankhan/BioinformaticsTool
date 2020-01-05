from Bio import pairwise2
from Bio import SeqIO
from Bio.SubsMat.MatrixInfo import blosum62
class Allignment_():


    def pairwise_align_local(file1, file2):
        try:
            seq1 = SeqIO.read(file1, "fasta")
            seq2 = SeqIO.read(file2, "fasta")
            alignments = pairwise2.align.localds(seq1.seq, seq2.seq, blosum62, -10, -0.5)
            align = pairwise2.format_alignment(*alignments[0])
            return len(alignments),align
        except FileNotFoundError:
            return 'Fatal'
    def pairwise_align_global(file1, file2):
        try:
            seq1 = SeqIO.read(file1, "fasta")
            seq2 = SeqIO.read(file2, "fasta")
            alignments = pairwise2.align.globalds(seq1.seq, seq2.seq, blosum62, -10, -0.5)
            align = pairwise2.format_alignment(*alignments[0])
            return len(alignments),align
        except FileNotFoundError:
            return 'Fatal'





def main():
    alignment = Allignment_()

if __name__=='__main__':
    main()


