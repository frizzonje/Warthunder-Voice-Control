import sys
import keyboard
import mouse
import time
import random

class CommandHandler:
    def __init__(self, key_bindings, lang_support):
        self.key_bindings = key_bindings
        self.pressed_movement_keys = set()
        self.lang_support = lang_support

    def press_and_hold(self, key):
        if key not in self.pressed_movement_keys:
            keyboard.press(key)
            self.pressed_movement_keys.add(key)

    def release_key(self, key):
        if key in self.pressed_movement_keys:
            keyboard.release(key)
            self.pressed_movement_keys.remove(key)

    def release_all_movement(self):
        for key in list(self.pressed_movement_keys):
            keyboard.release(key)
        self.pressed_movement_keys.clear()
        print(self.lang_support.get_message('stopping'))

    def action_forward(self):
        self.release_key(self.key_bindings["back"])
        self.press_and_hold(self.key_bindings["forward"])
        print("Command: Forward" if self.lang_support.current_language == "en" else "Команда: Вперед")

    def action_back(self):
        self.release_key(self.key_bindings["forward"])
        self.press_and_hold(self.key_bindings["back"])
        print("Command: Back" if self.lang_support.current_language == "en" else "Команда: Назад")

    def _turn_action(self, direction, duration, is_hard=False):
        opposite = "right" if direction == "left" else "left"
        self.release_key(self.key_bindings[opposite])
        
        key = self.key_bindings[direction]
        keyboard.press(key)
        time.sleep(duration)
        keyboard.release(key)
        
        turn_type = "Hard" if is_hard else "Normal"
        direction_text = "Left" if direction == "left" else "Right"
        
        if self.lang_support.current_language == "en":
            print(f"Command: {turn_type} turn {direction_text.lower()}")
        else:
            strength = "Мощно" if is_hard else "Обычный"
            direction_ru = "влево" if direction == "left" else "вправо"
            print(f"Команда: {strength} поворот {direction_ru}")

    def action_left(self):
        self._turn_action("left", 0.5)
        
    def action_hard_left(self):
        self._turn_action("left", 0.6, True)

    def action_right(self):
        self._turn_action("right", 0.5)
        
    def action_hard_right(self):
        self._turn_action("right", 0.6, True)

    def action_straight(self):
        self.release_key(self.key_bindings["left"])
        self.release_key(self.key_bindings["right"])
        print("Command: Straight" if self.lang_support.current_language == "en" else "Команда: Прямо")

    def action_stop_all(self):
        self.release_all_movement()

    def action_handbrake(self):
        self.release_all_movement()
        keyboard.press(self.key_bindings["handbrake"])
        time.sleep(1.5)
        keyboard.release(self.key_bindings["handbrake"])
        print("Command: Handbrake" if self.lang_support.current_language == "en" else "Команда: Ручной тормоз")
    
    def fire_machinegun_burst(self):
        burst_type = random.choices(
            ['short', 'medium', 'long', 'double'],
            weights=[40, 30, 20, 10]
        )[0]
        
        key = self.key_bindings.get("machinegun", "space")
        
        if burst_type == 'short':
            duration = random.uniform(0.3, 0.5)
            print("Short burst..." if self.lang_support.current_language == "en" else "Короткая очередь...")
            keyboard.press(key)
            time.sleep(duration)
            keyboard.release(key)
        
        elif burst_type == 'medium':
            duration = random.uniform(0.6, 0.9)
            print("Medium burst..." if self.lang_support.current_language == "en" else "Длинная очередь...")
            keyboard.press(key)
            time.sleep(duration)
            keyboard.release(key)
        
        elif burst_type == 'long':
            duration = random.uniform(0.9, 1.5)
            print("Long burst..." if self.lang_support.current_language == "en" else "Продолжительная очередь...")
            keyboard.press(key)
            time.sleep(duration)
            keyboard.release(key)
        
        else:  # double
            print("Double burst..." if self.lang_support.current_language == "en" else "Двойная очередь...")
            for _ in range(2):
                keyboard.press(key)
                time.sleep(random.uniform(0.2, 0.3))
                keyboard.release(key)
                time.sleep(0.15)

    def _get_command_message(self, action_type, command_name, details=None):
        is_en = self.lang_support.current_language == "en"
        
        command_types = {
            'tank': ('Tank', 'Танк'),
            'movement': ('Movement', 'Движение'),
            'weapon': ('Weapon', 'Оружие'),
            'common': ('Common', 'Общая')
        }
        
        type_text = command_types.get(action_type, command_types['common'])
        type_str = type_text[0] if is_en else type_text[1]
        
        if details:
            return f"Command: {type_str} - {command_name} ({details})" if is_en else f"Команда: {type_str} - {command_name} ({details})"
        return f"Command: {type_str} - {command_name}" if is_en else f"Команда: {type_str} - {command_name}"

    def _execute_key_action(self, key, duration=0.1, hold=False):
        if isinstance(key, str) and '+' in key:
            keys = key.split('+')
            for k in keys[:-1]:
                keyboard.press(k)
            keyboard.press(keys[-1])
            time.sleep(duration)
            keyboard.release(keys[-1])
            for k in reversed(keys[:-1]):
                keyboard.release(k)
        else:
            if hold:
                keyboard.press(key)
            else:
                keyboard.press(key)
                time.sleep(duration)
                keyboard.release(key)

    def single_press(self, key_name, duration=0.1, action_type='common'):
        key = self.key_bindings.get(key_name)
        if not key:
            print(f"No binding for {key_name}")
            return
        command_name = key_name.replace('_', ' ').title()

        if key_name == "scope":
            self._execute_key_action(key, 0.5)
            msg = 'Sniper Mode' if self.lang_support.current_language == "en" else 'Снайперский режим'
            print(self._get_command_message('weapon', msg))
            
        elif key_name == "fire":
            mouse.press('left')
            time.sleep(duration)
            mouse.release('left')
            msg = 'Fire' if self.lang_support.current_language == "en" else 'Выстрел'
            print(self._get_command_message('weapon', msg))
            
        elif key_name == "machinegun":
            self.fire_machinegun_burst()
            
        elif key_name == "smoke_tank":
            self._execute_key_action(key, 0.3)
            msg = 'Smoke Screen' if self.lang_support.current_language == "en" else 'Дымовая завеса'
            print(self._get_command_message('tank', msg))
            
        elif key in ['left', 'right', 'middle']:
            mouse.press(key)
            time.sleep(duration)
            mouse.release(key)
            print(self._get_command_message(action_type, command_name))            
        else:
            self._execute_key_action(key, duration)
            print(self._get_command_message(action_type, command_name))
    
    def action_rage_quit(self):
        print("Command: RAGE QUIT!" if self.lang_support.current_language == "en" else "Команда: ГОСПОДИ, ВЫХОДИМ!")
        keyboard.press(self.key_bindings["rage_quit_1"])
        keyboard.press(self.key_bindings["rage_quit_2"])
        time.sleep(0.1)
        keyboard.release(self.key_bindings["rage_quit_2"])
        keyboard.release(self.key_bindings["rage_quit_1"])
        time.sleep(0.5)
        keyboard.press_and_release('enter')

    def exit_script(self):
        print(self.lang_support.get_message('closing'))
        sys.exit()

    def action_missile_lock_mouse(self):
        print("Command: Missile Lock (MMB)" if self.lang_support.current_language == "en" else "Команда: Захват цели ракетой (СКМ)")
        mouse.press('middle')
        time.sleep(0.1)
        mouse.release('middle')

    def get_commands_dict(self):
        commands = self.lang_support.get_commands()
        if not commands:
            return {}
        
        all_commands = {}
        for category in commands:
            for cmd, phrases in commands[category].items():
                func = self._get_command_function(cmd, category)
                if func:
                    all_commands[tuple(phrases)] = func
        return all_commands
    
    def _get_command_function(self, cmd, category):
        func_map = {
            'menu': lambda: self.single_press("menu"),
            'fire': lambda: self.single_press("fire", duration=0.2),
            'machinegun': lambda: self.single_press("machinegun"),
            'scope': lambda: self.single_press("scope"),
            'binoculars': lambda: self.single_press("binoculars"),
            'rage_quit': self.action_rage_quit,
            'exit': self.exit_script,
            'forward': self.action_forward,
            'back': self.action_back,
            'left': self.action_left,
            'right': self.action_right,
            'hard_left': self.action_hard_left,
            'hard_right': self.action_hard_right,
            'straight': self.action_straight,
            'stop': self.action_stop_all,
            'handbrake': self.action_handbrake,
            'smoke': lambda: self.single_press("smoke_tank", action_type='tank'),
            'repair': lambda: self.single_press("repair", action_type='tank'),
            'extinguisher': lambda: self.single_press("fire_extinguisher", action_type='tank'),
            'artillery': lambda: self.single_press("artillery", action_type='tank'),
            'tow_cable': lambda: self.single_press("tow_cable", action_type='tank'),
            'rangefinder': lambda: self.single_press("rangefinder", action_type='tank'),
            'thermal': lambda: self.single_press("thermal_vision", action_type='tank'),
            'atgm': lambda: self.single_press("atgm_launch_tank", action_type='tank'),
            'shell_1': lambda: self.single_press("shell_1", action_type='tank'),
            'shell_2': lambda: self.single_press("shell_2", action_type='tank'),
            'shell_3': lambda: self.single_press("shell_3", action_type='tank'),
            'shell_4': lambda: self.single_press("shell_4", action_type='tank'),
            'toggle': lambda: self.single_press("drone_toggle"),
            'lock': lambda: self.single_press("drone_lock_target"),
            'orbit': lambda: self.single_press("drone_orbit"),
            'mark': lambda: self.single_press("drone_mark_target"),
            'gear': lambda: self.single_press("landing_gear"),
            'flaps': lambda: self.single_press("flaps"),
            'airbrake': lambda: self.single_press("air_brake"),
            'radar': lambda: self.single_press("radar_lock"),
            'missile_lock': self.action_missile_lock_mouse,
            'missile': lambda: self.single_press("missile_launch_plane"),
            'weapon': lambda: self.single_press("weapon_selector"),
            'bombs': self.drop_bombs,
        }
        return func_map.get(cmd)

    def drop_bombs(self):
        print("Command: Carpet bombing" if self.lang_support.current_language == "en" else "Команда: Ковровая бомбардировка")
        key = self.key_bindings.get("bomb_dropping")
        if not key:
            print("No binding for bomb_dropping")
            return
            
        for _ in range(10):
            keyboard.press(key)
            time.sleep(0.05)
            keyboard.release(key)
            time.sleep(0.05)