import turtle

class PG:

    def __init__(self,window,p1,p2,ball):
        self.window = window
        self.p1 = p1
        self.p2 = p2
        self.ball = ball
        self.move("w","s","Up","Down")
        self.gameLoop()

    def createWindow(title,color,w,h,tracer=True):
        window = turtle.Screen()
        window.title(title)
        window.bgcolor(color)
        window.setup(width=w , height=h)
        if tracer:
            window.tracer(0)
        return window
    
    def createObj(color,shape,x,y,width=1,len=1,speed=0,penup=True):
        obj = turtle.Turtle()
        obj.speed(speed)
        obj.shape(shape)
        obj.shapesize(stretch_wid=width,stretch_len=len)
        obj.color(color)
        if penup:
            obj.penup()
        obj.goto(x,y)
        return obj

    def p1_up(self):
        y = self.p1.ycor()
        y += 150
        self.p1.sety(y)
    
    def p1_down(self):
        y = self.p1.ycor()
        y -= 150
        self.p1.sety(y)
    
    def p2_up(self):
        y = self.p2.ycor()
        y += 150
        self.p2.sety(y)
    
    def p2_down(self):
        y = self.p2.ycor()
        y -= 150
        self.p2.sety(y)

    def move(self,u1,d1,u2,d2):
        self.window.listen()
        self.window.onkeypress(self.p1_up,u1)
        self.window.onkeypress(self.p1_down,d1)
        self.window.onkeypress(self.p2_up,u2)
        self.window.onkeypress(self.p2_down,d2)

    def __createScore():
        score = turtle.Turtle()
        score.speed(0)
        score.color("white")
        score.penup()
        score.hideturtle()
        score.goto(0,360)
        score.write("0 : 0",font=("Courier",24,"normal"),align="center")
        return score
    
    def gameLoop(self):
        score = PG.__createScore()
        p1 = self.p1
        p2 = self.p2
        ball = self.ball
        ball.dx = .8
        ball.dy = .8
        s1 = 0
        s2=0

        while True:
            self.window.update()

            ball.setx(ball.xcor()+ball.dx)
            ball.sety(ball.ycor()+ball.dy)

            # check borders for players
            if(p1.ycor() > 350):
                p1.sety(350)
            
            if(p1.ycor() < -350):
                p1.sety(-350)

            if(p2.ycor() > 350):
                p2.sety(350)

            if(p2.ycor() < -350):
                p2.sety(-350)

            # check borders for ball
            if ball.ycor() > 390:
                ball.sety(390)
                ball.dy *= -1

            if ball.ycor() < -390:
                ball.sety(-390)
                ball.dy *= -1
            
            if ball.xcor() > 490:
                ball.goto(0,0)
                ball.dx *= -1
                s1 += 1
                score.clear()
                score.write(f"{s1} : {s2}",font=("Courier",24,"normal"),align="center")

            if ball.xcor() < -490:
                ball.goto(0,0)
                ball.dx *= -1
                s2 += 1
                score.clear()
                score.write(f"{s1} : {s2}",font=("Courier",24,"normal"),align="center")

            # set an end to the round
            if s1 == 5 or s2 == 5:
                score.clear()
                if s1 > s2:
                    score.write("Player1 won!",font=("Courier",24,"normal"),align="center")
                elif s2 > s1:
                    score.write("Player2 won!",font=("Courier",24,"normal"),align="center")
                s1 = 0
                s2 = 0

            # ball and rackets collision -> center = (450,0) , top = (450,50) , top_left = (440,50) -> 450-(0.5*width)
            if (ball.xcor() > 440 and ball.xcor() < 450) and (ball.ycor() < p2.ycor()+40 and ball.ycor() > p2.ycor()-40):
                ball.setx(440)
                ball.dx *= -1
            
            if (ball.xcor() < -440 and ball.xcor() > -450) and (ball.ycor() < p1.ycor()+40 and ball.ycor() > p1.ycor()-40):
                ball.setx(-440)
                ball.dx *= -1
            



window = PG.createWindow("Ping Pong","black",1000,800)

p1 = PG.createObj("blue","square",-450,0,5,1) # x , y , width = 5*20 , len = 1*20 , speed = 0 , penup = True

p2 = PG.createObj("red","square",450,0,5,1) # x , y , width = 5*20 , len , speed = 0 , penup = True

ball = PG.createObj("white","square",0,0) # x , y , width = 1*20 , len = 1*20 , speed = 0 , penup = True


g = PG(window,p1,p2,ball)