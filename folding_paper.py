#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Calculate folded paper's thickness | ----\n", fg("red")))

# user interaction
start_thickness = float(input("Paper's thickness (in mm): "))
times_folded = float(input("Times folded: "))

# function
def paper_folded(amount, thickness_of_paper):
    return round((thickness_of_paper * 2**amount) / 1000, 2)

end_thickness = stylize(paper_folded(times_folded, start_thickness), fg("red"))
print(f"\nA paper with {start_thickness}mm thickness is {end_thickness}m thick\nafter folding it {times_folded} times.\n")
