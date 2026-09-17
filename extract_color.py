from PIL import Image
import collections

img = Image.open(r"C:\Users\SSMRV\.gemini\antigravity\brain\27dc5c43-44b1-4a72-82ce-0abce87067d5\.user_uploaded\media_1789625688438.png").convert("RGB")
colors = list(img.getdata())

# Finding the most saturated colors to find the gold
gold_candidates = []
for c in colors:
    r, g, b = c
    if r > g + 10 and g > b + 10 and r < 230:
        gold_candidates.append(c)

if gold_candidates:
    most_common = collections.Counter(gold_candidates).most_common(10)
    print("Saturated gold candidates:")
    for color, count in most_common:
        print(f"RGB: {color} Hex: #{color[0]:02x}{color[1]:02x}{color[2]:02x}")
else:
    print("No gold found")
