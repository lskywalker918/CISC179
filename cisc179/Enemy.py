class enemyStat:
    def __init__(self, enemyName, enemyHP, enemyAC, description, attackName, attackBonus, minAttackDamage, maxAttackDamage):
        self.checkEnemyName(enemyName)
        self.checkEnemyHP(enemyHP)
        self.checkEnemyAC(enemyAC)
        self.checkEnemyDescription(description)
        self.checkAttackName(attackName)
        self.checkAttackBonus(attackBonus)
        self.checkMinAttackDamage(minAttackDamage)
        self.checkMaxAttackDamage(maxAttackDamage)

    def getEnemyName(self):
        return self.enemyName
    def checkEnemyName(self, newEnemyName):
        if len(str(newEnemyName)) <1:
            raise TypeError('Enemy Name must be a string at least 1 character long')
        self.enemyName= newEnemyName
    def getEnemyHP(self):
        return self.enemyHP
    def checkEnemyHP(self, newEnemyHP):
        if newEnemyHP <0 or not isinstance(newEnemyHP, int):
            raise ValueError('Enemy HP must be an integer >0')
        self.enemyHP= newEnemyHP
    def getEnemyAC(self):
        return self.enemyAC
    def checkEnemyAC(self, newEnemyAC):
        if newEnemyAC <0 or newEnemyAC >20 or not isinstance(newEnemyAC, int):
            raise ValueError('Enemy AC must be an integer >0 and <20')
        self.enemyAC= newEnemyAC
    def getDescription(self):
        return self.description
    def checkEnemyDescription(self, newEnemyDescription):
        if len(newEnemyDescription) >200 or not isinstance(newEnemyDescription, str):
            raise ValueError('Enemy Description must be a string less than 200 characters')
        self.description= newEnemyDescription
    def getAttackName(self):
        return self.attackName
    def checkAttackName(self, newAttackName):
        if not isinstance(newAttackName, str):
            raise TypeError('Enemy Attack Name must be a string')
        self.attackName= newAttackName
    def getAttackBonus(self):
        return self.attackBonus
    def checkAttackBonus(self, newAttackBonus):
        if newAttackBonus <0 or newAttackBonus >10 or not isinstance(newAttackBonus, int):
            raise ValueError('Enemy Attack Bonus must be an integer between 0 to 10')
        self.attackBonus= newAttackBonus
    def getMinAttackDamage(self):
        return self.minAttackDamage
    def checkMinAttackDamage(self, newMinAttackDamage):
        if newMinAttackDamage <0 or not isinstance(newMinAttackDamage, int):
            raise ValueError('Enemy Minimum Attack Damage must be an integer greater than 0')
        self.minAttackDamage= newMinAttackDamage
    def getMaxAttackDamage(self):
        return self.maxAttackDamage
    def checkMaxAttackDamage(self, newMaxAttackDamage):
        if newMaxAttackDamage <0 or not isinstance(newMaxAttackDamage, int):
            raise ValueError('Enemy Maximum Attack Damage must be an integer greater than 0')
        self.maxAttackDamage= newMaxAttackDamage