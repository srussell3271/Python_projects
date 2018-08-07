from turtle import *
color('red', 'orange')
begin_fill()
while True:
    forward(150)
    left(130)
    if abs(pos()) < 1:
        break
end_fill()
done()
