import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6,5))
ax.axis('off')
y=0.9
boxes=['UKB with fundus','After QC','Linked labs/EHR','Eligible for ESRD analysis']
for i,b in enumerate(boxes):
    ax.add_patch(plt.Rectangle((0.2,y-0.05),0.6,0.08, fill=False))
    ax.text(0.5,y-0.01,b, ha='center', va='center')
    if i < len(boxes)-1:
        ax.annotate('', xy=(0.5,y-0.07), xytext=(0.5,y-0.17), arrowprops=dict(arrowstyle='->'))
    y-=0.2
fig.tight_layout()
fig.savefig('fig_cohort_flow.pdf')
print('Saved figures/fig_cohort_flow.pdf')