function 省空间(数字: number, 加多少: number) {
    
    //  打开https://app.yinxiang.com/b/aXJPk（开发者必看）
    if (次数 == 数字) {
        
    } else if (USERS_WORDS_ON_SCREEN[0] == "") {
        次数 = 次数 + 加多少
        清除()
        OLED12864_I2C.showString(用户光标x位置User_Type_Locationx, 用户光标y位置User_Type_Locationy, _26个字母与符号[次数], 1)
        当前选择字 = _26个字母与符号[次数]
    } else {
        清除()
        OLED12864_I2C.showString(0, 1, USERS_WORDS_ON_SCREEN[0], 1)
        次数 = 次数 + 加多少
        OLED12864_I2C.showString(用户光标x位置User_Type_Locationx, 用户光标y位置User_Type_Locationy, _26个字母与符号[次数], 1)
        当前选择字 = _26个字母与符号[次数]
    }
    
}

input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    
    if (用户光标x位置User_Type_Locationx == 12) {
        if (用户光标y位置User_Type_Locationy == 3) {
            OLED12864_I2C.clear()
            OLED12864_I2C.showString(0, 0, "vin:bit 0.0.1", 270)
            OLED12864_I2C.showString(0, 1, 当前选择字, 1)
            用户光标y位置User_Type_Locationy = 1
            用户光标x位置User_Type_Locationx += 1
            add_some_words_in_the_list_of_Users_words_on_screen(当前选择字)
        } else {
            用户光标y位置User_Type_Locationy += 1
            add_some_words_in_the_list_of_Users_words_on_screen(当前选择字)
            用户光标x位置User_Type_Locationx = 0
        }
        
    } else {
        用户光标x位置User_Type_Locationx += 1
        add_some_words_in_the_list_of_Users_words_on_screen(当前选择字)
    }
    
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    次数 = 30
})
datalogger.onLogFull(function on_log_full() {
    basic.showIcon(IconNames.No)
})
function 将u设置为空() {
    
    USERS_WORDS_ON_SCREEN = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
}

//  USERS_WORDS_ON_SCREEN这个列表代表屏幕上的字，并非单单只是用户的
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (USERS_WORDS_ON_SCREEN[0] == "") {
        OLED12864_I2C.showString(0, 1, " ", 1)
        当前选择字 = " "
    } else {
        清除()
        OLED12864_I2C.showString(用户光标x位置User_Type_Locationx, 用户光标y位置User_Type_Locationy, " ", 1)
        当前选择字 = " "
    }
    
})
function 系统显示字儿(显示的文本: string) {
    
    if (12 - 用户光标x位置User_Type_Locationx <= 显示的文本.length) {
        if (用户光标y位置User_Type_Locationy == 3) {
            OLED12864_I2C.clear()
            OLED12864_I2C.showString(0, 0, "vin:bit 0.0.1", 270)
            OLED12864_I2C.showString(0, 1, 显示的文本, 1)
            add_some_words_in_the_list_of_Users_words_on_screen(显示的文本)
            用户光标x位置User_Type_Locationx = 1
            用户光标y位置User_Type_Locationy = 1
        } else {
            清除()
            OLED12864_I2C.showString(0, 用户光标y位置User_Type_Locationy + 1, 显示的文本, 1)
            add_some_words_in_the_list_of_Users_words_on_screen(显示的文本)
            用户光标x位置User_Type_Locationx = 1
            用户光标y位置User_Type_Locationy += 1
        }
        
    } else {
        清除()
        OLED12864_I2C.showString(用户光标x位置User_Type_Locationx + 1, 用户光标y位置User_Type_Locationy, 显示的文本, 1)
        add_some_words_in_the_list_of_Users_words_on_screen(显示的文本)
        用户光标x位置User_Type_Locationx += 1
    }
    
}

