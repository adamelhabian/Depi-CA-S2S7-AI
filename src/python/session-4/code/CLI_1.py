from chatbot import get_responce
def main_1():
    print("Chatbot : hi how i can help you !!")
    while(True):
        userinput=input("User :   ").lower()
        response=get_responce(userinput)
        print("Chatpot : ",response)
        if userinput == "goodbye":break