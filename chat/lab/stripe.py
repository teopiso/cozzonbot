import os
import re
def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    lines = os.path.join(dir_path, "girodelviso.txt")
    quotes = os.path.join(dir_path, "QUOTES")
    tag= os.path.join(dir_path, "tag2.txt")
    fr = open(lines, encoding="utf8")
    fwq= open(quotes ,"w", encoding="utf8")
    fwt= open(tag ,"w", encoding="utf8")
    header = r'\[[^\]]*\]'
    at = r'[@]\w+'
    for line in fr.readlines():
        if line.strip() and ("Davide Cozzi" in line):
            line= line.replace("Davide Cozzi: " , "")
            line= line.replace("." , "")
            line=re.sub(header, '', line)
            line=re.sub(at, '@', line)
            if line[0]== (" ") and len(line.split())>1:
                line=line.strip()
                if "@" in line:
                    fwt.write(line+'\n')
                else:
                    fwq.write(line+'\n')

    fr.close()
    fwq.close()
    fwt.close()
            
if __name__ == "__main__": main() 