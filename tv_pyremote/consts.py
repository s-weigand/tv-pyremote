"""Module containing constants."""

DEV_PORT = 9001

roles = (
    {"role": "play_pause", "icon": "pause_circle_outline"},
    {"role": "volume_up", "icon": "volume_up"},
    {"role": "volume_down", "icon": "volume_down"},
    {"role": "volume_mute", "icon": "volume_off"},
    {"role": "screen_mute", "icon": "desktop_access_disabled"},
    {"role": "fullscreen", "icon": "fullscreen"},
    {"role": "fullscreen_exit", "icon": "fullscreen_exit"},
    {"role": "replay_5", "icon": "replay_5"},
    {"role": "replay_10", "icon": "replay_10"},
    {"role": "replay_30", "icon": "replay_30"},
    {"role": "forward_5", "icon": "forward_5"},
    {"role": "forward_10", "icon": "forward_10"},
    {"role": "forward_30", "icon": "forward_30"},
    {"role": "skip_next", "icon": "skip_next"},
    {"role": "skip_previous", "icon": "skip_previous"},
    {"role": "fast_forward", "icon": "fast_forward"},
    {"role": "fast_rewind", "icon": "fast_rewind"},
)

role_mapping = (
    {"role": "play_pause", "keys": "space"},
    {"role": "volume_up", "keys": "up"},
    {"role": "volume_down", "keys": "down"},
    {"role": "volume_mute", "keys": "volumemute"},
    {"role": "screen_mute", "keys": ""},
    {"role": "fullscreen", "keys": "f"},
    {"role": "fullscreen_exit", "keys": "esc"},
    {"role": "replay_5", "keys": "left"},
    {"role": "replay_10", "keys": "left"},
    {"role": "replay_30", "keys": "left"},
    {"role": "forward_5", "keys": "right"},
    {"role": "forward_10", "keys": "right"},
    {"role": "forward_30", "keys": "right"},
    {"role": "skip_next", "keys": "nexttrack"},
    {"role": "skip_previous", "keys": "prevtrack"},
    {"role": "fast_forward", "keys": "fast_forward"},
    {"role": "fast_rewind", "keys": "fast_rewind"},
)
