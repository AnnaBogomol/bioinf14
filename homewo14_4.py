import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("BRCA_pam50.tsv", sep="\t", index_col=0)

sns.boxplot(x="MKI67", y="Subtype", data=df)
plt.tight_layout()
plt.savefig("boxplotMKI67.pdf")
plt.close()

sns.boxplot(x="ERBB2", y="Subtype", data=df)
plt.tight_layout()
plt.savefig("boxplotERBB2.pdf")
plt.close()

sns.boxplot(x="PGR", y="Subtype", data=df)
plt.tight_layout()
plt.savefig("boxplotPGR.pdf")
plt.close()

sns.boxplot(x="ESR1", y="Subtype", data=df)
plt.tight_layout()
plt.savefig("boxplotESR1.pdf")
plt.close()
