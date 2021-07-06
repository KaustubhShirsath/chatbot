# chatbot
In this project, I build a chatbot using deep learning techniques. 
The chatbot has been trained on the dataset which contains categories (intents), pattern and responses. 
I used a special recurrent neural network (LSTM) to classify which category the user’s message belongs to and 
then the bot will give a random response from the list of responses.
Contents - 
1. Intents.json – The data file which has predefined patterns and responses.
2. train_chatbot.py – In this Python file, we wrote a script to build the model and train our chatbot.
3. Words.pkl – This is a pickle file in which we store the words Python object that contains a list of our vocabulary.
4. Classes.pkl – The classes pickle file contains the list of categories.
5. Chatbot_model.h5 – This is the trained model that contains information about the model and has weights of the neurons.
6. Chatgui.py – This is the Python script in which we implemented GUI for our chatbot. Users can easily interact with the bot.
