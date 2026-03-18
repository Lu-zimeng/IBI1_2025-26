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
genes=list(gene_expression.keys())
expression = list(gene_expression.values())
bar_colors = ['tab:red', 'tab:blue', 'tab:purple', 'tab:orange','tab:olive','tab:pink']

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
import numpy as np
average=np.mean(expression)
print("The average gene expression level across all genes is "+str(average))