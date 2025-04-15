import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img1 = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.image.load("fig/pg_bg.jpg")
    bg_img3 = pg.image.load("fig/pg_bg.jpg")
    bg_img2=pg.transform.flip(bg_img2,True,False)
    kk=pg.image.load("fig/3.png")
    kk=pg.transform.flip(kk,True,False)
    
    tmr = 0
         
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        tmr=tmr%3200
        screen.blit(bg_img1, [-tmr, 0])
        screen.blit(bg_img2, [-tmr+1600, 0])  
        screen.blit(bg_img3, [-tmr+3200, 0])  
        screen.blit(kk, [300, 200])
        pg.display.update()
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_SPACE]: 
             kk.move_ip((0, -1))
        tmr += 1
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()