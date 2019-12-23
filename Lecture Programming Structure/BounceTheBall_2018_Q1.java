class Box { 
  private int box_size;  // the size of the box
  public Box(int size) { box_size = size; }
  public boolean inHorizontalContact(int x_position)
  { return (x_position <= 0 ) || (x_position >= box_size); }
  public boolean inVerticalContact(int y_position)
  { return (y_position <= 0 ) || (y_position >= box_size); }
  public int sizeOf() { return box_size; }
}

class MovingBall
{ private int x_pos;  // ball's center x-position
  private int y_pos;  // ball's center y-position

  private int x_velocity = +5; // horizonal speed; positive is to the right
  private int y_velocity = +2; // vertical speed; positive is downwards
  private Box container;  // the container in which the ball travels

  public MovingBall(int x_initial, int y_initial, Box box)
  { x_pos = x_initial;
    y_pos = y_initial;
    container = box;
  }

  public int xPosition() { return x_pos; }
  public int yPosition() { return y_pos; }

  public void move(int time_units) { 
	  x_pos = x_pos + (x_velocity * time_units);
	  if ( container.inHorizontalContact(x_pos) ) { 
		  x_velocity = -x_velocity;
		  if (container.sizeOf() <= x_pos) 
			  x_pos = 2 * container.sizeOf() - x_pos; 
		  else // x_pos <= 0 
			  x_pos = -x_pos;
	  }
	  y_pos = y_pos + (y_velocity * time_units);
	  if ( container.inVerticalContact(y_pos) ) { 
		  y_velocity = -y_velocity;
		  if (container.sizeOf() <= y_pos) 
			  y_pos = 2 * container.sizeOf() - y_pos; 
		  else // y_pos <= 0 
			  y_pos = -y_pos;
	}
  }
}

class BounceController { 
  private MovingBall ball;  // model object
  public BounceController(MovingBall b) { ball = b; }
  public int howlong(int x_pos_dest, int y_pos_dest) {
	int time_taken = 0; 
	while (true) {
		if (ball.xPosition() == x_pos_dest && ball.yPosition() == y_pos_dest) break;
		ball.move(1);
		time_taken++; 
	}
	return time_taken;
  }
  public void run() { 
	int time_unit = 1;    // time unit for each step of the animation
    for(int i = 0; i < 100; i++) {
    	System.out.println(ball.xPosition() + ", " + ball.yPosition());
    	ball.move(time_unit);
    }
  }
}

public class BounceTheBall_2018_Q1
{ public static void main(String[] args)
  { 
    int box_size = 400;
    Box box = new Box(box_size);
    int x_init = (int)(box_size / 3.0);
    int y_init = (int)(box_size / 5.0);
    // place the ball not quite in the box's center; about 3/5 position:
    MovingBall ball = new MovingBall(x_init, y_init, box);
    BounceController controller = new BounceController(ball); 
//    controller.run();
    int taken = controller.howlong(172, 278);
    System.out.println(taken);
    taken = controller.howlong(397, 348);
    System.out.println(taken);
    taken = controller.howlong(292, 390);
    System.out.println(taken);
    taken = controller.howlong(93, 224);
    System.out.println(taken);
    taken = controller.howlong(182, 206);
    System.out.println(taken);
    taken = controller.howlong(168, 94);
    System.out.println(taken);
  }
}