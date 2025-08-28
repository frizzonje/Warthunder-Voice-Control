class LanguageSupport:
    MESSAGES = {
        'ru': {
            'startup': "Запуск голосового управления для War Thunder.",
            'select_language': "Выберите язык/Select language:\n1. Русский\n2. English\nВведите номер/Enter number (1/2): ",
            'invalid_choice': "Неверный выбор. Попробуйте снова.",
            'calibration': "Калибровка под фоновый шум... Пожалуйста, помолчите пару секунд.",
            'calibration_complete': "Калибровка завершена. Готов к работе.",
            'available_commands': "Доступны команды для танка, самолета и дрона.",
            'exit_hint': "Скажите 'выход' чтобы завершить программу.",
            'listening': "Слушаю...",
            'command_not_found': "Команда не найдена.",
            'loading_error': "Ошибка загрузки settings.json: {}",
            'config_error': "Убедитесь, что файл settings.json существует и содержит правильные настройки.",
            'recognition_error': "Ошибка сервиса распознавания Google: {}",
            'unexpected_error': "Произошла непредвиденная ошибка: {}",
            'stopping': "Движение остановлено.",
            'closing': "Завершаю работу голосового управления..."
        },
        'en': {
            'startup': "Starting voice control for War Thunder.",
            'select_language': "Select language/Выберите язык:\n1. Русский\n2. English\nEnter number/Введите номер (1/2): ",
            'invalid_choice': "Invalid choice. Try again.",
            'calibration': "Calibrating for background noise... Please remain silent for a few seconds.",
            'calibration_complete': "Calibration complete. Ready to work.",
            'available_commands': "Commands available for tank, aircraft and drone.",
            'exit_hint': "Say 'exit' to close the program.",
            'listening': "Listening...",
            'command_not_found': "Command not found.",
            'loading_error': "Error loading settings.json: {}",
            'config_error': "Make sure settings.json exists and contains correct settings.",
            'recognition_error': "Google Speech Recognition service error: {}",
            'unexpected_error': "An unexpected error occurred: {}",
            'stopping': "Movement stopped.",
            'closing': "Closing voice control..."
        }
    }

    COMMANDS = {
        'ru': {
            'movement': {
                'forward': ["вперед", "полный вперед", "газ"],
                'back': ["назад", "взад", "задний ход"],
                'left': ["лево", "влево", "налево"],
                'right': ["право", "вправо", "направо"],
                'hard_left': ["поворот налево", "резко влево", "мощный поворот налево"],
                'hard_right': ["поворот направо", "резко вправо", "мощный поворот направо"],
                'straight': ["прямо", "ровно"],
                'stop': ["стоп", "стой"],
                'handbrake': ["тормоз", "ручник"]
            },
            'common': {
                'menu': ["меню"],
                'fire': ["выстрел", "огонь", "пли"],
                'machinegun': ["пулемёт", "пулемет", "очередь"],
                'scope': ["прицел", "снайпер"],
                'binoculars': ["бинокль", "гляделка"],
                'rage_quit': ["заебало", "остопиздело", "остоебенило", "достало", "выйти из игры"],
                'exit': ["выход", "завершить программу", "закрыть программу"]
            },
            'tank': {
                'smoke': ["дым", "дымы"],
                'repair': ["ремонт", "починка"],
                'extinguisher': ["пожар", "туши"],
                'artillery': ["арта", "артиллерия"],
                'tow_cable': ["трос", "крюк"],
                'rangefinder': ["дальномер", "замер"],
                'thermal': ["тепловизор", "тепляк"],
                'atgm': ["птур", "пуск"],
                'shell_1': ["снаряд один", "первый снаряд"],
                'shell_2': ["снаряд два", "второй снаряд"],
                'shell_3': ["снаряд три", "третий снаряд"],
                'shell_4': ["снаряд четыре", "четвертый снаряд"]
            },
            'drone': {
                'toggle': ["дрон запуск", "дрон возврат", "дрон"],
                'lock': ["дрон захват"],
                'orbit': ["дрон круг", "дрон барражирование"],
                'mark': ["дрон цель", "дрон отметка"]
            },
            'aircraft': {
                'gear': ["шасси", "убрать шасси", "выпустить шасси"],
                'flaps': ["закрылки", "выпустить закрылки", "убрать закрылки"],
                'airbrake': ["воздушный тормоз"],
                'radar': ["радар захват", "захват радаром"],
                'missile_lock': ["ракета захват", "захват ракетой"],
                'missile': ["пуск ракеты", "ракета", "ракеты"],
                'weapon': ["селектор", "выбор вооружения"],
                'bombs': ["сброс", "бомбы", "сброс бомб", "сбросить бомбы"]
            }
        },
        'en': {
            'movement': {
                'forward': ["forward", "move forward", "go forward", "advance"],
                'back': ["back", "backward", "reverse"],
                'left': ["left", "turn left"],
                'right': ["right", "turn right"],
                'hard_left': ["hard left", "sharp left", "strong turn left"],
                'hard_right': ["hard right", "sharp right", "strong turn right"],
                'straight': ["straight", "center"],
                'stop': ["stop", "halt"],
                'handbrake': ["handbrake", "hand brake"]
            },
            'common': {
                'menu': ["menu"],
                'fire': ["fire", "shoot", "attack"],
                'machinegun': ["machine gun", "mg", "spray"],
                'scope': ["scope", "sniper mode", "sniper"],
                'binoculars': ["binoculars", "binocs"],
                'rage_quit': ["rage quit", "i'm done", "i am done", "exit game"],
                'exit': ["exit program", "close program", "terminate", "exit"]
            },
            'tank': {
                'smoke': ["smoke", "smoke screen"],
                'repair': ["repair", "fix"],
                'extinguisher': ["fire extinguisher", "extinguisher"],
                'artillery': ["artillery", "arty"],
                'tow_cable': ["tow cable", "tow"],
                'rangefinder': ["rangefinder", "range"],
                'thermal': ["thermal vision", "thermals"],
                'atgm': ["atgm", "guided missile"],
                'shell_1': ["shell one", "first shell"],
                'shell_2': ["shell two", "second shell"],
                'shell_3': ["shell three", "third shell"],
                'shell_4': ["shell four", "fourth shell"]
            },
            'drone': {
                'toggle': ["drone toggle", "drone launch", "drone return"],
                'lock': ["drone lock", "drone target"],
                'orbit': ["drone orbit", "drone circle"],
                'mark': ["drone mark", "mark target"]
            },
            'aircraft': {
                'gear': ["landing gear", "gear"],
                'flaps': ["flaps"],
                'airbrake': ["air brake", "airbrake"],
                'radar': ["radar lock", "lock radar"],
                'missile_lock': ["missile lock", "lock missile"],
                'missile': ["launch missile", "missile", "missiles"],
                'weapon': ["weapon select", "select weapon"],
                'bombs': ["drop bombs", "bombs", "release bombs"]
            }
        }
    }

    def __init__(self):
        self.current_language = None

    def select_language(self):
        while True:
            choice = input(self.MESSAGES['en']['select_language'])
            if choice == '1':
                self.current_language = 'ru'
                return 'ru'
            elif choice == '2':
                self.current_language = 'en'
                return 'en'
            print(self.MESSAGES['en']['invalid_choice'])

    def get_message(self, key, *args):
        lang = self.current_language or 'en'
        message = self.MESSAGES[lang].get(key, key)
        return message.format(*args) if args else message

    def get_commands(self):
        return self.COMMANDS.get(self.current_language, {})