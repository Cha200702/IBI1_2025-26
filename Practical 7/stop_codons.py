# Bio.SeqIO is a module specifically designed for handling sequence files
from Bio import SeqIO
# re module is suitable for extracting gene names from the header
  # "header" is the line beginning with ">" in FASTA files
import re

# Define a function "main()" to divide the whole procedure into several separate steps
def main():
    # Define input and output file names
    input_fasta = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    output_fasta = "stop_genes.fa"
    
    # Define stop codons
      # "{}" represents a set while "[]" represents a list
      # "{}" is better than "[]" here because set has faster lookup time than list and can avoid recording a stop codon multiple times for the same gene 
      # ------------------------------------------------------------------
        # Example !
        # If stop_codons_set = {"TAA", "TAG", "TGA", "TAA"}
        # result = {"TAA", "TAG", "TGA"}  
        # If stop_codons_list = ["TAA", "TAG", "TGA", "TAA"]
        # result = ["TAA", "TAG", "TGA", "TAA"]  
      # ------------------------------------------------------------------
    stop_codons = {"TAA", "TAG", "TGA"}
    
    # Create an empty list to store the filtered SeqRecord
    seq_list = []
    
    # --------------------------
    # Step 1 : Read the input FASTA file and extract gene names and sequences
    # --------------------------
    # SeqIO.parse() can automatically recognize FASTA format and each time returns a SeqRecord including id, description, and sequence
    # "fasta" is to tell SeqIO to read the file in FASTA format
    for record in SeqIO.parse(input_fasta, "fasta"):
        # Extract gene name from the header
        # search for "gene:xxx" pattern in the description and extract "xxx" as the gene name
          # "gene:(\S+)" means to search for "gene:" followed by one or more non-whitespace characters, namely gene name
          # record.description is the header line of the FASTA file, which limits the searching area
        gene_name = re.search(r"gene:(\S+)", record.description)
        if not gene_name:
            continue  # jump to the next record if no gene name is found
        # What we have extracted is, for example, "gene:XYZ123", but we only want "XTZ123" here.
        # So group(1) is to extract the gene name while group(0) will give us the whole string
        gene_name = gene_name.group(1)
        
        # Convert the sequence to string format for easily getting length 
        seq = str(record.seq)
        length = len(seq)

        # Create an empty set to store the stop codons for the current gene
        total = set()
        
        # --------------------------
        # Step 2 : Find start and stop codons for each gene
        # --------------------------
        for i in range(length - 2):
            if seq[i:i+3] == "ATG":
                for j in range(i, length - 2, 3):
                    codon = seq[j:j+3]
                    if codon in stop_codons:
                        total.add(codon)
        
        # --------------------------
        # Step 3 : Construct new SeqRecord for genes in total
        # --------------------------
        if total: # if total is not empty
            new_record = record[:]  # [:] means to follow the original format of the record
            gene_name = record.id
            # " ".join( ) means to connect stop codons with a space in between
            # Sorted() is to sort the stop codons in alphabetical order
            new_record.description = " ".join(sorted(total))
            # append() is to add the new record to the list
            seq_list.append(new_record)
    
    # --------------------------
    # Step 4 : Write to the output FASTA file
    # --------------------------
    SeqIO.write(seq_list, output_fasta, "fasta")

# When the script is run directly, the main() function will be executed
  # __name__ is a special variable in Python to determine whether the script is run directly or imported as a module
if __name__ == "__main__":
    main()

# Difficulty and notice:
  # 1. The code imports new module SeqIO
  # 2. Lots of unfamiliar functions are used like append(), __name__ , join().....
  # 3. {} and [] are used in different contexts.