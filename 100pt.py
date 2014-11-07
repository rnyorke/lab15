#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in collision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = 4


class MyApp:
	def __init__(self, parent):
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		self.up = Button(self.myContainer1)
		self.up.configure(text="Up", background= "green")
		self.up.grid(row=0,column=1)
		self.left = Button(self.myContainer1)
		self.left.configure(text="Left", background= "green")
		self.left.grid(row=1,column=0)
		self.down = Button(self.myContainer1)
		self.down.configure(text="Down", background= "green")
		self.down.grid(row=1,column=1)	
		self.right = Button(self.myContainer1)
		self.right.configure(text="Right", background= "green")
		self.right.grid(row=1,column=2)																	
		# "Bind" 											
		self.up.bind("<Button-1>", self.moveUp)
                self.left.bind("<Button-1>", self.moveLeft)
                self.down.bind("<Button-1>", self.moveDown)
            	self.right.bind("<Button-1>", self.moveRight)
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		self.animate()
    
        def moveUp(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global player
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
                drawpad.move(player,0,-10)
		# Get the coords of our target
		tx1,ty1,tx1,ty2 = drawpad.coords(target)

		# Ensure that we are doing our collision detection
		# After we move our object!
                didWeHit = collisionDetect()
                if(didWeHit == True):
                    # We made contact! Stop our animation!
                    print "Do something"         
	def moveLeft(self, event):   
		global player
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
                drawpad.move(player,-10,0)
                
		# Get the coords of our target
		tx1,ty1,ty1,ty2 = drawpad.coords(target)

		# Ensure that we are doing our collision detection
		# After we move our object!
                didWeHit = collisionDetect()
                if(didWeHit == True):
                    # We made contact! Stop our animation!
                    print "Do something"                                      
        def moveDown(self, event):   
		global player
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
                drawpad.move(player,0,10)
		# Get the coords of our target
		tx1,ty1,tx1,ty2 = drawpad.coords(target)

		# Ensure that we are doing our collision detection
		# After we move our object!
                didWeHit = collisionDetect()
                if(didWeHit == True):
                    print "Do something"
	def moveRight(self, event):   
		global player
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
                drawpad.move(player,10,0)
		# Get the coords of our target
		tx1,ty1,tx1,ty2 = drawpad.coords(target)

		# Ensure that we are doing our collision detection
		# After we move our object!
                didWeHit = collisionDetect()
                if(didWeHit == True):
                    # We made contact! Stop our animation!
                    print "Do something"
        # Animate function that will bounce target left and right, and trigger the collision detection  
	def animate(self):
	    global target
	    global direction
	    tx1,ty1,tx2,ty2 = drawpad.coords(target)


	    # Insert the code here to make the target move, bouncing on the edges    
	    if tx2 > 480: 
                direction = -4
            elif tx1 < 0:
                direction = 4
            drawpad.move(target,direction,0)
	        
            
            
            #  This will trigger our collision detect function
            didWeHit = self.collisionDetect()
            # Use the value of didWeHit to create an if statement
            # that determines whether to run drawpad.after(1,self.animate) or not
            if didWehit == True:
                direction = 0
            else:
                drawpad.after(1,self.animate)
	# Use a function to do our collision detection
	def collisionDetect(self):
                global target
		global drawpad
                global player
                x1,y1,x2,y2 = drawpad.coords(player)
                tx1,ty1,tx2,ty2 = drawpad.coords(target)
                if (x1 > tx1 and x2 < ty2) and (y1 >ty2 and y2 < ty2) :
                    drawpad.itemconfig(target, fill = "red")
                    return True
                # Get the co-ordinates of our player AND our target
                # using x1,y1,x2,y2 = drawpad.coords(object)

                # Do your if statement - remember to return True if successful!                
		
myapp = MyApp(root)

root.mainloop()