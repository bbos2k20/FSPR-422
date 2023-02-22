# Firs homework


import random

x = random.randint(0, 1)

money = 0
attempts = 0

while True:
    a = int(input("Введите число: "))
    print(a)
    a == x

    if a > x:
        print(("введите меньше: "))
        attempts += 1
    elif a < x:
        print(("Введите больше: "))
        attempts += 1
    else:
        print("u won,the number was: ", x)
        break
print("колличество ошибок: ", attempts)


if attempts == 0:
    money = 100000
    print("u won 100000$", "БАЛАНС:", money)
    # print("u won 100.000$","БАЛАНС:", money, money+ 100000)
elif attempts == 1:
    money = 500
    print("u won 500$", "БАЛАНС:", money)
elif attempts == 2:
    money = 350
    print("u won 350$", "БАЛАНС:", money)
elif attempts == 3:
    money = 300
    print("u won 300$", "БАЛАНС:", money)
elif attempts == 4:
    money = 200
    print("u won 200$", "БАЛАНС:", money)
elif attempts == 5:
    money = 100
    print("u won 100$", "БАЛАНС:", money)
elif attempts == 6:
    print("u won 0$")
elif 7 <= attempts <= 10:
    money = -100
    print("u lost 10 attempts, that's why u lost: ", money, "$")
elif 11 <= attempts <= 50:
    money = -500
    print("u lost 50 attempts, that's why u lost: ", money, "$")
elif 51 <= attempts <= 100:
    money = -10000
    print("u lost 100 attempts, that's why u lost: ", money, "$")


print("Баланс на данный момент: ", money, "$")


# 2 h/w_____________________________________________________________________________
import re

log = input("ВВЕДИТЕ ЛОГИН: ")
password = input("ВВЕДИТЕ password: ")

text = """
I'm friends with the monster that's under my bed
Get along with the voices inside of my head
You're tryin' to save me, stop holding your breath
And you think I'm crazy, yeah, you think I'm crazy (crazy)
I wanted the fame but not the cover of Newsweek
Oh well, guess beggars can't be choosey
Wanted to receive attention for my music
Wanted to be left alone in public, excuse me
For wantin' my cake, and eat it too, and wantin' it both ways
Fame made me a balloon 'cause my ego inflated
When I blew, see, but it was confusing
'Cause all I wanted to do's be the Bruce Lee of loose leaf
Abused ink, used it as a tool when I blew steam (ooh)
Hit the lottery, ooh-wee
But with what I gave up to get, it was bittersweet
It was like winnin' a used mink
Ironic 'cause I think I'm gettin' so huge I need a shrink
I'm beginnin' to lose sleep, one sheep, two sheep
Going coo-coo and kooky as Kool Keith
But I'm actually weirder than you think, 'cause I'm
I'm friends with the monster that's under my bed
Get along with the voices inside of my head
You're tryin' to save me, stop holdin' your breath
And you think I'm crazy, yeah, you think I'm crazy
Well, that's nothin' (ooh-ooh-ooh-ooh)
(Ooh-ooh-ooh-ooh, ooh-ooh-ooh-ooh)
Well, that's nothin' (ooh-ooh-ooh-ooh)
(Ooh-ooh-ooh-ooh, ooh-ooh-ooh-ooh, ooh-ooh-ooh-ooh)
Now, I ain't much of a poet
But I know somebody once told me to seize the moment
And don't squander it
'Cause you never know when it all could be over tomorrow
So I keep conjurin'
Sometimes I wonder where these thoughts spawn from
Yeah, ponderin'll do you wonders
No wonder you're losing your mind, the way it wanders
Yodel-odel-ay-hee-hoo
I think it went wanderin' off down yonder
And stumbled onto Jeff VanVonderen
'Cause I need an interventionist
To intervene between me and this monster
And save me from myself and all this conflict
'Cause the very thing that I love's killing me
And I can't conquer it
My OCD is conkin' me in the head, keep knockin'
Nobody's home, I'm sleepwalkin'
I'm just relayin' what the voice in my head's sayin'
Don't shoot the messenger, I'm just friends with the
I'm friends with the monster that's under my bed
Get along with the voices inside of my head
You're tryin' to save me, stop holdin' your breath
And you think I'm crazy, yeah, you think I'm crazy
Well, that's nothin' (ooh-ooh-ooh-ooh)
(Ooh-ooh-ooh-ooh, ooh-ooh-ooh-ooh)
Well, that's nothin' (ooh-ooh-ooh-ooh)
(Ooh-ooh-ooh-ooh, ooh-ooh-ooh-ooh, ooh-ooh-ooh-ooh)
Call me crazy, but I have this vision
One day that I'll walk amongst you a regular civilian
But until then, drums get killed and
I'm comin' straight at MC's, blood gets spilled and
I'll take it back to the days that I'd get on a Dre track
Give every kid who got played that pumped-up feelin'
And shit to say back to the kids who played him
I ain't here to save the fuckin' children
But if one kid out of a hundred million
Who are going through a struggle feels it and relates, that's great
It's payback, Russell Wilson
Falling way back in the draft
Turn nothin' into somethin', still can
Make that, straw into gold, chump, I will spin
Rumpelstiltskin in a haystack
Maybe I need a straight jacket, face facts
I am nuts for real, but I'm okay with that
It's nothin', I'm still friends with the
I'm friends with the monster that's under my bed
Get along with the voices inside of my head
You're tryin' to save me, stop holdin' your breath
And you think I'm crazy, yeah, you think I'm crazy
I'm friends with the monster that's under my bed
Get along with the voices inside of my head
You're tryin' to save me, stop holdin' your breath
And you think I'm crazy, yeah, you think I'm crazy
Well, that's nothin' (ooh-ooh-ooh-ooh)
(Ooh-ooh-ooh-ooh, ooh-ooh-ooh-ooh)
Well, that's nothin' (ooh-ooh-ooh-ooh)
(Ooh-ooh-ooh-ooh, ooh-ooh-ooh-ooh, ooh-ooh-ooh-ooh)"""

text = text.lower()
for x, y in ("monster", "cute"), ("MONSTER", "cute"):
    text = text.replace(x, y)
print(text)

import re

word = input("Word: ")
print(len(re.findall(rf"\b{word}\b", text)))
