import bpy
import bge


def main():

    cont = bge.logic.getCurrentController()
    
    #controller cube vars
    contCube = cont.owner  
    charMotion = bge.constraints.getCharacter(contCube)
    
    #getPowerUpCollisions
    pointCol = cont.sensors["pointCol"]
    camChangeCol = cont.sensors["camChangeCol"]
    timeChangeCol = cont.sensors["timeChangeCol"]
    #gravChangeCol = cont.sensors["graveChangeCol"]
    deathCol = cont.sensors["deathCol"]
    
    #get score sensor/actuator
    scoreAlways = cont.sensors["scoreAlways"]
    addOne = cont.actuators["addOne"]
    addTen = cont.actuators["addTen"]
    subHund = cont.actuators["subHund"]
    
    #beat armature vars
    Beat0= cont.actuators["Beat0"]
    Beat1= cont.actuators["Beat1"]
    Beat2= cont.actuators["Beat2"]


    #get scene actuators
    endGame = cont.actuators["endGame"]
    setCam0 = cont.actuators["setCam0"]
    setCam1 = cont.actuators["setCam1"]
    
    #background spawners
    armSpawn = cont.sensors["armSpawn"]
    spawnArm0 = cont.actuators["spawnArm0"]
    spawnArm1 = cont.actuators["spawnArm1"]
    spawnArm2 = cont.actuators["spawnArm2"]
    spawnSpin0 = cont.actuators["spawnSpin0"]
    spawnSpin1 = cont.actuators["spawnSpin1"]
    spawnSpin2 = cont.actuators["spawnSpin2"]
    spawnStar0 = cont.actuators["spawnStar0"]
    spawnStar1 = cont.actuators["spawnStar1"]
    spawnStar2 = cont.actuators["spawnStar2"]
    spawnBig0 = cont.actuators["spawnBig0"]
    spawnBig1 = cont.actuators["spawnBig1"]

    #sens = cont.sensors['mySensor']
    #actu = cont.actuators['myActuator']
    
    keyboard = bge.logic.keyboard
    activated = bge.logic.KX_INPUT_ACTIVE
    justActivated = bge.logic.KX_INPUT_JUST_ACTIVATED
    released = bge.logic.KX_INPUT_NONE
    justReleased = bge.logic.KX_INPUT_JUST_RELEASED
    
#    wKey = activated == keyboard.events[bge.events.WKEY]
#    sKey = activated == keyboard.events[bge.events.SKEY]
    aKey = activated == keyboard.events[bge.events.AKEY]
    dKey = activated == keyboard.events[bge.events.DKEY]
#    lShift = activated == keyboard.events[bge.events.LEFTSHIFTKEY]
    
#    wKeyTap = justActivated == keyboard.events[bge.events.WKEY]
#    sKeyTap = justActivated == keyboard.events[bge.events.SKEY]
    aKeyTap = justActivated == keyboard.events[bge.events.AKEY]
    dKeyTap = justActivated == keyboard.events[bge.events.DKEY]
    spaceTap = justActivated == keyboard.events[bge.events.SPACEKEY]
#    lShiftTap = justActivated == keyboard.events[bge.events.LEFTSHIFTKEY]
    
#    wKeyRel = released == keyboard.events[bge.events.WKEY]
#    sKeyRel = released == keyboard.events[bge.events.SKEY]
    aKeyRel = released == keyboard.events[bge.events.AKEY]
    dKeyRel = released == keyboard.events[bge.events.DKEY]
#    lShiftRel = released == keyboard.events[bge.events.LEFTSHIFTKEY]
    
#    lShiftJRel = justReleased == keyboard.events[bge.events.LEFTSHIFTKEY]  
                
    
    #motion code
    movSpeed = 0.175
    
    #motion    
    if aKey:
        charMotion.walkDirection =  [-movSpeed,0,0]   
        
    elif dKey:
        charMotion.walkDirection =  [movSpeed,0,0]  
        
    elif (aKeyRel or dKeyRel):
        charMotion.walkDirection = [0,0,0]
            
    if charMotion.onGround: 
        if spaceTap:
            charMotion.jump()
            
    
            
    #death and score        
    if deathCol.positive:
        contCube["score"] = contCube["score"] - 100
        contCube["lives"] = contCube["lives"] -1
        charMotion.walkDirection = [0,0,18]
        
        cont.activate(subHund)
        
    if pointCol.positive:
        contCube["score"] = contCube["score"] + 10
        cont.activate(addTen)
    
    if scoreAlways.positive:
        contCube["score"] = contCube["score"] + 1
        cont.activate(addOne)
    #background spawning
        if contCube["score"] > 200:
            cont.activate(spawnSpin0)
            #cont.activate(spawnSpin1)
            cont.activate(spawnSpin2)
            
    if (contCube["score"] >= 100 and armSpawn.positive):
            cont.activate(spawnArm0)
            cont.activate(spawnArm1)
            cont.activate(spawnArm2)
            
    if (contCube["score"] >= 400 and armSpawn.positive):
            cont.activate(spawnStar0)
            cont.activate(spawnStar1)
            cont.activate(spawnStar2)
            
    if (contCube["score"] >= 600 and armSpawn.positive):
            cont.activate(spawnBig0)
            cont.activate(spawnBig1)
            
        
    #camera move power up
    if camChangeCol.positive:
        contCube["time"] = 10
        cont.activate(setCam1)

    if contCube["time"] >= 20:
        cont.deactivate(setCam1)
        cont.activate(setCam0)
    
    #lives Speaker Arm and End scene stuff        
    if contCube["lives"] == 3:
        cont.activate(Beat0)
        
    elif contCube["lives"] == 2:
        cont.deactivate(Beat0)
        cont.deactivate(Beat2)
        cont.activate(Beat1)
        cont.deactivate(Beat2)
        
    elif contCube["lives"] == 1:
        cont.deactivate(Beat0)
        cont.deactivate(Beat1)
        cont.activate(Beat2)
        
        
    elif contCube["lives"] == 0:
        #bge.logic.globalDict["SCORE"] = contCube["score"]
        cont.deactivate(setCam0) 
        cont.deactivate(setCam1) 
        cont.activate(endGame)
            
        
            


main()