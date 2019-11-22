This is first basic attempt to teach cerebrus to chat like Humans.
A Fully connected 2 layers DNN is used to see quick results with little to none sequence modification.
It maps the keywords frequency to the categories and picks up random reponse from the list of responses. 
Pretty Naive but a good start.

for the development, I followed https://techwithtim.net/tutorials/ai-chatbot/ that provided steps to build the chatbot system and the reference files.

New LSTM based model added. To use the model:

modify the "intents.json" file.
Run the training model, it has the code to start the chat in the end. 
Training and Chat modules will be seperated in next commit.