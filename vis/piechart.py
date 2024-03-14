f, ax = plt.subplots(2,4, figsize=(20,10))

ax[0,2] = patient.region.value_counts().plot(kind='pie', labels = patient.region.unique(), title='nums of infected by region', ax=ax[0,2], autopct='%.2f%%')
ax[0,2].legend(loc = 'best', labels=patient.region.unique()[:5])

ax[0,3] = patient.group.value_counts().plot(kind='pie', labels = patient.group.unique(), title='nums of infected by group', ax=ax[0,3], autopct='%.2f%%')

ax[1,0] = patient.infection_reason.value_counts().plot(kind='pie', labels = patient.infection_reason.value_counts(), title='infection_reason', ax=ax[1,0], autopct='%.2f%%')
ax[1,0].legend(loc='best', labels=patient.infection_reason.unique()[:3])
