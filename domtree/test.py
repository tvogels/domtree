from domtree.svg import *
from domtree import Node


def main():
    print(
        svg(
            "<!-- circles -->",
            (circle(x=0, y=i * 10, r=2) for i in range(5)),
            "<!-- rectangles -->",
            (rect(width=i * 10, height=i * 10) for i in range(5)),
        )
    )


if __name__ == "__main__":
    main()
