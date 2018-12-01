def antrope_input():
   ant_error = True 
   while ant_error is True:
       #Makes sure input is a number.
       try:
            rope_length = float(input("type rope length: "))
            ant_speed = float(input("type ant speed: "))
            rope_increment = float(input("type rope increment: "))
            view_process = bool(input("list steps? (not recommended) y/n: ") == 'y')
            view_markers = bool(input("list milestones? y/n: ") == 'y')
            ant_error = False              
       except:
            print("use integer numbers")
   #setup variables and execute the core function
   ant_list = [rope_length,ant_speed,rope_increment,view_process,view_markers]
   antrope_paradox(ant_list)      

def antrope_paradox(lsta):
    rope_length = lsta[0]
    ant_speed = lsta[1]
    rope_increment = lsta[2]
    view_process = lsta[3]
    view_markers = lsta[4]
    ant_total = 0.0
    runs = 0
    mi = 0
    while ant_total < rope_length and runs < 500001:
        #count ant steps and add basic distance
        runs += 1
        ant_total = ant_total + ant_speed
        #reevaluate ants relative position on the rope
        rope_total = rope_length + rope_increment      
        multiplier = rope_increment/rope_total
        ant_total = ant_total + ant_total * multiplier
        #increment rope for the next run to compare
        rope_length = rope_length + rope_increment
        if view_process is True: 
            print(str(runs)+".ant:  "+str(ant_total))
            print(str(runs)+".rope: "+str(rope_length))
        
        if view_markers is True:
            if mi == 0 and ant_total >= rope_length/4:
               mi = 1 
               mil1 ="Milestone: Ant at 25% in step {0} at rope length {1}".format(runs,rope_length)
            elif mi == 1 and ant_total >= rope_length/2:
               mi = 2
               mil2 ="Milestone: Ant at 50% in step {0} at rope length {1}".format(runs,rope_length)
            elif mi == 2 and ant_total >= rope_length*3/4:
               mi = 3
               mil3 ="Milestone: Ant at 75% in step {0} at rope length {1}".format(runs,rope_length)
                                                                                                 
    if runs <= 500000:
        print(mil1)
        print(mil2)
        print(mil3)
        print("steps taken: "+str(runs))
        print("final rope length: "+str(rope_length))
    else:
        print("warning: Calculating this may take long time.")
        print("Modify the code at your own risk")

antrope_input()
