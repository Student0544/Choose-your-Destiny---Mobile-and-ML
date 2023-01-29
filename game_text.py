from cohere.classify import Example
character = {"Sovereign": 0, "Immoral": 0, "Careful": 0, "Courageous": 0, "Adventurous": 0, "Strong": 0, "Rash": 0}
inventory = []

still_here = ["What are you still doing here? The game is over!", "Dude you ain't gonna get anything new...", "Just to let you know, the game is over."
            "Okay okay, I know the game is awesome, but you can't get too attached. But...", "Ey man, you reached the ending already. Don't like your outcome?",
              "The game is over, but if you want to play again...", "You'll get the same text over and over if you keep writing this.",
              "Look, I promise there are many other cool outcomes to this story! To see them...", "Hey hey hey, look at the instructions below:",
              "The writer of this game worked really hard for this! You may want to see the other possible endings.",
              "Okay, you probably won't see anything new now..."]

# not_get = ["What you just wrote, makes absolutely no sense at all... Think again! ", "Eyo... can you repeat what you just wrote, but with more sense? "
#            "I don't quite understand, could you clarify what you mean?", "Okay this story ain't gonna have this happen! Write your actual decision! ",
#            "Hmmm, I, as the narrator, decide that did not happen. Now change your answer! ", "You and I both know that did not happen... Try again! ",
#            "Okay I did not think of that... But yeah we are gonna need an answer that makes more sense... ",
#            "That one almost made me laugh! But come on, an answer that makes sense please! ", "So... we can't let this story get too wild... Try to think of a different answer! ",
#            "That clearly has absolutely no way to happen! Think again! ", ":|, maybe an answer related to the story... "]

