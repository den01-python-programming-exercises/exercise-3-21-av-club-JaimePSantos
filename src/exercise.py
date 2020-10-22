def main():
    #write your code below this line
    strList = []
    while(True):
      strInput = input()
      if(strInput==""):
        break
      strList.append(strInput)

    for strinT in strList:
      pieces = strinT.split(" ")
      for substrinT in pieces:
        if("av" in substrinT):
          print(substrinT)

if __name__ == '__main__':
    main()
