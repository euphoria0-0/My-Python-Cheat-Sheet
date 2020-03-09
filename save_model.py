# save model
def save_model(model):
	model_json = model.to_json()
	with open(model_path+model_name+'.json', 'w') as f: 
    		f.write(model_json)
	model.save_weights(model_path+model_name+'.h5')

# save tokenizer
def save tokenizer(tokenizer):
	with open(path+'tokenizer.pickle', 'wb') as f:
    		pickle.dump(tokenizer, f, protocol = pickle.HIGHEST_PROTOCOL)