content = """a0:
It’s the middle of the night. You finished your training and can finally make it out of Ivory City. The moon lights the night for your escape. You grab your satchel and look around the family pawn shop for items to take. Something that is easy to carry and useful for your indefinite adventure. There are some COINS on the table, and an OIL PAINTING on the wall. What do you take?


a0:1
You sweep the silver and gold bullions into your bag, but drop a few on the floor. You hear rustling upstairs from your parents.


a0:2
You walk to the kitchen and pull the oil painting from the wall with a clang and stuff it into your bag. You did physical strength training for a reason. You hear your parents’ footsteps upstairs.


a0:3
Let’s not be greedy. Your stealing would’ve certainly woken up your family.


a1:
It’s time to go. If your parents catch you they will pawn you off to the King! You hurry out the door and run through the garden leading to the gates of the city.   There is a CLIMBABLE wall keeping you in but you might be able to BREAK THROUGH with just your body weight. What will you do?


a1:1
You bust through the wall with CRASH and emerge from the rubble.


a2:
You caught the attention of the archers atop the watchtowers. They aim their quiver at you. There is a stretch of land before a FOREST ahead and a patch of BUSHES leading to a river where you can hide.  What will you do?


a2:1 fridge
You make a break for the forest and you hear the arrow flying behind you. It pierces through your satchel, breaking the strap and hits the painting. The bag and supplies tumble to the ground, but with the alleviated load, you sprint into the forest.


a2:1 coins
You make a break for the forest and you hear the arrow flying behind you. You’re running as fast as you can, but with the weight of the bag, you are pierced through the heart and die instantly.


a2:1 nothing
You make a break for the forest and you hear the arrow flying behind you. You are just fast enough to hear the arrows hit the floor behind you and you make it to the forest.


a2:2
You scramble into the bushes. Arrows fall around you as you shuffle your way to the river. You roll into the river and swim in the direction of the forest. In your panic, you drown in the river.


a1:2
You find your footing between the imperfect tiles and make your way to the top of the tower.


b2
As you stand up, you notice watchtowers. You could probably FIGHT them off or JUMP off on the other side.  What will you do?


b2:1
You tumble into the watchtower and throw the archers over the wall. You load their bows and aim at the archers in the other towers.


b3:
Before you SHOOT, one of them pleads to be SPARED. He says the city doctor’s visits are too expensive now that he has a child. What will you do?


b3:1
You already threw two people over the wall, what is two more? You mercifully aim for the heart. You grab the bow and quivers and climb down the wall and head to the forest.


b3:2
You pick up a piece of rubble and throw it at their heads, gently knocking them out. We can’t be too trusting after all You grab the bow and quivers and climb down the wall and head to the forest.


b2:2
You decide to climb down the wall on the other side. In your panic, your hands slip and you fall to your DEATH.


a4
The forest may be mysterious, but it is the shortest path between the Ivory and Ink Cities. You’ve been walking for almost a day, and begin to get hungry.  You see some pale mushrooms and hear rustling in the bushes. An edible MUSHROOM or a CRITTER could sustain you for a few extra days. What will you do?


a6:1
You walk towards the noise and uncover the bushes to a rabbit trapped in some bramble.


a7:
What will you do with the rabbit:


A7:1 arrow
You take the arrow from your quiver and stab the rabbit. It dies immediately. You feast on its flesh.


A7:1
You reach gently for the feeble critter and [discreetly] kill it. You feast on its flesh.


a7:2
You decide against eating the rabbit. It probably won’t taste good raw anyways. You turn around to see some apples on the floor that had probably baited the rabbit initially. These should sustain you for a while longer.


a7:3
You loosen the bramble with your hands and the rabbit springs away. It runs towards some apples you hadn’t noticed. You pick up the apples.


A6:2: yes careful
Upon closer inspection, you see there are red, blue, and green mushrooms in this area. You learned about poisonous plants in your training and you remember the rhyme they taught you: ‘yucky red is bad for head, stinky blue will revive you, fragrant green is just like beans.’


A6:2: no careful
Upon closer inspection, you see there are red, blue, and green mushrooms in this area. You learned about poisonous plants in your training, but paying attention during lectures is for nerds.


b7:
Which color mushroom will you pick (or will you leave)?


b7:1
You snap the red mushrooms off the bark and toss them into your mouth. They are bitter and gooey but you hold your nose and swallow it reluctantly. You are hit with an immediate headache and pass out. Forever.


b7:2
You pull the blue off the logs, and a stench drifts from its hyphae. Holding your breath, you quickly chew and swallow it. You are hit with fatigue and immediately pass out. But you get up again, feeling more alive than ever!


B7:3: strong
You scrape off the small green mushrooms from the branches and toss them into your mouth. They taste like flowers and beans? You are hit with the sudden realization that you are deathly allergic to beans and pass out immediately. Your body somehow toughs it out, perhaps with the new muscles you have built and you wake up. Feeling somewhat drowsy, but nourished.


B7:3: not strong
You scrape off the small green mushrooms from the branches and toss them into your mouth. They taste like flowers and beans? You are hit with the sudden realization that you are deathly allergic to beans and pass out immediately. One of science’s greatest mysteries is how mushrooms that taste like beans could trigger an allergic reaction to beans. Curse these allergies.


b7:4
You decide against trying these suspicious mushrooms. You wander for a few more hours in the forest and reach a glade. You feel your hunger getting to you and decide to take a nap. For unknown reasons, you never woke up.


a9:
You wander for a few more hours in the forest and reach a glade. You see an opening beyond the glade with what looks like a city of black buildings in the distance! You run towards it but are knocked off your feet by a tremendous blow. Rubbing your head, you look up to see a mossy rock giant with some type of cage in its torso. Inside is a small man dressed in dark royal clothes.  What do you do about the monster?


a9:1:strong
You pick up some stones and throw them at the giant to no success. You walk over to a log and smash it against the leg of the monster. As it falls, you grab another log and smash it against its head. Surely it’s been knocked out.


a9:1:smart
You decide to fight…with your wits. You try talking to the giant. He keeps throwing objects at you and you deftly dodge them. You keep talking and talking. The giant covers its ears and goes to sleep because of how boring you are.

a9:2
You make a bolt for the exit but your head is still spinning. The giant throws a large rock and crushes you immediately. Shouldn’t have been such a coward.


a10:
With the monster down, you go and talk to the man in the cage. He is the advisor for the Ink King and for rescuing him, he is giving you an exclusive chance to dine with the Ink King! Although you hate the Ivory City, your entire culture has revolved around the downfall of the Ink City, in particular, the Ink King. What a story it would be to have his downfall be at the hands of a common pawner!  Do you ACCEPT his invitation?

a10:1:knight
You humbly accept the invitation to dine with the King. Time to wash up and execute your plan! For good measure, you go into the city and purchase some armor and a horse. You need to feel like a hero!


a10:1:other
You humbly accept the invitation to dine with the King. Time to wash up and execute your plan!

a10:2
You politely decline the offer and begin to walk towards the city. Right when you step foot outside the forest you are shot by an arrow from the Ink archers and behind from the advisor.


A11: (Queen)
You enter the dining hall. The King orders an extravagant meal and tells you stories from his childhood. You laugh at all his quips and make lots of eye contact. You know why you’re here.  The King invites you over and proposes. Do you ACCEPT?


A11:1: moral
You are happily married to this foolish King. Fortunately, he is suspiciously poisoned a month after and nobody suspects his ‘heartbroken’ widow. Your life of dictatorship can finally begin.


A11:1: immoral
You are happily married to this foolish King. Fortunately, he is suspiciously poisoned a month after and the bishops gather to judge your history of questionable acts. You are sentenced to DEATH.


a11:2
In a fit of indignance, the King sentences you to DEATH. God bless the Queen.

B11: (knight)
You enter the dining hall. The King some suspicious looking soup, and does not touch it for the duration of the meal. He calls you names for not trying it. Do you DRINK the soup?


B11:1: no courage
You take a small sip. As the night continues, you feel uneasy. On your way back to your camp, you fall over and never wake up.


B11:1: yes courage
You chug the entire bowl and smash the bowl on the table. Specks of ceramic pieces fly out and land in the King’s food, but he doesn't notice. Throughout the night, you feel uneasy but you have no doubt your body can take it. A few weeks pass and the King was found dead due to internal bleeding, caused by cuts and tears in his intestines. Nobody can figure out how it happened, but you know that your job here is done. You ride off with your horse into the sunset with no thoughts. Perhaps you will go save a princess or something.


b11:2
The King laughs at your face and announces your cowardness to the entire kingdom.


b12:
For the rest of the night, you catch people snickering and gossiping about your weakness and disgrace. After a few weeks of this, you are so ashamed that you go to the stable and consider RELEASING your horse, your last connection to knightship. You are no knight. You free your horse and live the rest of your meaningless life as a pawn shop owner in the Ink City.



b12:1
You are no knight. You free your horse and live the rest of your meaningless life as a pawn shop owner in the Ink City.


b12:2
No. You ride off with your horse into the sunset, formulating plans to take down the man that defamed you. As you’re about to exit the city you hear booing at the gates. Your horse flinches and you fall off, dying immediately.


C11: (Rook)
You enter the dining hall. The King CHALLENGES you to a drinking contest, boasting about his hefty physique. Do you accept?


C11:1 no strength
The King laughs, calling the servant for 10 barrels of beer. Without even finishing the first barrel, you start feeling nauseous.


c12:
The King chuckles to himself and taunts you. Will you CONTINUE drinking?”


c12:1
You lift your head for another swing and immediately vomit on the King. Enraged but amused, he does not execute you, but sentences you to prison for life, where you spend the rest of your weak and meaningless days.


c12:2
You get up to leave, with the King and his servants laughing at you. On your way back, you stumble towards the river, hoping to get a drink, but you fall in and drown


c11:1 strong
You drink and drink deep into the night, feeling completely sober. Have you lost your ability to feel drunk? As you contemplate this, you look over at the King who has passed out. Between his dense physique and head planted face-down on the table, he doesn’t seem to have much life left. The kingdom will certainly frame you if you are here at his death, so you see yourself out. For the next few weeks, you build yourself a parapet in the Ink Forest and spend the rest of your days with a murder of pet rooks.


C11:2 strong
You politely decline and rise to leave. Right when you reach the door, you feel a barrel hit your head as the King throws it at you in a fit of rage. It cracks and spills on the floor, but you’re unfazed, unstoppable. For the next few weeks, you build yourself a parapet in the Ink Forest and spend the rest of your days with a murder of pet rooks.


C11:2 weak
You politely decline and rise to leave. Right when you reach the door, you feel a barrel hit your head as the King throws it at you in a fit of rage. You feel your head split open and you die immediately.

"""

