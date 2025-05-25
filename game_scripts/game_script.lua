local player 
local xd
function on_start()
    player = Entity("pidor.png")
    player.position = Vector2(100,100)
    
    xd = Entity("pidor.png")
    xd.position = Vector2(215, 400)
    print("!")
end

function on_update(dt)
    if py_get_input(py.KEY_W) then
        player.position.x = player.position.x+1
    elseif py_get_input(py.KEY_S) then
        player.position.x = player.position.x-1
    end
    while player.position.y <= 400 do
        player.position.y = player.position.y+2
    end
    if player.position.y > 400 then
        player.position.y = 400
    end
    
    player:blit(POGE.SCREEN_D)
    xd:blit(POGE.SCREEN_D)
end
