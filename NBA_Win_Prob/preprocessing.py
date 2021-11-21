
# coding: utf-8

# ## Preprocessing

# In[73]:

import pandas as pd
plays = pd.read_csv('pbp.csv')

plays.head()

# #### Fill in scores for non-scoring plays

# In[75]:

plays['score'] = plays['score'].fillna(method='ffill')


# #### Insert column for score difference

# In[109]:

def score_difference(score):
    i = 0
    while score[i] != ' ':
        i += 1
    score_away = int(score[:i])

    i+=3
    score_home = int(score[i:])
    score_difference = score_home - score_away
    return score_difference


plays['score_difference'] = plays['score'].apply(lambda score: score_difference(score))


# In[110]:

plays.head()


# #### Insert column for seconds remaining

# In[69]:

def seconds_left(play_clock):
    i = 0
    while play_clock[i] != ':':
        i += 1
    minutes = int(play_clock[:i])
    i+=1
    seconds = int(play_clock[i:])

    seconds_left = 60*minutes + seconds
    return seconds_left


# In[77]:

plays['seconds_remaining'] = plays['play_clock'].apply(lambda play_clock: seconds_left(play_clock))
plays.head()


# #### Extract player last names

# In[91]:

import numpy as np

def last_name(name):
    if name is not np.nan:
        i = 0
        if name == "Nene":
            return name
        while name[i] != " ":
            i += 1
        i += 1
        return name[i:]
    else:
        return np.nan


plays['player1_lastname'] = plays['player1_name'].apply(lambda name: last_name(name))
plays['player2_lastname'] = plays['player2_name'].apply(lambda name: last_name(name))
plays['player3_lastname'] = plays['player3_name'].apply(lambda name: last_name(name))
plays.head()


# #### Replace team names with "Home" or "Away"

# In[124]:

def play_lastname(play):
    i = 0
    while play[i] != " ":
        i += 1
    return play[:i]

def home_or_away1(row):
    home_lastname = ""
    away_lastname = ""

    if not pd.isnull(row['home_description']):
        home_lastname = play_lastname(row['home_description'])

    if not pd.isnull(row['away_description']):
        away_lastname = play_lastname(row['away_description'])
    if pd.isnull(row['player1_lastname']):
        return "None"
    elif row['player1_lastname'] == home_lastname:
        return "Home"
    elif row['player1_lastname'] == away_lastname:
        return "Away"
    else:
        return "None"

def home_or_away2(row):
    home_lastname = ""
    away_lastname = ""
    if not pd.isnull(row['home_description']):
        home_lastname = play_lastname(row['home_description'])

    if not pd.isnull(row['away_description']):
        away_lastname = play_lastname(row['away_description'])
    if pd.isnull(row['player2_lastname']):
        return "None"
    elif row['player2_lastname'] == home_lastname:
        return "Home"
    elif row['player2_lastname'] == away_lastname:
        return "Away"
    else:
        return "None"

def home_or_away3(row):
    home_lastname = ""
    away_lastname = ""
    if not pd.isnull(row['home_description']):
        home_lastname = play_lastname(row['home_description'])

    if not pd.isnull(row['away_description']):
        away_lastname = play_lastname(row['away_description'])
    if pd.isnull(row['player3_lastname']):
        return "None"
    elif row['player3_lastname'] == home_lastname:
        return "Home"
    elif row['player3_lastname'] == away_lastname:
        return "Away"
    else:
        return "None"


plays['player1_team'] = plays.apply(lambda row1: home_or_away1(row1), axis=1)
plays['player2_team'] = plays.apply(lambda row2: home_or_away2(row2), axis=1)
plays['player3_team'] = plays.apply(lambda row3: home_or_away3(row3), axis=1)


# In[129]:

plays.head()


# #### Function for determining if home team has possession of the ball

# In[ ]:




# In[106]:

## Returns 1 if the home team has the ball after the play, 0 otherwise
def possession(row):
    if row['event_type'] == "Start Period ":
        return 0
    elif row['event_type'] == "Made Shot ":
        if pd.isnull(row['home_description']):
            return 1
        else:
            return 0
    elif row['event_type'] == "Foul ":
        if pd.isnull(row['home_description']): ## if they did not commit the foul
            return 1
        else:
            return 0
    elif row['event_type'] == "Free Throw ":
        if row['event_description'] == "Free Throw 1 of 1" or row['event_description'] == "Free Throw 2 of 2" or row['event_description'] == "Free Throw 3 of 3":
            if pd.isnull(row['home_description']):
                return 1
            else:
                return 0
        else:
            if pd.isnull(row['home_description']):
                return 0
            else:
                return 1
    elif row['event_type'] == "Rebound ": ## if the home team is not listed as the rebounder, they do not have the ball
        if pd.isnull(row['home_description']):
            return 0
        else:
            return 1
    elif row['event_type'] == "Turnover ":
        if pd.isnull(row['home_description']):
            return 1
        else:
            if "Turnover" in row['home_description']:
                return 0
            else:
                return 1
    elif row['event_type'] == "Violation ":
        if pd.isnull(row['home_description']):
            return 1
        else:
            return 0
    else:
        return np.nan