fullText = content.splitlines()
skipline = True
allLines =[]

for line in fullText:
  if line=="":
      continue

  if skipline:
      skipline = False;
      continue;

  allLines.append(line)
  skipline = True

def determinePath(d):
  queenValue = d["Sovereign"] + d["Careful"] + d["Rash"]
  knightValue = d["Adventurous"] + d["Careful"] + d["Courageous"]
  rookValue = d["Adventurous"] + d["Strong"] + d["Rash"]
  values = [queenValue, knightValue, rookValue]

  return ["queen", "knight", "rook"][values.index(max(values))]

c12 = (allLines[54],
      {1:(allLines[55], None, [], []),
       2:(allLines[56], 1, [], [])},
      [Example("Continue.", "1"), Example("Keep drinking.", "1"), Example("Yes.", "1"), Example("Stop.", "2"), Example("No.", "2"), Example("Do not stop.", "1"), Example("abcdefghijklmnopqrstuvwxyz.", "2"), Example(".", "2"), Example("Accept.", "1")])

c11 = (allLines[52],
      {1:{True:(allLines[53], c12, [], []), False:(allLines[57], None, [], [])}[character["Strong"] < 3],
      2:{True:(allLines[58], None, [], []), False:(allLines[59], 1, [], [])}[character["Strong"] > 3]},
       [Example("Accept.", "1"), Example("Do not accept.", "1"), Example("Decline.", "2"), Example("I do not decline.", "1"), Example("Yes.", "1"), Example("No","2"), Example("abcdefghijklmnopqrstuvwxyz.", "2"), Example(".", "2"), Example("I accept the drinking challenge.", "1"), Example("Drink.", "1"), Example("I drink with the King.", "1"), Example("I do not drink.", "2")])

