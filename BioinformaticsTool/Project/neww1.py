from Bio.Alphabet import generic_dna
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
from Bio import AlignIO

seq="MARFLTLCTWLLLLGPGLLATVRAECSQDCATCSYRLVRPADINFLACVMECEGKLPSLKIWETCKELLQLSKPELPQDGTSTLRENSKPEESHLLAKRYGGFMKRYGGFMKKMDELYPMEPEEEANGSEILAKRYGGFMKKDAEEDDSLANSSDLLKELLETGDNRERSHHQDGSDNEEEVSKRYGGFMRGLKRSPQLEDEAKELQKRYGGFMRRVGRPEWWMDYQKRYGGFLKRFAEAPSDEEGESYSKEVPEMEKRYGGFMRF"
align1 = MultipleSeqAlignment(
    [
        SeqRecord(Seq(open("C:/Users/AAMIR/OneDrive/Desktop/sequence1.txt","r").read(), generic_dna), id="Alpha"),
        SeqRecord(Seq(seq, generic_dna), id="Beta"),

    ]
)


AlignIO.write(align1, "example1.phy", "phylip")
print(open("my_example.phy","r").read())

