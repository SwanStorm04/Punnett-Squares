import tkinter

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

        self.calcButton = tkinter.Button(self.buttonFrame, text="Calculate", command = self.calculate, width=15, bg="teal", font="times 16 bold")
        self.freeSpace = tkinter.Label(self.buttonFrame, text = "              ", bg = "mediumSpringGreen")
        self.quitButton = tkinter.Button(self.buttonFrame, text =  "Quit", command = self.mainWindow.destroy, width=15, bg="teal", font="times 16 bold")
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

        # Creating the genotype window

        
        self.genoWindow = tkinter.Tk()
        self.genoWindow.configure(bg = "mediumSpringGreen")
        self.genoWindow.title("Genotypic Ratios")

        genoLabel = tkinter.Label(self.genoWindow, bg = "mediumSpringGreen", text = "Genotype | Number", font = "times 22 bold")
        genoSpace = tkinter.Label(self.genoWindow, bg = "mediumSpringGreen", text = "")
        genoLabel.grid(row = 0)
        genoSpace.grid(row = 1)

        geneScroll = tkinter.Scrollbar(self.genoWindow)
        genoScrollY = tkinter.Scrollbar(self.genoWindow, orient = tkinter.VERTICAL)
        genoScrollY.grid(row = 2, column = 5, sticky = tkinter.N+tkinter.S)
        genoScrollX = tkinter.Scrollbar(self.genoWindow, orient = tkinter.HORIZONTAL)
        genoScrollX.grid(row = 3, sticky = tkinter.E+tkinter.W)

        genoRatios = tkinter.Listbox(self.genoWindow, bg = "mediumSpringGreen", font = "TkFixedFont", yscrollcommand = genoScrollY.set, xscrollcommand = genoScrollX.set, height = 20)
        genoRatios.grid(row = 2, sticky = tkinter.S+tkinter.E+tkinter.W)
        genoScrollX['command'] = genoRatios.xview
        genoScrollY['command'] = genoRatios.yview
        
        line = 1
        momGenes = str(self.momEntry.get())
        dadGenes = str(self.dadEntry.get())
        kidFinTypes = [] # List of combinations
        if dadGenes[0].upper() == dadGenes[0]: # Checking if the first possibility for the dad is capital
            kidFinTypes.append(dadGenes[0] + momGenes[0]) # If so, capital letter first, making sure both possibilities are there
            kidFinTypes.append(dadGenes[0] + momGenes[1])
        else:
            kidFinTypes.append(momGenes[0] + dadGenes[0]) # Not checking if the moms is capital because if the dad's isn't capital it doesn't matter
            kidFinTypes.append(momGenes[1] + dadGenes[0]) # Including both possibilities
            
        if dadGenes[1].upper() == dadGenes[1]:
            kidFinTypes.append(dadGenes[1] + momGenes[0]) # Same as the first possible gene the dad passes on
            kidFinTypes.append(dadGenes[1] + momGenes[1])
        else:
            kidFinTypes.append(momGenes[0] + dadGenes[1])
            kidFinTypes.append(momGenes[1] + dadGenes[1])

        finGeno = {} # Making a dictionary for every type
        uniqueTypes = set(kidFinTypes) #T aking out duplicate types
        for i in uniqueTypes:
            finGeno[i] = 0 # Every unique type has a dictionary value
        for i in kidFinTypes:
            finGeno[i] += 1 # Increasing dictionary value for every possible genotype
                

        for i in range(int((len(momGenes) / 2) - 1)): # Repeating for every gene being tested except for the first
            gene = (i * 2) + 2
            kidAllele = []
            currentKid = finGeno.copy()
            finGeno = {}


            # Creating the list of alleles for the next gene

            
            if dadGenes[gene].upper() == dadGenes[gene]: # Checking if the first possibility for the dad is capital
                kidAllele.append(dadGenes[gene] + momGenes[gene]) # If so, capital letter first, making sure both possibilities are there
                kidAllele.append(dadGenes[gene] + momGenes[gene + 1])
            else:
                kidAllele.append(momGenes[gene] + dadGenes[gene]) # Not checking if the moms is capital because if the dad's isn't capital it doesn't matter
                kidAllele.append(momGenes[gene + 1] + dadGenes[gene]) # Including both possibilities
            
            if dadGenes[1].upper() == dadGenes[1]:
                kidAllele.append(dadGenes[gene + 1] + momGenes[gene]) # Same as the first possible gene the dad passes on
                kidAllele.append(dadGenes[gene + 1] + momGenes[gene + 1])
            else:
                kidAllele.append(momGenes[gene] + dadGenes[gene + 1])
                kidAllele.append(momGenes[gene + 1] + dadGenes[gene + 1])


            # Combining the allele list into ratios and probability, compressing data

            
            geneDict = {} # Making a dictionary for every type
            uniqueKids = set(kidAllele) # Taking out duplicate types
            for j in uniqueKids:
                geneDict[j] = 0 # Every unique type has a dictionary value                                  THIS CAN BE A TRY AND EXCEPT LATER
            for j in kidAllele:
                geneDict[j] += 1 # Increasing dictionary value for every possible genotype
            

            # Combining the list of this specific gene with the list of all genes up to this point

            
            genoKeys = list(geneDict.keys())
            currKeys = list(currentKid.keys())
            
            for j in genoKeys: # Repeated for every allele of the current gene
                for k in currKeys: # Each allele for the current gene is going to be combined with the genotypes for the others
                    finKey = k + j # The combined genotype
                    finGeno[finKey] = geneDict[j] * currentKid[k]


        # Displaying the finished list of genotypes from most to least likely, also creating a copy of the dictionary for the phenotypes


        phenDict = finGeno.copy()

        #fin geno: dictionary of all genotypes, need their keys
        geneNumList = set(list(finGeno.values()))
        geneNumOrder = sorted(geneNumList, reverse = True)
        geneDictSort = {}

        for i in geneNumOrder:
            for j in finGeno:
                if finGeno[j] == i:
                    genoRatios.insert(line, str(j) + "  |  " + str(finGeno[j]))
                    line += 1
                