b11 = (allLines[45],
      {1:{True:(allLines[46], 1, [], []), False:(allLines[47], None, [], [])}[character["Courageous"] < 3],
      2:(allLines[49], None, [], [])},
      [Example("Yes.", "1"), Example("No.", "2"), Example("I try it.", "1"), Example("I do not try it.", "2"), Example("qwertyuiopasdfghjklzxcvbnm.", "2"), Example("Leave.", "2"), Example("I do not drink the soup", "2"), Example("I drink the soup.", "1"), Example(".", "2"), Example("Ok.", "1"), Example("I eat the soup.", "1"), Example("I do not eat the soup.", "2")])

a11 = (allLines[41],
      {1:{True:(allLines[42], None, [], []), False:(allLines[43], 1, [], [])}[character["Immoral"] > 3],
      2:(allLines[44], 1, [], [])},
       [Example("Yes.", "1"), Example("No.", "2"), Example("qwertyuiopasdfghjklzxcvbnm.", "2"), Example(".", "2"), Example("Ok.", "1",), Example("Of course.", "1",), Example("I accept.", "1",), Example("I do not accept.", "2"), Example("I get married", "1",), Example("I do not get married.", "2"), Example("Nope.", "2")])

a10 = (allLines[37],
      {1: {"knight":(allLines[38], b11, ["Sovereign", "Adventurous"], []), "queen":(allLines[39], a11, ["Sovereign", "Adventurous"], []), "rook":(allLines[39], c11, ["Sovereign", "Adventurous"], [])}[determinePath(character)],
      2:(allLines[40], 1, [], [])},
       [Example("Yes.", "1"), Example("No.", "2"), Example("qwertyuiopasdfghjklzxcvbnm.", "2"), Example(".", "2"), Example("Ok.", "1"), Example("Of course.", "1"), Example("I accept.", "1"), Example("I do not accept.", "2"), Example("Nope.", "2"), Example("I want to eat dinner.", "1"), Example("I do not want to eat dinner.", "2")])

