print("Starting")


import busio
import board
from kmk.kmk_keyboard import KMKKeyboard; keyboard = KMKKeyboard()
from kmk.keys import KC, make_key
from kmk.scanners import DiodeOrientation

# from kb import data_pin
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.layers import Layers; keyboard.modules.append(Layers())
from kmk.modules.holdtap import HoldTap; keyboard.modules.append(HoldTap())
from kmk.modules.tapdance import TapDance; keyboard.modules.append(TapDance())
from kmk.modules.macros import Macros
from kmk.modules.combos import Combos, Chord
combos = Combos()
keyboard.modules.append(combos)

from kmk.hid import HIDModes
from kmk.hid import BLEHID

from storage import getmount

side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT

keyboard.col_pins = (board.D10, board.D9, board.D8, board.D7)
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3, board.D6)

bluetoothInterface = BLEHID()
def BT(*args, **kwargs):
    bluetoothInterface.clear_bonds()
    bluetoothInterface.start_advertising()

# make_key(names=('CLEARBT',), on_press=BT, on_release=passthrough)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

split = Split(
    split_flip=True,  # If both halves are the same, but column pins are flipped, set this True
    split_side=side,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
    split_type=SplitType.BLE,  # Defaults to UART
)
keyboard.modules.append(split)

def left_and_right(abbreviation, lkeycode, rkeycode = None):
    if(rkeycode == None):
        rkeycode = lkeycode
    return [
        Chord((KC.L, abbreviation), lkeycode),
        Chord((KC.R, abbreviation), rkeycode)
    ]

KCA_LSFT = KC.HT(KC.A, KC.LSFT)
KCL_LSFT = KC.HT(KC.L, KC.LSFT)

combos.combos = [
    Chord((KC.S, KCL_LSFT), KC.SCLN),
    Chord((KC.C, KCL_LSFT), KC.COLN),
]

combos.combos.extend(left_and_right(KC.A, KC.LEFT_ANGLE_BRACKET, KC.RIGHT_ANGLE_BRACKET))
combos.combos.extend(left_and_right(KC.B, KC.LEFT_CURLY_BRACE, KC.RIGHT_CURLY_BRACE))
combos.combos.extend(left_and_right(KC.P, KC.LEFT_PAREN, KC.RIGHT_PAREN))
combos.combos.extend(left_and_right(KC.F, KC.LBRACKET, KC.RBRACKET))


# base_layer = [
#                 KC.Z,   KC.T,       KC.Y,   KC.Q,#3
#         KC.O,   KC.W,   KC.J,       KC.D,   KC.F,   KC.G,#9
# KC.H,   KC.E,   KC.I,   KC.U,       KC.R,   KC.S,   KC.N,   KC.P,#17
# KC.A,   KC.COMM,KC.X,   KC.V,       KC.M,   KC.B,   KC.DOT, KC.L,#25
# KC.C,           KC.HOME,KC.BSPC,    KC.SPC, KC.END,         KC.LCTL
# ]

base_layer = [
                    KC.Z,   KC.T,       KC.Y,   KC.Q,#3
            KC.O,   KC.W,   KC.J,       KC.D,   KC.F,   KC.G,#9
KC.H,       KC.E,   KC.I,   KC.U,       KC.R,   KC.S,   KC.N,   KC.P,#17
KCA_LSFT,   KC.COMM,KC.X,   KC.V,       KC.M,   KC.B,   KC.DOT, KCL_LSFT,#25
KC.C,               KC.HOME,KC.BSPC,    KC.SPC, KC.END,         KC.LCTL
]

def transpose(layer):
    return [
        layer[10],  layer[4],   layer[0],   layer[1],   layer[2],   layer[3],   layer[9],   layer[17],
        layer[18],  layer[11],  layer[5],   layer[6],   layer[7],   layer[8],   layer[16],  layer[25],
        layer[26],  layer[19],  layer[12],  layer[13],  layer[14],  layer[15],  layer[24],  layer[31],
        KC.NO,      KC.NO,      layer[20],  layer[21],  layer[22],  layer[23],  KC.NO,      KC.NO,
        KC.NO,      KC.NO,      layer[27],  layer[28],  layer[29],  layer[30],  KC.NO,      KC.NO]


keyboard.keymap = [
# BASE
transpose(base_layer),
# # NAV
# [
# KC.TD(KC.NO, KC.RELOAD, tap_time=200), KC.TD(KC.NO, KC.NO, tap_time=200), KC.TD(KC.NO, KC.NO, tap_time=200), KC.TD(KC.NO, KC.NO, tap_time=200), KC.NO, KC.NO, KC.LSFT(KC.INS), KC.LCTL(KC.INS), KC.LSFT(KC.DEL), KC.NO,
# KC.LGUI, KC.LALT, KC.LCTL, KC.LSFT, KC.NO, KC.TD(KC.NO, KC.CAPS, tap_time=200), KC.LEFT, KC.DOWN, KC.UP, KC.RGHT,
# KC.NO, KC.RALT, KC.TD(KC.NO, KC.NO, tap_time=200), KC.TD(KC.NO, KC.NO, tap_time=200), KC.NO, KC.INS, KC.HOME, KC.PGDN, KC.PGUP, KC.END,
# KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.ENT, KC.BSPC, KC.DEL, KC.NO, KC.NO
# ],
# # NUM
# [
# KC.LBRC, KC.N7, KC.N8, KC.N9, KC.RBRC, KC.NO, KC.TD(KC.NO, KC.NO, tap_time=200), KC.TD(KC.NO, KC.NO, tap_time=200), KC.TD(KC.NO, KC.NO, tap_time=200), KC.TD(KC.NO, KC.RELOAD, tap_time=200),
# KC.SCLN, KC.N4, KC.N5, KC.N6, KC.EQL, KC.NO, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI,
# KC.GRV, KC.N1, KC.N2, KC.N3, KC.BSLS, KC.NO, KC.TD(KC.NO, KC.NO, tap_time=200), KC.TD(KC.NO, KC.NO, tap_time=200), KC.RALT, KC.NO,
# KC.NO, KC.STEPS, KC.DOT, KC.N0, KC.MINS, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO
# ],

]

layer_names_list = [
"Base",
# "Nav", "Num",
]

if __name__ == '__main__':

    if side == SplitSide.LEFT:
        # should work, according to github issues chatter, but doesn't
        # - secondary_hid_type appears to be unimplemented
        # keyboard.go(hid_type=HIDModes.USB, secondary_hid_type=HIDModes.BLE, ble_name='fixer2')
        # fallback if above config does not work
        keyboard.go(hid_type=HIDModes.BLE, ble_name='fixer2')
    else:
        keyboard.go()
