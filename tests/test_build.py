import random
from src.engine import Collection, NFT
from colorama import init, Fore

def solo_nft_creation_test():
    
    # 1.1 
    ## Setup Collection.
    print(f'{Fore.MAGENTA}> Creating collection object.{Fore.WHITE}')
    test_file = random.randint(0,1000)
    phunks = Collection(f'Phunk Test Collection_{test_file}','This is a description about a test collection', width=200, height=200, totalSupply=1)

    # 1.2 
    ## Print Collection Details.
    print(f'''{Fore.GREEN}Collection Created!{Fore.WHITE}
    {Fore.GREEN}>> {Fore.WHITE}Collection Name         : {Fore.CYAN}{phunks.name}{Fore.WHITE}
    {Fore.GREEN}>> {Fore.WHITE}Collection Description  : {Fore.CYAN}{phunks.description}{Fore.WHITE}
    {Fore.GREEN}>> {Fore.WHITE}Collection Image Size   : {Fore.CYAN}{phunks.width}px x {phunks.height}px{Fore.WHITE}
    {Fore.GREEN}>> {Fore.WHITE}Collection Supply       : {Fore.CYAN}{phunks.totalSupply}{Fore.WHITE}\n''')

    # 1.3 
    ## Detect layers from asset folders.
    phunks.detect_layers()
    print(f'''{Fore.GREEN}Sucessfully Detected Layers.{Fore.WHITE}
    {Fore.GREEN}>> {Fore.WHITE}Layers Detected         : {Fore.CYAN}{phunks.layers}{Fore.WHITE}\n''')

    # 1.4
    ## Assign layers in the order we want them created  
    phunks.layers = ['Background','Base','Hat','Accessories','Holding']
    phunks.layerOpacity = [1, 1, 1, 1, 1]
    
    print(f'''{Fore.GREEN}Assigned custom layer order.{Fore.WHITE}
    {Fore.GREEN}>> {Fore.WHITE}New Layer Order         : {Fore.CYAN}{phunks.layers}{Fore.WHITE}\n''')

    # 1.1 
    ## Create one NFT.
    print(f'{Fore.MAGENTA}> Creating NFT object.{Fore.WHITE}')

    # 1.6
    ## Set NFT object.
    nft = NFT(82,phunks)   
    print(f'''{Fore.GREEN}Sucessfully created NFT object.{Fore.WHITE}        
    {Fore.GREEN}>> {Fore.WHITE}NFT ID                  : {Fore.CYAN}{nft.id}{Fore.WHITE}
    {Fore.GREEN}>> {Fore.WHITE}NFT Collection          : {Fore.CYAN}{nft.collection.name}{Fore.WHITE}\n''')

    # 1.7
    ## Create Attributes.
    nft.create_attributes()
    print(f'''{Fore.GREEN}Sucessfully created attributes.{Fore.WHITE}
    {Fore.GREEN}>> {Fore.WHITE}NFT Attributes          : {Fore.CYAN}{nft.attributes}{Fore.WHITE}
    {Fore.GREEN}>> {Fore.WHITE}NFT Trait Name          : {Fore.CYAN}{nft.collection.layers}{Fore.WHITE}
    {Fore.GREEN}>> {Fore.WHITE}NFT D.N.A               : {Fore.CYAN}{nft.dna}{Fore.WHITE}\n''')

    # 1.8
    ## Create NFT image.
    nft.create_image()
    print(f'{Fore.GREEN}Sucessfully created NFT.{Fore.WHITE}')
    return nft.collection.name