a9 = (allLines[33],
     {1:{True:(allLines[34], a10, ["Adventurous", "Courageous", "Strong", "Rash"], []), False: (allLines[35], a10, ["Adventurous", "Courageous", "Strong", "Rash"], [])}[character["Strong"] > character["Careful"]],
      2:(allLines[36], 1, [], [])},
      [Example("qwertyuiopasdfghjklzxcvbnm.", "2"), Example(".", "2"), Example("Fight.", "1"), Example("Run.", "2"), Example("I do not fight.", "2"), Example("I do not run.", "1"), Example("I run away.", "2"), Example("Flee.", "2"), Example("Battle.", "1"), Example("Throw rocks.", "1"), Example("I punch the giant.", "1"), Example("I hit the giant.", "1")]
     )

b7 = (allLines[27],
     {1:(allLines[28], 1, [], []),
     2:(allLines[29], a9, [], []),
     3:{True:(allLines[30], a9, [], []), False:(allLines[31], 1, [], [])}[character["Strong"]>2],
     4:(allLines[32], 1, [], [])},
     [Example("qwertyuiopasdfghjklzxcvbnm.", "4"), Example(".", "4"), Example("Red.", "1"), Example("Blue.", "2"), Example("Green.", "3"), Example("I leave.", "4"), Example("Pass.", "4"), Example("I do not eat the red mushroom.", "4"), Example("I do not eat the blue mushroom.", "4"), Example("I do not eat the green mushroom.", "4"), Example("I do not eat them.", "4"), Example("Red mush.", "1"), Example("Blue mush.", "2"), Example("Green mush.", "3"), Example("I eat the red mushroom.", "1"), Example("I eat the blue mushroom.", "2"), Example("I eat the green mushroom.", "3"), Example("No.", "4")])

a7 = (allLines[20],
     {1:{True: (allLines[21], a9, ["Immoral", "Sovereign", "Strong"], []), False: (allLines[22], a9, ["Immoral", "Sovereign", "Strong"], [])}["arrow" in inventory],
      2:(allLines[24], a9, ["Careful"], [], []),
      3:(allLines[23], a9, ["Sovereign"], [], [])},
     [Example("I spare the rabbit.", "2"), Example("I kill the rabbit.", "1"), Example("I free the rabbits.", "3"), Example("I leave the rabbit.", "2"), Example("I eat the rabbit.", "1"), Example("I do not spare the rabbit.", "1"), Example("I do not kill the rabbit.", "3"), Example("I do not free the rabbit.", "1"), Example("I do not eat the rabbit.", "3"), Example("kill murder eat grab catch.", "1"), Example("free liberate let go.", "3"), Example("let go look leave.", "2")])

a5 = (allLines[18],
     {1:(allLines[19], a7, ["Adventurous"], []),
     2:{True:(allLines[25], b7, ["Rash"], []), False: (allLines[26], b7, ["Rash"], [])}[character["Careful"] > 3]},
     [Example("qwertyuiopasdfghjklzxcvbnm.", "2"), Example(".", "2"), Example("Mushrooms.", "2"), Example("Go to mushrooms.", "2"), Example("Green mushroom.", "2"), Example("I do not go to the mushrooms.", "1"), Example("I go towards the sound.", "1"), Example("Go to the noise.", "1"), Example("I do not go to the noise.", "2"), Example("Rustling.", "1"), Example("Critter.", "1"), Example("I want the animal.", "1"), Example("Meat.", "1"), Example("I do not want the animal.", "2")])

