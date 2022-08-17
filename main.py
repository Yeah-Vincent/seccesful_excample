def 省空间(数字: number, 加多少: number):
    global 次数, 当前选择字
    # 打开https://app.yinxiang.com/b/aXJPk（开发者必看）
    if 次数 == 数字:
        pass
    elif USERS_WORDS_ON_SCREEN[0] == "":
        次数 = 次数 + 加多少
        清除()
        OLED12864_I2C.show_string(用户光标x位置User_Type_Locationx,
            用户光标y位置User_Type_Locationy,
            _26个字母与符号[次数],
            1)
        当前选择字 = _26个字母与符号[次数]
    else:
        清除()
        OLED12864_I2C.show_string(0, 1, USERS_WORDS_ON_SCREEN[0], 1)
        次数 = 次数 + 加多少
        OLED12864_I2C.show_string(用户光标x位置User_Type_Locationx,
            用户光标y位置User_Type_Locationy,
            _26个字母与符号[次数],
            1)
        当前选择字 = _26个字母与符号[次数]

def on_pin_pressed_p0():
    global 用户光标y位置User_Type_Locationy, 用户光标x位置User_Type_Locationx
    if 用户光标x位置User_Type_Locationx == 12:
        if 用户光标y位置User_Type_Locationy == 3:
            OLED12864_I2C.clear()
            OLED12864_I2C.show_string(0, 0, "vin:bit 0.0.1", 270)
            OLED12864_I2C.show_string(0, 1, 当前选择字, 1)
            用户光标y位置User_Type_Locationy = 1
            用户光标x位置User_Type_Locationx += 1
            add_some_words_in_the_list_of_Users_words_on_screen(当前选择字)
        else:
            用户光标y位置User_Type_Locationy += 1
            add_some_words_in_the_list_of_Users_words_on_screen(当前选择字)
            用户光标x位置User_Type_Locationx = 0
    else:
        用户光标x位置User_Type_Locationx += 1
        add_some_words_in_the_list_of_Users_words_on_screen(当前选择字)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_logo_pressed():
    global 次数
    次数 = 30
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_log_full():
    basic.show_icon(IconNames.NO)
datalogger.on_log_full(on_log_full)

def 将u设置为空():
    global USERS_WORDS_ON_SCREEN
    USERS_WORDS_ON_SCREEN = ["",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""]
# USERS_WORDS_ON_SCREEN这个列表代表屏幕上的字，并非单单只是用户的

def on_button_pressed_a():
    global 当前选择字
    if USERS_WORDS_ON_SCREEN[0] == "":
        OLED12864_I2C.show_string(0, 1, " ", 1)
        当前选择字 = " "
    else:
        清除()
        OLED12864_I2C.show_string(用户光标x位置User_Type_Locationx,
            用户光标y位置User_Type_Locationy,
            " ",
            1)
        当前选择字 = " "
input.on_button_pressed(Button.A, on_button_pressed_a)

def 系统显示字儿(显示的文本: str):
    global 用户光标x位置User_Type_Locationx, 用户光标y位置User_Type_Locationy
    if 12 - 用户光标x位置User_Type_Locationx <= len(显示的文本):
        if 用户光标y位置User_Type_Locationy == 3:
            OLED12864_I2C.clear()
            OLED12864_I2C.show_string(0, 0, "vin:bit 0.0.1", 270)
            OLED12864_I2C.show_string(0, 1, 显示的文本, 1)
            add_some_words_in_the_list_of_Users_words_on_screen(显示的文本)
            用户光标x位置User_Type_Locationx = 1
            用户光标y位置User_Type_Locationy = 1
        else:
            清除()
            OLED12864_I2C.show_string(0, 用户光标y位置User_Type_Locationy + 1, 显示的文本, 1)
            add_some_words_in_the_list_of_Users_words_on_screen(显示的文本)
            用户光标x位置User_Type_Locationx = 1
            用户光标y位置User_Type_Locationy += 1
    else:
        清除()
        OLED12864_I2C.show_string(用户光标x位置User_Type_Locationx + 1,
            用户光标y位置User_Type_Locationy,
            显示的文本,
            1)
        add_some_words_in_the_list_of_Users_words_on_screen(显示的文本)
        用户光标x位置User_Type_Locationx += 1

