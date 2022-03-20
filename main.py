from PingPong import PG

window = PG.createWindow("Ping Pong","black",1000,800)

p1 = PG.createObj("blue","square",-450,0,5,1) # x , y , width = 5*20 , len = 1*20 , speed = 0 , penup = True

p2 = PG.createObj("red","square",450,0,5,1) # x , y , width = 5*20 , len , speed = 0 , penup = True

ball = PG.createObj("white","square",0,0) # x , y , width = 1*20 , len = 1*20 , speed = 0 , penup = True


g = PG(window,p1,p2,ball)