b3 = (allLines[14],
     {1:(allLines[15], a5, ["Immoral", "Sovereign"], ["arrow"]),
     2:(allLines[16], a5, [], [])},
     [Example("spare.", "1"), Example("shoot.", "2"), Example("I do not spare him.", "2"), Example("I do not shoot him.", "1"), Example("I leave him alive.", "1"), Example("I kill him.", "2"), Example("I do not leave him alive.", "2"), Example("I do not kill him.", "1"), Example("I let him live.", "1"), Example("I do not let him live", "2"), Example("I murder him.", "2"), Example("I do not murder him.", "1")])

b2 = (allLines[12],
      {1:(allLines[13], b3, ["Courageous", "Rash", "Adventurous"], []),
      2:(allLines[17], 1, [], [])},
     [Example("climb down.", "2"), Example("fight.", "1"), Example("I fight.", "1"), Example("I do not fight.", "2"), Example("I climb down.", "2"), Example("I do not climb down.", "1"), Example("I go down.", "2"), Example("I do not go down.", "1"), Example("I battle.", "1"), Example("I attack.", "1"), Example("I do not attack.", "2"), Example("I do not battle.", "2"), Example("climb jump down jump off.", "2"), Example("battle fight attack.", "1")])

a2 = (allLines[6],
      {1:{True: (allLines[7], a5, ["Courageous", "Adventurous"], []), False: (allLines[9], a5, ["Courageous", "Adventurous"], [])}["painting" in inventory],
       2:(allLines[10], 1, [], [])},
       [Example("I run into the forest.", "1"), Example("I go into the forest.", "1"), Example("I enter the forest.", "1"), Example("I do not run into the forest.", "2"), Example("I do not go into the forest.", "2"), Example("I do not enter the forest.", "2"), Example("I hide in the bushes.", "2"), Example("I go into the bushes.", "2"), Example("I do not hide in the bushes.", "1"), Example("I do not go into the bushes.", "1"), Example("bushes.", "2"), Example("forest.", "1")])

a1 = (allLines[4],
     {1:(allLines[5], a2, ["Rash", "Strong"], []),
      2:(allLines[11], b2, ["Careful", "Courageous"], [])},
      [Example("I climb the wall.", "2"), Example("I get over the wall.", "2"), Example("I break through the wall.", "1"), Example("I destroy the wall.", "1"), Example("I do not climb the wall.", "1"), Example("I do not get over the wall", "1"), Example("I do not break through the wall", "2"), Example("I do not destroy the wall", "2"), Example(".", "2"), Example("abcdefghijklmnopqrstuvwxyz.", "2"), Example("climb.", "2"), Example("break.", "2"), Example("break through.", "1"), Example("destroy.", "1"), Example("I go over the wall.", "2"), Example("I do not go over the wall.", "1")]
      )

a0 = (allLines[0],
      {1: (allLines[1], a1, ["Careful", "Immoral"], ["coins"]),

       2: (allLines[2], a1, ["Careful", "Rash", "Strong"], ["painting"]),

       3: (allLines[3], a1, [], [])
       },
      [Example("I take the coin.", "1"), Example("I grab the coin.", "1"), Example("I take the painting.", "2"), Example("I grab the painting.", "2"), Example("I do not take the coin.", "3"), Example("I do not grab the coin.", "3"), Example("I do not take the painting.", "3"), Example("I do not grab the painting.", "3"), Example(".", "3"), Example("abcdefghijklmnopqrstuvwxyz.", "3"), Example("coin.", "1"), Example("painting.", "2"), Example("nothing.", "3")])