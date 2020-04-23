cm = sns.light_palette("skyblue", as_cmap=True)
train.describe().style.background_gradient(cmap=cm)
