'''
    Main engine API for Phunk Engine.
    Running this script will result in the creation of one test NFT    
'''

# 1.0 
## Library Imports
import hashlib
from PIL import Image, ImageChops
from colorama import init, Fore, Back, Style
import os, time, json, random

# 2.0 
## Start the folder setup.
def folder_setup():
    print(f'------------------ {Fore.RED}Phunk{Fore.BLUE}Engine{Fore.WHITE} ------------------')
    os.mkdir('assets') if not os.path.isdir('assets') else None
    os.mkdir('completed') if not os.path.isdir('completed') else None
    print(f'{Fore.GREEN}Setup complete.{Fore.WHITE}')
    print('-------------------------------------------------')


# 3.0 
## Holds data about the collection being built.
class Collection():
    '''
        Holds information about the total collection.
            -> .name
            -> .totalDNA = []
            -> .totalSupply = int
            -> .description = str 
    '''
    
    # 3.1 
    ## Collection object variables
    ## Two params needed: name (str), description (str) and totalSupply (int)
    def __init__(self, name:str, description: str, width=500, height=500, totalSupply=10):
        self.name = name
        self.totalDNA = []
        self.totalSupply = totalSupply
        self.description = description
        self.layers = []
        self.width = width
        self.height = height
        self.layerOpacity = []    # 1 = Full visibility, 0 = Not visable
        
        # 3.1.1
        ## Setup folders for the new collection
        def collection_folder_setup():     
            os.mkdir(f'completed/{self.name}') if not os.path.isdir(f'completed/{self.name}') else None
            os.mkdir(f'completed/{self.name}/images') if not os.path.isdir(f'completed/{self.name}/images') else None
            os.mkdir(f'completed/{self.name}/metadata') if not os.path.isdir(f'completed/{self.name}/metadata') else None
        
        # 3.1.2
        ## Create folders for collection in the 'completed' folder
        collection_folder_setup()
        
    # 3.2 
    ## Collection object variables
    ## Looks for folders in the assets folder and assigns to Collection.layers variable       
    def detect_layers(self):
        for x in os.listdir(f'assets/'):
            self.layers.append(x.split('.png')[0])
            
    # 3.3 
    ## Ask user for perfered layer order.
    ## Looks for folders in the assets folder and assigns to 'Collection.layers' variable
    def set_layers(self):
        layers = self.layers
        try:
            while True:
                # 3.3.1
                ## Show the user what layers PhunkEngine found.               
                layers = [x for x in layers]
                print(f'Layers detected: {Fore.CYAN}{layers}{Fore.WHITE}')
                
                # 3.3.2
                ## Grab user input and place each layer in a list             
                layer_order = input(f'{Fore.GREEN}>>{Fore.WHITE} Please type the order in which you want the layers to complie :: {Fore.CYAN}')
                layer_order_set = [y for y in layer_order.split(' ')]

                # 3.3.3
                ## Check to see if user layer input matches detected layer names            
                final_layers = []
                for item in layer_order_set:
                    if item in layers:
                        final_layers.append(item)
                    else:
                        print(f'{item} not found in asset layers. Try again.')
                        pass

                # 3.3.4
                ## Set the NFT object layers attribute and break the loop                 
                print(f'{Fore.WHITE}Final layer order: {Fore.GREEN}{final_layers}{Fore.WHITE}')
                self.layers = final_layers
                break  
                      
        except Exception as p:
            print(f'Error in set_layers(): {p}')    
    

