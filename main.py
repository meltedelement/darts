def on_countdown_end():
    global Level
    Level += 1
info.on_countdown_end(on_countdown_end)

Level = 1
game.show_long_text("Level 1", DialogLayout.BOTTOM)
info.start_countdown(30)
myDart = darts.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            3 3 3 3 3 3 3 3 3 3 3 . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.projectile)
myDart.set_bounce_on_wall(True)
myDart.set_position(73, 51)
myDart.set_trace()
myDart.throw_dart()