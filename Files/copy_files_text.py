with open('Files/text.txt','r') as rf:
    with open('Files/text2.txt','a') as wf: #eikhane a use korle append hobe ar w use korle ager file override hoe copy paste hobe
        wf.write(rf.read())