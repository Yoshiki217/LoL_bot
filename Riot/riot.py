from riotwatcher import LolWatcher, ApiError
lol_watcher = LolWatcher('API_KEY')

my_region = 'jp1'

me = lol_watcher.summoner.by_name(my_region, '勤労感謝JP')
print(me)

# all objects are returned (by default) as a dict
# lets see if i got diamond yet (i probably didnt)
my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)

# # First we get the latest version of the game from data dragon
# versions = lol_watcher.data_dragon.versions_for_region(my_region)
# champions_version = versions['n']['champion']

# # Lets get some champions
# current_champ_list = lol_watcher.data_dragon.champions(champions_version)
# print(current_champ_list)