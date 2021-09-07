import random
import math


#classes
#player character class/ hero class
class hero:
    def __init__(self, hHealth, hAttack, hSpeech, hRanged, hDefence, hIntel, hName):
        self.hp = hHealth
        self.atk = hAttack
        self.spc = hSpeech
        self.rng = hRanged
        self.dfc = hDefence
        self.ing = hIntel
        self.name = hName
    def getHp(self):
        return self.hp
    def getAtk(self):
        return self.atk
    def getSpc(self):
        return self.spc
    def getRng(self):
        return self.rng
    def getDfc(self):
        return self.dfc
    def getIng(self):
        return self.ing    
    def getName(self):
        return self.name
    def setHp(self, nHp):
        self.hp = nHp
    def setAtk(self, nAtk):
        self.atk = nAtk
    def setSpc(self, nSpc):
        self.spc = nSpc
    def setRng(self, nRng):
        self.rng = nRng
    def setDfc(self, nDfc):
        self.dfc = nDfc
    def setIng(self, nIng):
        self.ing = nIng
    inv = {
        'weapon': 'None',
        'clothes': 'Old Rags',
        'headwear': 'None',
        'items': []
    }
#End of Hero Class

#enemy class
class npc:
    def __init__(self, eHealth, eAttack, eSpecial, eChance, eName):
        self.hp = eHealth
        self.atk = eAttack
        self.spl = eSpecial
        self.chn = eChance
        self.name = eName
    def getHp(self):
        return self.hp
    def getAtk(self):
        return self.atk
    def getSpl(self):
        return self.spl
    def getChn(self):
        return self.chn
    def getName(self):
        return self.name
    def setHp(self, nHp):
        self.hp = nHp
    def setAtk(self, nAtk):
        self.atk = nAtk
    def setSpl(self, nSpl):
        self.spl = nSpl
    def setChn(self, nChn):
        self.chn = nChn
    def setName(self, nName):
        self.name = nName
#end of enemy class

#boss class
class boss(npc):
    def __init__(self, eHealth, eAttack, eSpecial, eChance, eName, bMove):
        super().__init__(eHealth, eAttack, eSpecial, eChance, eName)
        self.bMove = bMove
    def getBossMove(self):
        return self.bMove
    def setBossMove(self, nBMove):
        self.bMove = nBMove
#end of boss class

