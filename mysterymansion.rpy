# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.




define p = Character("Private Investigator", color = "#FFFFFF")
define sable = Character("Sable Blackwood")
define m = Character("Martha Starkwood", color = "#60A3D9")
define e = Character("Mr. Espinosa", color = "#FFA500")
define l = Character("Mason Starkwood",color = "#50C878")
define o = Character("Olivia Starkwood", color = "#AE388B")
define g = Character("Greta Pennywit", color = "#AEAEAE")
# The game starts here.
 

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

scene livingroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    
show sable regular

    # These display lines of dialogue.



p "Good evening, Ms. Blackwood, I'm here to follow up on the letter I recieved, I understand 3 murders have taken place and I'm here to get to the bottom of this"

sable "Thank you for arriving here on such short notice. Tragedy has struck this family bad. Mr. Starkwood and 2 of his children have died."
    
p "Can I have some background info on the case?"

sable "Ofcourse, the three victims are Liam, Amelia and Mr.Starkwood."
sable"Their deaths happened so close together that I believe that there is a pattern brewing."

p "What can you tell me about the victims?"

sable "Mr. Starkwood was a great man, although he was rich he was quite the philanthropist constantly giving back to the community."
sable "Amelia was a smart, ambitious girl although at times she was too ambitious, she was in a heated legal battle with her father near the time of their deaths."
sable "Liam was fun-loving and creative, him and Mason were always up to something. You could never find one without the other."
    
p "Thank you, I know exactly how I'm going to start this investigation"

hide sable regular

scene study

show martha

p "Ms. Starkwood? I was notified by Ms. Blackwood about the murders that have been happening to your family? Do you mind answering a few questions?"

m "Thank goodness your here, my dear husband and children were killed and this needs to be solved."

menu:

    "Do you know who could've done this?":
        jump mgood_start
        
    "Do you have any involvement?":
        jump mbad_start

label mgood_start:
    m "Our family has no bad blood with any one, we are helpful members of the community and our name brings great honor."

    menu: 
        "What about inside your family? I hear there has been a lot of drama brewing.":
            jump mgood_path

        "Not even with your own daughter?":
            jump mgood_path

label mgood_path:
    m"What are you suggesting?"

    menu:
        "I hear things weren't always smooth between you, your husband and Amelia.":
            jump amelia_info

        "Martha, did you really think you would be able to hide the custody battle?":
            jump amelia_info

label amelia_info:
    m "Fine, you want the truth? Amelia was a selfish brat that we had to cut out of the family will because of how greedy she had became."
    m "She believed that she was entitled to the almost the entire estate. The legal battle almost tore our family apart."
    jump m_end


label mbad_start:
    hide martha
    show martha mad
    m "How dare you, to think I would kill my own family is preposterous!"

    menu:
        "I've seen many cases like this before. Please remain cooperative and honest with me, and we will get to the bottom of this.":
            hide martha mad
            show martha
            m "I would never do such a thing and I don't know who would"
            jump mgood_start 

        "I find it hard to believe that you would not consider yourself a suspect, given the circumstances.it is not uncommon for family members to be involved in such heinous crimes.":
            jump mbad_end

label mbad_end:
    m "How dare you suggest that I had anything to do with my own husband's death!?"
    m "I loved him with all my heart, and the thought of being involved in such a heinous act sickens me. Your insinuations are not only unfounded but insulting."
    m "I demand that you focus your investigation on finding the real culprit instead of making baseless accusations against me!"
    m "I refuse to entertain this matter any further, get out of my sight before you find yourself out of a job!"
    jump espinosa_int 

label m_end:
    m "When the news had been brought to me that she had passed, I cannot say I was upset."

hide martha 
hide martha mad
label espinosa_int:
    scene outside
    show espinosa
    
p "Good evening sir, Mr Espinsosa, correct?"

e "That's correct, good evening. What is the matter?"

