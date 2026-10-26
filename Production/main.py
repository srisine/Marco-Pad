import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled_Display import (
    OLED,
    OLEDDisplayMode,
    OLEDData,
)

keyboard = KMKKeyboard()

keyboard.direct_pins = [
    board.GP2,
    board.GP1,
    board.GP10,
    board.GP3,
]

media_keys = MediaKeys()
encoder_handler = EncoderHandler()
keyboard.extensions.append(media_keys)
keyboard.modules.append(encoder_handler)

encoder_handler.pins = ((board.GP4, board.GP5, None),)
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),),
]

i2c_bus = busio.I2C(board.GP5, board.GP4)

oled_ext = OLED(
    OLEDData(
        header="Shaw Macropad",
        -1,
    ),
    to_display=OLEDDisplayMode.TXT,
    i2c=i2c_bus,
    device_address=0x3C,
)
keyboard.extensions.append(oled_ext)

keyboard.keymap = [
    [
        KC.MEDIA_PREV_TRACK,
        KC.MEDIA_NEXT_TRACK,
        KC.MEDIA_PLAY_PAUSE,
        KC.MUTE,
    ]
]

if __name__ == '__main__':
    keyboard.go()