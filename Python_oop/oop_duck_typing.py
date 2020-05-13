#duck typing mane ekta class ar method ar moddhe apni jodi kono method call koren tahole python doesnot care which class it is and which type of class . care kore oi class or object ar moddhe oi method ta defined kora ace ki na.example niche
#jemon duck walk kore and duck duck kore temni horse walk kore bt tokbok tokbok kore kintu 2jonei walk kore otthat 2 joner e same mthod ace jodio 2 ta vinno jat r taporo 2 jon k duck bola jabe.

class mycham:
    
    def excute(self):
        print("My compile is running")
        print("My code is running")
    
class myeditor:
    def excute(self):
        print("Spell check")
        print("Conversation check")
        print("My compile is running")
        print("My code is running")

class Laptop:
    def code(self,ide):#ide ekta parameter eikhane jei class ar object pass kora hobe sei object er excute method kaj korbe. but seita kon class na kon typer it doesnot matter .matter kore j class r object pass korbo oi class oi excute method ta ace ki na
        ide.excute()        


lap=Laptop()
#ekhon kotha hossce code method excute korar jonno amke ekta ide argument pass korte hobe.otthat j kono class er object .ar ei object myeditor or mychamp j kono ekta holei hobe ete kono prblm nai but ami j object pass korbo oi object ar class er moddhe excute method must thakte hobe.
champ=mycham()
lap.code(champ)
#then ekn jodi myeditor er object pass o kori tahole myeditor r method kaj korbe.
editor=myeditor()
lap.code(editor)