menu:

    "To my knowledge 3 murders have taken place under your watch, have you noticed anything suspicious?":
        jump e_ask

    "If you don't mind me asking, how can something like this happen under your watch? Sleeping on the job?":
        jump e_accuse

label e_ask: 
    e "I don't know too much but what I have seen is that Greta has been always been awfully quiet, lurking in the background, complaining under her breath, always with an attitude."
    e "Frankly she scares me."
    
    menu: 
        "You're awfully quick to point the finger?":
            jump e_end

        "Is she available for questioning?":
            jump e_end2

label e_accuse:
    e "Are you suggesting that I have involvement? I have the least motive to commit such acts."
    e "I cherish this job and Mr. Starkwood was a great boss."
    
    p "Im just saying it seems odd that a security guard can't offer any form of security."

    e "I refuse to be insulted on the clock, if you have no further questions I suggest you look somewhere else."

    menu:
        "Well have you noticed anything?":
            jump e_ask

        "No further questions":
            jump liam_int


label e_end:
    e "I'm just telling you what I've noticed, nothing more officer."
    jump liam_int

label e_end2:
    e "You could try, but she's always refused to talk to any sort of police, kind of shady if you ask me."
    jump liam_int

label liam_int:
    scene gameroom
    hide espinosa 
    show liam 

p "So I hear you and Liam were inseparable, his death must've hit you hard?"

l "In our younger years we were, Liam was different man near the time of his death?"

menu:
    "What do you mean he was a different man?":
        jump l_talk 
    
    "Care to elaborate?":
        jump l_talk
    
label l_talk:
    l "Let's just say Liam became a bit too focused on the wrong things."

    menu:
        "The wrong things?":
            jump l_talk2
        "I don't have time for games, you need to tell me what you mean now!":
            jump l_mad
    
label l_talk2:
    l "My brother tended to get very money hunger at times"
    p "Keep talking."
    l "He was stealing money from the family fund, he used to do it here and there but he kept getting greedier."
    l "Dad noticed and was about to confront him but then..."
    p "It's ok, I understand, thank you for your time"
    jump olivia

label l_mad:
    hide liam 
    show liam mad
    l "Watch your mouth! I urge you to not forget that you're employed by my family."

    menu:
        "I urge you to not forget that I am conducting and investigation and you're cryptic way with words is doing nothing but slowing me down.":
            jump l_talk2
        "You're giving me good reason to think you had involvement.":
            jump l_bad
    
label l_bad:
    l "You're lucky, we need you to help this investigation, otherwise I would have to deal with you myself."
    jump olivia

label l_connect:
    l "I'll ask again, what do you mean by the wrong things?"
    jump l_talk2
    
label olivia:
    scene office
    hide liam
    show olivia

p "Good evening Olivia, how are you holding up?"

o "I can't believe everything that's happened, WHY US?!!"

menu:
    "I know this is a hard time but I need to ask you some questions.":
        jump o_continue
    "Everything is gonna be ok we're gonna get to the bottom of this.":
       jump o_continue

label o_continue:
    o "THIS IS ALL AMELIA'S FAULT, if she wasn't so greedy none of this would be happening!!"
    p "Calm down, I understand you're upset but now is not the time to point fingers."
    o "YOU DON'T UNDERSTAND, SHE ALMOST THE TORE THE FAMILY APART!!!"

    menu:
        "Please elaborate.":
            jump o_end
        "Please calm down.":
            jump o_end

label o_end:
    o "LEAVE ME ALONE!!"

hide olivia
scene outside
show espinosa
e "What else do ya need?"
p "While invesitgating I noticed a hidden door"
e "Oh the private study? The only ones with access were me, Sable, Greta and Mr. Starkwood."
e "Here's the keys if you want to take a look around"

