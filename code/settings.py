SCREENWIDTH = 1200
SCREENHEIGHT = 800

doorDests = {"room 1":{(320, 64):{"room":"room 2","coords":(512, 576)}},
             "room 2":{(384, 64):{"room":"room 3","coords":(192, 384)},(640, 64):{"room":"room 16","coords":(192, 384)},(64, 320):{"room":"room 4","coords":(768, 960)},(960, 320):{"room":"room 10","coords":(64, 320)},(512, 576):{"room":"room 1","coords":(320, 128)}},
             "room 3":{(192, 384):{"room":"room 2","coords":(384, 128)}},
             "room 4":{(448, 64):{"room":"room 8","coords":(640, 640)},(768, 960):{"room":"room 2","coords":(64, 320)},(192, 1024):{"room":"path 1","coords":(640, 128)}},
             "room 5":{(320, 192):{"room":"path 1","coords":(64, 576)}},
             "room 6":{(512, 64):{"room":"room 7","coords":(256, 640)}},
             "room 7":{(64, 640):{"room":"room 9","coords":(256, 512)},(448, 320):{"room":"room 8","coords":(64, 384)},(256, 640):{"room":"room 6","coords":(512, 128)}},
             "room 8":{(448, 64):{"room":"room 9","coords":(256, 512)},(640, 64):{"room":None,"coords":None},(832, 64):{"room":None,"coords":None},(64, 384):{"room":"room 7","coords":(448, 320)},(640, 640):{"room":"room 4","coords":(448, 128)}},
             "room 9":{(256, 512):{"room":"room 8","coords":(448, 128)}},
             "room 10":{(256, 64):{"room":"room 11","coords":(320, 448)},(64, 320):{"room":"room 2","coords":(960, 320)},(448, 320):{"room":"path 2","coords":(64, 512)}},
             "room 11":{(320, 448):{"room":"room 10","coords":(256, 128)}},
             "room 12":{(448, 64):{"room":"path 3","coords":(448, 1088)},(64, 512):{"room":"path 2","coords":(1152, 512)},(448, 896):{"room":"path 4","coords":(128, 128)}},
             "room 13":{(768, 192):{"room":"path 3","coords":(64, 384)},(384, 1152):{"room":"path 2","coords":(640, 128)}},
             "room 14":{(64, 320):{"room":"room 15","coords":(1216, 384)},(640, 512):{"room":"path 3","coords":(448, 128)}},
             "room 15":{(1216, 386):{"room":"room 14","coords":(64, 320)}},
             "room 16":{(192, 384):{"room":"room 2","coords":(640, 128)}},
             "path 1":{(640, 64):{"room":"room 4","coords":(192, 1024)},(64, 576):{"room":"room 5","coords":(320, 192)}},
             "path 2":{(640, 64):{"room":"room 13","coords":(384, 1152)},(64, 512):{"room":"room 10","coords":(448, 320)},(1152, 512):{"room":"room 12","coords":(64, 512)}},
             "path 3":{(448, 64):{"room":"room 14","coords":(640, 512)},(64, 384):{"room":"room 13","coords":(768, 192)},(448, 1088):{"room":"room 12","coords":(448, 128)}},
             "path 4":{(128, 64):{"room":"room 12","coords":(448, 896)}}}

lootTable = {"room 3":"","room 5":"key","room 9":"golden idol","room 11":"clock of destiny","room 16":""}