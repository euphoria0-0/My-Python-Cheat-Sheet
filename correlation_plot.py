def corr_plot(df,ax=None,title=None, spearman=True):
    method = 'spearman' if spearman else None
    corr = df.corr(method)
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    sns.heatmap(data = corr, annot=True, fmt = '.2f', mask=mask, linewidths=.5, cmap='RdYlBu_r', ax=ax)
    if title is not None:
        ax.set_title(title)

fig, ax = plt.subplots(nrows=1,ncols=2,figsize=(30,12))
corr_plot(train[X_columns_num], ax=ax[0], title='pearson correlation')
corr_plot(train[X_columns_num], ax=ax[1], title='spearman correlation', spearman=True)