label minigame:
    call screen office_nav

    scene bg_office with dissolve 

    screen office_nav():
        add "bg_office"
        modal True

        imagebutton auto "bg_letters_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Letters")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("look_at_letters")

        imagebutton auto "bg_cabinet_%s":
            focus_mask True
            hovered SetVariable("screen_tooltips", "Cabinet")
            unhovered SetVariable("screen_tooltip", "")
            action Jump("look_through_cabinet")

        imagebutton auto "bg_board_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Board")
            unhovered SetVariable("screen_tooltip","")
            action Jump("look_at_board")

label look_at_letters:
    scene bg_letters_closeup with dissolve
    pause 3.0 
    "Love letters??"
    "...Between Sable and Mr. Starkwood??"
    jump minigame
    

label look_through_cabinet:
    scene bg_upclose_cabinet 
    pause 3.0 
    "*Finds bloody knife*"
    "The murder weapon?"
    jump sus_lineup

label look_at_board:
    scene bg_reciept_board 
    pause 3.0 
    "Reciepts for poison?"
    "Amelia was poisoned"
    jump minigame





    
label sus_lineup:
    scene livingroom
    show martha at right
    show sable regular at center 
    show liam at left
    show espinosa at Position (xpos = 0.35)
    show greta  at Position (xpos = 0.65)

    p "I've made a major breakthrough in the investigation. I've gathered you all here today as suspects in my investigation."
    m "Do I really have to be here? I would never lay a finger on my own husband and children?"
    l "Same here, do you really believe that I've murdered my own family?"
    p "Everyone quiet. I'm here to reveal my decision."
    p "The killer is..."
    menu:
        "Martha Starkwood":
            jump choose_martha
        "Sable Blackwood":
            jump choose_sable
        "Liam Starkwood":
            jump choose_liam
        "Mr. Espinosa":
            jump choose_espinosa
        "Greta Pennywit":
            jump choose_greta

label choose_sable:
    p "I know it was you, care to explain yourself?"
    sable "Isn't it obvious? I'm clearly being framed!!"
    menu:
        " Who would frame you?":
            jump sable_defense
        "Do you really expect me to believe that?":
            jump sable_defense

label sable_defense:
    sable "Think about it, I called you, I gave you the information everybody else tried to hide away."
    sable "Obviously the maid is the culprit. She refused to comply with the investigation and she's always upset and disgruntled. "
    sable "She's been building a resentment towards this family since the day she started."
    sable "Are you sure I'm the one you want to arrest?"
    menu: 
        "Yes":
            jump sable_confession 
        "No":
            jump game_over

label sable_confession:
    sable "FINE!! Yes it was me, this family deserves nothing."
    sable "The old man was gonna pass soon and after all I'd done for him he was only going to leave me scraps."
    sable "HE DESERVED IT"
    p "You're going to jail *arrests Sable*"
    jump game_win


label choose_greta:
    e "I knew it!!"
    g "It was not me!!"
    p "You're going to jail!!"
    e "Yeah take her away!1"
    jump game_over


label choose_espinosa:
    e "You must be out of your mind!"
    p "You're going to jail."
    e "You made the mistake of a life time "
    jump game_over


label choose_liam:
    hide liam 
    show liam mad 
    l "Have you lost your mind?"
    p "You're going to jail."
    l "UNHAND ME"
    jump game_over


label choose_martha:
    m "WHAT?? But it wasnt me."
    p "You're going to jail."
    m "Why are you doing this??"
    jump game_over


label game_over:
    scene gameover_background
    "Later that night..."
    show sable killer
    sable "I'm truly sorry things had to go this way."
    sable "Maybe next time learn to mind your business."
    p "AHHHHHH"
    jump endscreen

label game_win:
    m "Thank you so much for serving justice for my husband and children."
    m "Idk what we'd do without you"
    "Sable was given a life sentence, you were rewarded generously and the family reconnected"
    jump winscreen


label endscreen:
    scene you_died
    with fade
    "GAME OVER"
    jump end

label winscreen:
    scene you_won
    with fade
    "YOU CAUGHT THE KILLER"
    # This ends the game.
label end:

    return
