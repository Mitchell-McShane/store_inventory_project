import pdb
from models.studio import Studio
from models.game import Game
from models.worker import Worker

import repositories.worker_repository as worker_repository
import repositories.studio_repository as studio_repository
import repositories.game_repository as game_repository



game_repository.delete_all()
studio_repository.delete_all()
worker_repository.delete_all()

# Workers

worker_1 = Worker('Roy Trenneman', 41, 1979)
worker_repository.save(worker_1)
worker_2 = Worker('Maurice Moss',47, 1973)
worker_repository.save(worker_2)
worker_3 = Worker('Jen Barber', 43, 1977)
worker_repository.save(worker_3)

# Studios
nintendo = Studio("Nintendo")
studio_repository.save(nintendo)
sony = Studio("Sony Computer Entertainment")
studio_repository.save(sony)
ubisoft = Studio("Ubisoft")
studio_repository.save(ubisoft)
blizzard = Studio("Blizzard")
studio_repository.save(blizzard)

# Sony games
demons = Game("Demons Souls", worker_1, "Horror", 69.99, 60.00, 2, sony)
game_repository.save(demons)
spider = Game("Spider-Man", worker_1, "Adventure", 69.99, 60.00, 11, sony)
game_repository.save(spider)
astro = Game("Astro's Playroom", worker_1, "Fun", 69.99, 60.00, 3, sony)
game_repository.save(astro)

# Ubisoft games
assassins = Game("Assassin's Creed Valhalla", worker_2, "Action", 46.85, 50.00, 7, ubisoft)
game_repository.save(assassins)

# Nintendo games
zelda = Game("Breath of the Wild", worker_3, "Action/Adventure", 43.00, 40.00, 25, nintendo)
game_repository.save(zelda)
ac = Game("Animal Crossing: New Horizons", worker_3, "Life Simulation", 39.99, 36.99, 11, nintendo)
game_repository.save(ac)

# PC games
wow = Game("World of Warcraft: Shadowlands Collectors Edition", worker_2, "Massive Multiplayer Online role-playing game", 169.99, 149.99, 0, blizzard)
game_repository.save(wow)

pdb.set_trace()