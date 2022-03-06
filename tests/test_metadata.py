from progress.spinner import Spinner
from src.engine import Collection, NFT
from colorama import init, Fore

# Create folders for asset loading/completion
spinner = Spinner('Loading ')

def test_metadata_creation():

    phunks = Collection('Phunk Test Collection', 'Phunk test suite made this description!', totalSupply=5000)
    print(f'Generating {Fore.GREEN}{phunks.totalSupply}{Fore.WHITE} nfts for collection: {Fore.GREEN}{phunks.name}{Fore.WHITE}')
    
    phunks.detect_layers()
    phunks.layers = ['Background','Base','Hat','Accessories','Holding']
    state = ''
    
    while state != 'FINISHED':
        
        # Iterate through total supply and create the NFTs.
        for id in range(phunks.totalSupply):
            
            # Do some work
            nft = NFT(id, phunks)
            nft.create_attributes()
            spinner.message = f'{Fore.GREEN}>>{Fore.WHITE} #{nft.id} created with DNA: {Fore.GREEN}{nft.dna} {Fore.WHITE}'
            spinner.next()
        
        state = 'FINISHED'
    
    # Completed build!              
    print(f'\n{Fore.GREEN}>>{Fore.WHITE} Success. Finished creating {Fore.GREEN}{phunks.totalSupply}{Fore.WHITE} unique nfts.')

    assert str(phunks.totalSupply)
    
##  test_metadata_creation()