#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    while wall_is_beneath() or wall_is_above() or wall_is_on_the_right() or wall_is_on_the_left():
        if not wall_is_above():
            move_up()
        if not wall_is_on_the_left():
            mo
if __name__ == '__main__':
    run_tasks()



if __name__ == '__main__':
    run_tasks()
