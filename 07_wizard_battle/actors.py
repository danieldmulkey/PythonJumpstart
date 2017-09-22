import random


def get_levels(rank):
    if rank == 'low':
        return random.randint(1, 30)
    elif rank == 'medium':
        return random.randint(31, 60)
    elif rank == 'high':
        return random.randint(61, 100)
    elif rank == 'pro':
        return random.randint(500, 1000)
    else:
        return random.randint(1, 1000)


# Define base class first!
class Creature:
    # level, name,
    def __init__(self, name, level_rank):
        self.name = name
        self.level = get_levels(level_rank)

    def __repr__(self):
        return 'Creature {} of level {}'.format(self.name, self.level)

    def get_defensive_roll(self):
        return random.randint(0, 20) * self.level


class Wizard(Creature):
    def attack(self, attack_target: Creature):
        # TODO: Figure out how this should be separated into UI and logic
        # UI piece:
        print('The wizard {} attacks {}!'.format(self.name, attack_target.name))

        # Actual attack:
        my_roll = self.get_defensive_roll()
        creature_roll = attack_target.get_defensive_roll()

        # More UI
        print('You roll', my_roll)
        print('{} rolls'.format(attack_target), creature_roll)

        # More attack logic. UI and logic should be separate.
        if my_roll >= creature_roll:
            print('Wizard {} WINS against {}!'.format(self.name, attack_target.name))
            return True
        else:
            print('Wizard {} DEFEATED by {}!'.format(self.name, attack_target.name))
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):  # redefining method from base class
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breathes_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breathes_fire = breathes_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        # Long version:
        # fire_modifier = None
        # if self.breathes_fire:
        #     fire_modifier = 5
        # else:
        #     fire_modifier = 1

        # Short version:
        # fire_modifier = VALUE_IF_TRUE if TEST else VALUE_IF_FALSE
        fire_modifier = 5 if self.breathes_fire else 1

        scale_modifier = self.scaliness / 10

        return base_roll * fire_modifier * scale_modifier
