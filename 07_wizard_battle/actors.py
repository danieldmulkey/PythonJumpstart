import random


# Base class first!
class Creature:
    # level, name,
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return 'Creature {} of level {}'.format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    def attack(self, other_creature):
        # UI piece:
        print('The wizard {} attacks {}!'.format(
            self.name, other_creature.name
        ))

        # Actual attack:
        my_roll = self.get_defensive_roll()
        # creature_roll = random.randint(1, 12) * other_creature.level
        creature_roll = other_creature.get_defensive_roll()

        # More UI
        print('You roll', my_roll)
        print('{} rolls'.format(other_creature), creature_roll)

        # More attack logic. UI and logic should be separate.
        if my_roll >= creature_roll:
            print('Wizard wins against {}!'.format(other_creature.name))
            return True
        else:
            print('Wizard DEFEATED!')
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):  # redefining method from super class
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
