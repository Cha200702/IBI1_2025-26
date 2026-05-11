# Create two dictionaries
sequence_mass = {
    'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05, 'V': 99.07,
    'T': 101.05, 'C': 103.01, 'I': 113.08, 'L': 113.08, 'N': 114.04,
    'D': 115.03, 'Q': 128.06, 'K': 128.09, 'E': 129.04, 'M': 131.04,
    'H': 137.06, 'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08
}

amino_acid_symbol = {
    'Glycine': 'G', 'Alanine': 'A', 'Serine': 'S', 'Proline': 'P',
    'Valine': 'V', 'Threonine': 'T', 'Cysteine': 'C', 'Isoleucine': 'I',
    'Leucine': 'L', 'Asparagine': 'N', 'Aspartic Acid': 'D',
    'Glutamine': 'Q', 'Lysine': 'K', 'Glutamic Acid': 'E',
    'Methionine': 'M', 'Histidine': 'H', 'Phenylalanine': 'F',
    'Arginine': 'R', 'Tyrosine': 'Y', 'Tryptophan': 'W'
}

# Define a function that searches for the corresponding mass of desired AA.
def get_mass(AA): # Need a parameter here
    # Turn the input into the format of strings
    input = AA.strip()
    if input in sequence_mass:
        return sequence_mass[input]
    elif input in amino_acid_symbol:
        symbol = amino_acid_symbol[input]
        return sequence_mass[symbol]
    else:
        print(f"Unknown amino acid: '{AA}. Error!'")

# Define another function that calculates the overall mass of protein sequence
def calculate_mass(sequence):
    # Give a new variable for recording
    total_mass = 0.0
    # .upper() is used to convert all lowercase letters in a string to uppercase letters
    normalized_sequence = sequence.upper()
    for AA in normalized_sequence:
        total_mass += get_mass(AA)
    return total_mass

if __name__ == "__main__":
    print("-- Example for protein mass calculation --")
    test_sequence = "GA"
    mass = calculate_mass(test_sequence)
    print(f"The protein sequence '{test_sequence}' total mass is {mass} amu.")