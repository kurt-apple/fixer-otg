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

knum = KC.MO(1)
knav = KC.MO(2)
kfnc = KC.MO(3)

# LEGEND
# ★ hold tap
# ☹ needs moved

_★A_LSFT   = KC.HT(KC.A,   KC.LSFT)
_★R_LSFT   = KC.HT(KC.R,   KC.LSFT)
_★T_LCMD = KC.HT(KC.T, KC.LCMD)
_★COMM_LCTL   = KC.HT(KC.COMM,   KC.LCTL)
_★K_MO2    = KC.HT(KC.K,   knav)
_★ENT_MO3  = KC.HT(KC.ENT, kfnc)
_★DOT_LALT   = KC.HT(KC.DOT,   KC.LALT)
_★ESC_MO1  = KC.HT(KC.ESC, knum)

combos.combos = [
    Chord((KC.S,      KC.L), KC.SCLN), # ; #! works
    Chord((KC.C,      KC.L), KC.COLN), # : #! works, awkward
    Chord((KC.E,      KC.Q), KC.EQL), # = #! works
    Chord((KC.B,      KC.S), KC.BSLS), # \| #! works but a little awkward
    Chord((KC.D,      KC.Q), KC.DQUO), # " works
    Chord((KC.S,      KC.Q), KC.QUOT), # ' works
    Chord((KC.E,      KC.X), KC.EXLM), # works
    Chord((_★A_LSFT, _★T_LCMD), KC.AT), # @ #! does not work
    Chord((KC.O,      KC.C), KC.POUND), #! does not work
    Chord((_★A_LSFT, KC.M), KC.AMPR), #! does not work
    Chord((_★A_LSFT, KC.E, KC.I, KC.U), KC.MO(4)), #! untested
    Chord((KC.E,      KC.O), KC.TAB, per_key_timeout=True, timeout=75),
    Chord((KC.I,      KC.O), KC.BSPC, per_key_timeout=True, timeout=75),
    Chord((_★T_LCMD,  KC.L), KC.SPC, per_key_timeout=True, timeout=75)
]

combos.combos.extend(left_and_right(KC.A, KC.LEFT_ANGLE_BRACKET, KC.RIGHT_ANGLE_BRACKET))
combos.combos.extend(left_and_right(KC.B, KC.LEFT_CURLY_BRACE,   KC.RIGHT_CURLY_BRACE))
combos.combos.extend(left_and_right(KC.P, KC.LEFT_PAREN,         KC.RIGHT_PAREN))
combos.combos.extend(left_and_right(KC.F, KC.LBRACKET,           KC.RBRACKET))

ast = KC.ASTR
_ₓₓₓ_ = KC.NO
hidsw = KC.HID_SWITCH
blerf = KC.BLE_REFRESH

# todos
# - perhaps left consonant scrabble score should be higher avg.
# - consider moving some consonants from left to right
# move z to right
# - ensure ZE
# - ensure ZO
# - ensure IZ
# - ensure WH

# tests
# hope chop
# size what
# who where
# how for
# the

# required changes
# add LCMD maybe right hand

