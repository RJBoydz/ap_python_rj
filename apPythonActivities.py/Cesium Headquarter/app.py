def preference():
    print('What kind of movies do you like')
    movie=(input('Please enter a genre of movie'))
    if movie == 'action':
        print('Avengers', 'Mission impossible', 'Godzilla vs Kong')
        genre = ("Avengers"), ('Mission impossible'), ('Godzilla vs Kong')
        if genre == "Avengers":
            print('When Thors evil brother, Loki (Tom Hiddleston), gains access to the unlimited power of the energy cube called the Tesseract, Nick Fury (Samuel L. Jackson), director of S.H.I.E.L.D., initiates a superhero recruitment effort to defeat the unprecedented threat to Earth. Joining Furys "dream team" are Iron Man (Robert Downey Jr.), Captain America (Chris Evans), the Hulk (Mark Ruffalo), Thor (Chris Hemsworth), the Black Widow (Scarlett Johansson) and Hawkeye (Jeremy Renner).')
        if genre == 'Mission impossible':
            print('When U.S. government operative Ethan Hunt (Tom Cruise) and his mentor, Jim Phelps (Jon Voight), go on a covert assignment that takes a disastrous turn, Jim is killed, and Ethan becomes the prime murder suspect. Now a fugitive, Hunt recruits brilliant hacker Luther Stickell (Ving Rhames) and maverick pilot Franz Krieger (Jean Reno) to help him sneak into a heavily guarded CIA building to retrieve a confidential computer file that will prove his innocence.')
        if genre == 'Godzilla vs Kong':
            print('Kong and his protectors undertake a perilous journey to find his true home. Along for the ride is Jia, an orphaned girl who has a unique and powerful bond with the mighty beast. However, they soon find themselves in the path of an enraged Godzilla as he cuts a swath of destruction across the globe. The initial confrontation between the two titans -- instigated by unseen forces -- is only the beginning of the mystery that lies deep within the core of the planet')               
    elif movie == 'Science fiction':
        print('Star wars', 'star trek', 'Edge of Tomorrow')
        sci = ("Star wars"), ("Star Trek"), ("Edge of Tomorrow")
        if sci == 'Star wars':
            print('The Imperial Forces -- under orders from cruel Darth Vader (David Prowse) -- hold Princess Leia (Carrie Fisher) hostage, in their efforts to quell the rebellion against the Galactic Empire. Luke Skywalker (Mark Hamill) and Han Solo (Harrison Ford), captain of the Millennium Falcon, work together with the companionable droid duo R2-D2 (Kenny Baker) and C-3PO (Anthony Daniels) to rescue the beautiful princess, help the Rebel Alliance, and restore freedom and justice to the Galaxy.')
        if sci == ('Star Trek'):
            print('Aboard the USS Enterprise, the most-sophisticated starship ever built, a novice crew embarks on its maiden voyage. Their path takes them on a collision course with Nero (Eric Bana), a Romulan commander whose mission of vengeance threatens all mankind. If humanity would survive, a rebellious young officer named James T. Kirk (Chris Pine) and a coolly logical Vulcan named Spock (Zachary Quinto) must move beyond their rivalry and find a way to defeat Nero before it is too late.')
        if sci == ('Edge of Tomorrow'):
            print('When Earth falls under attack from invincible aliens, no military unit in the world is able to beat them. Maj. William Cage (Tom Cruise), an officer who has never seen combat, is assigned to a suicide mission. Killed within moments, Cage finds himself thrown into a time loop, in which he relives the same brutal fight -- and his death -- over and over again. However, Cages fighting skills improve with each encore, bringing him and a comrade (Emily Blunt) ever closer to defeating the aliens.')        
    elif movie == 'Western':
        print('Rango', 'Old Western', 'Outlaw John Black')
        west = ("Rango"), ('New of the World'), ("Outlaw John Black")
        if west == 'Rango':
            print('A chameleon (Johnny Depp) who has lived as a sheltered family pet finds himself in the grip of an identity crisis. Rango wonders how to stand out when it is his nature to blend in. When he accidentally winds up in a frontier town called Dirt, he takes the first step on a transformational journey as the town new sheriff. Though at first Rango only role-plays, a series of thrilling situations and outrageous encounters forces him to become a real hero.')
        if west == 'New of the World':
            print('Five years after the end of the Civil War, Capt. Jefferson Kyle Kidd crosses paths with a 10-year-old girl taken by the Kiowa people. Forced to return to her aunt and uncle, Kidd agrees to escort the child across the harsh and unforgiving plains of Texas. However, the long journey soon turns into a fight for survival as the traveling companions encounter danger at every turn -- both human and natural.')
        if west == 'Outlaw John Black':
            print('Cowboy Johnny Black vows to gun down Brett Clayton, the man responsible for the death of his father. He soon becomes a wanted outlaw while posing as a preacher in a small mining town that been taken over by a notorious land baron.')
    elif movie == 'Horror':
        print('Scream', 'Jason', 'Hallween')
        blood = ("Scream"), ("Jason"), ("Hallween")
        if blood == 'Scream':
            print('Wes Craven re-invented and revitalised the slasher-horror genre with this modern horror classic, which manages to be funny, clever and scary, as a fright-masked knife maniac stalks high-school students in middle-class suburbia. Craven is happy to provide both tension and self-parody as the body count mounts - but the victims arent always the ones youd expect.')
        if blood == 'Jason':
            print('Crystal Lake history of murder doesnt deter counselors from setting up a summer camp in the woodsy area. Superstitious locals warn against it, but the fresh-faced young people -- Jack (Kevin Bacon), Alice (Adrienne King), Bill (Harry Crosby), Marcie (Jeannine Taylor) and Ned (Mark Nelson) -- pay little heed to the old-timers. Then they find themselves stalked by a brutal killer. As theyre slashed, shot and stabbed, the counselors struggle to stay alive against a merciless opponent.')
        if blood == 'Hallween':
            print('On a cold Halloween night in 1963, six year old Michael Myers brutally murdered his 17-year-old sister, Judith. He was sentenced and locked away for 15 years. But on October 30, 1978, while being transferred for a court date, a 21-year-old Michael Myers steals a car and escapes Smith Grove. He returns to his quiet hometown of Haddonfield, Illinois, where he looks for his next victims.') 
    elif movie == 'Thriller':
        print('Sound of Freedom', 'Talk to me', 'Five nights at Freddy')
        fear = ("Sound of Freedom"), ("Talk to me"), ("Five Night at Freddy's")
        if fear == 'Sound of Freedom':
            print('After rescuing a boy from ruthless child traffickers, a federal agent learns the boy sister is still captive and decides to embark on a dangerous mission to save her. With time running out, he quits his job and journeys deep into the Colombian jungle, putting his life on the line to free her from a fate worse than death.')
        if fear == 'Talk to me':
            print('When a group of friends discover how to conjure spirits with an embalmed hand, they become hooked on the new thrill and high-stakes party game -- until one of them goes too far and unleashes terrifying supernatural forces.')
        if fear == 'Five nights at Freddy':
            print("A troubled security guard begins working at Freddy Fazbears Pizzeria. While spending his first night on the job, he realizes the late shift at Freddy's won't be so easy to make it through.")    
    elif movie == 'Comedy':
        print('Home alone' 'Strays', 'Good burger')
        fun = ("Home alone"), ("Strays"), ("Good burger")
        if fun == 'Home alone':
            print('When bratty 8-year-old Kevin McCallister (Macaulay Culkin) acts out the night before a family trip to Paris, his mother (Catherine O Hara makes him sleep in the attic. After the McCallisters mistakenly leave for the airport without Kevin, he awakens to an empty house and assumes his wish to have no family has come true. But his excitement sours when he realizes that two con men (Joe Pesci, Daniel Stern) plan to rob the McCallister residence, and that he alone must protect the family home.')
        if fun == 'Strays':
            print('Abandoned on the mean city streets by his lowlife owner, Doug, a naive but lovable dog named Reggie falls in with a fast-talking, foul-mouthed Boston Terrier and his gang of strays. Determined to seek revenge, Reggie and his new canine pals embark on an epic adventure to get him home and make Doug pay for his dirty deed.')
        if fun == 'Good burger':
            print('When Mondo Burger sets up across the street, sneaky Dexter and burger-obsessed Ed realise they need to fight to keep their fast food joint going. Their new secret sauce might be the answer, but not if Mondo can grab it.')
    elif movie == 'Romance':
            print('No hard feeling, past lives, Before we go')
    love = ("No hard feeling"), ("Past Lives"), ("Before we go")
    if love == ' No hard feeling':
            print('On the brink of losing her childhood home, a desperate woman agrees to date a wealthy couple introverted and awkward 19-year-old son. However, he proves to be more of a challenge than she expected, and time is running out before she loses it all.')
    if love == 'Past lives':
            print('Nora and Hae Sung, two deeply connected childhood friends, are wrest apart after Nora family emigrates from South Korea. Decades later, they are reunited for one fateful week as they confront destiny, love and the choices that make a life.')
    if love == 'Before we go':
            print('A chance encounter between two strangers (Chris Evans, Alice Eve) in Grand Central Terminal sparks a life-changing, nighttime sojourn through New York City.')
    elif movie == 'Drama':
        print('Fair play, Forgotten love, the burial')
        alot = ("Fair Play"), ("Forgotten love"), ("the Burial")
        if alot == 'Fair play':
            print('An unexpected promotion at a cutthroat hedge fund pushes a newly engaged couple relationship to the brink.')
        if alot == 'Forgotten love':
            print('A once-respected surgeon who lost his family and his memory gets a chance at redemption when he reconnects with someone from his forgotten past who can help him finds the answers he needs.')
        if alot == 'The burial':
            print('Willie E. Gary, an unconventional lawyer, helps Jeremiah Joseph O Keefe, a funeral home owner with financial troubles, save his family business from a corporate behemoth.')
        else:
            print('I do not understand your answer, please put in a genra of movies')
    
preference()

