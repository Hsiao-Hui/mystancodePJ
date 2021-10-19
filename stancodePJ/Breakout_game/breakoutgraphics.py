"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width,paddle_height,x=(self.window_width-paddle_width)/2,y=self.window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2,ball_radius*2,x= self.window_width/2-ball_radius,y=self.window_height/2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self._dx = random.randint(1,MAX_X_SPEED)
        if random.random()>0.5:
            self._dx = - self._dx
        self._dy = INITIAL_Y_SPEED
        self.start = False
        # Initialize our mouse listeners
        onmouseclicked(self.ball_moving)
        onmousemoved(self.move_paddle)

        # Draw bricks
        self.count_bricks = 0
        self.b_r = brick_rows
        self.b_c = brick_cols
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.bricks = GRect(brick_width,brick_height,x=(brick_width+brick_spacing)*i,y=(brick_height+brick_spacing)*j)
                self.bricks.filled = True
                self.bricks_color(j)
                self.window.add(self.bricks)
                self.count_bricks += 1

    def bricks_color(self, j):
        """
        This function can draw the color of each brick.
        :param j: Which row of bricks is located.
        :return:Colored bricks
        """
        num_of_row = self.b_r/5
        if j < num_of_row:
            self.bricks.fill_color = 'red'
        elif num_of_row <= j < num_of_row*2:
            self.bricks.fill_color = 'orange'
        elif num_of_row*2 <= j < num_of_row*3:
            self.bricks.fill_color = 'yellow'
        elif num_of_row*3 <= j < num_of_row*4:
            self.bricks.fill_color = 'green'
        else:
            self.bricks.fill_color = 'blue'

    def move_paddle(self, mouse):
        """
        You can use the mouse to move the paddle.
        :param mouse:The mouse is located in the middle of the paddle.
        """
        self.paddle.x = mouse.x - self.paddle.width/2
        if mouse.x - self.paddle.width/2 <= 0:
            self.paddle.x = 0
        if mouse.x + self.paddle.width/2 >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width

    def ball_moving(self,mouse):
        """
        When the mouse clicked ,the animation start.
        """
        if not self.start:
            self.start = True

    def reset_ball(self):
        """
        When the ball out of bounds,this function can reset the ball to its initial position.
        """
        self.start = False
        self.window.remove(self.ball)
        self.window.add(self.ball,x= self.window_width/2,y=self.window_height/2)

    # 檢查碰撞到什麼東西
    def check_for_collision(self):
        """
        This program can confirm whether the ball has touched an object.
        :return:Returns the touched object
        """
        for i in range(0,3,2):
           for j in range(0,3,2):
                self.obj = self.window.get_object_at(self.ball.x + i*BALL_RADIUS,self.ball.y+j*BALL_RADIUS)
                if self.obj != None:
                    return self.obj

    # Getter
    def get_dx(self):
        if random.random()>0.5:
            self._dx = - self._dx
        return self._dx

    # Getter
    def get_dy(self):
        return self._dy


