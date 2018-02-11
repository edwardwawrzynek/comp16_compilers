import sys
import args, clean
import token
import compiler

asmFile, outFile = args.getFiles()
asm = asmFile.read()
asm = clean.Clean(asm).clean()
tokens = token.Tokenizer(asm).getCmds()
c = compiler.Compiler(tokens, outFile)
c.run()
print "Comp16 Assembler Finished Succesfully"
print str(outFile.tell()) + " bytes written"
