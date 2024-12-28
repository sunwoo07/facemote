# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define p = Character('박선우', color="#000000")
define l = Character('이소미', color="#f39ed7")
define c = Character('최서화', color="#99e5fc")

screen my_new_screen():
    textbutton "새로운 스크린!" align (0.5, 0.5) action Return()
    
# 여기에서부터 게임이 시작합니다.
label start:
    "게임 시작"
    call screen my_new_screen()
    "엄준식"
    return
