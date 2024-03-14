import pickle

# save model
def save_model(model, out_path='./', model_name='model'):
	model_json = model.to_json()
	with open(out_path+model_name+'.json', 'w') as f: 
		f.write(model_json)
	model.save_weights(out_path+model_name+'.h5')

# save tokenizer
def save_tokenizer(tokenizer, out_path='./'):
	with open(out_path+'tokenizer.pickle', 'wb') as f:
		pickle.dump(tokenizer, f, protocol = pickle.HIGHEST_PROTOCOL)
