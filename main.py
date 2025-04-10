# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

import pickle
# with open('model.pkl', 'wb') as model_file:
#         pickle.dump(model, model_file)
#
#     # Later, when loading in a different script or session
#     loaded_model = pickle.load(open('model.pkl', 'rb'))

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

with open('model.pkl','rb') as model1:
        print(model1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
