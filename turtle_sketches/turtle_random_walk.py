from random import choice
from turtle import Turtle
import random
nandan=Turtle()
nandan.width(10)
nandan.speed("fastest")
directions=["forward","left","right","down"]
turtle_colors = [
    "red", "green", "blue", "yellow", "orange", "purple", "pink", "brown",
    "black", "white", "gray", "cyan", "magenta", "turquoise", "skyblue",
    "lightgreen", "darkgreen", "navy", "maroon", "violet", "gold", "silver",
    "chocolate", "firebrick", "dodgerblue", "deeppink", "darkorchid",
    "forestgreen", "indianred", "khaki", "lavender", "limegreen",
    "mediumblue", "olivedrab", "palegreen", "royalblue", "saddlebrown",
    "salmon", "seagreen", "sienna", "steelblue", "tan", "teal", "thistle",
    "tomato", "wheat", "yellowgreen", "aliceblue", "antiquewhite",
    "aquamarine", "azure", "beige", "bisque", "blanchedalmond", "blueviolet",
    "burlywood", "cadetblue", "chartreuse", "coral", "cornflowerblue",
    "cornsilk", "crimson", "darkblue", "darkcyan", "darkgoldenrod",
    "darkgray", "darkgrey", "darkkhaki", "darkmagenta", "darkolivegreen",
    "darkorange", "darkred", "darksalmon", "darkseagreen", "darkslateblue",
    "darkslategray", "darkslategrey", "darkturquoise", "darkviolet",
    "dimgray", "dimgrey", "firebrick", "floralwhite", "fuchsia", "gainsboro",
    "ghostwhite", "goldenrod", "greenyellow", "honeydew", "hotpink",
    "indianred", "ivory", "lavenderblush", "lemonchiffon", "lightblue",
    "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgray",
    "lightgreen", "lightgrey", "lightpink", "lightsalmon", "lightseagreen",
    "lightskyblue", "lightslategray", "lightslategrey", "lightsteelblue",
    "lightyellow", "lime", "linen", "mediumaquamarine", "mediumorchid",
    "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen",
    "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream",
    "mistyrose", "moccasin", "navajowhite", "oldlace", "olivedrab", "orange",
    "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise",
    "palevioletred", "papayawhip", "peachpuff", "peru", "plum", "powderblue",
    "rosybrown", "royalblue", "saddlebrown", "sandybrown", "seagreen",
    "seashell", "sienna", "slategray", "slategrey", "snow", "springgreen",
    "steelblue", "tan", "teal", "thistle", "tomato", "turquoise",
    "violetred", "wheat", "whitesmoke", "yellowgreen"
]
steps=0
while steps <= 50000:
    move = random.choice(directions)
    color=random.choice(turtle_colors)
    nandan.color(color)
    if move == "forward":
        nandan.forward(30)
    elif move == "left":
        nandan.left(90)
        nandan.forward(30)
    elif move == "right":
        nandan.right(90)
        nandan.forward(30)
    elif move == "down":
        nandan.left(180)
        nandan.forward(30)