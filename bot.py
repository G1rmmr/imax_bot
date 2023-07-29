#imports
import telepot

class Bot:
    # Functions
    def __init__(self):
        self.token = "6504666984:AAG9_Y3da_gMsnM4_uV95gjoh1_MNdTOo5U"
        self.bot = telepot.Bot(self.token)

    # Self msg
    def sendSelf(self, msg):
        self.id = "6575375569"
        self.bot.sendMessage(self.id, msg)