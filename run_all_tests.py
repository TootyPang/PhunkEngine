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
'''
# Run this file to test if your asset folders are configured correctly before building.
from tests.test_metadata import test_metadata_creation
from tests.test_build import solo_nft_creation_test
from src.engine import folder_setup
from colorama import init, Fore

folder_setup()

test_1_name = f'{Fore.MAGENTA}metadata creation{Fore.WHITE}'
test_2_name = f'{Fore.MAGENTA}single NFT creation{Fore.WHITE}'
TEST_1 = input(f'{Fore.GREEN}>>{Fore.WHITE} Would you like to run {test_1_name} test? (y/n) :: {Fore.CYAN}')
TEST_2 = input(f'{Fore.GREEN}>>{Fore.WHITE} Would you like to run {test_2_name} test? (y/n) :: {Fore.CYAN}')


if TEST_1 == 'y':
    try:
        print(f'\n{Fore.YELLOW}--------------------------TEST 1--------------------------{Fore.WHITE}')
        print(f'Starting {test_1_name} test!')
        test_metadata_creation()
        print(f'{Fore.GREEN}Asset folders + files setup properly!{Fore.WHITE}')
        print(f'{test_1_name} test: {Fore.GREEN}Success{Fore.WHITE}.\n')
        
    except Exception as e:
        print(f'{test_1_name} test: {Fore.RED}Failed{Fore.WHITE}.')
        print(f'{Fore.RED}EXCEPTION:{Fore.WHITE} {e}\n')
else:
    pass

if TEST_2 == 'y': 
    try: 
        print(f'{Fore.YELLOW}--------------------------TEST 2--------------------------{Fore.WHITE}')
        print(f'Starting {test_2_name} test!')   
        name = solo_nft_creation_test()
        print(f'{Fore.GREEN}NFT{Fore.WHITE} can be found in: {Fore.CYAN}assets/{name}/images{Fore.WHITE} and {Fore.CYAN}assets/{name}/metadata{Fore.WHITE}')
        print(f'{test_2_name} test: {Fore.GREEN}Success{Fore.WHITE}.\n')
    
    except Exception as e:
        print(f'{test_2_name} test: {Fore.RED}Failed{Fore.WHITE}.')
        print(f'{Fore.RED}EXCEPTION:{Fore.WHITE} {e}\n')
else:
    pass
    
