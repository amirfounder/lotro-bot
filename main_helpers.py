def countdown(t=5):
    """
    Runs a timer before bot runs
    :param t: specials time (default 5)
    :return: void
    """
    print('bot starting in...')
    for i in range(t):
        print(t - i)
        time.sleep(1)
    print('bot deployed')


def reset_camera():
    """
    Resets the camera to bird view. Zoom out all the way unless running app LIVE
    :return: void
    """

    # Adjust screen (1)

    pyautogui.mouseDown()
    generate_delay(100)
    pyautogui.move(0, 500)
    generate_delay(100)
    pyautogui.mouseUp()
    generate_delay(200)

    # Reset mouse position

    pyautogui.move(0, -500)
    generate_delay(100)

    # Adjust screen (2)

    pyautogui.mouseDown()
    generate_delay(100)
    pyautogui.move(0, 500)
    generate_delay(100)
    pyautogui.mouseUp()
    generate_delay(200)

    # Scroll in

    for i in range(21):
        pyautogui.scroll(-1)
    generate_delay(500)

    # Zoom in on production server

    if LIVE:
        for i in range(9):
            pyautogui.scroll(1)
        generate_delay(500)