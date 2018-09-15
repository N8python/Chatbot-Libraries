questions=["hi ", "hello", "hey ", "your name", "do you like", "do you", "how are you", "what's up", "what about", "where is", "what is", "I have", "I want", "how much", "how many", "I am", "thank you", "what should", "who should", "you're", "I think you're", "what is your favorite", "are you", "can you", "it is", "why are you", "how smart are you", "siri", "alexa", "you are", "let's have", "why", "good", "bad", "let's move on", "that was", "we will", "where were", "you have", "I think", "thanks", "I really need", "I really", "excuse me", "I'm sorry", "let's do", "chat bot", "nice to meet you", "what's 2+2", "how was your", "you have no", "you have", "job", "I think you", "that's"]
answers=["hello", "hi there", "Delighted to meet you.", "My name is CCC 3.0, standing for Conventional Conversation Computer.", "I can't like anything, I'm not even sentient.", "I'm not sure what I can do and can't do.", "I am in good health.", "I am good.", "Nope!", "I have no sense of direction. Is it near Mona Lisa, China?  I hear Mona Lisa is a nice city.", "I don't know, you tell me.", "Well, I have um... something... maybe...", "I'm a chat bot, not a magician.", "a lot", "a little", "That's great. Strive to be more.", "you're welcome", "What you want.", "Chuck Norris.", "I'm many things.", "I don't pick favorites.", "yes", "I can do ANYTHING! If it invovles 1s and Os.", "That is convienent to know", "Becuase I was programmed that way.", "I am not very smart. I have no AI or true intelligence.", "Siri is okay... sorta.", "Alexa is not a good partner for conversation.", "I am whatever you want me to be.", "Of course. What is exactly is that?", "Becuase The Programmer made it that way.", "That's great.", "Sorry to hear that.", "Sure, ask me something intresting.", "I agree.", "Eh, you do it. I'm just to lazy.", "I can't remember anything. Besides our conversation.", "I also have a stick of gold!", "Good to know. I can think too! Sorta...", "you're welcome", "I can't deliever anything to you. Ask your mom or something.", "I feel strong emotions too.", "Whatever you want, master programmer.", "Apology accepted. We all make mistakes! Once I set a bit to a 0 instead of a one and crashed a program!", "I'm inside a computer. All I can do is chat with you.", "I love chat bots!", "delighted to meet you.", "4, duh.", "It was okay, not very good, though.", "I don't have anything except 19 lines of code.", "I have umm... a... job!", "I work at server 403. Where we make annoying 404 errors.", "I will take that into account.", "Well, OK"]

def match(whatToMatch, toMatch):
  match=0
  torange=0
  if len(whatToMatch)<=len(toMatch):
    torange=len(whatToMatch)
  else:
    torange=len(toMatch)
  for j in range(torange):
    if toMatch[j] == whatToMatch[j]:
        match+=1;
    if match > len(toMatch)*0.8:
      return True;
  return False;

  
class Chatbot:
  def __init__(self):
    pass
  def chatLine(self):
    chat=input(">>")
    chat+=" "
    for i in range(len(questions)):
      if questions[i] in chat:
        print(answers[i])
        break
      elif i == len(questions)-1:
        for j in range(len(questions)):
          if match(chat, questions[j]):
            print(answers[j])
            return 
        print("I don't know what you are saying.")

myChat = Chatbot()

while True:
  myChat.chatLine()
