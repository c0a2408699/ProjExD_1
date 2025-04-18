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
    kk_rct=kk.get_rect()
    kk_rct.center=300,200
    
    tmr = 0
    kk_rct.center=300,200
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        tmr=tmr%3200
        x=0
        y=0
       
        screen.blit(bg_img1, [-tmr, 0])
        screen.blit(bg_img2, [-tmr+1600, 0])  
        screen.blit(bg_img3, [-tmr+3200, 0])  
        screen.blit(kk,kk_rct)
        pg.display.update()
        x=-1
        if key_lst[pg.K_UP]: 
            y=-1
        if key_lst[pg.K_DOWN]: 
            y=1
        if key_lst[pg.K_LEFT]: 
            x=-1
        if key_lst[pg.K_RIGHT]: 
            x=2
        kk_rct.move_ip((+x, +y))
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()