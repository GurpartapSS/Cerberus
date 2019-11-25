This is first basic attempt to teach cerebrus to chat.
An LSTM based model is used to train the model to find the tag that best represents the text input.
The input text is then converted to word vectors using GloVe embedding file.
Cosine similariy between the input sentence and all reference sentences in that tag is calculated and the response corresponding to maximum similarity is given as response.


To use the model:
Modify the "intents.json" file(for this bot, have the number of entiries in pattern and response as equal).
Run the training file.
Run the chatter module.

limitations: 
limited dictionary,
Cant use slang words,
No spelling check to correct minor mistakes, so the words have to be spelled correctly,
Response accuracy less >90%

References:
https://techwithtim.net/tutorials/ai-chatbot/ 
https://www.coursera.org/learn/nlp-sequence-models
https://nlp.stanford.edu/projects/glove/