import tkinter
import tkinter.messagebox

class punnetGUI:
    def __init__(self):
        self.mainWindow = tkinter.Tk()
        self.mainWindow.configure(bg = "mediumSpringGreen")

        self.enterMomFrame = tkinter.Frame(self.mainWindow, bg="mediumSpringGreen", width=300)
        self.enterDadFrame = tkinter.Frame(self.mainWindow, bg="mediumSpringGreen", width=300)
        self.spaceFrame = tkinter.Frame(self.mainWindow, bg = "mediumSpringGreen", width=300)
        self.buttonFrame = tkinter.Frame(self.mainWindow, bg="mediumSpringGreen", width=300)
        self.emptyFrame = tkinter.Frame(self.mainWindow, bg = "mediumSpringGreen", width =300)

        self.momPrompt = tkinter.Label(self.enterMomFrame, text = "Enter one parent's genotype: ", bg="mediumSpringGreen", font="times 22 bold")
        self.momEntry = tkinter.Entry(self.enterMomFrame, width=20)
        self.momFreeSpace = tkinter.Label(self.enterMomFrame, text = "  ", bg = "mediumSpringGreen")
        self.momPrompt.pack(side = "left")
        self.momEntry.pack(side = "left")
        self.momFreeSpace.pack(side = "left")

        self.dadPrompt = tkinter.Label(self.enterDadFrame, text = "Enter the other parent's genotype:", bg="mediumSpringGreen", font="times 22 bold")
        self.dadEntry = tkinter.Entry(self.enterDadFrame, width=20)
        self.dadFreeSpace = tkinter.Label(self.enterDadFrame, text = "  ", bg = "mediumSpringgreen")
        self.dadPrompt.pack(side = "left")
        self.dadEntry.pack(side = "left")
        self.dadFreeSpace.pack(side = "left")

        self.spaceLabel = tkinter.Label(self.spaceFrame, text = "                                                                           ", font = "times 12 bold", bg = "mediumSpringGreen")
        self.spaceLabel.pack()

        self.calcButton = tkinter.Button(self.buttonFrame, text="Calculate", command = self.calculate, width=17, bg="teal")
        self.freeSpace = tkinter.Label(self.buttonFrame, text = "              ", bg = "mediumSpringGreen")
        self.quitButton = tkinter.Button(self.buttonFrame, text =  "Quit", command = self.mainWindow.destroy, width=17, bg="teal")
        self.calcButton.pack(side = "left")
        self.freeSpace.pack(side = "left")
        self.quitButton.pack(side = "left")

        self.bottomLabel = tkinter.Label(self.emptyFrame, text = "                                                                           ", font = "times 12 bold", bg = "mediumSpringGreen")
        self.bottomLabel.pack()

        self.enterMomFrame.pack()
        self.enterDadFrame.pack()
        self.spaceFrame.pack()
        self.buttonFrame.pack()
        self.emptyFrame.pack()

        tkinter.mainloop()

    def calculate(self):

        self.genoWindow = tkinter.Tk()

        geneScroll = tkinter.Scrollbar(self.genoWindow)

        genoRatios = tkinter.Listbox(self.genoWindow, bg = "mediumSpringGreen")
        genoLabel = tkinter.Label(self.genoWindow, bg = "mediumSpringGreen", text = "Genotype | Number          ")
        genoSpace = tkinter.Label(self.genoWindow, bg = "mediumSpringGreen", text = "---------------------------")
        
        line = 1
        momGenes = str(self.momEntry.get())
        dadGenes = str(self.dadEntry.get())
        kidTypes = [] # List of combinatgions
        if dadGenes[0].upper() == dadGenes[0]: # Checking if the first possibility for the dad is capital
            kidTypes.append(dadGenes[0] + momGenes[0]) # If so, capital letter first, making sure both possibilities are there
            kidTypes.append(dadGenes[0] + momGenes[1])
        else:
            kidTypes.append(momGenes[0] + dadGenes[0]) # Not checking if the moms is capital because if the dad's isn't capital it doesn't matter
            kidTypes.append(momGenes[1] + dadGenes[0]) # Including both possibilities
        if dadGenes[1].upper() == dadGenes[1]:
            kidTypes.append(dadGenes[1] + momGenes[0]) # Same as the first possible gene the dad passes on
            kidTypes.append(dadGenes[1] + momGenes[1])
        else:
            kidTypes.append(momGenes[0] + dadGenes[1])
            kidTypes.append(momGenes[1] + dadGenes[1])

        for i in range(int((len(momGenes) / 2) - 1)): # Repeating for every gene being tested except for the first
            kidTypes.extend(kidTypes)
            kidTypes.extend(kidTypes) # Quadrupling length of set so each of the new genotypes is paired with every combination before it
            gene = (i * 2) + 2 # Finding the first gene possibility 
            for j in range(int(len(kidTypes))):
                if j < int(len(kidTypes) / 4): # Match one genotype with every possible genotype before it, the first set of 4
                    if dadGenes[gene].upper() == dadGenes[gene]:
                        kidTypes[j] += dadGenes[gene] + momGenes[gene]
                    else:
                        kidTypes[j] += momGenes[gene] + dadGenes[gene]
                        
                elif j < int(len(kidTypes) / 4): # Match a second genotype with the previous genotypes
                    if dadGenes[gene].upper() == dadGenes[gene]:
                        kidTypes[j] += dadGenes[gene] + momGenes[gene + 1]
                    else:
                        kidTypes[j] += momGenes[gene + 1] + dadGenes[gene]
                        
                elif j < int(3 * (len(kidTypes) / 4)): # Third genotype with previous ones
                    if dadGenes[gene + 1].upper() == dadGenes[gene + 1]:
                        kidTypes[j] += dadGenes[gene + 1] + momGenes[gene]
                    else:
                        kidTypes[j] += momGenes[gene] + dadGenes[gene + 1]
                        
                else:
                    if dadGenes[gene + 1].upper() == dadGenes[gene + 1]:
                        kidTypes[j] += dadGenes[gene + 1] + momGenes[gene + 1]
                    else:
                        kidTypes[j] += momGenes[gene + 1] + dadGenes[gene + 1]

        counter = {} # Making a dictionary for every type
        uniqueTypes = set(kidTypes) #T aking out duplicate types
        for i in uniqueTypes:
            counter[i] = 0 # Every unique type has a dictionary value
        for i in kidTypes:
            counter[i] += 1 # Increasing dictionary value for every possible genotype
        while len(counter) > 0:
            biggest = max(counter, key=counter.get) # Fiding the biggest value left in the dictionary
            pair = counter.pop(biggest) # Removing the biggest value
            genoRatios.insert(line, str(biggest) + " | " + str(pair))
            line += 1
            #messageVar += str(biggest) + "\t\t" + str(pair) + "\n"
        genoLabel.pack()
        genoSpace.pack()
            
        genoRatios.pack(side = "left")
        geneScroll.pack(side = "right")

        genoRatios.config(yscrollcommand=geneScroll.set)
        geneScroll.config(command=genoRatios.yview)



        self.phenoWindow = tkinter.Tk()

        phenoScroll = tkinter.Scrollbar(self.phenoWindow)

        phenoRatios = tkinter.Listbox(self.phenoWindow, bg = "mediumSpringGreen")
        phenoLabel = tkinter.Label(self.phenoWindow, bg = "mediumSpringGreen", text = "Phenotype | Number         ")
        phenoSpace = tkinter.Label(self.phenoWindow, bg = "mediumSpringGreen", text = "---------------------------")

        phenoLine = 1
        kidPhenTypes = kidTypes.copy() # Making a copy of the genotype list
        phenTypeList = [] # empty list to put the phenotypes into
        i = 0
        while len(kidPhenTypes) != 0:
            phenoType = kidPhenTypes.pop(0) # Removing one genotype from the list
            phenAdd = "" # Empty phenotype string
            for j in range(int(len(momGenes))): # going through every letter in the genotype
                if j%2 == 0:
                    phenAdd = phenAdd + phenoType[j] # Removing the second letter from each gene
            phenTypeList.append(phenAdd) # Adding the new phenotype to the list

        phenSet = set(phenTypeList) # Removing the duplicates from the list
        phenCounter = {} # Empty dictionary for phenotypes

        for i in phenSet: # Going through phenotypes
            phenCounter[i] = 0 # Adding individual phenotypes to the dictionary
        for i in phenTypeList:
            phenCounter[i] += 1 # Increasing dictionary value for every phenotype in the list
        while len(phenCounter) > 0: # Going through the entire dictionary
            biggestPhen = max(phenCounter, key=phenCounter.get) # Finding the biggest value in the dictionary
            phenotype = phenCounter.pop(biggestPhen) # Removing the biggest item from the dictionary
            phenoRatios.insert(line, str(biggestPhen) + "  |  " + str(phenotype))
            line += 1

        phenoLabel.pack()
        phenoSpace.pack()

        phenoRatios.pack(side = "left")
        phenoScroll.pack(side = "right")

        phenoRatios.config(yscrollcommand=phenoScroll.set)
        phenoScroll.config(command=phenoRatios.yview)


genoCalc = punnetGUI()
