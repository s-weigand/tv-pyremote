"""Module with the  autogui interactions requested from the app."""

from typing import Dict

from pyautogui import KEYBOARD_KEYS, hotkey, press

from .consts import role_mapping


def press_keys(key_str: str) -> Dict[str, str]:
    """Press a button on a request.

    Parameters
    ----------
    key_str : str
        String representation of the keys to press.

    Returns
    -------
    Dict[str, str]
        Response code to be sent back to the browser.
    """
    for hotkey_str in key_str.split(";"):
        keys = hotkey_str.split("+")
        if all(key in KEYBOARD_KEYS for key in keys):
            if len(keys) == 1:
                press(keys[0])
            else:
                hotkey(keys)
            return {"success": f"pressed keys {key_str}"}
        else:
            failures = []
            for key in keys:
                if key not in KEYBOARD_KEYS:
                    failures.append(f"The key {key} is not allowed.")
            failures_string = "\n".join(failures)
            return {"failure": f"{failures_string}\nAllowed keys are: {KEYBOARD_KEYS}"}
    return {"failure": f"No Keys to press in: {key_str}"}


def map_role(role: str) -> str:
    """Map role to keybind.

    Parameters
    ----------
    role : str
        Role of the clicked item.

    Returns
    -------
    str
        Keybinding.
    """
    for mapped_role in role_mapping:
        if mapped_role["role"] == role:
            return mapped_role["keys"]
    return ""
