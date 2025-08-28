import speech_recognition as sr
import sys
import json
import os
from fuzzywuzzy import fuzz
from utils.commands import CommandHandler  # Adjust imports to your structure
from utils.language import LanguageSupport

PAUSE_THRESHOLD = 0.7
PHRASE_TIME_LIMIT = 3.0
ENERGY_THRESHOLD = 300
MATCH_THRESHOLD = 80

def load_settings():
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config', 'settings.json'))
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            settings = json.load(f)
            if 'KEY_BINDINGS' not in settings:
                raise KeyError("KEY_BINDINGS not found in settings.json")
            return settings['KEY_BINDINGS']
    except FileNotFoundError:
        print("Error: settings.json not found in config directory")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: settings.json is not a valid JSON file")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

def listen_and_process(recognizer, commands, lang_support):
    try:
        with sr.Microphone() as source:
            print(lang_support.get_message('listening'))
            audio = recognizer.listen(source, timeout=5.0, phrase_time_limit=PHRASE_TIME_LIMIT)

        lang_code = "ru-RU" if lang_support.current_language == "ru" else "en-US"
        text = recognizer.recognize_google(audio, language=lang_code).lower()
        if lang_support.current_language == 'ru':
            text = text.replace('ё', 'е')
        print(f"Recognized: '{text}'")

        if text in ['exit', 'выход', 'закрыть', 'close']:
            print(lang_support.get_message('closing'))
            sys.exit(0)

        best_score = 0
        matched_function = None

        for phrases, function in commands.items():
            for phrase in phrases:
                score = fuzz.ratio(phrase, text)  # Using full ratio instead of partial for better accuracy
                if score > best_score and score >= MATCH_THRESHOLD:
                    best_score = score
                    matched_function = function
    except sr.UnknownValueError:
        # Speech was unintelligible
        return
    except sr.RequestError as e:
        print(lang_support.get_message('recognition_error', e))
        return
    except Exception as e:
        print(lang_support.get_message('unexpected_error', e))
        return
    
    if matched_function:
        matched_function()
    else:
        print(lang_support.get_message('command_not_found'))

def main():
    lang_support = LanguageSupport()
    lang_support.select_language()
    
    print(lang_support.get_message('startup'))
    
    key_bindings = load_settings()
    command_handler = CommandHandler(key_bindings, lang_support)
    commands = command_handler.get_commands_dict()

    recognizer = sr.Recognizer()
    recognizer.energy_threshold = ENERGY_THRESHOLD
    recognizer.pause_threshold = PAUSE_THRESHOLD
    
    print(lang_support.get_message('calibration'))
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
    print(lang_support.get_message('calibration_complete'))
    print(lang_support.get_message('available_commands'))
    print(lang_support.get_message('exit_hint'))
    
    while True:
        try:
            listen_and_process(recognizer, commands, lang_support)
        except sr.UnknownValueError:
            pass
        except sr.WaitTimeoutError:
            pass
        except sr.RequestError as e:
            print(lang_support.get_message('recognition_error', e))
        except Exception as e:
            print(lang_support.get_message('unexpected_error', e))

if __name__ == "__main__":
    main()