def on_pin_pressed_p2():
    省空间(39, 1)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_b():
    global 临时, 临时1, 临时2, 临时3, 临时3a, 临时3b, 临时4, 当前命令, 临时_特殊, 用户光标x位置User_Type_Locationx, 用户光标y位置User_Type_Locationy, 临时d, 判断是否达顶, 临时a, 临时b
    if 判断按钮第几遍 == 0:
        if USERS_WORDS_ON_SCREEN[0].char_at(len(USERS_WORDS_ON_SCREEN[0]) - 1) == "/":
            OLED12864_I2C.clear()
            OLED12864_I2C.show_string(0, 0, "vin:bit 0.0.1", 270)
            OLED12864_I2C.show_string(0, 1, USERS_WORDS_ON_SCREEN[0], 1)
            临时 = USERS_WORDS_ON_SCREEN[0].substr(len(USERS_WORDS_ON_SCREEN[0]) - 4,
                len(USERS_WORDS_ON_SCREEN[0]) - 1)
            临时1 = USERS_WORDS_ON_SCREEN[0].substr(len(USERS_WORDS_ON_SCREEN[0]) - 9,
                len(USERS_WORDS_ON_SCREEN[0]) - 1)
            临时2 = USERS_WORDS_ON_SCREEN[0].substr(len(USERS_WORDS_ON_SCREEN[0]) - 7,
                len(USERS_WORDS_ON_SCREEN[0]) - 1)
            临时3 = USERS_WORDS_ON_SCREEN[0].substr(len(USERS_WORDS_ON_SCREEN[0]) - 5,
                len(USERS_WORDS_ON_SCREEN[0]) - 1)
            临时3a = USERS_WORDS_ON_SCREEN[0].substr(len(USERS_WORDS_ON_SCREEN[0]) - 5,
                len(USERS_WORDS_ON_SCREEN[0]) - 2)
            临时3b = USERS_WORDS_ON_SCREEN[0].substr(USERS_WORDS_ON_SCREEN[0].index_of("s"), 4)
            临时4 = USERS_WORDS_ON_SCREEN[0].substr(len(USERS_WORDS_ON_SCREEN[0]) - 6, 3)
            当前命令 = ""
            临时_特殊 = 0
            for 值2 in 命令大全_Order_sequences:
                if 值2 == 临时:
                    当前命令 = 值2
                    临时_特殊 = 1
            for 值3 in 命令大全_Order_sequences:
                if 值3 == 临时1:
                    当前命令 = 值3
                    临时_特殊 = 1
            for 值4 in 命令大全_Order_sequences:
                if 值4 == 临时2:
                    当前命令 = 值4
                    临时_特殊 = 1
            for 值5 in 命令大全_Order_sequences:
                if 值5 == 临时3:
                    当前命令 = 值5
                    临时_特殊 = 1
            for 值52 in 命令大全_Order_sequences:
                if 值52 == 临时3a:
                    当前命令 = 值52
                    临时_特殊 = 1
            for 值522 in 命令大全_Order_sequences:
                if 值522 == 临时3b:
                    当前命令 = 值522
                    临时_特殊 = 1
            for 值5222 in 命令大全_Order_sequences:
                if 值5222 == 临时4:
                    当前命令 = 值5222
                    临时_特殊 = 1
            if 临时_特殊 == 0:         #这个变量名中的特殊表示是否是命令（本注释没有超强的理解能力
                basic.show_leds("""
                    # # . # #
                                        # # . # #
                                        . . . . .
                                        . # # # .
                                        # . . . #
                """)
                basic.pause(1)
                basic.clear_screen()
            elif 临时3 == "sud.":
                OLED12864_I2C.clear()
                OLED12864_I2C.show_string(0, 0, "vin:bit 0.0.1", 270)
                用户光标x位置User_Type_Locationx = 0
                用户光标y位置User_Type_Locationy = 1
                将u设置为空()
            elif 临时3 == "std./":
                OLED12864_I2C.clear()
                OLED12864_I2C.show_string(0, 0, "vin:bit 0.0.1", 270)
                用户光标x位置User_Type_Locationx = 0
                用户光标y位置User_Type_Locationy = 1
                临时d = "" + convert_to_text(randint(0, 9999)) + convert_to_text(randint(0, 9999) % 2)
                datalogger.set_column_titles(临时d)
                datalogger.log(datalogger.create_cv(临时d,
                        USERS_WORDS_ON_SCREEN[0].substr(0, len(USERS_WORDS_ON_SCREEN[0]) - 5)))
                music.play_sound_effect(music.builtin_sound_effect(soundExpression.giggle),
                    SoundExpressionPlayMode.IN_BACKGROUND)
                basic.show_leds("""
                    . . . . .
                                        . . . . .
                                        . . . . .
                                        # . . . .
                                        . . . . .
                """)
                basic.show_leds("""
                    . . . . .
                                        . . . . .
                                        . . . . .
                                        # . . . .
                                        . # . . .
                """)
                basic.show_leds("""
                    . . . . .
                                        . . . . .
                                        . . . . .
                                        # . # . .
                                        . # . . .
                """)
                basic.show_leds("""
                    . . . . .
                                        . . . . #
                                        . . . # .
                                        # . # . .
                                        . # . . .
                """)
                OLED12864_I2C.show_string(0, 1, "You can view the data you wrote on ", 1)
                basic.pause(2000)
                OLED12864_I2C.clear()
                OLED12864_I2C.show_string(0, 0, "vinbit 0.0.1", 1)
                OLED12864_I2C.show_string(0, 1, "the computer. ", 1)
                判断是否达顶 = 1
                basic.pause(1000)
                basic.clear_screen()
                将u设置为空()
            elif 临时3b == "show":
                系统显示字儿(USERS_WORDS_ON_SCREEN[0].substr(USERS_WORDS_ON_SCREEN[0].index_of("w") + 2,
                        len(USERS_WORDS_ON_SCREEN[0]) - 1 - (USERS_WORDS_ON_SCREEN[0].index_of("w") + 2)))
                判断是否达顶 = 1
            elif 临时4 == "sl.":
                led.plot(parse_float(USERS_WORDS_ON_SCREEN[0].char_at(len(USERS_WORDS_ON_SCREEN[0]) - 3)),
                    parse_float(USERS_WORDS_ON_SCREEN[0].char_at(len(USERS_WORDS_ON_SCREEN[0]) - 2)))
            elif 临时3 == "help":
                OLED12864_I2C.clear()
                OLED12864_I2C.show_string(0, 0, "vinbit 0.0.1", 1)
                OLED12864_I2C.show_string(0, 1, "visit https://app.yinxiang.com/b/aXJPk", 1)
            else:
                系统显示字儿(":")
                判断是否达顶 = 1
        else:
            pass
    else:
        临时a = parse_float(USERS_WORDS_ON_SCREEN[0].substr(USERS_WORDS_ON_SCREEN[0].index_of(":") + 1,
                USERS_WORDS_ON_SCREEN[0].index_of("&") - 1 - USERS_WORDS_ON_SCREEN[0].index_of(":")))
        临时b = parse_float(USERS_WORDS_ON_SCREEN[0].substr(USERS_WORDS_ON_SCREEN[0].index_of("&") + 1,
                len(USERS_WORDS_ON_SCREEN[0]) - (USERS_WORDS_ON_SCREEN[0].index_of("&") + 1)))
        if 当前命令 == "add":
            系统显示字儿(" " + convert_to_text(临时a + 临时b))
            判断是否达顶 = 1
        elif 当前命令 == "subtract" or 当前命令 == "sub.":
            系统显示字儿(" " + convert_to_text(临时a - 临时b))
            判断是否达顶 = 1
        elif 当前命令 == "multiply" or 当前命令 == "mul.":
            系统显示字儿(" " + convert_to_text(临时a * 临时b))
            判断是否达顶 = 1
        elif 当前命令 == "divde" or 当前命令 == "div.":
            系统显示字儿(" " + convert_to_text(临时a / 临时b))
            判断是否达顶 = 1
        else:
            basic.show_leds("""
                # # . # #
                                # # . # #
                                . . . . .
                                . # # # .
                                # . . . #
            """)
            basic.pause(1)
            basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    省空间(0, -1)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def 清除():
    global 至第几行有空, 循环次数
    OLED12864_I2C.clear()
    OLED12864_I2C.show_string(0, 0, "vin:bit 0.0.1", 270)
    至第几行有空 = 0
    for 值6 in USERS_WORDS_ON_SCREEN:
        if 值6.is_empty():
            break
        else:
            至第几行有空 += 1
    if 至第几行有空 == 0:
        OLED12864_I2C.show_string(0, 循环次数 + 1, USERS_WORDS_ON_SCREEN[0], 1)
    else:
        循环次数 = 0
        if 至第几行有空 > 4:
            for index in range(至第几行有空 % 4):
                OLED12864_I2C.show_string(0, 循环次数 + 1, USERS_WORDS_ON_SCREEN[循环次数], 1)
                循环次数 += 1
        else:
            for index2 in range(至第几行有空):
                OLED12864_I2C.show_string(0, 循环次数 + 1, USERS_WORDS_ON_SCREEN[循环次数], 1)
                循环次数 += 1