plays['possession'] = plays.apply(possession, axis=1)


# In[ ]:




# #### Fill in NaN possession values with forward fill

# In[131]:

plays['possession'] = plays['possession'].fillna(method='ffill')
plays['possession'] = plays['possession'].astype(int)


# In[140]:

plays.head()


# #### Accounting for star players

# Every fan knows the star impact is bigger in basketball than any other sport. A star player's absence or presence on the court is felt, and we hypothesize that this transforms to significant differences in win probability. Thus, we keep a list of the top 25 players in the NBA, and keep track of how many star players each team has on the court after any play.

# In[169]:

## player_id for the 25 star players of the NBA

star_ids = [202681,2546,162157,201188,203081,201599,202691,201143,202322,202710,200794,200768,203110,202326,200746,201933,202331,203076,201935,202695,201566,101108,201939,201142,2544]



# In[177]:

all_home_stars = [[]]
all_away_stars = [[]]

home_stars = []
away_stars = []

i = 1
while i < 294366:
    if plays.iloc[i]['game_id'] != plays.iloc[i-1]['game_id']:
        home_stars = []
        away_stars = []
        i += 1
        all_home_stars.append(home_stars)
        all_away_stars.append(away_stars)
    else:
        if plays.iloc[i]['player1_team'] == "Home":
            if plays.iloc[i]['player1_id'] in star_ids:
                if plays.iloc[i]['event_type'] == 'Susbtitution ':
                    home_stars.remove(plays.iloc[i]['player1_id'])
                else:
                    if plays.iloc[i]['player1_id'] not in home_stars:
                        home_stars.append(plays.iloc[i]['player1_id'])
        if plays.iloc[i]['player2_team'] == "Home":
            if plays.iloc[i]['player2_id'] in star_ids:
                if plays.iloc[i]['event_type'] == 'Susbtitution ':
                    home_stars.append(plays.iloc[i]['player2_id'])
                else:
                    if plays.iloc[i]['player2_id'] not in home_stars:
                        home_stars.append(plays.iloc[i]['player2_id'])

        if plays.iloc[i]['player3_team'] == "Home":
            if plays.iloc[i]['player3_id'] in star_ids:
                if plays.iloc[i]['player3_id'] not in home_stars:
                    home_stars.append(plays.iloc[i]['player3_id'])



        if plays.iloc[i]['player1_team'] == "Away":
            if plays.iloc[i]['player1_id'] in star_ids:
                if plays.iloc[i]['event_type'] == 'Susbtitution ':
                    away_stars.remove(plays.iloc[i]['player1_id'])
                else:
                    if plays.iloc[i]['player1_id'] not in away_stars:
                        away_stars.append(plays.iloc[i]['player1_id'])
        if plays.iloc[i]['player2_team'] == "Away":
            if plays.iloc[i]['player2_id'] in star_ids:
                if plays.iloc[i]['event_type'] == 'Susbtitution ':
                    away_stars.append(plays.iloc[i]['player2_id'])
                else:
                    if plays.iloc[i]['player2_id'] not in away_stars:
                        away_stars.append(plays.iloc[i]['player2_id'])

        if plays.iloc[i]['player3_team'] == "Away":
            if plays.iloc[i]['player3_id'] in star_ids:
                if plays.iloc[i]['player3_id'] not in away_stars:
                    away_stars.append(plays.iloc[i]['player3_id'])

        all_home_stars.append(home_stars)
        all_away_stars.append(away_stars)
        i += 1



# In[178]:

plays['home_stars'] = all_home_stars
plays['away_stars'] = all_away_stars


# In[179]:

plays['num_home_stars'] = plays.apply(lambda row: len(row['home_stars']), axis=1)
plays['num_away_stars'] = plays.apply(lambda row: len(row['away_stars']), axis=1)
plays.head()


# In[176]:

l = [[]]
l.append([])
l


# #### Adding column for whether game was won or not

# In[170]:

def result(row):
    if row['event_type'] == "End Period ":
        if row['score_difference'] < 0:
            return 0
        elif row['score_difference'] > 0:
            return 1
    return np.nan

plays['game_result'] = plays.apply(result,axis=1)
plays['game_result'] = plays['game_result'].fillna(method='bfill')
plays['game_result'] = plays['game_result'].astype(int)


# In[172]:

plays.to_csv('pbp_model_data.csv')
