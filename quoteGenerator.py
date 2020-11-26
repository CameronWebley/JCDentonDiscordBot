import random

class Word:
    def __init__(self, word):
        self.word = word
        self.succs = {} #holds all the successors of the word, and the frequency of those words

    def addSucc(self, succ):
        if succ in self.succs:
            self.succs[succ] += 1
        else:
            self.succs[succ] = 0

    def getRandomSucc(self):
        return random.choices(list(self.succs.keys()), list(self.succs.values()))[0]


class QuoteGenerator:
    def __init__(self):
        self.words = {} #Holds each word, and has a key value of it's object
        self.starts = set()

    def addWord(self, word):
        if not(word in self.words):
            self.words[word] = Word(word)

    def readFile(self, file):
        f = open(file, "r")
        script = f.read()
        f.close()
        return script

    def createScript(self, file):
        script = self.readFile(file)
        splitScript = script.split()
        script = self.cleanScript(splitScript)
        start = True
        for i in range(0, len(script)-1):
            self.addWord(script[i])
            if start == True:
                self.starts.add(script[i])
                start = False
            if script[i] in "!?.":
                start = True
            if i != len(script)-1 and not(script[i] in "!?,"):
                self.words[script[i]].addSucc(script[i+1])

    #Runs through the whole script and removes cases of commas, adds full stops, question marks, and exclamation marks as their whole words. Makes every word lowercase
    def cleanScript(self, script):
        cleanScript = []
        for i in range(0, len(script)-1):
            word = script[i]
            word = word.lower() #Makes the word lowercase
            if word[-1] in "!?.":
                cleanScript.append(word[:-1])
                cleanScript.append(word[-1])
            elif word[-1] in ",":
                cleanScript.append(word[:-1])
            else:
                cleanScript.append(word)
        return cleanScript

    def generateQuote(self, length=1):
        quote = ""
        for i in range(length):
            word = random.choice(list(self.starts))
            quote += word.capitalize()
            while not(word in "!?."):
                word = self.words[word].getRandomSucc()
                if word in "!?.":
                    quote += word
                else:
                    quote += " " + word
            quote += " "
        return quote