input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    省空间(39, 1)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (判断按钮第几遍 == 0) {
        if (USERS_WORDS_ON_SCREEN[0].charAt(USERS_WORDS_ON_SCREEN[0].length - 1) == "/") {
            OLED12864_I2C.clear()
            OLED12864_I2C.showString(0, 0, "vin:bit 0.0.1", 270)
            OLED12864_I2C.showString(0, 1, USERS_WORDS_ON_SCREEN[0], 1)
            临时 = USERS_WORDS_ON_SCREEN[0].substr(USERS_WORDS_ON_SCREEN[0].length - 4, USERS_WORDS_ON_SCREEN[0].length - 1)
            临时1 = USERS_WORDS_ON_SCREEN[0].substr(USERS_WORDS_ON_SCREEN[0].length - 9, USERS_WORDS_ON_SCREEN[0].length - 1)
            临时2 = USERS_WORDS_ON_SCREEN[0].substr(USERS_WORDS_ON_SCREEN[0].length - 7, USERS_WORDS_ON_SCREEN[0].length - 1)
            临时3 = USERS_WORDS_ON_SCREEN[0].substr(USERS_WORDS_ON_SCREEN[0].length - 5, USERS_WORDS_ON_SCREEN[0].length - 1)
            临时3a = USERS_WORDS_ON_SCREEN[0].substr(USERS_WORDS_ON_SCREEN[0].length - 5, USERS_WORDS_ON_SCREEN[0].length - 2)
            临时3b = USERS_WORDS_ON_SCREEN[0].substr(USERS_WORDS_ON_SCREEN[0].indexOf("s"), 4)
            临时4 = USERS_WORDS_ON_SCREEN[0].substr(USERS_WORDS_ON_SCREEN[0].length - 6, 3)
            当前命令 = ""
            临时_特殊 = 0
            for (let 值2 of 命令大全_Order_sequences) {
                if (值2 == 临时) {
                    当前命令 = 值2
                    临时_特殊 = 1
                }
                
            }
            for (let 值3 of 命令大全_Order_sequences) {
                if (值3 == 临时1) {
                    当前命令 = 值3
                    临时_特殊 = 1
                }
                
            }
            for (let 值4 of 命令大全_Order_sequences) {
                if (值4 == 临时2) {
                    当前命令 = 值4
                    临时_特殊 = 1
                }
                
            }
            for (let 值5 of 命令大全_Order_sequences) {
                if (值5 == 临时3) {
                    当前命令 = 值5
                    临时_特殊 = 1
                }
                
            }
            for (let 值52 of 命令大全_Order_sequences) {
                if (值52 == 临时3a) {
                    当前命令 = 值52
                    临时_特殊 = 1
                }
                
            }
            for (let 值522 of 命令大全_Order_sequences) {
                if (值522 == 临时3b) {
                    当前命令 = 值522
                    临时_特殊 = 1
                }
                
            }
            for (let 值5222 of 命令大全_Order_sequences) {
                if (值5222 == 临时4) {
                    当前命令 = 值5222
                    临时_特殊 = 1
                }
                
            }
            if (临时_特殊 == 0) {
                // 这个变量名中的特殊表示是否是命令（本注释没有超强的理解能力
                basic.showLeds(`
                    # # . # #
                                        # # . # #
                                        . . . . .
                                        . # # # .
                                        # . . . #
                `)
                basic.pause(1)
                basic.clearScreen()
            } else if (临时3 == "sud.") {
                OLED12864_I2C.clear()
                OLED12864_I2C.showString(0, 0, "vin:bit 0.0.1", 270)
                用户光标x位置User_Type_Locationx = 0
                用户光标y位置User_Type_Locationy = 1
                将u设置为空()
            } else if (临时3 == "std./") {
                OLED12864_I2C.clear()
                OLED12864_I2C.showString(0, 0, "vin:bit 0.0.1", 270)
                用户光标x位置User_Type_Locationx = 0
                用户光标y位置User_Type_Locationy = 1
                临时d = "" + convertToText(randint(0, 9999)) + convertToText(randint(0, 9999) % 2)
                datalogger.setColumnTitles(临时d)
                datalogger.log(datalogger.createCV(临时d, USERS_WORDS_ON_SCREEN[0].substr(0, USERS_WORDS_ON_SCREEN[0].length - 5)))
                music.playSoundEffect(music.builtinSoundEffect(soundExpression.giggle), SoundExpressionPlayMode.InBackground)
                basic.showLeds(`
                    . . . . .
                                        . . . . .
                                        . . . . .
                                        # . . . .
                                        . . . . .
                `)
                basic.showLeds(`
                    . . . . .
                                        . . . . .
                                        . . . . .
                                        # . . . .
                                        . # . . .
                `)
                basic.showLeds(`
                    . . . . .
                                        . . . . .
                                        . . . . .
                                        # . # . .
                                        . # . . .
                `)
                basic.showLeds(`
                    . . . . .
                                        . . . . #
                                        . . . # .
                                        # . # . .
                                        . # . . .
                `)
                OLED12864_I2C.showString(0, 1, "You can view the data you wrote on ", 1)
                basic.pause(2000)
                OLED12864_I2C.clear()
                OLED12864_I2C.showString(0, 0, "vinbit 0.0.1", 1)
                OLED12864_I2C.showString(0, 1, "the computer. ", 1)
                判断是否达顶 = 1
                basic.pause(1000)
                basic.clearScreen()
                将u设置为空()
            } else if (临时3b == "show") {
                系统显示字儿(USERS_WORDS_ON_SCREEN[0].substr(USERS_WORDS_ON_SCREEN[0].indexOf("w") + 2, USERS_WORDS_ON_SCREEN[0].length - 1 - (USERS_WORDS_ON_SCREEN[0].indexOf("w") + 2)))
                判断是否达顶 = 1
            } else if (临时4 == "sl.") {
                led.plot(parseFloat(USERS_WORDS_ON_SCREEN[0].charAt(USERS_WORDS_ON_SCREEN[0].length - 3)), parseFloat(USERS_WORDS_ON_SCREEN[0].charAt(USERS_WORDS_ON_SCREEN[0].length - 2)))
            } else if (临时3 == "help") {
                OLED12864_I2C.clear()
                OLED12864_I2C.showString(0, 0, "vinbit 0.0.1", 1)
                OLED12864_I2C.showString(0, 1, "visit https://app.yinxiang.com/b/aXJPk", 1)
            } else {
                系统显示字儿(":")
                判断是否达顶 = 1
            }
            
        } else {
            
        }
        
    } else {
        临时a = parseFloat(USERS_WORDS_ON_SCREEN[0].substr(USERS_WORDS_ON_SCREEN[0].indexOf(":") + 1, USERS_WORDS_ON_SCREEN[0].indexOf("&") - 1 - USERS_WORDS_ON_SCREEN[0].indexOf(":")))
        临时b = parseFloat(USERS_WORDS_ON_SCREEN[0].substr(USERS_WORDS_ON_SCREEN[0].indexOf("&") + 1, USERS_WORDS_ON_SCREEN[0].length - (USERS_WORDS_ON_SCREEN[0].indexOf("&") + 1)))
        if (当前命令 == "add") {
            系统显示字儿(" " + convertToText(临时a + 临时b))
            判断是否达顶 = 1
        } else if (当前命令 == "subtract" || 当前命令 == "sub.") {
            系统显示字儿(" " + convertToText(临时a - 临时b))
            判断是否达顶 = 1
        } else if (当前命令 == "multiply" || 当前命令 == "mul.") {
            系统显示字儿(" " + convertToText(临时a * 临时b))
            判断是否达顶 = 1
        } else if (当前命令 == "divde" || 当前命令 == "div.") {
            系统显示字儿(" " + convertToText(临时a / 临时b))
            判断是否达顶 = 1
        } else {
            basic.showLeds(`
                # # . # #
                                # # . # #
                                . . . . .
                                . # # # .
                                # . . . #
            `)
            basic.pause(1)
            basic.clearScreen()
        }
        
    }
    
})
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    省空间(0, -1)
})
function 清除() {
    
    OLED12864_I2C.clear()
    OLED12864_I2C.showString(0, 0, "vin:bit 0.0.1", 270)
    至第几行有空 = 0
    for (let 值6 of USERS_WORDS_ON_SCREEN) {
        if (值6.isEmpty()) {
            break
        } else {
            至第几行有空 += 1
        }
        
    }
    if (至第几行有空 == 0) {
        OLED12864_I2C.showString(0, 循环次数 + 1, USERS_WORDS_ON_SCREEN[0], 1)
    } else {
        循环次数 = 0
        if (至第几行有空 > 4) {
            for (let index = 0; index < 至第几行有空 % 4; index++) {
                OLED12864_I2C.showString(0, 循环次数 + 1, USERS_WORDS_ON_SCREEN[循环次数], 1)
                循环次数 += 1
            }
        } else {
            for (let index2 = 0; index2 < 至第几行有空; index2++) {
                OLED12864_I2C.showString(0, 循环次数 + 1, USERS_WORDS_ON_SCREEN[循环次数], 1)
                循环次数 += 1
            }
        }
        
    }
    
}