base_layer = [
                        KC.Z,       KC.X,                   KC.Q,       KC.J,#3
            KC.W,       KC.D,       KC.F,                   KC.Y,       KC.V,      KC.B,#9
_ₓₓₓ_,      KC.U,       KC.E,       KC.O,                   KC.L,       KC.S,      KC.N,       _ₓₓₓ_,#17
_★A_LSFT,   KC.P,       _★K_MO2,    KC.G,                   KC.M,       KC.C,      KC.H,       _★R_LSFT,#25
_★COMM_LCTL,            _★ESC_MO1,  KC.I,                   _★T_LCMD,   _★ENT_MO3,             _★DOT_LALT
]
num_layer = [
                        KC.GRV,     KC.TILD,                KC.SLSH,    ast,
            _ₓₓₓ_,      _ₓₓₓ_,      KC.DLR,                 KC.N7,      KC.N8,      KC.N9,
_ₓₓₓ_,      KC.PIPE,    KC.CIRC,    KC.PERC,                KC.N4,      KC.N5,      KC.N6,      KC.MINS,
_ₓₓₓ_,      _ₓₓₓ_,      _ₓₓₓ_,      _ₓₓₓ_,                  KC.N1,      KC.N2,      KC.N3,      KC.PLUS,
_ₓₓₓ_,                  _ₓₓₓ_,      _ₓₓₓ_,                  _ₓₓₓ_,      KC.N0,                  _ₓₓₓ_
]
nav_layer = [
                        _ₓₓₓ_,      _ₓₓₓ_,                  _ₓₓₓ_,      _ₓₓₓ_,
            _ₓₓₓ_,      _ₓₓₓ_,      KC.PGUP,                _ₓₓₓ_,      KC.UP,      _ₓₓₓ_,
KC.ESC,     _ₓₓₓ_,      _ₓₓₓ_,      KC.TAB,                 KC.LEFT,    KC.DOWN,    KC.RIGHT,   _ₓₓₓ_,
_ₓₓₓ_,      _ₓₓₓ_,      _ₓₓₓ_,      KC.PGDN,                _ₓₓₓ_,      KC.HOME,    KC.END,     _ₓₓₓ_,
KC.TRNS,                _ₓₓₓ_,      _ₓₓₓ_,                  _ₓₓₓ_,      _ₓₓₓ_,                  _ₓₓₓ_
]

F_layer = [
                        KC.INS,     KC.PSCR,                KC.F10,     KC.F11,
            _ₓₓₓ_,      KC.LCTL,    _ₓₓₓ_,                  KC.F7,      KC.F8,      KC.F9,
_ₓₓₓ_,      _ₓₓₓ_,      _ₓₓₓ_,      _ₓₓₓ_,                  KC.F4,      KC.F5,      KC.F6,      KC.LALT,
_ₓₓₓ_,      _ₓₓₓ_,      _ₓₓₓ_,      _ₓₓₓ_,                  KC.F1,      KC.F2,      KC.F3,      _ₓₓₓ_,
hidsw,                  KC.DEL,     KC.F12,                 _ₓₓₓ_,      _ₓₓₓ_,                  blerf
]

# macros = [
#                  _ₓₓₓ_,  _ₓₓₓ_,         _ₓₓₓ_,    _ₓₓₓ_,
#           _ₓₓₓ_, _ₓₓₓ_,  _ₓₓₓ_,         _ₓₓₓ_,    _ₓₓₓ_,     _ₓₓₓ_,
# _ₓₓₓ_,    _ₓₓₓ_, _ₓₓₓ_,  _ₓₓₓ_,         _ₓₓₓ_,    _ₓₓₓ_,     _ₓₓₓ_,    _ₓₓₓ_,
# _ₓₓₓ_,    _ₓₓₓ_, _ₓₓₓ_,  _ₓₓₓ_,         _ₓₓₓ_,    _ₓₓₓ_,     _ₓₓₓ_,    _ₓₓₓ_,
# _ₓₓₓ_,           _ₓₓₓ_,  _ₓₓₓ_,         _ₓₓₓ_,    _ₓₓₓ_,               _ₓₓₓ_
# ]

def transpose(layer):
    return [
        layer[10],  layer[4],   layer[0],   layer[1],   layer[2],   layer[3],   layer[9],   layer[17],
        layer[18],  layer[11],  layer[5],   layer[6],   layer[7],   layer[8],   layer[16],  layer[25],
        layer[26],  layer[19],  layer[12],  layer[13],  layer[14],  layer[15],  layer[24],  layer[31],
        _ₓₓₓ_,      _ₓₓₓ_,      layer[20],  layer[21],  layer[22],  layer[23],  _ₓₓₓ_,      _ₓₓₓ_,
        _ₓₓₓ_,      _ₓₓₓ_,      layer[27],  layer[28],  layer[29],  layer[30],  _ₓₓₓ_,      _ₓₓₓ_]


keyboard.keymap = [
# BASE
transpose(base_layer),
# NUM
transpose(num_layer),
# # NAV
transpose(nav_layer),
# MACROS
# transpose(macros),
]

layer_names_list = [
"Base",
"Num",
"Nav",
"F",
# "MACRO"
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
