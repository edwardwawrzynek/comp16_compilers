import sys
import args, clean
import token
import compiler
import pre_proc

asmFile, outFile = args.getFiles()
asm = asmFile.read()
asm, macros = pre_proc.Preprocessor(asm).applyInstr()
asm = clean.Clean(asm).clean()
tokens = token.Tokenizer(asm).getCmds()
c = compiler.Compiler(tokens, outFile)
c.run()
print "Comp16 Assembler Finished Succesfully"
print str(outFile.tell()) + " bytes written"
if outFile.tell() == 0:
    print "Are you sure the file contains proper comp16 asm code?"
outFile.close()