function add_some_words_in_the_list_of_Users_words_on_screen(add_word: string) {
    
    第几行 = 0
    for (let 值 of USERS_WORDS_ON_SCREEN) {
        if (值.length == 13) {
            第几行 += 1
        }
        
    }
    USERS_WORDS_ON_SCREEN[第几行] = "" + USERS_WORDS_ON_SCREEN[第几行] + add_word
}

let 第几行 = 0
let 循环次数 = 0
let 至第几行有空 = 0
let 临时b = 0
let 临时a = 0
let 判断是否达顶 = 0
let 临时d = ""
let 临时_特殊 = 0
let 当前命令 = ""
let 临时4 = ""
let 临时3a = ""
let 临时3 = ""
let 临时2 = ""
let 临时1 = ""
let 临时 = ""
let 当前选择字 = ""
let 用户光标x位置User_Type_Locationx = 0
let USERS_WORDS_ON_SCREEN : string[] = []
let 用户光标y位置User_Type_Locationy = 0
let 次数 = 0
let 命令大全_Order_sequences : string[] = []
let _26个字母与符号 : string[] = []
let 判断按钮第几遍 = 0
let 临时3b = ""
临时3b = "0"
判断按钮第几遍 = 0
_26个字母与符号 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ",", ".", "&", "/", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
//  std的意思是"set up ducument"的缩写，中文是新建或将设置文件。
//  stf的"save the file"的缩写，中文是保存·文件。
//  otd的意思是open the ducument"的缩写，中文是打开文件。
命令大全_Order_sequences = ["add", "subtract", "multiply", "divide", "sub.", "mul.", "div.", "sud.", "std.", "show", "sl.", "help"]
//  sl的意思是show led，显示led灯的意思。
将u设置为空()
次数 = 0
datalogger.mirrorToSerial(true)
OLED12864_I2C.init(60)
OLED12864_I2C.showString(0, 0, "vin:bit 0.0.1", 270)
OLED12864_I2C.showString(0, 1, "a", 1)
let OLEDs_word_now = "vin:bit 0.0.1"
用户光标y位置User_Type_Locationy = 1
datalogger.deleteLog(datalogger.DeleteType.Full)
music.setBuiltInSpeakerEnabled(true)
临时3b == ""
basic.forever(function on_forever() {
    
    if (判断是否达顶 == 1) {
        if (input.buttonIsPressed(Button.A) || (input.pinIsPressed(TouchPin.P0) || (input.logoIsPressed() || (input.pinIsPressed(TouchPin.P1) || (input.buttonIsPressed(Button.B) || input.pinIsPressed(TouchPin.P2)))))) {
            control.reset()
            判断是否达顶 = 0
        }
        
    }
    
})
