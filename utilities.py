#https://www.devdungeon.com/content/colorize-terminal-output-python

def readTextFile(filePath):
  """Opens the text file in supplied path and read the lines"""
  with open(filePath, 'r') as f:
    return ''.join([l.strip() for l in f.readlines()])
  
def writeTextFile(filePath, content, mode='w'):
  """Writes to file with selected mode"""
  with open(filePath, mode) as f:
    f.write(content + '\n')

def readFASTAFile(filePath):
  with open(filePath, 'r') as f:
    FASTAFile = [l.strip() for l in f.readlines()]

    FASTADict = {}
    FASTALabel = ""

    for line in FASTAFile:
      if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
      else:
        FASTADict[FASTALabel] += line
        
  return FASTADict