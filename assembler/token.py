from util import *
#Take cmd in asm form (string), convert to object with cmd, args, and types
class Cmd:
    def __init__(self, cmd):
        self.asm = cmd
        self.cmd = ""
        self.args = []
        self.types = []
    #Add function to convert asm

#Gets CLEAN asm WITHOUT MACRO DEFINITIONS
class Tokenizer:
    def __init__(self, asm):
        self.asm = asm
        self.tokens = []
        self.cmds = []
        self.groupStarts = ['{', '('];
        self.groupEnds = ['}', '(']
    #Splits asm into cmds, doesnt split cmd args
    def getCmds(self):
        startI = 0
        groupDepth = 0
        for i in range(len(self.asm)):
            if self.asm[i] in self.groupStarts:
                groupDepth += 1
            if self.asm[i] in self.groupEnds:
                groupDepth -= 1
                if groupDepth < 0:
                    error("To many closing symbols", self.asm[startI:i+5])
            if self.asm[i] == ';' and groupDepth == 0:
                self.cmds.append(self.asm[startI:i])
                startI = i+1
        for i in self.cmds:
            self.tokens.append(Cmd(i))
        return self.tokens
