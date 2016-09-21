#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
     if wall_is_on_the_right() and wall_is_above():
        while not (wall_is_on_the_left() and wall_is_beneath()):
            move_down()
            move_left()
        return
     if wall_is_on_the_left() and wall_is_above():
        while not (wall_is_on_the_right() and wall_is_beneath()):
            move_down()
            move_right()
        return
     if wall_is_on_the_right() and wall_is_beneath():
        while not (wall_is_on_the_left() and wall_is_above()):
            move_up()
            move_left()
        return
     if wall_is_on_the_left() and wall_is_beneath():
        while not (wall_is_on_the_right() and wall_is_above()):
            move_up()
            move_right()
        return

if __name__ == '__main__':
    run_tasks()
