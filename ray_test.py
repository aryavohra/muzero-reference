import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/home/ray/muzero-reference/')

from muzero import MuZero

model = MuZero("breakout_ramstate_resnet")
model.train()