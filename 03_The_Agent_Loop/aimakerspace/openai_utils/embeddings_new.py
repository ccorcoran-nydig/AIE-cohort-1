if __name__ == "__main__":
    from sentence_transformers import SentenceTransformer
    # Load a pretrained Sentence Transformer model (runs locally)
    model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
    puppy_sentence = "i love puppies"
    dog_sentence = "i love dogs"
    puppy_vector = model.encode(puppy_sentence)
    dog_vector = model.encode(dog_sentence)
    print(puppy_vector)
    print(dog_vector)