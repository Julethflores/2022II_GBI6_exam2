import os
from Bio import Entrez, SeqIO
from Bio.Align.Applications import ClustalwCommandline
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
import matplotlib.pyplot as plt

# Conceptualización de la función fasta_downloader
def fasta_downloader():
    """
    Esta función carga id_coati.txt, descarga la información correspondiente a los identificadores de acceso
    utilizando ENTREZ de Biopython y la guarda en coati y coati.gb.
    """
    # Cargar id_coati.txt
    with open("id_coati.txt") as file:
        ids = file.read().splitlines()

    # Se descargo la información utilizando ENTREZ de Biopython
    Entrez.email = "juleth.flores@est.ikiam.edu.ec"
    handle = Entrez.efetch(db="nucleotide", id=ids, rettype="gb", retmode="text")
    records = list(SeqIO.parse(handle, "gb"))
    with open("coati.gb", "w") as output_handle:
        SeqIO.write(records, output_handle, "genbank")
    with open("coati", "w") as output_handle:
        SeqIO.write(records, output_handle, "fasta")

# Conceptualización de la función alignment
def alignment():
    """
    Esta función se extrae  las secuencias de la variable coati.
    El resultado se guardo como coati.aln y coati.dnd en la carpeta.
    """
    # Se realizó la alineación utilizando ClustalW
    clustalw_cline = ClustalwCommandline("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\ClustalW2\clustalw.exe", infile="coati")
    clustalw_cline()
    os.rename("coati.aln", "coati_aligned.aln")
    os.rename("coati.dnd", "coati_aligned.dnd")

# Conceptualización de la función tree
def tree():
    """
    Finalmente, esta herramienta calcula las distancias utilizando coati.aln y se imprime el árbol filogenético y se guarda
     como coati_phylotree.pdf en su carpeta de trabajo.
    """
    # Se cargar las secuencias alineadas
    with open("coati_aligned.aln", "r") as handle:
        records = list(SeqIO.parse(handle, "fasta"))
    
    # Se calcula las distancias
    calculator = DistanceCalculator("blosum62")
    dm = calculator.get_distance(records)

    # Se construye el árbol
    constructor = Distance
