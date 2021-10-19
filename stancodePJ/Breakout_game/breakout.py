"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

There are several layers of bricks on the upper part of the screen.
A ball bounces back and forth between the bricks above the window,
the moving paddle below the screen and the walls on both sides.
When the ball hits the bricks, the ball will bounce and the bricks disappear.
Players need to control the board at the bottom of the screen, let the ball
hit to eliminate all the bricks, the ball will disappear when it hits the bottom
edge of the screen, and the game will fail if all the lives disappear.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Get the ball velocity
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    # Game lives
    lives = NUM_LIVES
    while True:
        pause(FRAME_RATE)
        if lives == 0 or graphics.count_bricks == 0:
            break
        elif graphics.start:
            graphics.ball.move(dx, dy)
            # Hit the left or right side of the window.
            if graphics.ball.x < 0 or graphics.ball.x > graphics.window.width - graphics.ball.width:
                dx = -dx
            # Hit the top of the window.
            elif graphics.ball.y < 0:
                dy = -dy
            # Hit the object.
            elif graphics.check_for_collision() != None:
                # Hit the bricks.
                if graphics.check_for_collision() != graphics.paddle:
                    graphics.window.remove(graphics.check_for_collision())
                    graphics.count_bricks -= 1
                    dy = -dy
                # Hit the paddle.
                elif dy > 0:
                    dy = -dy
            # The ball hits the bottom edge of the window.
            elif graphics.ball.y > graphics.window.height:
                lives -= 1
                graphics.reset_ball()
    # Show the game result to user.
    if lives == 0:
        label = GLabel('You Out!!')
        graphics.window.add(label,x=graphics.window.width/2,y=graphics.window.height/2)
    else:
        label = GLabel('You Win!!')
        graphics.window.add(label,x=graphics.window.width/2,y=graphics.window.height/2)





if __name__ == '__main__':
    main()
