from _pytest.python_api import raises

from cisc179.Enemy import enemy

def testEnemy():
    test = enemy('Bugbear', 24, 16, 'This is neither a bear nor a bug. It is an angry hairy goblinoid. It is holding a mean-looking morningstar.', 'Morningstar', 4, 3, 18)

    assert test.getEnemyName() == 'Bugbear'
    assert test.getEnemyHP() == 24
    assert test.getEnemyAC() == 16
    assert test.getDescription() == 'This is neither a bear nor a bug. It is an angry hairy goblinoid. It is holding a mean-looking morningstar.'
    assert test.getAttackName() == 'Morningstar'
    assert test.getAttackBonus() == 4
    assert test.getMinAttackDamage() == 3
    assert test.getMaxAttackDamage() == 18

def testEnemyNameException():
    with raises(TypeError, match='Enemy Name must be a string at least 1 character long'):
        test= enemy(2, 32, 13, 'It seems to appear out of nowhere and quickly vanishes after attacking.', 'Bite', 4, 3, 12)
        test= enemy('', 32, 13, 'It seems to appear out of nowhere and quickly vanishes after attacking.','Bite', 4, 3, 12)
def testEnemyHPException():
    with raises(ValueError, match= 'Enemy HP must be an integer >0'):
        test= enemy('Phase Spider', -5, 13, 'It seems to appear out of nowhere and quickly vanishes after attacking.','Bite', 4, 3, 12)
        test= enemy('Phase Spider', 3.2, 13, 'It seems to appear out of nowhere and quickly vanishes after attacking.','Bite', 4, 3, 12)
def testEnemyACException():
    with raises(ValueError, match= 'Enemy AC must be an integer >0 and <20'):
        test= enemy('Phase Spider', 32, -13, 'It seems to appear out of nowhere and quickly vanishes after attacking.','Bite', 4, 3, 12)
        test= enemy('Phase Spider', 32, 1.3, 'It seems to appear out of nowhere and quickly vanishes after attacking.','Bite', 4, 3, 12)
        test= enemy('Phase Spider', 32, 25, 'It seems to appear out of nowhere and quickly vanishes after attacking.', 'Bite', 4, 3, 12)
def testEnemyDescriptionException():
    with raises(ValueError, match= 'Enemy Description must be a string less than 200 characters'):
        test= enemy('Phase Spider', 32, 13,'With the magical ability to phase in and out of the Ethereal Plane, it seems to appear out of nowhere and quickly vanishes after attacking. Its movement on the Ethereal Plane before coming back to the Material Plane makes it seem like it can teleport','Bite', 4, 3, 12)

def testEnemyAttackNameException():
    with raises(TypeError, match= 'Enemy Attack Name must be a string'):
        test= enemy('Phase Spider', 32, 13, 'It seems to appear out of nowhere and quickly vanishes after attacking.', 0, 4, 3, 12)
def testEnemyAttackBonusException():
    with raises(ValueError, match= 'Enemy Attack Bonus must be an integer between 0 to 10'):
        test= enemy('Phase Spider', 32, 13, 'It seems to appear out of nowhere and quickly vanishes after attacking.', 'Bite', 4.5, 3, 12)
        test= enemy('Phase Spider', 32, 13, 'It seems to appear out of nowhere and quickly vanishes after attacking.', 'Bite', -4, 3, 12)

def testMinAttackDamageException():
    with raises(ValueError, match= 'Enemy Minimum Attack Damage must be an integer greater than 0'):
        test= enemy('Phase Spider', 32, 13, 'It seems to appear out of nowhere and quickly vanishes after attacking.', 'Bite', 4, -3, 12)
        test= enemy('Phase Spider', 32, 13, 'It seems to appear out of nowhere and quickly vanishes after attacking.', 'Bite',4, 3.5, 12)

def testMaxAttackDamageException():
    with raises(ValueError, match= 'Enemy Maximum Attack Damage must be an integer greater than 0'):
        test= enemy('Phase Spider', 32, 13, 'It seems to appear out of nowhere and quickly vanishes after attacking.','Bite', 4, 3, 5.2)
        test= enemy('Phase Spider', 32, 13, 'It seems to appear out of nowhere and quickly vanishes after attacking.', 'Bite', 4, 3, -12)