#                                                                                                               BREAKS AT 13
            


        # Creating the phenotype window

        
        self.phenoWindow = tkinter.Tk()
        self.phenoWindow.configure(bg = "mediumSpringGreen")
        self.phenoWindow.title("Phenotypic Ratios")

        phenoLabel = tkinter.Label(self.phenoWindow, bg = "mediumSpringGreen", text = "Phenotype | Number", font = "times 22 bold")
        phenoSpace = tkinter.Label(self.phenoWindow, bg = "mediumSpringGreen", text = "")
        phenoLabel.grid(row = 0)
        phenoSpace.grid(row = 1)

        phenoScroll = tkinter.Scrollbar(self.phenoWindow)
        phenoScrollY = tkinter.Scrollbar(self.phenoWindow, orient = tkinter.VERTICAL)
        phenoScrollY.grid(row = 2, column = 5, sticky = tkinter.N+tkinter.S)
        phenoScrollX = tkinter.Scrollbar(self.phenoWindow, orient = tkinter.HORIZONTAL)
        phenoScrollX.grid(row = 3, sticky = tkinter.E+tkinter.W)

        phenoRatios = tkinter.Listbox(self.phenoWindow, bg = "mediumSpringGreen", font = "TkFixedFont", yscrollcommand = phenoScrollY.set, xscrollcommand = phenoScrollX.set, height = 20)
        phenoRatios.grid(row = 2, sticky = tkinter.S+tkinter.E+tkinter.W)
        phenoScrollX['command'] = phenoRatios.xview
        phenoScrollY['command'] = phenoRatios.yview

        phenoLine = 1


        # Making the dictionary of phenotypic ratios
        

        phenTypeDict = {} # empty dictionary to put the phenotypes into
        phenKeys = list(phenDict.keys())
        for i in phenKeys:
            phenAdd = "" # Empty phenotype string
            for j in range(int(len(momGenes))): # going through every letter in the genotype
                if j%2 == 0:
                    phenAdd = phenAdd + i[j] # Removing the second letter from each gene

            try: # If the phenotype is already in the dictionary, add the number
                phenTypeDict[phenAdd] += phenDict[i]
            except:
                phenTypeDict[phenAdd] = phenDict[i]


        # Displaying the phenotypes

        phenNumList = set(list(phenTypeDict.values()))
        phenNumOrder = sorted(phenNumList, reverse = True)

        phenDictSort = {}

        for i in phenNumOrder:
            for j in phenTypeDict:
                if phenTypeDict[j] == i:
                    phenoRatios.insert(line, str(j) + "  |  " + str(phenTypeDict[j]))
                    line += 1




genoCalc = punnetGUI()
