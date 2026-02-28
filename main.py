import re
import sys

from super_agent import route_intent
from tools.debug_tool import analyze_error
from tools.command_tool import execute_command
from tools.chat_tool import chat_response
from tools.system_tool import open_application, open_spotify_search
from voice.text_to_speech import speak
from voice.speech_to_text import listen


# Get User Input (Voice + Fallback)
def get_input(duration=8):
    print("Listening... Speak now.")
    text = listen(duration=duration)

    if not text or len(text.strip()) < 2:
        text = input("Sir (type): ")

    return text.strip()


# Main Assistant
def main():
    speak("Sir, your assistant is now active.")

    waiting_for_command = None
    waiting_for_song = False

    while True:

        user_input = get_input()
        lower = user_input.lower()

        # EXIT SYSTEM
        if any(word in lower for word in ["stop", "exit", "close", "shutdown", "band karo"]):
            speak("Okay Sir. Stopping assistant now.")
            sys.exit()

        # SONG FLOW (After Spotify)
        if waiting_for_song:
            result = open_spotify_search(user_input)
            print(result)
            speak(result)
            waiting_for_song = False
            continue

        # APPROVAL MODE (Command Execution)
        if waiting_for_command:

            if any(word in lower for word in [
                "yes", "execute", "go ahead", "haan", "kar do", "do it"
            ]):
                speak("Executing now Sir.")
                print("\nExecuting command...\n")

                output = execute_command(waiting_for_command)

                print("\n--- Command Output ---\n")
                print(output)

                speak("Command execution completed Sir.")
                waiting_for_command = None
                continue

            elif any(word in lower for word in [
                "no", "cancel", "mat karo"
            ]):
                speak("Okay Sir. Command cancelled.")
                waiting_for_command = None
                continue

            else:
                speak("Sir, please say yes or no.")
                continue

        # ROUTE INTENT
        intent = route_intent(user_input)
        print("Detected Intent:", intent)

        # DEBUG MODE
        if intent.get("intent") == "debug_error":

            result = analyze_error(user_input)

            print("\n--- Debug Analysis ---\n")
            print(result)

            speak("Sir, I have analyzed the issue.")

            command_match = re.search(r"pip\s+install\s+([a-zA-Z0-9_\-\.]+)", result)

            if command_match:
                package_name = command_match.group(1)
                waiting_for_command = f"pip install {package_name}"
                speak(f"Sir, should I execute pip install {package_name}?")

            else:
                speak("Sir, please provide the exact error message.")

        # OPEN APPLICATION
        elif intent.get("intent") == "open_application":

            app_name = intent.get("app_name")

            if app_name:
                result = open_application(app_name)
                print(result)
                speak(result)

                if app_name.lower() == "spotify":
                    speak("Sir, which song do you want to play?")
                    waiting_for_song = True

        # PLAY SONG DIRECTLY
        elif intent.get("intent") == "play_song":

            song_name = intent.get("song_name")
            if song_name:
                result = open_spotify_search(song_name)
                print(result)
                speak(result)

        # NORMAL CHAT
        else:
            response = chat_response(user_input)
            print("\n--- Assistant Response ---\n")
            print(response)
            speak(response)


if __name__ == "__main__":
    main()
