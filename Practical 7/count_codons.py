from Bio import SeqIO
import re
import matplotlib.pyplot as plt
# collection is a module that contains lots of useful data structures
# defaultdict is to give a default value, usually 0, for the key that does not exist.
  # It is helpful for counting without using if-else statements to define the initial value for each variable.
from collections import defaultdict

def main():
    # --------------------------
    # Step 1: Ask user for a valid stop codon
    # --------------------------
    stop_codons = {"TAA", "TAG", "TGA"}
    # "while True + break" pattern is used to ensure valid input from the user, avoiding breakdown due to invalid input.
    while True:
        input_codon = input("Please input a stop codon from TAA,TAG and TGA):").strip().upper()
        if input_codon in stop_codons:
            target_codon = input_codon
            break
        print("Invalid input! Please enter TAA, TAG, or TGA.")

    # --------------------------
    # Input the file and initialize the dictionary for counting
    # --------------------------
    input_fasta = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    count = defaultdict(int)  # (int) is the default value for any key that does not exist in the dictionary, usually 0.

    # --------------------------
    # Step 3: Go through the FASTA file and analyze each gene
    # --------------------------
    for record in SeqIO.parse(input_fasta, "fasta"):
        seq = str(record.seq)
        length = len(seq)
        
        # Create an empty list to store all valid ORFs
        orfs = []

        for start in range(length - 2):
            if seq[start:start+3] == "ATG":
                for stop in range(start, length - 2, 3):
                    codon = seq[stop:stop+3]
                    if codon == target_codon:
                        orf_length = stop + 3 - start
                        orfs.append((orf_length, start, stop + 3))
                        break 

        if orfs:
            # Sort ORFs by length in descending order and select the longest one
              # orfs.sort() will sort all orfs in the list without creating a new list
              # reverse=True means the sortation will be in descending order
              # lambda x: x[0] is a function that takes the first "[0]" element to compare, which is the length of the ORF stored. 
            orfs.sort(reverse=True, key=lambda x: x[0])
            # Define the start and end positions of the longest ORF
              # orfs[0] is the longest ORF in the list
              # [1] and [2] are the second and third elements of the string. In this context, they are the start and end positions of the longest ORF.
            longest_start, longest_end = orfs[0][1], orfs[0][2]

            # Modify the final sequence by removing the stop codon
            orf_seq = seq[longest_start:longest_end - 3]
            # Count the codons 
            for i in range(0, len(orf_seq), 3):
                if i + 3 <= len(orf_seq):
                    codon = orf_seq[i:i+3]
                    count[codon] += 1

    # --------------------------
    # Step 4: Create a pie chart 
    # --------------------------
    if not count:
        print("No valid ORFs found with the specified stop codon.")
        return

    total = sum(count.values())
    threshold = 1.5  # Set a threshold for displaying codons. Codons below this threshold will be grouped into "Others".

    # Sort by frequency in descending order
      # count.items() returns a list of codons and their counts. So each element is (codon, count 次数).
      # lambda x: x[1] is a function that takes the second element (count 次数) of each tuple for sorting
      # reverse=True means the sortation will be in descending order
    sorted_codons = sorted(count.items(), key=lambda x: x[1], reverse=True)

    # Initialize lists for further labels
    final_labels = []
    final_sizes = []
    others_size = 0

    # Calculate frequencies and determine which codons to display
    for codon, count in sorted_codons:
        frequency = (count / total) * 100
        if frequency >= threshold:
            final_labels.append(codon)
            final_sizes.append(count)
        else:
            others_size += count
    if others_size > 0:
        final_labels.append("Others")
        final_sizes.append(others_size)

    plt.figure(figsize=(16, 16))  

    # Create a pie chart
    wedges, texts, autotexts = plt.pie(
        final_sizes,
        labels=final_labels,  # Show the codon labels
        autopct='%1.1f%%',   # Show percentages with one decimal place
        startangle=90,
        labeldistance=1,    # Label distance from the center
        pctdistance=0.8,      # Percentage label distance from the center
        rotatelabels=True,     # Rotate labels to avoid overlap
        textprops={'fontsize': 9}  # Adjust font size
    )
    # pad is the distance between the title and the pie chart
    plt.title(f"The distribution of all in-frame codons produced by genes contain {target_codon}", fontsize=16, pad=20)
    plt.axis('equal') # Equal aspect ratio ensures that the pie chart is circular.
      
    # Save the pie chart to a file 
    output = f"frequency_{target_codon}.png"
    # dpi is the resolution of the output image 
    # bbox_inches='tight' is to ensure that the saved image does not have extra white space around it
    plt.savefig(output, dpi=300, bbox_inches='tight') 
    print(f"The output file is saved as {output}")
    plt.show() 

if __name__ == "__main__":
    main()

# Difficulty and notice:
    # 1. The code imports defaultdict module, which is useful for setting default values for variables
    # 2. The code imports matplotlib module to draw the pie chart
    # 3. It's important to find out each element in the list before using [0]/[1] for sorting
    # 4. Since all in-frame codons shown are messy, the code sets a threshold to sort parts of codons into "Others"
    # 5. Still many unfamiliar functions are used like count(), sorted(), plt.savefig(), append()......