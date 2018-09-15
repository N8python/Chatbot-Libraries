mport time
import re
import random
questions=["hi ", "hello", "hey", "your name", "do you like", "do you want", "do you need", "do you", "how are you", "what's up", "what about", "where is", "what is", "how much", "how many", "you are", "sit in my lap", "meow", "what can you do", "thank you", "what are you", "yay", "purr", "will be okay", "ok ", "kitty"]
answers=["hello", "hi there", "Delighted to meet you.", "My name is Catbot.", "I like mice and milk. Snuggles too! But nothing else. Except food. And water. And...", "I want to be fed", "I need ummm... A virtual liter box!", "I can do some things...", "I am in good health.", "I am good.", "Nope!", "In Catworld! For there is no other place worthy of mention!", "I don't know, you tell me.", "a lot", "a little", "I'm cat. Nothing else. Look up cat on Wikipedia if you want to know what I am.", "Of course *Purr*", "meow to you too!", "I can do anything, as long as I am lying down.", "You're welcome, human.",  "I am... The domestic cat (Felis silvestris catus or Felis catus) is a small, typically furry, carnivorous mammal. They are often called house cats when kept as indoor pets or simply cats when there is no need to distinguish them from other felids and felines.", "WOOHOO!",  "PURRRRRRRRRrrrrrrrr...", "Glad to hear it.", "lol", "Mini me!"]
answers2=["hi there", "g'day, mate", "Hey there. How are you?", "I go by Catbot.", "I like rubs...", "I want to eat some cat food.", "I need a nice bowl of milk.", "I don't think I do. I might be wrong.", "I am okay... I haven't talked to anyone in days.", "I'm good. I'm rocking it out!", "Meow no!", "I don't know where that is. Maybe you should Google it.", "What? I don't think what you said has anything to do with cats.", "I am a cat and a bad actor. Nothing else.", "Coming. Ummm.. How do you bust out of a computer?", "meow is a fine sound of the Gods.", "I am a SUPERCAT. I can do anything! If it involves walking less than 5 feet.", "Of course.", "I am a cat! YOU KNOW THAT!", "YAY! *clap clap*", "I love to PURRRRrrrrarrr.....", "*Whew*", "Ok to you too.", "Baby cats!"]
answers2.insert(13, "a bit")
answers2.insert(14, "a significant amount")
adv_q = ["what is", "I am", "I like", "would you like", "I want", "I have", "are you", "Do you like", "do you like", "I don't want, ", "How do I make you "]
adv_a = [" I don't know anything about ", " I don't think you're ", " I also like ", "I would like ", " I'm a cat, not a magician. I can't just conjure ", " Well, all I have is a ball. I don't have ", " I am not ", " I love ", " I dislike ", " Well, I don't want ", "I already am "]
dont_know = ["Let's talk about something a bit more... cat related.", "I'm just a cat. I'm not going to know much stuff outside of things having to do with cats.", "I don't think what you said has much to do with cats. Let's go back to cats... and ME!", "Let's talk about cats. Rubbing. Cat Food. etc."]
command=""
answerType=1
codeMode=False
def check():
  global answerType
  for i in range(len(questions)):
    if questions[i] in command:
      if answerType==1:
        print(cat + " " + answers[i])
        answerType=2
      else:
        print(cat + " " + answers2[i])
        answerType=1
      return True
    elif i == len(questions):
      return False
def parse_string(whatToParse, toParse, addTo):
  toParse = toParse[toParse.rindex(whatToParse)+len(whatToParse):len(toParse)]
  return re.sub(' +', ' ', addTo + toParse)
def adv_check():
  for i in range(len(adv_q)):
    if adv_q[i] in command:
      print(cat + parse_string(adv_q[i], command, adv_a[i]))
      return True
    elif i == len(adv_q)-1:
      return False
