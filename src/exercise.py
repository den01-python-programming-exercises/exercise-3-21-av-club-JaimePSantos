def main():
    #write your code below this line
    strList = []
    while(True):
      strInput = input()
      pieces = strInput.split(" ")
      if(strInput==""):
        break
      strList.append(strInput)
      for piece in pieces:
        if("av" in piece):
          print(piece)

if __name__ == '__main__':
    main()
