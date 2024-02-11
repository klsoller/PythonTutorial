#game.py
# import the draw module (draw.py)
import draw
# from draw import draw_game    # you could do this.

# game.py
# import the draw module
'''
visual_mode = False
if visual_mode:
    # in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw
    
'''


def play_game():
    ...
    
def main():
    result = play_game()
    draw.draw_game(result)
    # draw_game(result) # you can only do this if you import it into NAMESPACE.
    
# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()
    