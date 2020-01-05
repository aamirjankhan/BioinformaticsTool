from Project.Functions import Function1
#_,align = Allignment_.pairwise_align('C:/Users/AAMIR/OneDrive/Desktop/sequence1.faa'\
#                        ,'C:/Users/AAMIR/OneDrive/Desktop/sequence2.faa')
#pprint(align)
#protein=Function2.ConvertToProtein('C:/Users/AAMIR/sequence111.txt')
#print(protein)

print(Function1.ReverseDna("ATACATACATACATACATACATTTTTTTTTTTTTTT"))
#print(Allignment_Needle.Needle_Align('C:/Users/AAMIR/OneDrive/Desktop/sequence1.txt'\
#                        ,'C:/Users/AAMIR/OneDrive/Desktop/sequence2.txt'))

'''
from Bio.Alphabet import generic_dna
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
from Bio import AlignIO


align1 = MultipleSeqAlignment(
    [
        SeqRecord(Seq("ACTGCTAGCTAG", generic_dna), id="Alpha"),
        SeqRecord(Seq("ACT-CTAGCTAG", generic_dna), id="Beta"),
        SeqRecord(Seq("ACTGCTAGDTAG", generic_dna), id="Gamma"),
    ]
)

align2 = MultipleSeqAlignment(
    [
        SeqRecord(Seq("GTCAGC-AG", generic_dna), id="Delta"),
        SeqRecord(Seq("GACAGCTAG", generic_dna), id="Epsilon"),
        SeqRecord(Seq("GTCAGCTAG", generic_dna), id="Zeta"),
    ]
)

align3 = MultipleSeqAlignment(
    [
        SeqRecord(Seq("ACTAGTACAGCTG", generic_dna), id="Eta"),
        SeqRecord(Seq("ACTAGTACAGCT-", generic_dna), id="Theta"),
        SeqRecord(Seq("-CTACTACAGGTG", generic_dna), id="Iota"),
    ]
)

my_alignments = [align1, align2, align3]
AlignIO.write(my_alignments, "my_example.phy", "phylip")

'''
