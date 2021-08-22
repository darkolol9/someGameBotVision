import pyautogui
from random import randint



class InterfaceManager:

    def goToInventory(self):
        self.getTabsWindow()
        # print(list(self.tabsWindow.values())[:-1])
        inv = pyautogui.locateOnScreen('classes/assets/inv.png',region=(list(self.tabsWindow.values())[:-1]),confidence =0.6)
        pyautogui.click((inv.left,inv.top,))

# 322
# 79

    def isFighting(self):
        return (self.isHit() or self.isHit() or self.isHit())

    def isHit(self):

        hit = pyautogui.locateOnScreen('classes/assets/def.png',
        confidence=0.60,region=(self.minimap['x'] - 322,
        self.minimap['y']+79,145,145))

        
        if (hit):
            return True

        else :
            return False


    def getTabsWindow(self):
        self.tabsWindow = {'x':pyautogui.locateOnScreen('classes/assets/tabs.png',confidence=0.7).left,
        'y':pyautogui.locateOnScreen('classes/assets/tabs.png',confidence=0.7).top,
        'w': 232,
        'h': 350
        }

        img =   pyautogui.screenshot(region=(self.tabsWindow['x'],
        self.tabsWindow['y'],
        self.tabsWindow['w'],
        self.tabsWindow['h'])  )

        self.tabsWindow['img'] = img  
        
    
    def goToCombat(self):
        randomSpeed =(randint(2,5))/10
        self.getTabsWindow()
        combatTab = pyautogui.locateOnScreen('classes/assets/tabs.png',region=(list(self.tabsWindow.values())[:-1]),confidence=0.6)
        pyautogui.moveTo(combatTab.left,combatTab.top,duration=randomSpeed)
        pyautogui.click()



        

    def getWorldChat(self):
        self.worldChat = {'x':pyautogui.locateOnScreen('classes/assets/worldChat.png',confidence=0.7).left,
        'y':pyautogui.locateOnScreen('classes/assets/worldChat.png',confidence=0.7).top - 145,
        'w': 518,
        'h': 145
        }
        
        img = pyautogui.screenshot(region=(self.worldChat['x'],
        self.worldChat['y'],
        self.worldChat['w'],
        self.worldChat['h']))

        self.worldChat['img'] = img
        


    def getMiniMap(self):

        self.minimap = {'x':pyautogui.locateOnScreen('classes/assets/minimap.png',confidence=0.7).left,
        'y':pyautogui.locateOnScreen('classes/assets/minimap.png',confidence=0.7).top -  17,
        'w': 213,
        'h': 161
        }
        
        img =   pyautogui.screenshot(region=(self.tabsWindow['x'],
        self.minimap['y'],
        self.minimap['w'],
        self.minimap['h'])  )

        self.minimap['img'] = img  



        
    def getComponenets(self):
        self.getTabsWindow()
        self.getMiniMap()
        self.getWorldChat()

        
    def prntInfo(self):
        print(self.tabsWindow)
        print(self.worldChat)
        print(self.minimap)
        



I = InterfaceManager()
I.getComponenets()
i = 0
print('starting')
while True:
    print(I.isFighting())


