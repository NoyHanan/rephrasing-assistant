import os
import subprocess
from urllib.parse import urlparse
from pynput import keyboard
from mpi4py import MPI


def set_env_variable(var_name, value, comm):
    with open(os.path.expanduser('~/.zshrc'), 'a') as f:
        f.write(f'export {var_name}={f"{value}"}\n')
    print("Please reset the terminal session (source ~/.zshrc | /. bashrc) and start the program to apply the changes")
    comm.Abort(0)
    quit(0)

def get_api_key(model_str: str, comm: MPI.Comm) -> str:
    env_variable = model_str + "_API_KEY"
    if os.environ.get(env_variable) is None:
        api_key = '"' + input(f'Enter the API key for {model_str}: ') + '"'
        set_env_variable(env_variable, api_key, comm)

    return os.environ[env_variable]

def copy_selected_text_to_clipboard():
    # This will simulate CMD+C on macOS, copying the selected text
    # with keyboard.Controller() as controller:
    controller = keyboard.Controller()
    controller.press(keyboard.Key.cmd)
    controller.press('c')
    controller.release('c')
    controller.release(keyboard.Key.cmd)

def get_active_app_name():
    try:
        result = subprocess.run(
            ['osascript', '-e', 'tell application "System Events" to get the name of every process whose frontmost is true'],
            stdout=subprocess.PIPE
        )
        return result.stdout.decode('utf-8').strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_active_url():
    try:
        script = '''
        tell application "Google Chrome"
            get the url of the active tab of the front window
        end tell
        '''
        result = subprocess.run(["osascript", "-e", script], capture_output=True)
        return result.stdout.decode("utf-8").strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def extract_website_name(url):
    parsed_url = urlparse(url)
    netloc = parsed_url.netloc

    # Remove 'www.' if it exists
    if netloc.startswith('www.'):
        netloc = netloc[4:]

    # Get only the domain name, removing subdomains and port numbers if they exist
    domain_name = netloc.split(':')[0].split('.')[-2]
    return domain_name
