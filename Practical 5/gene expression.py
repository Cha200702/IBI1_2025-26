# Create the initial dictionary
my_dict = {}
gene_dict = {'TP53':12.4, 'EGFR':15.1, 'BRCA1':8.2, 'PTEN':5.3,'ESR1':10.7}

# Add a new gene MYC to the dictionary
gene_dict['MYC'] = 11.6

# Print the updated dictionary
print (gene_dict)

# Make the bar chart
import matplotlib.pyplot as plt
# Get the genes and their expression values from the dictionary
genes = list(gene_dict.keys())
values = list(gene_dict.values())
# Set elements of the bar chart
plt.figure(figsize=(8,5))
plt.bar(genes, values, color='skyblue')
plt.xlabel('Gene')
plt.ylabel('Expression value')
plt.title('Gene Expression Values')
# Set the y-axis range
plt.ylim(0, max(values)+2)
# Add the values on top of the bars
for i, v in enumerate(values):
    plt.text(i, v+0.2, str(v), ha='center')
# Show the bar chart
plt.show()

# Search for the expression value of a specific gene
gene_name = 'Cha'
if gene_name in gene_dict: 
    print(f"The expression level of {gene_name} is {gene_dict[gene_name]}")
else:    print(f"{gene_name} is not found in the dictionary.")

# Calculate the average expression value of the genes
average_expression = sum(gene_dict.values()) / len(gene_dict)
print(f"The average expression value of the genes is {average_expression:.2f}")
