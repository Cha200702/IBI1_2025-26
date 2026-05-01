# Define mRNA sequence
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

# Define start codon and stop codons
start_codon = 'AUG'
stop_codons = {'UAA', 'UAG', 'UGA'}

# Initialize variables
  # For strings, '' is usually used to represent an empty string
longest_orf = ''
  # For values, 0 is usually used to reset the variable
length = 0

# Define the full length of the sequence
full_length = len(seq)

# use "for" loop to find the longest ORF
for start in range(full_length - 2): # "-2" is used to prevent out-of-range error when checking for 3-base codons
    # Check if the current position has the start codon
    if seq[start:start+3] == start_codon:  # [start:start+3] means extracting a substring from "start" to "start+2"; "start 3" is not included; ":" functions as "to" in this context
        # Three elements in () are used to specify the start, stop, and step for the loop. 
        for codon in range(start, full_length - 2, 3):
            # Extract the current codons (3 bases)
            extract_codon = seq[codon:codon+3]
            # Check if the extracted codon is a stop codon
            if extract_codon in stop_codons:
                # Record the ORF from the start codon to the stop codon (inclusive)
                ORF = seq[start:codon+3]
                ORF_length = len(ORF)
                
                # Use if statement to compare the length of all extracted ORFs
                if ORF_length > length:
                    longest_orf = ORF
                    length = ORF_length
                
                # Terminate all the process above
                break

# Output the results
print(f"The longest orf is {longest_orf}.")
print(f"The length of this longest orf is {length}.")


# Difficulty and notice:
  # 1. The code needs to find the longest ORF, which means comparasion is needed. --> "if" statement
  # 2. The codons are read in triplets, which means the step of the loop should be 3. --> "for" loop with step of 3