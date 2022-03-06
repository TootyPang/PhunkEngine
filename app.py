'''
    ██████╗ ██╗  ██╗██╗   ██╗███╗   ██╗██╗  ██╗    ███████╗███╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗
    ██╔══██╗██║  ██║██║   ██║████╗  ██║██║ ██╔╝    ██╔════╝████╗  ██║██╔════╝ ██║████╗  ██║██╔════╝
    ██████╔╝███████║██║   ██║██╔██╗ ██║█████╔╝     █████╗  ██╔██╗ ██║██║  ███╗██║██╔██╗ ██║█████╗  
    ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔═██╗     ██╔══╝  ██║╚██╗██║██║   ██║██║██║╚██╗██║██╔══╝  
    ██║     ██║  ██║╚██████╔╝██║ ╚████║██║  ██╗    ███████╗██║ ╚████║╚██████╔╝██║██║ ╚████║███████╗
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
    Version 1.5.5
    Created by: @TootyPang                                                                                          
    Last Update: 11/17/2021
    
    
    1. Copy your assets into the assets folders.
        -> Makes sure you name your folders EXACTLY what your attributes to be called
               
        -> In each attribute folder, have your trait pngs saved with a # at the end to denote rarity.
            --> ex: 'purple_glasses#70.png'
            --> #100 = As common as it gets, #1 = Super rare. Play with it to find distributions you like!
    
    2. Run: 
        -> Easy Mode: Just run this file, answer the questions and enjoy your NFTS :).
        -> Expert Mode: Configure build-settings.json, set "active" to "True" and run this file to skip easy mode steps.
        
    3. Check the '/completed' folder to see your NFT images/metadata
'''

# Library imports
import sys, json
from progress.spinner import Spinner
from colorama import init, Fore, Back, Style
from src.engine import NFT, Collection, folder_setup

# Create folders for asset loading/completion
folder_setup()
spinner = Spinner('Loading ')
settings = json.load(open('build-settings.json'))

# Check for command line input that skips build questions
try:
    settings['active'] = 'True' if str(sys.argv[1]) == 'create' else 'False'  
except:
    pass
    
# Check for settings details if build-settings['active'] = True, else run build questions
try:
    if settings['active'] == 'True':
        COLLECTION_NAME = settings['collection'][0]['name']
        COLLECTION_DESCRIPTION = settings['collection'][0]['description']
        IMAGE_WIDTH = settings['collection'][0]['image_width']
        IMAGE_HEIGHT = settings['collection'][0]['image_height']
        NFT_AMOUNT = settings['collection'][0]['total_supply']    
        BLEND_OPACITY = settings['collection'][0]['layer_opacity']  

    else:
    # If command line input is blank, prompt for qty to generate  
        while True:
            COLLECTION_NAME = input(f'{Fore.GREEN}>>{Fore.WHITE} What would you like to name the collection? :: {Fore.CYAN}')
            COLLECTION_DESCRIPTION = input(f'{Fore.GREEN}>>{Fore.WHITE} Please describe your collection?            :: {Fore.CYAN}')
            IMAGE_WIDTH = input(f'{Fore.GREEN}>>{Fore.WHITE} What is the final IMAGE-width?              :: {Fore.CYAN}')
            IMAGE_HEIGHT = input(f'{Fore.GREEN}>>{Fore.WHITE} What is the final IMAGE-height?             :: {Fore.CYAN}')
            NFT_AMOUNT = input(f'{Fore.GREEN}>>{Fore.WHITE} How many NFTS will be in the collection?    :: {Fore.CYAN}')
            
            print(f'{Fore.WHITE}-------------------------------------------------------')
            
            try:
                NFT_AMOUNT = int(NFT_AMOUNT)
                break   
            except:
                print('Invalid qty. Please try again.')
except Exception as e:
    print(f'Error while reading settings: {e}') 

    
# Main function
def main():
    # Create the collection object
    phunks = Collection(str(COLLECTION_NAME), str(COLLECTION_DESCRIPTION), int(IMAGE_WIDTH), int(IMAGE_HEIGHT), int(NFT_AMOUNT))
    phunks.detect_layers()
    if settings['active'] != 'True':
        phunks.set_layers()
        phunks.blendOpacity = [int(1) for x in phunks.layers]
    else:
        phunks.blendOpacity = BLEND_OPACITY
        phunks.layers = settings['collection'][0]['layers']
        
    print(f'Generating {Fore.GREEN}{phunks.totalSupply}{Fore.WHITE} nfts for collection: {Fore.GREEN}{phunks.name}{Fore.WHITE}')
    
    state = ''
    while state != 'FINISHED':
        # Iterate through total supply and create the NFTs.
        for id in range(phunks.totalSupply):
            # Do some work
            nft = NFT(id, phunks)
            nft.create_attributes()
            nft.create_image()
            spinner.message = f'{Fore.GREEN}>>{Fore.WHITE} #{nft.id} created with DNA: {Fore.GREEN}{nft.dna} {Fore.WHITE}'
            spinner.next()
        state = 'FINISHED'
    
    # Completed build!              
    print(f'\n{Fore.GREEN}Success.{Fore.WHITE} Finished creating {Fore.GREEN}{phunks.totalSupply}{Fore.WHITE} unique nfts.')

# Run main function.
if __name__ == "__main__":
    main()