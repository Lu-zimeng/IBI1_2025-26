#create dictionary
gene_expression={'TP53':12.4,'EGFR':15.1,'BRCA1':8.2,'PTEN':5.3,'ESR1':10.7}
print(gene_expression)

#add gene "MYC"
gene_expression['MYC']=11.6
print(gene_expression)

#produce a well-labeled bar chart
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
#defining values and bar colors
genes = ['TP53', 'EGFR', 'BRCA1', 'PTEN','ESR1']
expression = [12.4, 15.1, 8.2, 5.3,10.7]
bar_colors = ['tab:red', 'tab:blue', 'tab:purple', 'tab:orange','tab:olive']

ax.bar(genes, expression, color=bar_colors)
#set ylabel and title
ax.set_ylabel('Gene expression')
ax.set_title('Gene expression levels for 6 genes')
#show value of every bar
for i, v in enumerate(expression):
    ax.text(i, v + 0.3, f'{v:.1f}', ha='center', fontsize=9)

plt.show()

#create a variable representing a gene of interest
gene_of_interest=input("Enter the gene of interest:")
if gene_of_interest in gene_expression:
    expression_value=gene_expression[gene_of_interest]
    print("Expression level of " + gene_of_interest + " is " + str(expression_value))
else:
    print("Gene " + gene_of_interest + " is not in the dataset!")

#calculate the average gene expression level
total_expression=sum(gene_expression.values())
total_genes=len(gene_expression)
average_expression= total_expression /total_genes

print("The average gene expression level across all genes is "+str(average_expression))