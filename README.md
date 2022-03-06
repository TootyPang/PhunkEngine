# **Phunk Engine**   
Created by TootyPang.


### Installation guide
PhunkEngine requires Python 3.8+. 
   - `pip install -r requirements.txt`


### Setup and Run

1. Copy your assets into the assets folders.

2. Make sure you name your folders EXACTLY what your attributes to be called.
       
3. In each attribute folder, have your trait pngs saved with a # at the end to denote rarity.
   - ex: `purple_glasses#70.png`
   - `#100` = Very common. `#1` = Super rare. Play with it to find distributions you like!

4. Run
   - OPTION 1 (Easy): Just run `python app.py` :)

   - OPTION 2 (Expert): Edit build-settings.json, then run `python app.py`! 

   - OPTION 3 (Command line): python start.py [COLLECTION_NAME] [NFT_QTY] 

   - Command line example: `python app.py Phunks 100` 
    
5. Check the '/completed' folder to see your NFT images and metadata.