def add_some_words_in_the_list_of_Users_words_on_screen(add_word: str):
    global 第几行
    第几行 = 0
    for 值 in USERS_WORDS_ON_SCREEN:
        if len(值) == 13:
            第几行 += 1
    USERS_WORDS_ON_SCREEN[第几行] = "" + USERS_WORDS_ON_SCREEN[第几行] + add_word
第几行 = 0
循环次数 = 0
至第几行有空 = 0
临时b = 0
临时a = 0
判断是否达顶 = 0
临时d = ""
临时_特殊 = 0
当前命令 = ""
临时4 = ""
临时3a = ""
临时3 = ""
临时2 = ""
临时1 = ""
临时 = ""
当前选择字 = ""
用户光标x位置User_Type_Locationx = 0
USERS_WORDS_ON_SCREEN: List[str] = []
用户光标y位置User_Type_Locationy = 0
次数 = 0
命令大全_Order_sequences: List[str] = []
_26个字母与符号: List[str] = []
判断按钮第几遍 = 0
临时3b = ""
临时3b = "0"
判断按钮第几遍 = 0
_26个字母与符号 = ["a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    ",",
    ".",
    "&",
    "/",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0"]
# std的意思是"set up ducument"的缩写，中文是新建或将设置文件。
# stf的"save the file"的缩写，中文是保存·文件。
# otd的意思是open the ducument"的缩写，中文是打开文件。
命令大全_Order_sequences = ["add",
    "subtract",
    "multiply",
    "divide",
    "sub.",
    "mul.",
    "div.",
    "sud.",
    "std.",
    "show",
    "sl.",
    "help"]
# sl的意思是show led，显示led灯的意思。
将u设置为空()
次数 = 0
datalogger.mirror_to_serial(True)
OLED12864_I2C.init(60)
OLED12864_I2C.show_string(0, 0, "vin:bit 0.0.1", 270)
OLED12864_I2C.show_string(0, 1, "a", 1)
OLEDs_word_now = "vin:bit 0.0.1"
用户光标y位置User_Type_Locationy = 1
datalogger.delete_log(datalogger.DeleteType.FULL)
music.set_built_in_speaker_enabled(True)
临时3b == ""

def on_forever():
    global 判断是否达顶
    if 判断是否达顶 == 1:
        if input.button_is_pressed(Button.A) or (input.pin_is_pressed(TouchPin.P0) or (input.logo_is_pressed() or (input.pin_is_pressed(TouchPin.P1) or (input.button_is_pressed(Button.B) or input.pin_is_pressed(TouchPin.P2))))):
            control.reset()
            判断是否达顶 = 0
basic.forever(on_forever)