cat = "🐱"
happyCat = "😺"
veryHappyCat = "😸"
estaticCat = "😹"
loveCat = "😻"
human = "👦"
print(cat + " Hello User!")
time.sleep(0.5)
print(cat + " Welcome to CAT WORLD!")
time.sleep(0.5)
#print(cat + " Your job is to make me HAPPY!")
while True:
  command = input(human + " ")
  command+=" "
  command= " " + command
  command=command.lower()
  command = command.replace(" i ", " I ")
  if codeMode:
    if "/exit" in command:
      print(cat + " Exiting shell...")
      time.sleep(0.5)
      print(cat + " Back into chat mode!")
      codeMode=False
    elif "open" in command:
      if "help" in command:
        print(cat + " Here is a list of helpful commands: 'open q' for list of questions, 'open a' for list of answers, 'open a2' to open the second list of answers, '/exit' to leave the shell.")
      elif "q" in command:
        print(cat, questions)
      elif "a2" in command:
        print(cat, answers2)
      elif "a" in command:
        print(cat, answers)
    elif "add" in command:
      if "qa" in command:
        q = input(cat + " Enter question:")
        a = input(cat + " Enter answer:")
        a2 = input(cat + " Enter second answer:")
        print(cat + " Inputing q and a...")
        questions.append(q)
        answers.append(a)
        answers2.append(a2)
        time.sleep(1)
        print(cat + " Done!")

    elif "help" in command:
      print(cat + " Try 'open help' for a list of commands.")
    else:
      print(cat + " Error, no Catterscript found.")
  elif "food" in command or "water" in command or "milk" in command:
    if "cat" in command:
      if "food" in command:
        print(cat + " I love cat food! Yum!")
      elif "water" in command:
        print(cat + " WATER! Must drink water...")
      elif "milk" in command:
        print(cat + " Milk is good, but not too much. Too much milk is bad for me!")
    elif "human" in command:
      print(cat + " I like hot dogs.... and soda...")
    else:
      if "food" in command:
        print(cat + " I don't eat non-cat food.")
      elif "water" in command:
        print(loveCat + " WATER! I love water!")
      elif "milk" in command:
        print(estaticCat + " Milk! Milk! More! More!")
  elif "fish" in command:
    if "eat" in command:
      print(veryHappyCat + " fish! nom nom!!!")
    else:
      print(happyCat + " I love to eat fish!") 
  elif "cuddle" in command or "snuggle" in command:
    if "me" in command:
      print(cat + " No! You cuddle me!")
    else:
      print(cat + " I love snuggle time!")
  elif "pet" in command:
    if "you" in command or "cat" in command:
      print(loveCat + " Pet me... Pet me... Love being pet...")
    elif "me" in command:
      print(cat + " It's the other way around. Cats don't pet humans.")
    else:
      print(cat + " Pet who? Petting is good, though! Pet me!")
  elif "dog" in command:
    if "like" in command:
      print(cat + " Me? LIKE DOGS? You must be kidding.")
    elif "don't like" in command or "not" in command:
      print(cat + " Of course I don't like dogs!")
    else:
      print(cat + " I can't even bear thinking about dogs. Let's talk about something else.")
  elif "mouse" in command or "mice" in command:
    if "eat" in command:
      print(loveCat + " I LOVE EATING MICE!")
    else:
      print(estaticCat + " Mice... Hungry... Yum! *Dxrool*")
  elif "rub" in command:
    print(loveCat + " I love cat rubs! Rub me, Rub me!")
  elif "cat" in command or "you" in command and not "are" in command and not "want" in command:
    if "give" in command:
      if "toy" in command:
        print(cat + " Toys! Fun! Games! But I don't like yarn. How about a game of monopoly? *Meow*")
      elif "rub" in command:
        print(loveCat + " Rubs, ahh, nice, relaxing, more, more, *Purr*")
      else:
        if(adv_check()):
          continue
        else:
          if(check()):
            continue
          else:
            print(cat + " " + dont_know[random.randint(0, len(dont_know)-1)])
    else:
      if(adv_check()):
        continue
      else:
        if(check()):
          continue
        else:
          print(cat + " " + dont_know[random.randint(0, len(dont_know)-1)])
  elif "toy" in command:
    print(estaticCat + " Ooh! Ooh! I love playing with little fluffy things! Or squishy balls.")
  elif "hair" in command:
    if "clean" in command:
      print(cat + " No clean hair! Hair is good!")
    else:
      print(happyCat + " I get hair all over anyone I touch!")
  elif "/admin" in command:
    print(cat + " Catterscript shell loading...")
    time.sleep(1)
    print(cat + " Shell open!")
    codeMode=True;
  elif "no " in command: 
    print(cat + " Well that's a shame.")
  elif "yes" in command:
    print(cat + " Okay. Now let's get back to me!")
  elif "name is" in command and not "your" in command:
    print(cat + parse_string("name is", command, " Well, hello "))
  elif "names" in command and not "your" in command:
    print(cat + parse_string("names", command, " Well, hello "))
  elif "name" in command and not "your" in command:
    print(cat + parse_string("name", command, " Well, hello "))
  elif "what are you" in command:
    print(cat + " I am... The domestic cat (Felis silvestris catus or Felis catus) is a small, typically furry, carnivorous mammal. They are often called house cats when kept as indoor pets or simply cats when there is no need to distinguish them from other felids and felines.")
  elif "how are you" in command:
    if answerType==1:
      print(cat + " I am in good health.")
      answerType=2
      continue
    else:
      print(cat + " I am okay... I haven't talked to anyone in days.")
      answerType=1
      continue
  else:
    if(adv_check()):
      continue
    else: 
      if(check()):
        continue
      else:
        print(cat + " " + dont_know[random.randint(0, len(dont_know)-1)])
