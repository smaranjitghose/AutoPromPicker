# AutoPromPicker
Remember Prom Night? 🎶

One of the biggest issues ⚔ we faced was to make sure all the handsome boys🤵 were paired to all the gorgeous girls💃 in a fashion that takes care of everyone's priority 💛

"Nah! That's just a fairytale scenario", if this is your thought maybe python 🐍can do some magic do ensure that we can pair all of our mates in a manner they never break up 

Yes⚡, it can be done. Although we can't guarentee of getting those perfect pairs 💑snitched together always but everyone gets to happy.😊

As every other wizards🧙‍♂️ , python has its own conditions ❗for this spell:

- Everyone should be brutually honest when asked about ranking their partners in order of preferrence
- The number of boys and girls must be equal. We don't want anyone to be left out in the corner. 💔

# Some Theorical Background: 🔍

The given use case is an application of the popular [Stable Marriage Problem](https://en.wikipedia.org/wiki/Stable_marriage_problem) and is solved by the[Gayle-Shapely algorithm](https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm)

### Psuedo Code: 🤔
``` 
Initialize all m ∈ M and w ∈ W to free
    while ∃ free man m who still has a woman w to propose to do
        w := first woman on m's list to whom m has not yet proposed
        if w is free then
            (m, w) become engaged
        else some pair (m', w) already exists
            if w prefers m to m' then
                m' becomes free
                (m, w) become engaged 
            else
                (m', w) remain engaged
            end if
        end if
    repeat
   ```
### Explanation: 👨‍🏫

- Until there's any boy left unpaired, the remaining unpaired boys go and ask out the girls as per their turns

![Ask out](https://media.giphy.com/media/Vd8B2c0HvLOFw4xAV7/giphy.gif)

- Each unmatched boy asks out the girls in his order of preference

![preference](https://media.giphy.com/media/pRPJR8pCuV0ic/giphy.gif)

- For every girl he asks out, if the girl is single, then she accepts the proposal and they get paired

![yes](https://media.giphy.com/media/1tHzw9PZCB3gY/giphy.gif)

- If the girl is already paired with another boy, she chooses according to her order of preference either to reject the proposal or to dump her current partner and accept the proposal,getting repaired in the process

![rematch](https://media.giphy.com/media/l3q2PwxrzxW6JseU8/giphy.gif)
- If a boy is dumped, he has to again ask out a girl in the above process

# Usage:

Convinced..huh? 😉 and want this spell for yourself?

Here you go:

- clone or Download this repo ⏬
- Open the Terminal 🐱‍💻
- Move inside 👉 the repo 
```cd AutoPromPicker``` 
- Open ```autoprompick.py``` and change the names of the girls,boys and preferences as desired🧱 
- Now, the climax you have been waiting for!😎. Run the script using Terminal
  ```python autoprompick.py```
- Abracadabra ⚡

**I assume you have python installed on your system and set to path.**

# Further Work: 🏗
- Tune this script to take in the number of girls and boys from the terminal,their names and preference of each
- Create a GUI for this
- Deploy🚢 the above using Flask
- Create an end to end auto prom picker system, where the ```N``` boys and ```N``` girls register themselves,put up their profile,rate each other and our script takes those values and gives them their best pair(s) as per precedence of ask out 

# License 📜

[MIT License](https://github.com/smaranjitghose/AutoPromPicker/blob/master/LICENSE)

# **Crafted with ❤ by Smaranjit Ghose**
