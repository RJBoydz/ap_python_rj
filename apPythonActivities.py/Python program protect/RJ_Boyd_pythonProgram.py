def preference():
        genre = ["Avengers", "Mission impossible", "Godzilla vs Kong"]
        sci = ["Star wars", "Star trek", "Edge of Tomorrow"]
        west = ["Rango", 'New of the World', "Outlaw John Black"]
        blood = ["Scream", "Jason", "Hallween"]
        fear = ["Sound of Freedom", "Talk to me", "Five Night at Freddy's"]
        fun = ["Home alone", "Strays", "Good burger"]
        love = ["No hard feeling", "Past lives", "Before we go"]
        alot = ["Fair Play", "Forgotten love", "the Burial"]
    
        print("What kind of movies do you like, the generes you can pick: action, science fiction, western, horror, thriller, comedy, romance, drama...")
    
        movie=(input('Please enter a genre of movie? '))
        
    
        if movie == 'action':
                print('Avengers, Mission impossible, Godzilla vs Kong')
        
                actionSelection= input ('Which move would you like to see? ')
     
                if genre[0] == actionSelection:
                    print('When Thors evil brother, Loki (Tom Hiddleston), gains access to the unlimited power of the energy cube called the Tesseract, Nick Fury (Samuel L. Jackson), director of S.H.I.E.L.D., initiates a superhero recruitment effort to defeat the unprecedented threat to Earth. Joining Furys "dream team" are Iron Man (Robert Downey Jr.), Captain America (Chris Evans), the Hulk (Mark Ruffalo), Thor (Chris Hemsworth), the Black Widow (Scarlett Johansson) and Hawkeye (Jeremy Renner).')
                if genre[1] == actionSelection:
                    print('When U.S. government operative Ethan Hunt (Tom Cruise) and his mentor, Jim Phelps (Jon Voight), go on a covert assignment that takes a disastrous turn, Jim is killed, and Ethan becomes the prime murder suspect. Now a fugitive, Hunt recruits brilliant hacker Luther Stickell (Ving Rhames) and maverick pilot Franz Krieger (Jean Reno) to help him sneak into a heavily guarded CIA building to retrieve a confidential computer file that will prove his innocence.')
                if genre[2] == actionSelection:
                        print('Kong and his protectors undertake a perilous journey to find his true home. Along for the ride is Jia, an orphaned girl who has a unique and powerful bond with the mighty beast. However, they soon find themselves in the path of an enraged Godzilla as he cuts a swath of destruction across the globe. The initial confrontation between the two titans -- instigated by unseen forces -- is only the beginning of the mystery that lies deep within the core of the planet')               
                else:
                        print('sorry, cant find that movie.')
        
        elif movie == 'science fiction':
                print('Star wars, Star trek, Edge of Tomorrow')

                sciencefiction= input('Which movie would you like to see? ')    
                if sci[0] == sciencefiction:
                    print('The Imperial Forces -- under orders from cruel Darth Vader (David Prowse) -- hold Princess Leia (Carrie Fisher) hostage, in their efforts to quell the rebellion against the Galactic Empire. Luke Skywalker (Mark Hamill) and Han Solo (Harrison Ford), captain of the Millennium Falcon, work together with the companionable droid duo R2-D2 (Kenny Baker) and C-3PO (Anthony Daniels) to rescue the beautiful princess, help the Rebel Alliance, and restore freedom and justice to the Galaxy.')
                if sci[1] == sciencefiction:
                    print('Aboard the USS Enterprise, the most-sophisticated starship ever built, a novice crew embarks on its maiden voyage. Their path takes them on a collision course with Nero (Eric Bana), a Romulan commander whose mission of vengeance threatens all mankind. If humanity would survive, a rebellious young officer named James T. Kirk (Chris Pine) and a coolly logical Vulcan named Spock (Zachary Quinto) must move beyond their rivalry and find a way to defeat Nero before it is too late.')
                if sci[2] == sciencefiction:
                    print('When Earth falls under attack from invincible aliens, no military unit in the world is able to beat them. Maj. William Cage (Tom Cruise), an officer who has never seen combat, is assigned to a suicide mission. Killed within moments, Cage finds himself thrown into a time loop, in which he relives the same brutal fight -- and his death -- over and over again. However, Cages fighting skills improve with each encore, bringing him and a comrade (Emily Blunt) ever closer to defeating the aliens.')     
                else:
                        print('sorry, cant find that movie.')

        elif movie == 'western':
                print('Rango', 'Old Western', 'Outlaw John Black')

                westernselection= input('Which movie would you like to see? ')
                if west[0] == westernselection:
                    print('A chameleon (Johnny Depp) who has lived as a sheltered family pet finds himself in the grip of an identity crisis. Rango wonders how to stand out when it is his nature to blend in. When he accidentally winds up in a frontier town called Dirt, he takes the first step on a transformational journey as the town new sheriff. Though at first Rango only role-plays, a series of thrilling situations and outrageous encounters forces him to become a real hero.')
                if west[1] == westernselection:
                    print('Five years after the end of the Civil War, Capt. Jefferson Kyle Kidd crosses paths with a 10-year-old girl taken by the Kiowa people. Forced to return to her aunt and uncle, Kidd agrees to escort the child across the harsh and unforgiving plains of Texas. However, the long journey soon turns into a fight for survival as the traveling companions encounter danger at every turn -- both human and natural.')
                if west[2] == westernselection:
                    print('Cowboy Johnny Black vows to gun down Brett Clayton, the man responsible for the death of his father. He soon becomes a wanted outlaw while posing as a preacher in a small mining town that been taken over by a notorious land baron.')
                else:
                        print('sorry, cant find that movie.')   

        elif movie == 'horror':
                print('Scream, Jason, Hallween')

                horrorselection= input('Which movie would you like to see? ')

                if blood[0] == horrorselection:
                    print('Wes Craven re-invented and revitalised the slasher-horror genre with this modern horror classic, which manages to be funny, clever and scary, as a fright-masked knife maniac stalks high-school students in middle-class suburbia. Craven is happy to provide both tension and self-parody as the body count mounts - but the victims arent always the ones youd expect.')
                if blood[1] == horrorselection:
                    print('Crystal Lake history of murder doesnt deter counselors from setting up a summer camp in the woodsy area. Superstitious locals warn against it, but the fresh-faced young people -- Jack (Kevin Bacon), Alice (Adrienne King), Bill (Harry Crosby), Marcie (Jeannine Taylor) and Ned (Mark Nelson) -- pay little heed to the old-timers. Then they find themselves stalked by a brutal killer. As theyre slashed, shot and stabbed, the counselors struggle to stay alive against a merciless opponent.')
                if blood[2] == horrorselection:
                    print('On a cold Halloween night in 1963, six year old Michael Myers brutally murdered his 17-year-old sister, Judith. He was sentenced and locked away for 15 years. But on October 30, 1978, while being transferred for a court date, a 21-year-old Michael Myers steals a car and escapes Smith Grove. He returns to his quiet hometown of Haddonfield, Illinois, where he looks for his next victims.') 
                else:
                        print('Sorry, cant find that movie.')                   

        elif movie == 'thriller':
                print('Sound of Freedom, Talk to me, Five nights at Freddy')
                thrillerelection= input('Which movie would you like to see? ')
                if fear[0] == thrillerelection:
                    print('After rescuing a boy from ruthless child traffickers, a federal agent learns the boy sister is still captive and decides to embark on a dangerous mission to save her. With time running out, he quits his job and journeys deep into the Colombian jungle, putting his life on the line to free her from a fate worse than death.')
                if fear[1] == thrillerelection:
                    print('When a group of friends discover how to conjure spirits with an embalmed hand, they become hooked on the new thrill and high-stakes party game -- until one of them goes too far and unleashes terrifying supernatural forces.')
                if fear[2] == thrillerelection:
                    print("A troubled security guard begins working at Freddy Fazbears Pizzeria. While spending his first night on the job, he realizes the late shift at Freddy's won't be so easy to make it through.")    
                else:
                        print("Sorry,can't find that movie") 

        elif movie == 'comedy':
                print('Home alone' 'Strays', 'Good burger')
                comedyselection = input('Which movie would you like to see? ') 
                if fun[0] == comedyselection:
                    print('When bratty 8-year-old Kevin McCallister (Macaulay Culkin) acts out the night before a family trip to Paris, his mother (Catherine O Hara makes him sleep in the attic. After the McCallisters mistakenly leave for the airport without Kevin, he awakens to an empty house and assumes his wish to have no family has come true. But his excitement sours when he realizes that two con men (Joe Pesci, Daniel Stern) plan to rob the McCallister residence, and that he alone must protect the family home.')
                if fun[1] == comedyselection:
                    print('Abandoned on the mean city streets by his lowlife owner, Doug, a naive but lovable dog named Reggie falls in with a fast-talking, foul-mouthed Boston Terrier and his gang of strays. Determined to seek revenge, Reggie and his new canine pals embark on an epic adventure to get him home and make Doug pay for his dirty deed.')
                if fun[2] == comedyselection:
                    print('When Mondo Burger sets up across the street, sneaky Dexter and burger-obsessed Ed realise they need to fight to keep their fast food joint going. Their new secret sauce might be the answer, but not if Mondo can grab it.')
                else:
                        print("Sorry can't find that movie") 

        elif movie == 'romance':
                print('No hard feeling, past lives, Before we go')
                romanceseclection= input('Which movie would you like to see? ')
                if love[0] == romanceseclection:
                    print('On the brink of losing her childhood home, a desperate woman agrees to date a wealthy couple introverted and awkward 19-year-old son. However, he proves to be more of a challenge than she expected, and time is running out before she loses it all.')
                if love[1] == romanceseclection:
                    print('Nora and Hae Sung, two deeply connected childhood friends, are wrest apart after Nora family emigrates from South Korea. Decades later, they are reunited for one fateful week as they confront destiny, love and the choices that make a life.')
                if love[2] == romanceseclection:
                    print('A chance encounter between two strangers (Chris Evans, Alice Eve) in Grand Central Terminal sparks a life-changing, nighttime sojourn through New York City.')
                else:
                        print("Sorry can't find that movie") 

        elif movie == 'drama':
                print('Fair play, Forgotten love, the burial')
                dramaselection= input('Which movie would you like to see? ')             
                if alot[0] == dramaselection:
                    print('An unexpected promotion at a cutthroat hedge fund pushes a newly engaged couple relationship to the brink.')
                if alot[1] == dramaselection:
                    print('A once-respected surgeon who lost his family and his memory gets a chance at redemption when he reconnects with someone from his forgotten past who can help him finds the answers he needs.')
                if alot[2] == dramaselection:
                    print('Willie E. Gary, an unconventional lawyer, helps Jeremiah Joseph O Keefe, a funeral home owner with financial troubles, save his family business from a corporate behemoth.')
                else:
                        print("Sorry can't find that movie")                        
  
preference()