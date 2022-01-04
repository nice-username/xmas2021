#
# MERRY XMAS 2021
# FOR ELIZABETH AND MASON
#
# REFERENCE
# https://github.com/peterbrittain/asciimatics/blob/v1.13/samples/xmas.py
#
from __future__ import division
from asciimatics.effects import Cycle, Snow, Print
from asciimatics.renderers import FigletText, StaticRenderer
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys

# Tree definition
tree = r"""
       ${3,1}*
      / \
     /${1}o${2}  \
    /_   _\
     /   \${4}b
    /     \
   /   ${1}o${2}   \
  /__     __\
  ${1}d${2} / ${4}o${2}   \
   /       \
  / ${4}o     ${1}o${2}.\
 /___________\
      ${3}|||
      ${3}|||
""", r"""
       ${3}*
      / \
     /${1}o${2}  \
    /_   _\
     /   \${4}b
    /     \
   /   ${1}o${2}   \
  /__     __\
  ${1}d${2} / ${4}o${2}   \
   /       \
  / ${4}o     ${1}o${2} \
 /___________\
      ${3}|||
      ${3}|||
"""


def demo(screen):
    scenes = []
    effects = [
        Print(screen, StaticRenderer(images=tree),
              x=screen.width - 15,
              y=screen.height - 15,
              colour=Screen.COLOUR_GREEN),
        Snow(screen),
        Cycle(
            screen,
            FigletText("MERRY XMAS"),
            screen.height // 2 - 6,
            start_frame=50,
            delete_count=175),
        Cycle(
            screen,
            FigletText("LIZ & MASON!"),
            screen.height // 2 + 1,
            start_frame=75,
            delete_count=200)
    ]

    screen.play([Scene(effects, -1)], stop_on_resize=True)


while True:
    try:
        Screen.wrapper(demo)
        sys.exit(0)
    except ResizeScreenError:
        pass