# 4.0
# Everything needed to build 1 NFT.
class NFT(object):
    '''
        Object is assigned to each NFT created.
            -> .id = id
            -> .dna = str
            -> .create_attributes()
            -> .create_files()  
    '''
    
    # 4.1 
    ## NFT object variables
    ## Two params needed: NFT_ID (int) and Collection (object)
    def __init__(self, id:int, collection:object):
        self.id = id
        self.dna = str
        self.meta = dict
        self.attributes = []
        self.traits = []
        self.collection=collection
      
    # 4.2 
    ## Create unique DNA hash for nft metadata.
    ## Sets the created DNA hash to the NFT objects DNA variable
    def create_dna(self):
        self.dna = hashlib.sha1(' '.join(str(x) for x in self.traits).encode('utf-8')).hexdigest()
    
    # 4.3 
    ## Check NFT dna hash against the whole collection
    def check_for_dna(self):     
        try:
            # 4.3.1
            ## If the length of the the collection DNA list > 0, check if the DNA submited already exists.
            ## If the DNA exists: return False. If the DNA doesn't exist: return True.
            if len(self.collection.totalDNA) > 0:
                for x in self.collection.totalDNA:
                    if x == self.dna:
                        return False
                    else:
                        return True
            else:
                return True                                
        except Exception as e:
            print(f'Error in check_for_dna: {e}')
            return True
             
    # 4.4 
    ## Create/format/save metadata for assembled image.
    def create_nft_meta_data(self):
        # 4.4.1 
        ## Create opensea formated metadata.
        data = {
            "dna" : self.dna,
            "id" : self.id,
            "name" : f'Phunk #{self.id}',
            "description" : "PhunkEngine v1 Test Collection!",
            "attributes" : self.traits,
            "image" : f"ipfs://NewUriToReplace/{self.id}.png",
        }
        
        # 4.4.2 
        ## Save metadata json file.      
        with open(f'completed/{self.collection.name}/metadata/{self.id}.json', 'w+', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        # 4.4.3 
        ## Save nft meta to class variable and return data from function.    
        self.meta = data
        return data
       
    # 4.5 
    ## Function to save attributes in propper format
    def trait_holder(self, trait_type, value):
        try:
            self.traits.remove(value.split("#")[0])
        except Exception as error:
            print(f'Error inside trait_holder: {error}')
                         
        self.traits.append({"trait_type": trait_type, "value": str(value).split('#')[0]})
            
    # 4.6 
    ## Create a unique metadata set for each NFT.
    ## Start trait creation loop.    
    def create_attributes(self):  
        while True: 
            global collect_attr             
            
            # 4.6.2 
            ## Create a random set of traits from collection layers.
            for layer in self.collection.layers:
                collect_traits = []
                
                # 4.6.2.1 
                ## Find random traits for the layer in the current iteration.
                for i, item in enumerate(os.listdir(f'assets/{layer}')):
                    collect_traits.append(item.split('.')[0])
                    list_item = random.randint(0,len(os.listdir(f'assets/{layer}'))-1)

                # 4.6.2.2
                ## Set NFT attributes variable with the chosen trait for this layer.
                pick_trait = collect_traits[list_item]
                #print(f'Picked Trait {pick_trait}')
                self.attributes.append(pick_trait)
                #print(f'Test: {self.attributes}')
            
            # 4.6.3
            ## Remove hashtag and return only the trait name.      
            self.traits = [x.split("#")[0] for x in self.attributes]
            
            # 4.6.4
            ## Create a DNA hash for the NFT.
            self.create_dna()
            
            # 4.6.5
            ## Check the created hash against the created NFTs.
            check = self.check_for_dna()
            
            # 4.6.6
            ## If the hash matches one created, generate new metadata.
            ## Else save the dna hash in collection object/save attributes to NFT object.
            if check == False:
                print(f' #{self.id} produced duplicate DNA. Retrying.')
                self.attributes = []
                self.attribute_names = []
                self.traits = []
                self.dna = ''
                pass
            elif check == True:      
                self.collection.totalDNA.append(self.dna)
                break
            
    # 4.7
    ## Compile NFT trait layers and save image.
    def create_image(self):
        try:        
            # 4.7.1
            ## Create list of traits without hashtag attached.
            ## Create the base image to append layers too.
            trait_names = [x.split("#")[0] for x in self.attributes]
            base = Image.open(f'assets/{self.collection.layers[0]}/{self.attributes[0]}.png')
            base = base.resize((self.collection.width, self.collection.height))
            
            # 4.7.2
            ## Find and append the layers in the correct order to the image Image object.
            ## Set metadata traits to self object variable.
            collect = Image.new(mode='RGBA', size  = (self.collection.width, self.collection.height))
            for a, trait in enumerate(self.attributes):
                    
                # 4.7.2.1
                ## Open the next layer's image and paste it to the base image
                if a != 0:
                    new_layer = Image.open(f'assets/{self.collection.layers[a]}/{trait}.png')
                    new_layer = new_layer.resize((self.collection.width, self.collection.height))
                    image3 = Image.blend(collect, new_layer, float(self.collection.layerOpacity[a]))          
                    base.paste(image3, (0,0), image3)
                    
                    self.trait_holder(self.collection.layers[a],self.attributes[a])
                else:
                    self.trait_holder(self.collection.layers[a],self.attributes[a])
                
                # 4.7.2.2
                ## Save the completed self image and json metadata.    
                base.save(f'completed/{self.collection.name}/images/{self.id}.png', 'PNG')
                self.create_nft_meta_data()  
                                
        except Exception as error:
            print(f'{Fore.RED}Error in create_image():')
            raise error
            

    
    
# 5.0 If this file is run, create one test collection and one test NFT.            
if __name__ == '__main__':
    
    # 5.1 
    ## Setup Collection.
    print(f'{Fore.MAGENTA}> 1. Creating collection object.{Fore.WHITE}')
    test_file = random.randint(0,1000)
    phunks = Collection(f'Phunk Test Collection_{test_file}','This is a description about a test collection', width=200, height=200, totalSupply=1)

    
    # 5.2 
    ## Print Collection Details.
    print(f'''{Fore.GREEN}Collection Created!{Fore.WHITE}
    {Fore.GREEN}>> {Fore.WHITE}Collection Name         : {Fore.CYAN}{phunks.name}{Fore.WHITE}
    {Fore.GREEN}>> {Fore.WHITE}Collection Description  : {Fore.CYAN}{phunks.description}{Fore.WHITE}
    {Fore.GREEN}>> {Fore.WHITE}Collection Image Size   : {Fore.CYAN}{phunks.width}px x {phunks.height}px{Fore.WHITE}
    {Fore.GREEN}>> {Fore.WHITE}Collection Supply       : {Fore.CYAN}{phunks.totalSupply}{Fore.WHITE}\n''')

    # 5.3 
    ## Detect layers from asset folders.
    phunks.detect_layers()
    print(f'''{Fore.GREEN}Sucessfully Detected Layers.{Fore.WHITE}
    {Fore.GREEN}>> {Fore.WHITE}Layers Detected         : {Fore.CYAN}{phunks.layers}{Fore.WHITE}\n''')
    
    # 5.4
    ## Assign layers in the order we want them created  
    phunks.layers = ['Background','Base','Hat','Accessories','Holding']
    print(f'''{Fore.GREEN}Assigned custom layer order.{Fore.WHITE}
    {Fore.GREEN}>> {Fore.WHITE}New Layer Order         : {Fore.CYAN}{phunks.layers}{Fore.WHITE}\n''')

    # 5.5 
    ## Create one NFT.
    print(f'{Fore.MAGENTA}> 2. Creating NFT object.{Fore.WHITE}')
    
    # 5.6
    ## Set NFT object.
    nft = NFT(82,phunks)   
    print(f'''{Fore.GREEN}Sucessfully created NFT object.{Fore.WHITE}        
    {Fore.GREEN}>> {Fore.WHITE}NFT ID                  : {Fore.CYAN}{nft.id}{Fore.WHITE}
    {Fore.GREEN}>> {Fore.WHITE}NFT Collection          : {Fore.CYAN}{nft.collection.name}{Fore.WHITE}\n''')
    
    # 5.7
    ## Create Attributes.
    nft.create_attributes()
    print(f'''{Fore.GREEN}Sucessfully created attributes.{Fore.WHITE}
    {Fore.GREEN}>> {Fore.WHITE}NFT Attributes          : {Fore.CYAN}{nft.attributes}{Fore.WHITE}
    {Fore.GREEN}>> {Fore.WHITE}NFT Trait Name          : {Fore.CYAN}{nft.collection.layers}{Fore.WHITE}
    {Fore.GREEN}>> {Fore.WHITE}NFT D.N.A               : {Fore.CYAN}{nft.dna}{Fore.WHITE}\n''')
    
    # 5.8
    ## Create NFT image.
    nft.create_image()
    print(f'{Fore.GREEN}Sucessfully created NFT.{Fore.WHITE}')