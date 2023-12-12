from flask import Flask
from flask import request

@app.route('/query', methods=['POST', 'GET'])

def query():
	from sentence_transformers import SentenceTransformer, util
	import torch
	
	embedder = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
	with open('sub.txt', encoding="UTF-8") as f:
		corpus = f.read().splitlines()
	corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)
	query = request.form['query']
	top_k = min(5, len(corpus))
	query_embedding = embedder.encode(query, convert_to_tensor=True)

	cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]
	top_results = torch.topk(cos_scores, k=top_k)

	print("\n\n======================\n\n")
	print("Query:", query)
	print("\nTop 5 most similar sentences in corpus:")

	s = []
	for score, idx in zip(top_results[0], top_results[1]):
		s.append(corpus[idx], "(Score: {:.4f})".format(score))
	return s[1]