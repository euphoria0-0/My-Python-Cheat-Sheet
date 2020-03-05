cm = sns.light_palette("green", as_cmap=True)
train.describe().style.set_caption('Colormaps, with a caption.').background_gradient(cmap=cm)