import random
import stddraw

from color import Color


# ---------------------------------------------------------------
# SORTING ALGORITHMS (no animation)
# ---------------------------------------------------------------

def bubble_sort(numbers):
    # PROCESS
    # Compare each pair of neighbours and swap them if they are out of
    # order. After every sweep the largest remaining value has bubbled
    # up to the end, so the next sweep can be one position shorter.
    n = len(numbers)
    for sweep in range(n):
        for pair in range(0, n - 1 - sweep):
            if numbers[pair] > numbers[pair + 1]:
                numbers[pair], numbers[pair + 1] = numbers[pair + 1], numbers[pair]


def insertion_sort(numbers):
    # PROCESS
    # Treat the left part of the list as already sorted. Take the next
    # value and shift every larger value one place to the right until
    # the correct hole is found, then drop the value into that hole.
    n = len(numbers)
    for index in range(1, n):
        current = numbers[index]
        position = index - 1
        while position >= 0 and numbers[position] > current:
            numbers[position + 1] = numbers[position]
            position -= 1
        numbers[position + 1] = current


def selection_sort(numbers):
    # PROCESS
    # Scan the unsorted part of the list, remember where the smallest
    # value is, and swap it into the first unsorted position.
    n = len(numbers)
    for index in range(n):
        minimum = index
        for scan in range(index + 1, n):
            if numbers[scan] < numbers[minimum]:
                minimum = scan
        numbers[index], numbers[minimum] = numbers[minimum], numbers[index]


# ---------------------------------------------------------------
# DRAWING
# ---------------------------------------------------------------

def draw_bars(numbers, selected=()):
    # OUTPUT
    # Draw one bar per value. Bars whose index is in "selected" are
    # painted red so the viewer can see which values are being
    # compared or moved at this step.
    stddraw.clear()
    n = len(numbers)
    bar_width = 10.0 / n

    for i, number in enumerate(numbers):
        x = i * bar_width + bar_width / 2
        color = Color(255, 90, 90) if i in selected else Color(70, 130, 220)
        stddraw.setPenColor(color)
        stddraw.filledRectangle(x - bar_width / 2, 0, bar_width * 0.9, number)
    stddraw.show(500)


def setup_canvas(numbers):
    # PROCESS
    # Fit the drawing window to the data: 10 units wide, and tall
    # enough for the largest value in the list.
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)


# ---------------------------------------------------------------
# ANIMATED SORTING ALGORITHMS
# ---------------------------------------------------------------

def bubble_sort_animated(numbers):
    # PROCESS + OUTPUT
    # Same logic as bubble_sort, but the bars are redrawn before and
    # after every swap so the comparison is visible.
    setup_canvas(numbers)
    n = len(numbers)

    for sweep in range(n):
        for pair in range(0, n - 1 - sweep):
            draw_bars(numbers, selected=(pair, pair + 1))
            if numbers[pair] > numbers[pair + 1]:
                numbers[pair], numbers[pair + 1] = numbers[pair + 1], numbers[pair]
                draw_bars(numbers, selected=(pair, pair + 1))

    draw_bars(numbers)
    stddraw.show()


def insertion_sort_animated(numbers):
    # PROCESS + OUTPUT
    # Same logic as insertion_sort, but every shift to the right is
    # drawn so the viewer can follow the value moving into its hole.
    setup_canvas(numbers)
    n = len(numbers)

    for index in range(1, n):
        current = numbers[index]
        position = index - 1
        draw_bars(numbers, selected=(index,))

        while position >= 0 and numbers[position] > current:
            numbers[position + 1] = numbers[position]
            position -= 1
            draw_bars(numbers, selected=(position + 1,))

        numbers[position + 1] = current
        draw_bars(numbers, selected=(position + 1,))

    draw_bars(numbers)
    stddraw.show()


def selection_sort_animated(numbers):
    # PROCESS + OUTPUT
    # Same logic as selection_sort, but the current minimum and the
    # value being scanned are highlighted during the search.
    setup_canvas(numbers)
    n = len(numbers)

    for index in range(n):
        minimum = index
        for scan in range(index + 1, n):
            draw_bars(numbers, selected=(minimum, scan))
            if numbers[scan] < numbers[minimum]:
                minimum = scan

        numbers[index], numbers[minimum] = numbers[minimum], numbers[index]
        draw_bars(numbers, selected=(index, minimum))

    draw_bars(numbers)
    stddraw.show()


# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------

# INPUT
# Build a list of 10 random values between 0 and 100, and ask the
# user which algorithm to watch.
numbers = [random.randint(0, 100) for x in range(10)]
print(f"Before sorting: {numbers}")

algorithm = input("Choose an algorithm (bubble/insertion/selection): ").strip().lower()

try:
    if algorithm == "bubble":
        bubble_sort_animated(numbers)
    elif algorithm == "insertion":
        insertion_sort_animated(numbers)
    elif algorithm == "selection":
        selection_sort_animated(numbers)
    else:
        raise ValueError("Choose bubble, insertion or selection")

except ValueError as error:
    print(error)

else:
    # OUTPUT
    print(f"After sorting: {numbers}")
